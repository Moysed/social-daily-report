---
type: social-topic-report
date: '2026-06-20'
topic: audio-ai
lang: en
pair: audio-ai.th.md
generated_at: '2026-06-20T03:48:17+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 95
salience: 0.6
sentiment: mixed
confidence: 0.58
tags:
- audio-ai
- tts
- music-generation
- licensing
- multilingual
- voice-cloning
thumbnail: https://pbs.twimg.com/media/HLHMUUhbsAA1r6D.jpg
---

# Audio AI — 2026-06-20

## TL;DR
- Grok TTS scored 96/100 on Vapi's blind Humaneness Index, ranked #1 among voice models and beating ElevenLabs; a real human scores 100 [2][40][46].
- The Atlantic published a searchable database of copyrighted songs used to train Suno and Udio; multiple independent artists (Quadeca ~295 grabs across 8 datasets, Logic, others) say their catalogs were scraped without consent [4][5][16][18][19].
- Rumik AI's Silk Mulberry 1.5 (India) claims ~95% lower cost than ElevenLabs at ₹0.40/min with Hindi/English mid-sentence code-switching [11].
- ElevenLabs raised a round with the Polish state (via Vinci/BGK) joining Sequoia, a16z, ICONIQ, and ran a voice-only retail pop-up in NYC [14][47].
- TTS is moving into app builders and local stacks: Lovable added TTS/STT, Kokoro runs TTS locally, and Google showed Gemini 3.5 Live Translate across 70+ languages [13][33][54].

## What happened
Two distinct stories dominate Audio AI today. First, TTS/voice quality and access: Grok TTS topped Vapi's blind Humaneness Index at 96/100, ahead of ElevenLabs and 4 points below a human baseline [2][40][46]. Cheaper multilingual options appeared, notably Rumik AI's Silk Mulberry 1.5 at ~₹0.40/min with Hindi/English code-switching [11]. Voice features are spreading into tooling (Lovable TTS/STT [13]), local runtimes (Kokoro [54]), and real-time translation (Gemini 3.5 Live Translate, 70+ languages [33]). ElevenLabs took sovereign investment from Poland and opened a voice-ordering pop-up [14][47]. Second, music-generation legality: The Atlantic released a database tracking copyrighted songs used to train Suno and Udio, and many independent artists publicly claim their catalogs were scraped without consent or payment [1][3][4][5][8][16][18][19][42][53][59]. One artist notes absence from the leaked dataset does not prove a track was not used [19]. Much of the remaining feed is noise: the $TTS "TimeSoul" crypto-wellness token [32][34][41], generic AI-tool listicles [7][26][37][43], and faceless-YouTube monetization threads [30][50][55].

## Why it matters (reasoning)
For NDF DEV, the practical split is clear: TTS/voice is maturing fast and is safe to adopt, while AI music generation carries real licensing risk. Near-human TTS benchmarks [2][46] plus price competition from new labs [11] and builder/local integrations [13][54] mean narration for edutech and in-game lines is increasingly cheap and easy to source — but the benchmarks are self-reported via single sources (Vapi index, vendor posts), and none of the items validate Thai quality, which is a core requirement. On the music side, the scraping controversy and The Atlantic database [4][8][16][19] make commercial use of Suno/Udio output legally uncertain: labels were paid in prior suits while artists were not [8], and provenance is murky [19]. A second-order effect is platform consolidation and productization — sovereign money and retail experiments around ElevenLabs [14][47] signal voice is becoming infrastructure, which favors picking vendors with clear, written commercial terms over chasing benchmark leaders.

## Possibility
Likely: licensing uncertainty around Suno/Udio persists in the near term, given the public training-data database, multiple artist claims, and prior label litigation [4][8][16][18][19] — commercial deliverables built on their output stay legally exposed. Plausible: TTS quality keeps converging toward human parity (96 vs 100 [2][46]) and price pressure from labs like Rumik pushes incumbent pricing down [11]. Plausible: ElevenLabs expands from API into broader voice products and regional/sovereign deals [14][47]. Unlikely to claim from today's evidence: a named, validated high-quality Thai TTS/voice-clone option — no item addresses Thai specifically, so treat Thai support as unverified. No source gives numeric probabilities, so none are asserted here.

