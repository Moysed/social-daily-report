---
type: social-topic-report
date: '2026-06-13'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-06-13T03:10:04+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 249
salience: 0.7
sentiment: negative
confidence: 0.55
tags:
- anthropic
- export-controls
- claude-code
- model-access
- ai-tooling
- local-models
thumbnail: https://pbs.twimg.com/media/HJZPopiakAAeIW0.jpg
---

# AI News & New Skills — 2026-06-13

## TL;DR
- Anthropic disabled Fable 5 and Mythos 5 for all customers worldwide to comply with a US export-control directive barring access by any foreign national inside or outside the US [1][5][23][38][47].
- Fable 5 was removed from Claude Code [54]; subscribers who upgraded (e.g. $200/Max) specifically for the model report losing it mid-cycle and requesting refunds [22][43][56].
- Anthropic states it believes the order is a misunderstanding [47]; one commentator frames it as a de facto, accidental regulation touching recursive self-improvement since non-US Anthropic staff also lose access [46].
- A single unverified post claims Fable 5 scored 87.8% on FrontierMath Tier 4 v2, +31.7pp over Opus 4.8 and ahead of DeepMind [51] — no independent confirmation.
- Smaller concrete tool drops in the feed: OpenAI shipped a docs agent on its platform [34]; an 'appshots' utility for piping screenshots into Codex circulated [12].

## What happened
The US government issued an export-control directive citing national security to suspend all access to Fable 5 and Mythos 5 by any foreign national, located anywhere [1][38][49]. Anthropic complied by disabling both models for all customers globally [5][21][23][47] and removing Fable 5 from Claude Code [54]; it posted a notice on its site and said it believes the order is a misunderstanding [23][47]. Reports claim US officials tried to stop the Fable 5 release before imposing controls [26]. Paying subscribers report losing access and asking for refunds [22][43][56].

## Why it matters (reasoning)
Most of the feed is low-signal: Thai celebrity 'Gemini' birthday posts [3][6][31][44][45][53][58][59] and political commentary [2][4][8] dominate by engagement but are off-topic. The relevant signal is the access cut. A Chiang Mai studio counts as a foreign national located outside the US, so the directive directly removes Fable 5/Mythos 5 access if those models were in use [1][38]; because Anthropic disabled worldwide, US-based access is gone too [5][23]. The second-order effect is precedent: a top model treated like an export-controlled weapon [36][46] creates continuity risk for any workflow pinned to one frontier model, and commentators flag zero non-US revenue and possible extension to OpenAI/Google/xAI [14][40]. This is what pushes interest toward local/open-weight models as a hedge [10].

## Possibility
Likely: short-term disruption that Anthropic contests as a misunderstanding and seeks to reverse [47]. Plausible: the control regime extends to other vendors, and competitors delay or downplay releases to avoid the same treatment [14][40]. Plausible: accelerated adoption of local/open-weight models for continuity [10]. Unlikely without independent confirmation: the specific FrontierMath benchmark figures hold up [51]. No source provides a numeric probability; Polymarket is referenced but no odds are given in these items [21][26].

## Org applicability — NDF DEV
1) Do not pin production or internal AI workflows to Fable 5/Mythos 5; assume access can vanish for non-US users (effort low) [1][38][54]. 2) Audit which Claude models your Claude Code setup uses and confirm a configured fallback model (effort low) [54]. 3) Keep a provider-agnostic model abstraction so you can swap between Anthropic, OpenAI, Google, or local without rework (effort med) [14][10]. 4) Evaluate a local/open-weight model for continuity-critical or sensitive tasks as a hedge (effort med-high) [10]. 5) Trial low-cost tooling: OpenAI's docs agent for dev Q&A [34] and 'appshots' for a screenshot→Codex flow [12] (effort low). Skip: the FrontierMath claim [51] (unverified), celebrity/political noise [2][3][4][8], and the CRISPR item [33] (off-topic).

