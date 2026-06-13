---
type: social-topic-report
date: '2026-06-13'
topic: multimodal-ai
lang: en
pair: multimodal-ai.th.md
generated_at: '2026-06-13T03:42:49+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 157
salience: 0.6
sentiment: mixed
confidence: 0.5
tags:
- video-generation
- image-generation
- comfyui
- open-weights
- text-to-video
- asset-pipeline
thumbnail: https://pbs.twimg.com/media/HKi1tA1XgAAF1Qp.jpg
---

# Multimodal AI — 2026-06-13

## TL;DR
- Midjourney made V8.1 the default for all users, will deprecate V8 in two weeks, and says V8.2 is entering testing 'extremely soon' [7]; separately it reports 20M registered vs ~1M paying, with 19M churned after the free tier ended [19].
- A wave of low-cost hosted video models is converging: India's Varya (Avataar) claims $0.01/second and 4 inference steps instead of 50 [17][44], and multiple posts circulate rumors of a cheap Dreamina 'Seedance 2.0 mini' release within a week [32][37][40][60].
- ComfyUI is the recurring production-pipeline layer: an LLM-to-bounding-box/JSON workflow for image setup [10] and a 'Playblast → finished shot' workflow using Seedance 2.0 with no traditional render pipeline [13].
- LTX 2.3 added Multiple Subject Reference (up to 5 images, e.g. 2 characters + background) with claimed no face-mixing [29] — relevant because LTX ships open weights.
- Runway is deepening its Lionsgate partnership into a joint original-IP development program [5][22] and held a sold-out AI Festival at Lincoln Center [21][34]; current image/video stack named across creators is GPT Image 2, Nano Banana 2, Veo 3.1 Fast, and Ray 3.14 [27][33].

## What happened
On the image side, Midjourney promoted V8.1 to default for all users, set V8 for deprecation in two weeks, and flagged V8.2 for imminent testing [7]; a separate post claims 20M registered users, ~1M paying, and 19M churned after the free tier was removed [19]. GPT Image 2, Google's Nano Banana 2, and Midjourney are the image models creators cite [11][27][35], with Adobe offering a free daily tier (5 images, 2 videos) spanning Nano Banana 2, GPT Image 2, Veo 3.1 Fast, and Ray 3.14 [33]. On video, low-cost models dominate the chatter: Varya from Avataar markets $0.01/second and a 50→4 step reduction [17][44], Kling 3.0 is being promoted for high-volume UGC ad generation [16][26][57], and several accounts amplify rumors of a cheap Dreamina Seedance 2.0/mini release next week [32][37][40][60].

## Why it matters (reasoning)
Two trends matter for production pipelines. First, the orchestration layer is consolidating around ComfyUI: structured-JSON/bounding-box prompting [10] and playblast-to-finished-shot rendering with Seedance 2.0 [13] show video/image models being wired into deterministic, repeatable workflows rather than one-off chat demos — the form that actually feeds game and XR asset work. Second, video generation is in active price compression, with explicit per-second pricing ($0.01/s [17][44]) and rumored cheap model drops [40][60]; if real, this lowers the cost of edutech motion visuals and animatics. The Midjourney churn figure [19] is a caution: free-tier removal collapsed its user base ~20x, signaling that hosted-tool lock-in is fragile and that open-weights options (LTX 2.3 [29], the claimed 117k-star local tool generating images/video/3D/audio [41]) are worth keeping as fallbacks. Most volume in the feed is marketing claims, rumors, and generic '100+ tools' lists [23][36][39][45][55], not verified releases.

## Possibility
Continued video price/step cuts are likely given multiple independent low-cost signals ([17][44] confirmed launch claim; [40][60] rumored) — though specific Dreamina/Seedance timing is unverified rumor and should be treated as plausible, not certain. Open-weights multi-subject video reference (LTX 2.3 [29]) becoming usable for consistent characters/scenes in real pipelines is plausible, since it ships weights rather than a closed demo. A Midjourney free/cheap tier return is plausible given the stated 19M churn problem [19], but no source confirms it. Marketing claims like Kling 3.0 '$1/video, 550/day' [16][26] are unlikely to hold at quality once tested, as no independent benchmark is provided.

