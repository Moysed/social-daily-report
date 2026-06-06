---
type: social-topic-report
date: '2026-06-06'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-06-06T15:27:10+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 228
salience: 0.45
sentiment: mixed
confidence: 0.5
tags:
- ai-models
- open-source
- on-device-ai
- anthropic
- devtools
- rumor
thumbnail: https://pbs.twimg.com/media/HKHb-VdacAAe4E6.jpg
---

# AI News & New Skills — 2026-06-06

## TL;DR
- Google released Gemma 4 QAT (quantization-aware training) models tuned to run on mobile and laptop hardware [32].
- Microsoft open-sourced pg_durable, durable workflow execution running inside Postgres [24].
- Anthropic doubled Claude Cowork usage limits for all paid plans through July 5 [25].
- Rumor cluster: DeepSeek v4 said to be launched and cheap [2], GPT-5.6 'kindle-alpha' picked as release candidate [35], and a 'Claude Mythos 5' slug spotted in Dev Mode/API then pulled [7][19][48][53] — none officially confirmed.
- Most of today's feed is non-AI noise (Thai series actor named 'Gemini', painter 'Claude Monet', zodiac posts), so real signal is thin.

## What happened
Two concrete, verifiable artifacts landed: Google's Gemma 4 QAT models optimized via quantization-aware training for on-device (mobile/laptop) inference [32], and Microsoft's open-source pg_durable for in-database durable execution on Postgres [24]. On the operations side, Anthropic doubled Claude Cowork limits for paid plans until July 5 [25], and a NotebookLM teaser suggests multi-format file export, possibly paired with a Gemini 3.5 Flash release [33]. Microsoft AI also promoted MAI-Transcribe-1.5 as a transcription leader, citing an ArtificialAnalysis chart [44].

## Why it matters (reasoning)
The two real releases map directly to NDF DEV's stack. Gemma 4 QAT [32] matters for mobile apps and edutech that need offline or low-latency on-device inference instead of per-call API costs. pg_durable [24] matters if backend workflows run on Postgres (the session has a Supabase connection), since it removes the need for a separate orchestration service for retries and long-running jobs. The rest of the day is rumor and engagement-bait: model-launch leaks [2][35][7][19] signal an imminent release cycle worth planning around but offer nothing to integrate yet. Skepticism is warranted — the viral claim that Google and Anthropic pay SpaceX $2.17B/month [4] is unsourced and sits oddly against [11], which reports SpaceX/OpenAI/Anthropic are too unprofitable for S&P 500 entry; crypto 'Claude Opus audited zcash' posts [50][57] are unverified hype.

## Possibility
Likely: a clustered model-release window soon, given multiple independent rumor sources naming GPT-5.6 checkpoints [35] and a Claude tier above Opus [7][19][47]. Plausible: 'Claude Mythos 5' ships in the near term given an API sighting that was pulled [53], but the source quality is low and the name/timing are unconfirmed. Plausible: NotebookLM gains multi-format export bundled with a Gemini Flash update [33]. Unlikely: the $2.17B/month SpaceX compute figure [4] is accurate as stated, given the contradicting profitability reporting in [11]. No source gives a numeric probability, so none is asserted here.

## Org applicability — NDF DEV
1) Evaluate Gemma 4 QAT for an on-device feature in a mobile or edutech app (offline tutor, local captioning) and benchmark size/latency vs current API calls — effort: med [32]. 2) If a project uses Postgres/Supabase, prototype pg_durable for a long-running or retry-heavy workflow before adding a separate queue/orchestrator — effort: med [24]. 3) Trial DeepSeek v4 via API on a non-critical batch task to measure cost vs current models, but verify the 'cheap/competent' claim yourself since it rests on one low-credibility post — effort: low [2]. 4) If anyone on the team uses Claude paid plans, note the doubled Cowork limits through July 5 for heavier sessions — effort: low [25]. 5) Shortlist MAI-Transcribe-1.5 for a transcription/captioning comparison for e-learning, treating the vendor chart [44] as a starting point not proof — effort: low [44]. Skip: the Claude 'use it 25 ways' / prompt-book / 'duplicate your brain' / PhD-pipeline marketing threads [39][40][42][46], the unverified SpaceX/crypto-audit claims [4][50][57], and all Mythos 5 / GPT-5.6 rumors as action items — track them, don't build on them.