## Org applicability — NDF DEV
Actions: (1) Benchmark Grok TTS [2][46] and ElevenLabs [14][47] head-to-head for edutech narration and in-game voice, scoring Thai and English specifically since no item validates Thai — effort med. (2) Trial Silk Mulberry 1.5 for cost-sensitive multilingual narration and confirm whether Thai (not just Hindi/EN) and commercial licensing are supported [11] — effort low. (3) Stand up a local Kokoro TTS server for internal/dev tooling and privacy-sensitive drafts to cut per-minute cost [54] — effort low. (4) For web/mobile prototypes needing voice in/out, evaluate Lovable's built-in TTS/STT before wiring a separate vendor [13] — effort low. (5) Set a policy to avoid Suno/Udio for paid client cinematics and e-learning soundscapes until licensing clears; prefer libraries or models with written commercial terms [4][8][16][19] — effort low. (6) Watch Gemini 3.5 Live Translate for future multilingual edutech, pending Thai validation [33] — effort low. Skip: the $TTS/TimeSoul crypto items [32][34][41], AI-tool listicles [7][26][37][43], and faceless-YouTube monetization threads [30][50][55] — no production value.

## Signals to Watch
- Grok TTS public availability, pricing, and commercial license terms once it ships beyond the benchmark [2][46].
- Whether any music tool NDF considers appears in The Atlantic's leaked training-data database [16][19].
- Rumik Silk Mulberry's Thai support and commercial-use terms beyond the ₹0.40/min Hindi/EN claim [11].
- ElevenLabs productization signals (sovereign funding, retail voice) as a sign voice is becoming standardized infrastructure [14][47].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Rishhie | ^5023 c23 | [Apparently an AI music generation software has been trained on my music and 3 so](https://x.com/Rishhie/status/2067589593029820498) |
| x | XFreeze | ^1800 c221 | [Grok TTS is already sounding insanely human In Vapi’s blind voting Humaneness In](https://x.com/XFreeze/status/2067658361487921484) |
| x | DJSTTDJ | ^1211 c8 | [to everyone who thought my music sounded like ai slop, did you ever think it was](https://x.com/DJSTTDJ/status/2067512823513514294) |
| x | oralon | ^1163 c17 | [Suno &amp; other AI models are reportedly being used to scrape music catalogs as](https://x.com/oralon/status/2067606379322384702) |
| x | hyphen_c_ | ^979 c36 | [An overwhelming chunk of Quadeca’s catalog was scraped for training sets for Sun](https://x.com/hyphen_c_/status/2067506727277232362) |
| x | Timcast | ^956 c163 | [One big problem i find with AI is that as the owner of a large publicly visible ](https://x.com/Timcast/status/2067635844672799228) |
| x | abacusai | ^725 c49 | [🚨 Access 100+ AI Models On ChatLLM Smartly routes to the best model based on you](https://x.com/abacusai/status/2067833694665261522) |
| x | TheCamSteady | ^678 c11 | [All of my music has been stolen by AI companies. But we’ve known this. The CEO o](https://x.com/TheCamSteady/status/2068037066617991566) |
| x | PANOROM1883 | ^411 c70 | [Note #59: Taking care of your mental health Make peace with the hard days. I see](https://x.com/PANOROM1883/status/2067849957403513048) |
| x | kellyeld | ^410 c34 | [“Maybe Tomorrow” about all the promises we make to ourselves but might not keep.](https://x.com/kellyeld/status/2067970990899187737) |
| x | VaibhavSisinty | ^391 c2 | [This Indian AI lab built a voice model 95% cheaper than ElevenLabs. And it switc](https://x.com/VaibhavSisinty/status/2067608358551695632) |
| x | yabhishekhd | ^323 c16 | [🚨 Reliance AGM 2026: Here's everything that was announced today 👇 📄 Jio's IPO is](https://x.com/yabhishekhd/status/2067928761572684042) |
| x | Lovable | ^246 c15 | [Your app talks back. Lovable now supports text-to-speech and-speech-to-text, so ](https://x.com/Lovable/status/2067608317392732617) |
| x | mati | ^234 c15 | [The Polish state is taking a stake in @ElevenLabs. Through Vinci, part of the BG](https://x.com/mati/status/2067613148052406692) |
| x | 0xZephh | ^222 c130 | [Your portfolio gets tracked. Your screen time gets tracked. Your steps get track](https://x.com/0xZephh/status/2067610143777546635) |
| x | LinesofLogic | ^209 c5 | [The Atlantic leaked a searchable database tracking the exact copyrighted music u](https://x.com/LinesofLogic/status/2067614487104884940) |
| x | YellowRobotXYZ | ^193 c10 | [AI News - June 2026. New generation of LLMs for local use. Elevenlabs now as goo](https://x.com/YellowRobotXYZ/status/2067687865287319852) |
| x | VinceValholla | ^189 c13 | [Late last night I found out over 100+ songs from our catalog were used to train ](https://x.com/VinceValholla/status/2067766980279664993) |
| x | ednewtonrex | ^159 c6 | [An important point for musicians to be aware of: If your music is *not* included](https://x.com/ednewtonrex/status/2067884253904318719) |
| x | OfficialBTSM | ^143 c5 | [Just opened twitter for the first time in a while today, big mistake 😅 just seei](https://x.com/OfficialBTSM/status/2067786140254707899) |
| x | vikktorrrre | ^134 c60 | [this creator spends over $3,500 a month on ai models to maximise his content qua](https://x.com/vikktorrrre/status/2067555985913164065) |
| x | SultanNasir51 | ^128 c139 | [Mental health apps give you reminders. @timesoulcom gives you sustainable reward](https://x.com/SultanNasir51/status/2067906888390643877) |
| x | Musty_hasheedu | ^128 c132 | [Good morning Most apps are designed to keep you scrolling. @timesoulcom takes a ](https://x.com/Musty_hasheedu/status/2067807454725886405) |
| x | kokondukwe | ^124 c98 | [Happy Friday CT ☀️ I've always found it interesting how difficult it is to build](https://x.com/kokondukwe/status/2067840029439803896) |
| x | evrendag1284 | ^120 c97 | [What impressed me most about @timesoulcom wasn't actually the technology side. I](https://x.com/evrendag1284/status/2067819200555454966) |
| x | Aqib__786Ai | ^118 c44 | [Most people are still doing 10-hour tasks manually. Meanwhile, AI users are fini](https://x.com/Aqib__786Ai/status/2067621355991048489) |
| x | Connor_Quest | ^118 c4 | [The funny part of the AI suno scraping thing is there’s just some objectively as](https://x.com/Connor_Quest/status/2067648881312117153) |
| x | wannercashcow | ^116 c4 | [So simple to monetize this kind of content: Make music in Suno -> Distribute via](https://x.com/wannercashcow/status/2067543417744245185) |
| x | eigoasobi | ^112 c0 | [STEEL BALL CANON IX / Generative Artifact Pachelbel’s Canon in D Inspired by Ste](https://x.com/eigoasobi/status/2067917809422905821) |
| x | grundstromleo | ^109 c7 | [$25k/month faceless YT channel kit: - claude (scripts &amp; ideation) - nexlev (](https://x.com/grundstromleo/status/2067712303986827364) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Rishhie</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5023 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Rishhie/status/2067589593029820498">View @Rishhie on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Apparently an AI music generation software has been trained on my music and 3 songs I never even released to streaming platforms. Genuinely so disgusting”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Musician @Rishhie found an AI music generation tool was trained on her catalogue, including 3 songs never released to any streaming platform.</dd>
      <dt>Why interesting</dt>
      <dd>Unreleased tracks appearing in AI training sets shows data scrapers reach beyond public platforms — a concrete legal risk for studios using third-party audio AI tools.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Before integrating any audio AI tool, verify training data provenance and confirm the vendor's terms cover liability for unlicensed or non-public content.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Rishhie/status/2067589593029820498" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@XFreeze</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1800 · 💬 221</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/XFreeze/status/2067658361487921484">View @XFreeze on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Grok TTS is already sounding insanely human In Vapi’s blind voting Humaneness Index, Grok TTS ranked as the top AI voice model in the chart with a humaneness score of 96.....just 4 points below the re”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Grok TTS scored 96/100 on Vapi's blind Humaneness Index, ranking first among all tested AI voice models — 4 points below a recorded human voice benchmark.</dd>
      <dt>Why interesting</dt>
      <dd>Near-human TTS with low latency and low cost directly cuts voice recording budget for e-learning narration or XR/VR dialogue in the studio's projects.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a side-by-side test of Grok TTS against the studio's current TTS pipeline on one e-learning or XR narration script before the next voice recording session.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/XFreeze/status/2067658361487921484" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DJSTTDJ</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1211 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DJSTTDJ/status/2067512823513514294">View @DJSTTDJ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“to everyone who thought my music sounded like ai slop, did you ever think it was because Suno was using a dataset that contained 22 of my songs? it’s funny how there were no accusations of my music so”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A musician confirmed Suno's training dataset contains 22 of their copyrighted songs without consent, and claims AI output now mimics their style as a direct result.</dd>
      <dt>Why interesting</dt>
      <dd>Confirms Suno's dataset includes identifiable copyrighted tracks — using Suno-generated audio in commercial deliverables carries real IP liability.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio should avoid using Suno output in game audio or e-learning assets for clients until Suno's dataset legal status is resolved.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DJSTTDJ/status/2067512823513514294" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@oralon</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1163 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/oralon/status/2067606379322384702">View @oralon on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Suno &amp;amp; other AI models are reportedly being used to scrape music catalogs as training sets against artists’ wills. (via The Atlantic) Independent artists such as Quadeca, Jane Remover, Lucy Bedroq”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Suno and other AI music models are accused of scraping artists' catalogs without consent to build training sets, per a report in The Atlantic.</dd>
      <dt>Why interesting</dt>
      <dd>Studios using AI-generated music in commercial game or XR builds face copyright exposure if those tools trained on unlicensed catalogs.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Audit any AI music tools in active projects and document their licensing terms before delivering to clients.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/oralon/status/2067606379322384702" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@hyphen_c_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 979 · 💬 36</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/hyphen_c_/status/2067506727277232362">View @hyphen_c_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“An overwhelming chunk of Quadeca’s catalog was scraped for training sets for Suno and other Gen-AI models, presumably against his will 295 grabs across 8 known data sets from various releases, snippet”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Quadeca's catalog was scraped 295 times across 8 datasets to train Suno and other AI audio models — including lyrics from Genius — reportedly without his consent, per The Atlantic.</dd>
      <dt>Why interesting</dt>
      <dd>This confirms AI audio generators like Suno are built on scraped copyrighted content — a live legal liability for any team shipping products that use or embed these tools.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Before embedding Suno or similar AI audio tools in any studio project, audit the tool's ToS and legal exposure on training data origin.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/hyphen_c_/status/2067506727277232362" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Timcast</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 956 · 💬 163</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Timcast/status/2067635844672799228">View @Timcast on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One big problem i find with AI is that as the owner of a large publicly visible company I cannot use it for creative works GPT for instance sometimes refuses to create content for my company saying it”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>ChatGPT and Suno block the owner of a large public brand from generating or remixing his own company's content due to IP/trademark detection, while smaller unknown brands pass through freely.</dd>
      <dt>Why interesting</dt>
      <dd>Any studio with a public brand name risks false-positive IP blocks inside AI generation tools — the more visible the brand, the higher the chance of being locked out of your own assets.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a quick test: prompt Suno and ChatGPT with the studio's actual brand name and logo descriptions to see if IP filters block output before building any AI-assisted content pipeline around them.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Timcast/status/2067635844672799228" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@abacusai</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 725 · 💬 49</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/abacusai/status/2067833694665261522">View @abacusai on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 Access 100+ AI Models On ChatLLM Smartly routes to the best model based on your prompt Opus 4.8 - front-end GPT 5.5 - back-end coding Grok 4.5 - real-time Flash 3.5 - chat Nano Banana Pro - image Se”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Abacus AI's ChatLLM auto-routes prompts to the best model from 100+ options — ElevenLabs for voice, Seedance 2.0 for video, GPT-5.5 for backend code — via one interface.</dd>
      <dt>Why interesting</dt>
      <dd>One subscription covering voice, video, coding, and research models cuts the overhead of managing separate provider accounts for a small dev team.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Evaluate ChatLLM as a rapid-prototyping layer for projects that need voice or video AI without wiring multiple provider APIs separately.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/abacusai/status/2067833694665261522" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheCamSteady</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 678 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheCamSteady/status/2068037066617991566">View @TheCamSteady on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“All of my music has been stolen by AI companies. But we’ve known this. The CEO of Suno literally bragged about it in an interview last year. They were sued by the labels. The labels got paid. But the ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Musician @TheCamSteady asserts Suno trained on copyrighted music without consent; record labels settled the lawsuit but the model remains in use, and no law has changed.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheCamSteady/status/2068037066617991566" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
