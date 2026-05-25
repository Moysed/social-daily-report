"""LLM access with two backends + a graceful STUB fallback.

- "api" : Anthropic API via the `anthropic` SDK (pay-per-token; sanctioned for automation).
- "cli" : shell out to the Claude Code CLI (`claude -p`). When you are logged in with a
          Pro/Max subscription, this bills against that subscription instead of the API.

Select with env var LLM_BACKEND=api|cli (default: api). If the chosen backend has no
usable credentials, `enabled` is False and the pipeline falls back to STUB mode.

NOTE on the CLI backend: it runs `claude -p` WITHOUT `--bare`, so OAuth/subscription auth
is used. It must run on a machine where Claude Code is installed and logged in
(`claude login`). Using a subscription for unattended automation is a gray area Anthropic
is tightening — fine for personal/internal use, but keep production on the API backend.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import time

# Full model IDs (used by the API backend + recorded in front-matter).
OPUS_MODEL = os.environ.get("OPUS_MODEL", "claude-opus-4-7")
SONNET_MODEL = os.environ.get("SONNET_MODEL", "claude-sonnet-4-6")

# The CLI backend uses model aliases by default (resilient to ID changes).
CLI_OPUS_MODEL = os.environ.get("CLI_OPUS_MODEL", "opus")
CLI_SONNET_MODEL = os.environ.get("CLI_SONNET_MODEL", "sonnet")


class BaseLLM:
    enabled: bool = False
    backend: str = "stub"

    def analyze(self, system: str, user: str, max_tokens: int = 4000) -> str:
        raise NotImplementedError

    def translate(self, body: str, max_tokens: int = 8000) -> str:
        from .prompts import TRANSLATE_SYSTEM

        return self._translate(TRANSLATE_SYSTEM, body, max_tokens)

    def _translate(self, system: str, body: str, max_tokens: int) -> str:
        raise NotImplementedError


class ApiClient(BaseLLM):
    backend = "api"

    def __init__(self) -> None:
        self.api_key = os.environ.get("ANTHROPIC_API_KEY")
        self.enabled = bool(self.api_key)
        self._client = None
        if self.enabled:
            from anthropic import Anthropic  # imported lazily

            self._client = Anthropic(api_key=self.api_key)

    def _text(self, model: str, system: str, user: str, max_tokens: int) -> str:
        msg = self._client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return "".join(b.text for b in msg.content if b.type == "text")

    def analyze(self, system: str, user: str, max_tokens: int = 4000) -> str:
        return self._text(OPUS_MODEL, system, user, max_tokens)

    def _translate(self, system: str, body: str, max_tokens: int) -> str:
        return self._text(SONNET_MODEL, system, body, max_tokens)


class CliClient(BaseLLM):
    """Drive Claude Code headlessly. Uses your subscription when logged in."""

    backend = "cli"

    def __init__(self, cwd: str | None = None, timeout: float | None = None) -> None:
        self.bin = os.environ.get("CLAUDE_BIN") or shutil.which("claude")
        self.enabled = bool(self.bin)
        self.cwd = cwd
        if timeout is None:
            try:
                timeout = float(os.environ.get("CLI_TIMEOUT", "900"))
            except ValueError:
                timeout = 900.0
        self.timeout = timeout

    # Transient API statuses that warrant an automatic retry-with-backoff.
    # 529 = Overloaded (Anthropic-side), 503 = Service Unavailable,
    # 502/504 = upstream/gateway timeout, 429 = rate limited.
    _RETRY_STATUSES = ("529", "503", "502", "504", "429")

    def _run(self, model: str, system: str, user: str) -> str:
        # User prompt goes via stdin (avoids OS arg-length limits on big inputs).
        cmd = [
            self.bin,
            "-p",
            "--system-prompt", system,
            "--model", model,
            "--output-format", "json",
            "--permission-mode", "bypassPermissions",
            "--no-session-persistence",  # one-shot; avoids session-file collisions between calls
        ]
        # Drop ANTHROPIC_API_KEY so the CLI uses OAuth/subscription, not the API.
        env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}

        max_attempts = int(os.environ.get("CLI_MAX_ATTEMPTS", "3"))
        backoff = float(os.environ.get("CLI_RETRY_BACKOFF", "8"))
        last_exc: Exception | None = None

        for attempt in range(1, max_attempts + 1):
            try:
                proc = subprocess.run(
                    cmd,
                    input=user,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=self.timeout,
                    cwd=self.cwd,
                    env=env,
                )
            except subprocess.TimeoutExpired as exc:
                last_exc = exc
                if attempt < max_attempts:
                    time.sleep(backoff * attempt)
                    continue
                raise

            if proc.returncode == 0:
                try:
                    return json.loads(proc.stdout).get("result", "")
                except json.JSONDecodeError:
                    return proc.stdout

            detail = (proc.stderr or proc.stdout or "").strip()[:800]
            # Retry only for known transient statuses; surface everything else.
            if (
                attempt < max_attempts
                and any(s in detail for s in self._RETRY_STATUSES)
            ):
                time.sleep(backoff * attempt)
                continue
            raise RuntimeError(f"claude CLI exited {proc.returncode}: {detail}")

        # Defensive — loop should have either returned or raised.
        raise last_exc if last_exc else RuntimeError("claude CLI: exhausted retries with no result")

    def analyze(self, system: str, user: str, max_tokens: int = 4000) -> str:
        return self._run(CLI_OPUS_MODEL, system, user)

    def _translate(self, system: str, body: str, max_tokens: int) -> str:
        return self._run(CLI_SONNET_MODEL, system, body)


def make_llm_client(cwd: str | None = None) -> BaseLLM:
    """Pick a backend from LLM_BACKEND (default: api)."""
    backend = os.environ.get("LLM_BACKEND", "api").strip().lower()
    if backend == "cli":
        return CliClient(cwd=cwd)
    return ApiClient()