## Org applicability — NDF DEV
1) Evaluate ComfyUI as the asset-gen orchestration layer for Unity/XR — node graphs that emit structured JSON/bounding boxes [10] and playblast-to-render flows [13] fit concept art, backgrounds, and animatics; effort med. 2) Test LTX 2.3 open weights for character/scene consistency (up to 5 references, claimed no face-mixing [29]) — useful for edutech characters that must stay on-model across shots; effort med. 3) Trial affordable hosted video for edutech visuals — benchmark Varya at $0.01/s [17][44] against Veo 3.1 Fast and Ray 3.14 from Adobe's free tier [33]; effort low (hosted APIs). 4) Keep using Midjourney V8.1 for concept art but re-test prompt/sref libraries now, since V8 deprecates in two weeks [7]; effort low. Skip: the UGC ad-farm pipelines [16][26][57], the generic '100+/120+ AI tools' lists [23][36][39][45][55][58], and unverified Seedance release rumors [32][37][40][60] until a real API/pricing page exists.

## Signals to Watch
- Dreamina 'Seedance 2.0 mini' rumored for release within ~a week — watch for an actual API and per-second price, not just leak posts [37][60].
- Midjourney V8.2 entering testing 'extremely soon' with V8 deprecating in two weeks [7].
- Runway × Lionsgate joint original-IP development program — a licensed-studio model for generative video [5][22].
- LTX 2.3 Multiple Subject Reference (5 images, no face-mixing) as an open-weights option for production consistency [29].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Suhail | ^12913 c69 | [My favorite @elonmusk quote that I often send friends: Do not fear losing. “You ](https://x.com/Suhail/status/2065476904543481907) |
| x | EMostaque | ^971 c22 | [So looks like @SpaceX will spend 2.5% of its market cap to buy @cursor_ai at 15x](https://x.com/EMostaque/status/2065514350090059901) |
| x | tan_stack | ^826 c31 | [TanStack AI is now in Beta! TanStack AI is no longer just a text-generation libr](https://x.com/tan_stack/status/2065102675390189916) |
| x | Suhail | ^624 c20 | [Priorities for high agency people are almost always communicated by the latency ](https://x.com/Suhail/status/2065127494014120056) |
| x | runwayml | ^343 c43 | [Today, we’re deepening our partnership with Lionsgate with a slate of new initia](https://x.com/runwayml/status/2065072377596088525) |
| x | gurniaiart | ^297 c0 | [Knight art #AIArt #AIイラスト #midjourney #AIgirl #knight #aiGallery https://t.co/20](https://x.com/gurniaiart/status/2065067622610145360) |
| x | midjourney | ^280 c28 | [We've made V8.1 the new default model for all users on Midjourney. V8 will now b](https://x.com/midjourney/status/2064921117618557292) |
| x | Suhail | ^238 c7 | [SpaceX feels like a bet on rooting for humanity's grand ability to invent, thriv](https://x.com/Suhail/status/2065472394156773705) |
| x | bull_bnb | ^234 c33 | [AI data was big because models needed the internet. Robot data will be bigger be](https://x.com/bull_bnb/status/2065131071252103412) |
| x | hellorob | ^229 c8 | [The only thing worse than looking at a blank canvas is prompting with JSON. Here](https://x.com/hellorob/status/2065209723184676973) |
| x | AvelyrahnAI | ^215 c29 | [Created with GPT Image 2 on Chatgpt Prompt: Create image Here's a cleaner, optim](https://x.com/AvelyrahnAI/status/2065383336722493531) |
| x | Suhail | ^197 c13 | [I’ve enjoyed this prompt for learning more than I thought I would: Teach me this](https://x.com/Suhail/status/2065103647848157369) |
| x | ComfyUI | ^190 c7 | [Seedance Playblast 2 Render Demo: VFX artist @heydoughogan built a workflow in C](https://x.com/ComfyUI/status/2065217065490034775) |
| x | Endory2 | ^188 c5 | [KH4 sora is weirdly AI Upscaled btw. KH4 does not look like this. And I am not t](https://x.com/Endory2/status/2065176708836217258) |
| x | sunaiuse | ^174 c28 | [1 guy in China made $1,000,000 last year. No employees. No code. Just AI and a v](https://x.com/sunaiuse/status/2065183221135069232) |
| x | FynCas | ^171 c93 | [MakeUGC & Kling 3.0 = 550 videos/day Fully realistic UGC ads — cinematic lightin](https://x.com/FynCas/status/2065071656100298813) |
| x | kingofknowwhere | ^168 c13 | [India just launched it's first video AI model Varya. (@Avataar) It is marketted ](https://x.com/kingofknowwhere/status/2065352682328690689) |
| x | Tanaypawar27 | ^156 c31 | [Best accounts to follow from each frontier lab to stay constantly up to date Ant](https://x.com/Tanaypawar27/status/2064920550418645252) |
| x | ekinoks_26 | ^155 c160 | [Midjourney has 20 million registered users. Roughly 1 million pay. The other 19 ](https://x.com/ekinoks_26/status/2064950762715951536) |
| x | treyisforever | ^150 c0 | [@cihywastaken @ctrlkugi ai image generation has been around publicly since 2020 ](https://x.com/treyisforever/status/2065118866943176709) |
| x | c_valenzuelab | ^146 c16 | [Yesterday, we hosted our 4th Annual AI Festival at Lincoln Center in NYC, our bi](https://x.com/c_valenzuelab/status/2065417356986208632) |
| x | c_valenzuelab | ^145 c19 | [Excited to announce that we’re expanding our partnership with Lionsgate through ](https://x.com/c_valenzuelab/status/2065081068630282541) |
| x | Bhanusinghyede | ^144 c21 | [🚀 𝟏𝟐𝟎 𝐌𝐢𝐧𝐝-𝐁𝐥𝐨𝐰𝐢𝐧𝐠 𝐀𝐈 𝐓𝐨𝐨𝐥𝐬 𝐘𝐨𝐮 𝐒𝐡𝐨𝐮𝐥𝐝 𝐊𝐧𝐨𝐰 𝐢𝐧 𝟐𝟎𝟐𝟔 Most people know 5–10 tools…](https://x.com/Bhanusinghyede/status/2065036535645470797) |
| x | kellyeld | ^143 c15 | [‘Beautiful Pink Heart’ Lyrics by me. About a tough time in my life many years ag](https://x.com/kellyeld/status/2065444518426734700) |
| x | GlitterPixely | ^142 c25 | ["Oh! it's you!"🤭I found the cutest sref so had to test it! Prompt below, too ₍ᐢ.](https://x.com/GlitterPixely/status/2065294658532442368) |
| x | spwfeijen | ^142 c79 | [Kling 3.0 = 550 videos per day Fully-realistic UGC ads — cinematic lighting, hum](https://x.com/spwfeijen/status/2065056560154370451) |
| x | churvikv | ^141 c53 | [Northern lights and neon reefs Created in @Somake_ai Model: Midjourney Experimen](https://x.com/churvikv/status/2065155683301917132) |
| x | avidseries | ^140 c21 | [A lot of people follow AI more closely than I do, but almost everything I'm read](https://x.com/avidseries/status/2065446869652652106) |
| x | sunbaolong_2001 | ^136 c2 | [LTX 2.3 just reached "Omni-Reference" level! 🎬🔥 The new MSR (Multiple Subject Re](https://x.com/sunbaolong_2001/status/2065098450333839446) |
| x | EMostaque | ^136 c8 | [Thanks @elder_plinius 😂 https://t.co/n6Ff9zJHyv](https://x.com/EMostaque/status/2065605506165518722) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Suhail</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 12913 · 💬 69</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Suhail/status/2065476904543481907">View @Suhail on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“My favorite @elonmusk quote that I often send friends: Do not fear losing. “You will lose,” Musk says. “It will hurt the first fifty times. When you get used to losing, you will play each game with le”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>User shares an Elon Musk quote about embracing loss to become more fearless and willing to take risks.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Suhail/status/2065476904543481907" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EMostaque</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 971 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EMostaque/status/2065514350090059901">View @EMostaque on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“So looks like @SpaceX will spend 2.5% of its market cap to buy @cursor_ai at 15x revenue 👀”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>EMostaque reports SpaceX is set to acquire Cursor AI at ~15x revenue, a deal worth roughly 2.5% of SpaceX's market cap.</dd>
      <dt>Why interesting</dt>
      <dd>Cursor is a primary AI coding tool for many dev teams; SpaceX ownership shifts who controls its roadmap and pricing direction.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Track Cursor roadmap announcements after the deal closes; if focus shifts toward enterprise, evaluate Windsurf or VS Code + Copilot as fallbacks.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EMostaque/status/2065514350090059901" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@tan_stack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 826 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/tan_stack/status/2065102675390189916">View @tan_stack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“TanStack AI is now in Beta! TanStack AI is no longer just a text-generation library with extras bolted on. TanStack AI has first-class dev experience for: ✅ Text and Streaming Structured Data ✅ Tool C”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>TanStack AI entered Beta as a unified JS/TS generative-AI library covering text, tool calls, image/video/audio generation, realtime voice, MCP hosting, and orchestration — all with per-model type-safety.</dd>
      <dt>Why interesting</dt>
      <dd>One typed library covering the full generative AI surface removes the need to stitch multiple SDKs together in web or e-learning projects with AI features.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Pilot TanStack AI as the AI integration layer in the studio's next web project, especially where multimodal output or voice chat is scoped.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/tan_stack/status/2065102675390189916" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Suhail</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 624 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Suhail/status/2065127494014120056">View @Suhail on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Priorities for high agency people are almost always communicated by the latency of their response.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The author claims that high-agency people signal their priorities by how quickly they respond to messages.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Suhail/status/2065127494014120056" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@runwayml</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 343 · 💬 43</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/runwayml/status/2065072377596088525">View @runwayml on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Today, we’re deepening our partnership with Lionsgate with a slate of new initiatives, including a joint development program focused on creating original IP together. Learn more at the link below. htt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Runway ML and Lionsgate are expanding their partnership to co-develop original IP, going beyond tooling access into a joint creative production program.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/runwayml/status/2065072377596088525" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gurniaiart</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 297 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gurniaiart/status/2065067622610145360">View @gurniaiart on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Knight art #AIArt #AIイラスト #midjourney #AIgirl #knight #aiGallery https://t.co/20cs9inIha”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An X user posted an AI-generated knight illustration made with Midjourney, tagged under #AIArt and #aiGallery with 297 likes.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gurniaiart/status/2065067622610145360" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@midjourney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 280 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2064921117618557292">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We've made V8.1 the new default model for all users on Midjourney. V8 will now be deprecated in 2 weeks. V8.2 will start testing extremely soon.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney promoted V8.1 to default for all users effective immediately, retiring V8 in 2 weeks, with V8.2 entering testing shortly after.</dd>
      <dt>Why interesting</dt>
      <dd>Any workflow or script that pins Midjourney V8 explicitly will break in 2 weeks; V8.1 output style differs and can shift concept-art or asset results.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Check all Midjourney API calls and saved prompts that target V8 and update them to V8.1 before the 2-week deprecation window closes.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/midjourney/status/2064921117618557292" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Suhail</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 238 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Suhail/status/2065472394156773705">View @Suhail on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“SpaceX feels like a bet on rooting for humanity's grand ability to invent, thrive, and far surpass our wildest imaginations. Bravo to you all that made this happen.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@Suhail posted a congratulatory message praising SpaceX for an unspecified achievement, framing it as a win for human ingenuity.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Suhail/status/2065472394156773705" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
