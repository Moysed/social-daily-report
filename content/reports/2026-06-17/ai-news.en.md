---
type: social-topic-report
date: '2026-06-17'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-06-17T15:10:08+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 242
salience: 0.5
sentiment: mixed
confidence: 0.5
tags:
- open-weights
- glm-5.2
- model-access
- devtools
- ai-policy
- model-portability
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2067212364966141952/img/B2iaJKQdjOI4kZVb.jpg
---

# AI News & New Skills — 2026-06-17

## TL;DR
- GLM-5.2 (Z.ai/Zhipu) launched open-weights and ranks #1 open model / ~4th overall on the Artificial Analysis Intelligence Index (score 51), reportedly trained on Huawei Ascend chips (no Nvidia) for ~$25m and ~90% cheaper than peers [41][43][59][60].
- OpenAI's Codex App, CLI and SDK run with any open-source model, not only OpenAI's — relevant for model-agnostic agent tooling [2].
- Recurring (unconfirmed) social reports of US political pressure on Claude access: Macron pressing G7 for a workaround, frontier-lab CEOs (Amodei, Altman) meeting on model access [23][31][40][42].
- Wipro opened an Anthropic Claude AI center in Bengaluru and plans to train 10,000 staff on Claude [11][34][36].
- WP VIP 'Future of the Web 2026' report: 60% of US consumers say 'AI' in brand messaging is a turnoff [37]. Caveat: most high-engagement items today are noise — a Thai actor named 'Gemini' fandom and crypto spam — not AI artifacts.

## What happened
Signal density was low. The bulk of top-engagement items are unrelated: a Thai celebrity/BL fandom around an actor named 'Gemini' [1][3][5][6][7][8][9][10][12][14][15][19][20][22][24][26][28][38][48][53] and crypto/get-rich spam [44][52][55][56]. Within the genuine AI items, the clearest concrete drop is GLM-5.2, an open-weights model from Z.ai that topped open models and placed ~4th overall on Artificial Analysis (score 51), with claims it was trained on Huawei Ascend chips for ~$25m and is ~90% cheaper [41][43][59][60]. OpenAI noted Codex (App/CLI/SDK) works with any open-source model [2]. Anthropic-adjacent items dominate the policy thread: Wipro's Bengaluru Claude center and 10,000-person training plan [11][34][36], and several speculative posts about US restrictions on Claude access and CEO/G7 discussions [23][31][40][42].

## Why it matters (reasoning)
Two threads matter for a studio building AI into edutech and apps. First, open-weights quality keeps rising while cost falls: GLM-5.2's reported $25m training run on a fully Chinese (Huawei Ascend) stack at ~90% lower cost [59], plus its AA ranking [41][60], means a credible cheaper option for backend inference in e-learning/app features versus closed Claude/GPT pricing. Codex accepting any open model [2] reinforces that agent tooling is decoupling from a single vendor. Second, the Claude-access posts [23][31][40][42] — though unverified tweets/prediction-market chatter — point at provider/geopolitical risk; an offshore Chiang Mai studio relying on one US model could face access or pricing disruption, so a provider-agnostic abstraction is prudent. Separately, the 60%-AI-turnoff data [37] is a direct input for how to (not) label AI features in edutech marketing.

## Possibility
Likely: open-weights models continue closing the gap and getting cheaper, given GLM-5.2's trajectory and corroboration from a credible third-party benchmark [41][59][60]. Plausible: some friction on Claude access materializes, given repeated reports of political pressure and CEO meetings [40][23][31] — but these are unconfirmed social posts, so treat as a risk to monitor, not a fact. Unlikely-without-verification: the claim that Anthropic open-sourced 'the entire Wall Street workflow' (DCF/LBO/KYC) for free [45] — single hyped source, confirm before relying on it. No source gives numeric probabilities except [37]'s 60% turnoff figure.

## Org applicability — NDF DEV
1) Run a small eval of GLM-5.2 (open-weights) for non-critical inference in edutech/app features and internal tooling to compare cost/quality vs current Claude/GPT use — effort med [41][43][59]. 2) Keep AI integrations behind a provider-agnostic interface so models can be swapped if Claude access or pricing shifts — effort med, justified by access-risk posts [23][40]. 3) If anyone uses Codex CLI, test pointing it at an open/self-hosted model — effort low [2]. 4) Apply the 60%-turnoff finding to app/edutech marketing: describe features by outcome rather than foregrounding 'AI' labeling — effort low [37]. 5) Trial Google's free chat-based AI video editor for game trailers/marketing clips — effort low, but verify it exists/availability [54]. Skip: the Anthropic finance-workflow artifact [45] (not relevant to games/XR and unverified), the 'threaten the model' prompt trick [51] (no evidence, dubious), and all fandom/crypto items.