## Signals to Watch
- Whether Anthropic restores Fable 5/Mythos 5 or the directive widens to other vendors [14][40][47].
- Independent confirmation or retraction of the FrontierMath Tier 4 v2 score [51].
- Momentum behind local/open 'Opus-level' models pitched as government-proof [10].
- Maturity of OpenAI's docs agent as a support pattern a studio could copy [34].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **addyosmani/agent-skills** — Production-grade engineering skills for AI coding agents.Agent Skills Production-grade engineering s | rss | <https://github.com/addyosmani/agent-skills> |
| **music-assistant/server** — Music Assistant is a free, opensource Media library manager that connects to your streaming services | rss | <https://github.com/music-assistant/server> |
| **mattermost/mattermost** — Mattermost is an open source platform for secure collaboration across the entire software developmen | rss | <https://github.com/mattermost/mattermost> |
| **apple/container** — A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is  | rss | <https://github.com/apple/container> |
| **iptv-org/iptv** — Collection of publicly available IPTV channels from all over the worldIPTV Collection of publicly av | rss | <https://github.com/iptv-org/iptv> |
| **obra/superpowers** — An agentic skills framework & software development methodology that works.Superpowers Superpowers is | rss | <https://github.com/obra/superpowers> |
| **refactoringhq/tolaria** — Desktop app to manage markdown knowledge bases 💧 Tolaria Tolaria is a desktop app for macOS, Windows | rss | <https://github.com/refactoringhq/tolaria> |
| **maziyarpanahi/openmed** — open-source healthcare ai Local-first healthcare AI that never leaves the device Turn clinical text  | rss | <https://github.com/maziyarpanahi/openmed> |
| **LMCache/LMCache** — LMCache: Supercharge Your LLM with the Fastest KV Cache Layer A KV Cache Management Layer for Scalab | rss | <https://github.com/LMCache/LMCache> |
| **phuryn/pm-skills** — PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, exec | rss | <https://github.com/phuryn/pm-skills> |
| **masterking32/MasterDnsVPN** — Advanced DNS tunneling VPN for censorship bypass, optimized beyond DNSTT and SlipStream with low-ove | rss | <https://github.com/masterking32/MasterDnsVPN> |
| **msitarzewski/agency-agents** — A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whi | rss | <https://github.com/msitarzewski/agency-agents> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | AnthropicAI | ^26493 c4406 | [The US government, citing national security authorities, has issued an export co](https://x.com/AnthropicAI/status/2065597531644743999) |
| x | MikeBenzCyber | ^14828 c320 | [@SenWarren You could give “the typical American” 11 MILLION years and they still](https://x.com/MikeBenzCyber/status/2065542348595941803) |
| x | GMMTV | ^10890 c406 | [Happy Birthday to Gemini #GMMTV @gemini_ti https://t.co/dYoN8ARzEE](https://x.com/GMMTV/status/2065600041474199693) |
| x | MikeBenzCyber | ^9019 c321 | [You could give “the typical American” 11 MILLION years and they still would not ](https://x.com/MikeBenzCyber/status/2065541971163169124) |
| x | WatcherGuru | ^4956 c398 | [JUST IN: 🇺🇸 US government orders Anthropic to suspend foreign access to Mythos F](https://x.com/WatcherGuru/status/2065601203304534268) |
| x | RiserMusic | ^3415 c111 | [HAPPY BIRTHDAY TO GEMINI ♊🌟🎂 @gemini_ti #Gemini_NT #RISERMUSIC https://t.co/kwSB](https://x.com/RiserMusic/status/2065600038605099445) |
| x | MatthewBerman | ^2896 c221 | [self-inflicted. this would have NEVER happened if anthropic didn't make such a b](https://x.com/MatthewBerman/status/2065601391117361553) |
| x | PopDetective | ^2343 c4 | [This is a scam. It's a move to socialize the risk and inevitable massive losses ](https://x.com/PopDetective/status/2065519138702024900) |
| x | kiwifot | ^2245 c3 | [he’s a little insane about gemini https://t.co/DbI0LgTbpI](https://x.com/kiwifot/status/2065499939719749772) |
| x | AlexFinn | ^2149 c229 | [This is your wakeup call. Anthropic just took down Fable 5. It's over. Here's th](https://x.com/AlexFinn/status/2065614148537299149) |
| x | VictorTaelin | ^2008 c83 | [great fucking job, Anthropic incredible fear-mongering fuck progress, fuck scien](https://x.com/VictorTaelin/status/2065606970032201952) |
| x | steipete | ^1563 c91 | [How am I only now finding out about appshots? I was dragging screenshots into co](https://x.com/steipete/status/2065564094879637546) |
| x | adonis_singh | ^1561 c17 | [openai has the chance to the funniest thing ever https://t.co/o0n2aVnFMh](https://x.com/adonis_singh/status/2065495329743470868) |
| x | scaling01 | ^1555 c124 | [For anyone wondering what this means: - Anthropic (and potentially future OpenAI](https://x.com/scaling01/status/2065607360115302639) |
| x | NewsFromGoogle | ^1402 c46 | [Today, we filed a lawsuit to permanently dismantle a group of organized cybercri](https://x.com/NewsFromGoogle/status/2065522455205343475) |
| x | MattWallace888 | ^1296 c153 | [Here is a photo of the meeting from another angle! I asked all the top AIs about](https://x.com/MattWallace888/status/2065580665144521038) |
| x | bridgemindai | ^1240 c87 | [Anthropic has been ordered by the US government to suspend access to Fable 5. WT](https://x.com/bridgemindai/status/2065599350546288742) |
| x | buccocapital | ^1116 c28 | [Anthropic rubs their nipples and begs to be regulated then whines and whines and](https://x.com/buccocapital/status/2065609481715699929) |
| x | GreenIrisTarot | ^1115 c10 | [˗ˏˋ ♡ ˎˊ˗ gemini, virgo, sagittarius, pisces (s, m, r,) — blessings incoming! 🌟✨](https://x.com/GreenIrisTarot/status/2065495383942312320) |
| x | vxunderground | ^1077 c49 | ["Bro it's so totally badass and scary, I swear bro, like, the GOVERNMENT is cens](https://x.com/vxunderground/status/2065606525217919160) |
| x | Polymarket | ^1072 c106 | [NEW: Anthropic disables Fable 5 &amp; Mythos 5 for all customers.](https://x.com/Polymarket/status/2065607899036975237) |
| x | TimJayas | ^1052 c18 | [@AnthropicAI Me after buying $200 Claude plan just to use Fable https://t.co/u5W](https://x.com/TimJayas/status/2065607091562361207) |
| radar | Dylan1312 | ^1049 c642 | [US Government directive to suspend access to Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access) |
| x | FurkanGozukara | ^991 c62 | [@AnthropicAI Cancel your Claude subscription, refund and never look back again t](https://x.com/FurkanGozukara/status/2065602228614754407) |
| x | Kaivtuber_ | ^966 c55 | [🔥DEBUT ANNOUNCEMENT🔥 ⌛️: Saturday June 13th @ 5pm PST ✨New Model ✨New Background](https://x.com/Kaivtuber_/status/2065600631650541601) |
| x | Polymarket | ^841 c64 | [JUST IN: U.S. officials reportedly tried to stop Anthropic from releasing Claude](https://x.com/Polymarket/status/2065605717873017160) |
| x | unusual_whales | ^796 c101 | [The SpaceX, Anthropic and OpenAI IPOs are expected to create about 20 new billio](https://x.com/unusual_whales/status/2065568314072469576) |
| x | blknoiz06 | ^785 c137 | [the US govt shut down access to claude's new model as a national security concer](https://x.com/blknoiz06/status/2065610232944840967) |
| x | stillgh4y | ^725 c28 | [@ClaudeDevs This is a PR stunt in collusion with the US Government (Trump admini](https://x.com/stillgh4y/status/2065607605876306123) |
| x | gothburz | ^725 c45 | [A short history of how we got here, because the chronology is the whole story. J](https://x.com/gothburz/status/2065601302705398034) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AnthropicAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 26493 · 💬 4406</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AnthropicAI/status/2065597531644743999">View @AnthropicAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The US government, citing national security authorities, has issued an export control directive to suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the Uni”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>US export control order forces Anthropic to disable Fable 5 and Mythos 5 globally; the restriction targets foreign national access, and all other Claude models remain available.</dd>
      <dt>Why interesting</dt>
      <dd>The studio is a foreign-national team in Thailand, so Fable 5 and Mythos 5 are immediately inaccessible; any pipeline or API call targeting these models breaks now.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Audit studio tools and API integrations for Fable 5 / Mythos 5 references and reroute them to available Claude models.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AnthropicAI/status/2065597531644743999" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MikeBenzCyber</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 14828 · 💬 320</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MikeBenzCyber/status/2065542348595941803">View @MikeBenzCyber on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@SenWarren You could give “the typical American” 11 MILLION years and they still would not create PayPal, Tesla, SpaceX, OpenAI, xAI, Neuralink, Boring Company, Ad Astra, all while single-handedly sav”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Mike Benz posts a political jab at Sen. Elizabeth Warren, listing Elon Musk's companies to argue no typical American could replicate his output.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MikeBenzCyber/status/2065542348595941803" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GMMTV</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 10890 · 💬 406</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GMMTV/status/2065600041474199693">View @GMMTV on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Happy Birthday to Gemini #GMMTV @gemini_ti https://t.co/dYoN8ARzEE”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Thai entertainment company GMMTV posted a birthday greeting for their actor Gemini (@gemini_ti), unrelated to the AI model.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GMMTV/status/2065600041474199693" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MikeBenzCyber</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 9019 · 💬 321</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MikeBenzCyber/status/2065541971163169124">View @MikeBenzCyber on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“You could give “the typical American” 11 MILLION years and they still would not create PayPal, Tesla, SpaceX, OpenAI, xAI, Neuralink, Boring Company, Ad Astra, all while single-handedly saving free sp”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Twitter account posts a hyperbolic tribute claiming the average American could never match Elon Musk's company portfolio or cultural impact in 11 million years.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MikeBenzCyber/status/2065541971163169124" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@WatcherGuru</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4956 · 💬 398</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/WatcherGuru/status/2065601203304534268">View @WatcherGuru on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“JUST IN: 🇺🇸 US government orders Anthropic to suspend foreign access to Mythos Fable 5 AI model, citing national security concerns. Anthropic has disabled access for all users worldwide. https://t.co/”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@WatcherGuru claims the US government ordered Anthropic to globally disable a model called 'Mythos Fable 5' over national security grounds — but 'Mythos Fable 5' does not match any real Anthropic model name, making this post unverified or fabricated.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/WatcherGuru/status/2065601203304534268" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RiserMusic</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3415 · 💬 111</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RiserMusic/status/2065600038605099445">View @RiserMusic on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“HAPPY BIRTHDAY TO GEMINI ♊🌟🎂 @gemini_ti #Gemini_NT #RISERMUSIC https://t.co/kwSBmgPVMJ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan account posts a birthday greeting to Thai celebrity Gemini (a K-pop/entertainment figure), unrelated to Google Gemini AI.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RiserMusic/status/2065600038605099445" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MatthewBerman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2896 · 💬 221</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MatthewBerman/status/2065601391117361553">View @MatthewBerman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“self-inflicted. this would have NEVER happened if anthropic didn't make such a big deal about mythos being dangerous.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@MatthewBerman argues that Anthropic brought negative attention on itself by publicly flagging 'Mythos' as dangerous, implying the backlash was avoidable.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MatthewBerman/status/2065601391117361553" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PopDetective</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2343 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PopDetective/status/2065519138702024900">View @PopDetective on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is a scam. It's a move to socialize the risk and inevitable massive losses of an unprofitable company, to shift the burden from billionaires onto the backs of ordinary people and eventually to ta”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An X user claims Anthropic and OpenAI are financially unsustainable and are offloading risk onto the public and taxpayers.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/PopDetective/status/2065519138702024900" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