## Signals to Watch
- Claude 'Mythos 5' slug appearing then disappearing from API/Dev Mode — confirm only via official Anthropic channels [53][7].
- GPT-5.6 'kindle-alpha' as named release candidate; watch for an actual OpenAI ship [35].
- Gemma 4 QAT real-device benchmarks (size, latency, accuracy) once independent tests appear [32].
- pg_durable adoption and production-readiness signals for Postgres/Supabase backends [24].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **microsoft/pg_durable** — pg_durable: Microsoft open sources in-database durable execution | radar | <https://github.com/microsoft/pg_durable> |
| **NousResearch/hermes-agent** — The agent that grows with you Hermes Agent ☤ The self-improving AI agent built by Nous Research. It' | rss | <https://github.com/NousResearch/hermes-agent> |
| **chopratejas/headroom** — Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, s | rss | <https://github.com/chopratejas/headroom> |
| **Panniantong/Agent-Reach** — Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub,  | rss | <https://github.com/Panniantong/Agent-Reach> |
| **666ghj/MiroFish** — A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物 简洁通用的群体智能引擎， | rss | <https://github.com/666ghj/MiroFish> |
| **mvanhorn/last30days-skill** — AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - th | rss | <https://github.com/mvanhorn/last30days-skill> |
| **PaddlePaddle/PaddleOCR** — Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit | rss | <https://github.com/PaddlePaddle/PaddleOCR> |
| **MemPalace/mempalace** — The best-benchmarked open-source AI memory system. And it's free. MemPalace Local-first AI memory. V | rss | <https://github.com/MemPalace/mempalace> |
| **ZhuLinsen/daily_stock_analysis** — LLM驱动的 A/H/美股智能分析：多数据源行情 + 实时新闻 + LLM决策仪表盘 + 多渠道推送，零成本定时运行，纯白嫖. LLM-powered stock analysis system fo | rss | <https://github.com/ZhuLinsen/daily_stock_analysis> |
| **microsoft/agent-framework** — A framework for building, orchestrating and deploying AI agents and multi-agent workflows with suppo | rss | <https://github.com/microsoft/agent-framework> |
| **jundot/omlx** — LLM inference server with continuous batching & SSD caching for Apple Silicon — managed from the mac | rss | <https://github.com/jundot/omlx> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | GMMTV | ^9663 c266 | [[Teaser] แทนรัก (Tanrak) Ost.Ticket to Heaven เด็กชายไม่ไปสวรรค์ - Gemini Norawi](https://x.com/GMMTV/status/2063173150012227981) |
| x | might_offend | ^1782 c35 | [DeepSeek - launched v4, quite a competent model which also happens to be ridicul](https://x.com/might_offend/status/2063134663091368233) |
| x | widwnnyj | ^1458 c0 | [compilation of ANY singing in the recent giggle gang episode! felizz - abracadab](https://x.com/widwnnyj/status/2063204860552773823) |
| x | pubity | ^1373 c50 | [Google and Anthropic are now paying Elon Musk's SpaceX a combined $2,170,000,000](https://x.com/pubity/status/2063184121501823473) |
| x | GMMTV | ^1334 c24 | [แทนรัก (Tanrak) Ost.Ticket to Heaven เด็กชายไม่ไปสวรรค์ - Gemini Norawit 📍MV out](https://x.com/GMMTV/status/2063271693930672337) |
| x | atmoio | ^1278 c201 | [Once the bubble pops, Anthropic and OpenAI will become the Coinbase and Block of](https://x.com/atmoio/status/2063211858387931283) |
| x | testingcatalog | ^1164 c56 | [BREAKING 🔥: A new Claude Mythos 5 model slug has been spotted via Dev Mode. Clau](https://x.com/testingcatalog/status/2063234385227252184) |
| x | 22hrr22min | ^1095 c1 | [claude monet's violet paintings (french, 1840-1926) https://t.co/34R6CizpVj](https://x.com/22hrr22min/status/2063220814250385510) |
| x | nongsiii | ^1075 c9 | [did yall realize that every time gemini calls tanrak, he always calls him “Rak” ](https://x.com/nongsiii/status/2063221370713207009) |
| x | nongsiii | ^968 c0 | [GEMINI PLEASE 🤣🤣 BARTHTANRAK ONE STEP CLOSER #TicketToHeavenEP2 https://t.co/gn7](https://x.com/nongsiii/status/2063208984421744859) |
| radar | maltalex | ^942 c340 | [S&P 500 rejects SpaceX, also blocking entry for OpenAI and Anthropic](https://arstechnica.com/tech-policy/2026/06/sp-500-blocks-fast-spacex-entry-wont-waive-rule-for-unprofitable-ai-firms/) |
| x | tillamookbay | ^934 c14 | [the new model omg… Please telltale fix this](https://x.com/tillamookbay/status/2063211356199739881) |
| x | geminiscity | ^907 c0 | [4️⃣: Everyone might think it's tiring to work with Gemini. I'm not tired, he's m](https://x.com/geminiscity/status/2063224546321395947) |
| x | FinanaRyugu | ^885 c5 | [fuckin claude](https://x.com/FinanaRyugu/status/2063208874681725258) |
| x | nongsiii | ^775 c4 | [that’s Gemini and Gemini is FotFot’s baby 🫪 BARTHTANRAK ONE STEP CLOSER #TicketT](https://x.com/nongsiii/status/2063223757054075270) |
| x | nongsiii | ^766 c5 | [not Gemini having the biggest cutest aggression toward Tanrak 🫪 BARTHTANRAK ONE ](https://x.com/nongsiii/status/2063209700192378899) |
| x | levelsio | ^685 c33 | [Logically how this ends is you will have 3 groups being successful in startups: ](https://x.com/levelsio/status/2063185306874945697) |
| x | aydellch | ^615 c2 | [Bro, Gemini looking at their intertwined hands while stroking it lightly, I'm dy](https://x.com/aydellch/status/2063181615124140134) |
| x | kimmonismus | ^589 c47 | [Holy, release is so close. It will be named „Claude Mythos 5“, a tier above Opus](https://x.com/kimmonismus/status/2063239490240487884) |
| x | aydellch | ^582 c0 | [Gemini getting jealous of Kongthap bcs Fourth wants to be his faen, and Gemini a](https://x.com/aydellch/status/2063222118624686110) |
| radar | toomuchtodo | ^526 c200 | [Gov.uk has replaced Stripe with Dutch provider Adyen](https://www.theregister.com/public-sector/2026/06/04/govuk-goes-dutch-on-payments-as-it-dumps-stripe/5250763) |
| x | fotgems | ^480 c1 | [fourth's smile when gemini complimented him ☹️💘 https://t.co/0fZXRk19qA](https://x.com/fotgems/status/2063231349570359521) |
| x | aydellch | ^458 c0 | [☆ Ticket To Heaven EP 1 GeminiFourth Reaction ☆ Ticket To Heaven OST - Tanrak by](https://x.com/aydellch/status/2063201005764792487) |
| radar | coffeemug | ^437 c98 | [pg_durable: Microsoft open sources in-database durable execution](https://github.com/microsoft/pg_durable) |
| x | testingcatalog | ^427 c28 | [ANTHROPIC 🔥: Claude Cowork limits have been doubled until July 5 for all paid pl](https://x.com/testingcatalog/status/2063195692969984232) |
| x | levelsio | ^416 c13 | [I always keep retelling this story But @travisk was famously kicked out of Uber,](https://x.com/levelsio/status/2063226245014323422) |
| x | justalesky | ^405 c2 | [Another day of Gemini being a Barth hater 😭😭😭😭 BARTHTANRAK ONE STEP CLOSER #Tick](https://x.com/justalesky/status/2063208561044492297) |
| x | GeminiFourthsup | ^404 c1 | [This whole video is just so cute 😂❤️ BARTHTANRAK ONE STEP CLOSER #TicketToHeaven](https://x.com/GeminiFourthsup/status/2063228130727448721) |
| x | OneLuckyGirl_28 | ^397 c3 | [JUNE 6-JUNE 28 Aries: Manifest Wealth Taurus: Good Fortune Gemini: Abundance Can](https://x.com/OneLuckyGirl_28/status/2063241270508577264) |
| x | nongsiii | ^397 c1 | [Gemini is so funny😭 BARTHTANRAK ONE STEP CLOSER #TicketToHeavenEP2 https://t.co/](https://x.com/nongsiii/status/2063217500276551703) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GMMTV</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 9663 · 💬 266</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GMMTV/status/2063173150012227981">View @GMMTV on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“[Teaser] แทนรัก (Tanrak) Ost.Ticket to Heaven เด็กชายไม่ไปสวรรค์ - Gemini Norawit 📍Official MV Today on YouTube : GMMTV RECORDS #TicketToHeaven #GMMTV @gemini_ti @tawattannn https://t.co/lLy6ieSABz”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>GMMTV released the official MV teaser for 'Tanrak', the OST from Thai BL drama 'Ticket to Heaven', performed by actor Gemini Norawit.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GMMTV/status/2063173150012227981" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@might_offend</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1782 · 💬 35</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/might_offend/status/2063134663091368233">View @might_offend on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“DeepSeek - launched v4, quite a competent model which also happens to be ridiculously cheap Sora - shut down by OpenAI permanently GitHub Copilot - who tf uses that? Llama - who tf uses that (pt 2)? C”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A sarcastic AI roundup confirms: DeepSeek v4 launched (cheap, capable); OpenAI permanently shut down Sora; Cursor hit a $60B valuation backed by a SpaceX deal.</dd>
      <dt>Why interesting</dt>
      <dd>DeepSeek v4's price point is a real signal for studios running LLM inference, and Sora's closure removes a video-gen option from the toolbox.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a cost comparison: benchmark DeepSeek v4 via API against the studio's current LLM to check if it reduces inference spend.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/might_offend/status/2063134663091368233" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@widwnnyj</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1458 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/widwnnyj/status/2063204860552773823">View @widwnnyj on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“compilation of ANY singing in the recent giggle gang episode! felizz - abracadabra gemini fourth - re-move on film rachanun - linger lykn - who says #ANY #GeminiFourth #filmracha #LYKN #EmiBonnie http”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan-compiled clip of Thai idol group members singing covers in a recent variety show episode, featuring artists from ANY, GeminiFourth, Film Rachanun, and LYKN.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/widwnnyj/status/2063204860552773823" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@pubity</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1373 · 💬 50</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/pubity/status/2063184121501823473">View @pubity on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Google and Anthropic are now paying Elon Musk's SpaceX a combined $2,170,000,000 per month for cloud compute capacity to run their AI services. https://t.co/hLECg4Riyr”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Google and Anthropic together pay SpaceX $2.17 billion per month for cloud compute capacity to power their AI services — positioning SpaceX as a major cloud infrastructure vendor.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/pubity/status/2063184121501823473" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GMMTV</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1334 · 💬 24</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GMMTV/status/2063271693930672337">View @GMMTV on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“แทนรัก (Tanrak) Ost.Ticket to Heaven เด็กชายไม่ไปสวรรค์ - Gemini Norawit 📍MV out now on YouTube : GMMTV RECORDS 🎥 Official MV : https://t.co/DVxqZQvhuv and available on all streaming platforms. #Tanra”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>GMMTV released the official MV for 'Tanrak', the OST of Thai drama 'Ticket to Heaven', performed by Gemini Norawit.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GMMTV/status/2063271693930672337" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@atmoio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1278 · 💬 201</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/atmoio/status/2063211858387931283">View @atmoio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Once the bubble pops, Anthropic and OpenAI will become the Coinbase and Block of the AI world. Mundane companies that ship narrative wrappers on mundane bytes. That the bubble will pop isn’t some apoc”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A tech commentator predicts Anthropic and OpenAI will shrink to mundane IT providers after an AI bubble pop, arguing that AI's high serving costs are unlikely to be offset by real-world returns — drawing a parallel to crypto companies post-2021.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/atmoio/status/2063211858387931283" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@testingcatalog</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1164 · 💬 56</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/testingcatalog/status/2063234385227252184">View @testingcatalog on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“BREAKING 🔥: A new Claude Mythos 5 model slug has been spotted via Dev Mode. Claude Mythos is planned to be released as its own model class, besides Haiku, Sonnet and Opus model families. Soon? 👀 https”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A model slug 'claude-mythos-5' was spotted in Anthropic's Dev Mode, indicating a new 'Mythos' model family is in development as a fourth line alongside Haiku, Sonnet, and Opus.</dd>
      <dt>Why interesting</dt>
      <dd>A new model class means a potential new capability or price tier that could change which Claude model the studio selects for different task types via the API.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Monitor Anthropic release notes; when Mythos is announced, benchmark it against current model choices for cost-sensitive and high-complexity tasks in the studio's pipelines.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/testingcatalog/status/2063234385227252184" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@22hrr22min</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1095 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/22hrr22min/status/2063220814250385510">View @22hrr22min on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“claude monet's violet paintings (french, 1840-1926) https://t.co/34R6CizpVj”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A social media post shares a collection of violet-toned paintings by Impressionist artist Claude Monet (French, 1840–1926).</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/22hrr22min/status/2063220814250385510" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