## Signals to Watch
- Open-weights leadership and cost: watch whether GLM-5.2's Ascend-trained, ~90%-cheaper claim holds up in independent testing [41][59].
- Claude access/geopolitics: confirm whether US restrictions or G7 'workarounds' move beyond social rumor [23][40].
- Tooling gap: no good cross-tool (Claude Code/Codex/Cursor) thread search yet — shadcn flagged it; an internal fix could help the team [46].
- Google's chat-driven video editor as a CapCut alternative for marketing content — verify launch and access [54].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **rxi/microui** — MicroUI – A tiny, portable, immediate-mode UI library written in ANSI C | radar | <https://github.com/rxi/microui> |
| **freeCodeCamp/freeCodeCamp** — freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer scienc | rss | <https://github.com/freeCodeCamp/freeCodeCamp> |
| **swc-project/swc** — Rust-based platform for the Web Make the web (development) faster. SWC (stands for Speedy Web Compil | rss | <https://github.com/swc-project/swc> |
| **teslamate-org/teslamate** — A self-hosted data logger for your Tesla 🚘 [main maintainer=@JakobLichterfeld]TeslaMate A powerful,  | rss | <https://github.com/teslamate-org/teslamate> |
| **iptv-org/iptv** — Collection of publicly available IPTV channels from all over the worldIPTV Collection of publicly av | rss | <https://github.com/iptv-org/iptv> |
| **puppeteer/puppeteer** — JavaScript API for Chrome and FirefoxPuppeteer Puppeteer is a JavaScript library which provides a hi | rss | <https://github.com/puppeteer/puppeteer> |
| **meshery/meshery** — Meshery, the cloud native manager If you like Meshery, please ★ this repository to show your support | rss | <https://github.com/meshery/meshery> |
| **cypress-io/cypress** — Fast, easy and reliable testing for anything that runs in a browser. Documentation / Changelog / Roa | rss | <https://github.com/cypress-io/cypress> |
| **music-assistant/server** — Music Assistant is a free, opensource Media library manager that connects to your streaming services | rss | <https://github.com/music-assistant/server> |
| **Universal-Debloater-Alliance/universal-android-debloater-next-generation** — Cross-platform GUI written in Rust using ADB to debloat non-rooted Android devices. Improve your pri | rss | <https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation> |
| **OpenBMB/VoxCPM** — VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-L | rss | <https://github.com/OpenBMB/VoxCPM> |
| **alibaba/zvec** — A lightweight, lightning-fast, in-process vector database English / 中文 🚀 Quickstart / 🏠 Home / 📚 Doc | rss | <https://github.com/alibaba/zvec> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | RRinda6 | ^4121 c2 | [(1/3) 🐻: Good evening everyone, so glad to meet y’all. Earlier, I phoned to Gemi](https://x.com/RRinda6/status/2067212506096103440) |
| x | thsottiaux | ^3466 c278 | [Reminder that you can use the Codex App, CLI and SDK with any open source model,](https://x.com/thsottiaux/status/2067181377028538431) |
| x | aydellch | ^3280 c1 | [Fotfot turn is to say the line with 'angry voice', he hesitated to choose Gemini](https://x.com/aydellch/status/2067215427672101008) |
| x | ergoquerencia | ^2652 c4 | [https://t.co/q0coJOoFxR they were talking about "size diff" but gf + ppw didn't ](https://x.com/ergoquerencia/status/2067222787756900729) |
| x | MarziaRahman55 | ^2526 c2 | [~ #WilliamEst #williamjkp ~ PondPhuwin & Gemini appreciating William's hardwork🥹](https://x.com/MarziaRahman55/status/2067161006519042076) |
| x | nongsiii | ^1756 c2 | [choose someone to be angry at 4️⃣: need to be angry, right? 4️⃣: *looked at gem*](https://x.com/nongsiii/status/2067218521432678701) |
| x | softforg4 | ^1530 c0 | [oh the teams being "nani, fourth, phuwin" and "sky, gemini, pond"... this puppyk](https://x.com/softforg4/status/2067218214573256973) |
| x | nongsiii | ^1367 c1 | [FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเปิดบ้านGrabFood #GeminiFourth #เจมีไนน](https://x.com/nongsiii/status/2067219972145959150) |
| x | aydellch | ^1246 c0 | [Even Gemini as cake is cute in Fourth's eyes 😭🤏🏻🤏🏻 FRIENDS OF GRAB OPEN HOUSE #F](https://x.com/aydellch/status/2067230709681619025) |
| x | nongsiii | ^1231 c2 | [Birthday blessing for Gemini 4️⃣: I wish Gemini to have strong health, to have h](https://x.com/nongsiii/status/2067232431074365919) |
| x | IndianTechGuide | ^962 c46 | [🚨 Wipro has opened an applied AI center in Bengaluru focused on Anthropic's Clau](https://x.com/IndianTechGuide/status/2067238388910965016) |
| x | ttfotgem | ^955 c0 | ["are they still making out till now?" he is crazy for saying that look at fourth](https://x.com/ttfotgem/status/2067187143726743807) |
| radar | Cider9986 | ^909 c476 | [GrapheneOS has been ported to Android 17](https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon) |
| x | centralparkBKK | ^900 c7 | [Happy birthday to Phuwin Gemini Sky🎂🤍 FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเ](https://x.com/centralparkBKK/status/2067230762437583194) |
| x | jjforgf | ^891 c0 | [They looked nonchalant after doing that right but look at Fourth 😆😆 he's shy and](https://x.com/jjforgf/status/2067225889289740344) |
| x | ttfotgem | ^868 c0 | [gemini after the bathroom scene. bro was zoning out https://t.co/3ES5yMQViF](https://x.com/ttfotgem/status/2067183699246895565) |
| x | kapsology | ^836 c27 | [WTF is training on Anthropic models? 😂😂😂](https://x.com/kapsology/status/2067135468467277973) |
| x | WilliamsRuto | ^831 c153 | [On the margins of the G7 Leaders’ Summit, I held discussions with OpenAI Chief E](https://x.com/WilliamsRuto/status/2067208801049051286) |
| x | naranest08 | ^761 c0 | [Word Guessing Game / Team: Sky, Gemini, Pond Q:​Right now, what are you to GrabF](https://x.com/naranest08/status/2067218402813653223) |
| x | geminiscity | ^752 c0 | [FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเปิดบ้านGrabFood ♊️: Sawadeekrub, I'm G](https://x.com/geminiscity/status/2067208368687878623) |
| x | ThePrimeagen | ^741 c48 | [Sacrebleu! This new model is insane https://t.co/z1nuDnW55v](https://x.com/ThePrimeagen/status/2067127546676953322) |
| x | aydellch | ^722 c0 | [Fourth's wish for Gemini 🤍 FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเปิดบ้านGrab](https://x.com/aydellch/status/2067232899380994218) |
| x | Polymarket | ^704 c82 | [NEW: Macron is reportedly pressing G7 leaders &amp; tech CEOs for a workaround t](https://x.com/Polymarket/status/2067232291395661848) |
| x | BRNarawins | ^701 c1 | [Gemini is Pond’s loved one… alright 😌👀 FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrab](https://x.com/BRNarawins/status/2067216991862018331) |
| x | shoguncheang | ^622 c0 | [Phuwin said he ask Progress about his ages and Pond said he is 8 years younger t](https://x.com/shoguncheang/status/2067156759102566413) |
| x | misswinmetawin | ^611 c0 | [gemini is so narawins coded im cryingggsgdgdg 😭 FRIENDS OF GRAB OPEN HOUSE #Frie](https://x.com/misswinmetawin/status/2067217866525651146) |
| x | Kenyans | ^558 c43 | [President Ruto and OpenAI CEO Sam Altman hold talks on establishing OpenAI Acade](https://x.com/Kenyans/status/2067220274525647186) |
| x | geminiscity | ^554 c0 | [Fourth is playing with the nose of mini Gemini on the cake 🥹🤏🏻 FRIENDS OF GRAB O](https://x.com/geminiscity/status/2067230945443565979) |
| x | etherXwave | ^542 c9 | [Things have never been better, actually. “We have Claude, we have phones, we hav](https://x.com/etherXwave/status/2067119380400415030) |
| x | BritIndianVoice | ^532 c13 | [China’s online war against India — documented facts: 🤖 23,750+ fake accounts rem](https://x.com/BritIndianVoice/status/2067169865358549247) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RRinda6</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4121 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RRinda6/status/2067212506096103440">View @RRinda6 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“(1/3) 🐻: Good evening everyone, so glad to meet y’all. Earlier, I phoned to Gemini &amp;amp; said I’d buy Grab…it’s not what you assume, I didn’t want to buy something on Grab ♊️: Then what? 🐻: I want the”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A celebrity or public figure shared a joke about wanting to buy the entire Grab company, posted as part of a Grab Food promotional open house event.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RRinda6/status/2067212506096103440" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@thsottiaux</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3466 · 💬 278</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/thsottiaux/status/2067181377028538431">View @thsottiaux on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Reminder that you can use the Codex App, CLI and SDK with any open source model, not just with OpenAI models. https://t.co/spPifB4ck3”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>OpenAI's Codex App, CLI, and SDK accept any open-source model as the backend, not only OpenAI's own models.</dd>
      <dt>Why interesting</dt>
      <dd>The studio can run Codex tooling against a self-hosted open-source model, cutting API costs and removing vendor dependency for code-gen workflows.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Point Codex CLI at a local open-source model (e.g., Qwen-Coder or Llama) and benchmark output quality against cost for the team's daily coding tasks.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/thsottiaux/status/2067181377028538431" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aydellch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3280 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aydellch/status/2067215427672101008">View @aydellch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Fotfot turn is to say the line with 'angry voice', he hesitated to choose Gemini as the partner bcs he doesn't want to be mad at him 😭 FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเปิดบ้านGrabFood #Gemini”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Thai celebrity fan-event post about actor Fourth hesitating to say an angry line because his AI partner is named 'Gemini' — purely entertainment content with no tech substance.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aydellch/status/2067215427672101008" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ergoquerencia</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2652 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ergoquerencia/status/2067222787756900729">View @ergoquerencia on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/q0coJOoFxR they were talking about &quot;size diff&quot; but gf + ppw didn't understand so p'godji made sknn stand together in the middle 😭 p'godji: ah sky stand in the middle, nani stand in the mi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan account shared a comedic K-pop fan-event clip where the Thai word 'ไส้ดิบ' (raw intestine) was misheard as 'size diff' during a group photo arrangement.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ergoquerencia/status/2067222787756900729" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MarziaRahman55</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2526 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MarziaRahman55/status/2067161006519042076">View @MarziaRahman55 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“~ #WilliamEst #williamjkp ~ PondPhuwin &amp; Gemini appreciating William's hardwork🥹🙏🏻 Phu: Wait, did WilliamEst stay overnight, na? Pond: WilliamEst went back earlier.. Gem: They're heading to Frankfurt ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Thai celebrity fan post celebrating actor/idol William's busy schedule and Aston Martin purchase, with no tech or industry content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MarziaRahman55/status/2067161006519042076" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nongsiii</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1756 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nongsiii/status/2067218521432678701">View @nongsiii on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“choose someone to be angry at 4️⃣: need to be angry, right? 4️⃣: *looked at gem* i also dont want to be mad at you (🤭) ♊️: try it once (🫪) 4️⃣: then i choose Gemini FRIENDS OF GRAB OPEN HOUSE #Friends”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Thai celebrity fan post about GeminiFourth (a Thai actor/idol duo) at a Grab Food event — no tech content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nongsiii/status/2067218521432678701" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@softforg4</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1530 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/softforg4/status/2067218214573256973">View @softforg4 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“oh the teams being &quot;nani, fourth, phuwin&quot; and &quot;sky, gemini, pond&quot;... this puppykitty division !! FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเปิดบ้านGrabFood https://t.co/4Y0HJmfUsA”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan post reacting to Thai celebrity group pairings at a GrabFood promotional event called Friends of Grab Open House.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/softforg4/status/2067218214573256973" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nongsiii</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1367 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nongsiii/status/2067219972145959150">View @nongsiii on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเปิดบ้านGrabFood #GeminiFourth #เจมีไนน์โฟร์ท should be angy 😹🤏🏻 4️⃣: i’m hungry!! order grab for me! are you going to order it or not? 😼 ♊️: i’m not ordering!”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan post from a GrabFood celebrity open house event featuring Thai entertainers, with no technical content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nongsiii/status/2067219972145959150" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
