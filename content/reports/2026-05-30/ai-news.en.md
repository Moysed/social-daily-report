---
type: social-topic-report
date: '2026-05-30'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-05-30T18:19:06+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 154
salience: 0.25
sentiment: neutral
confidence: 0.55
tags:
- ai-tooling
- api-pricing
- mcp
- coding-assistants
- low-signal
- noise-polluted
thumbnail: https://pbs.twimg.com/ext_tw_video_thumb/2060703402305454080/pu/img/fgtYUQc_UorZFdOJ.jpg
---

# AI News & New Skills — 2026-05-30

## TL;DR
- Feed is heavily polluted by K-pop/Thai BL posts about an actor nicknamed 'Gemini' (GeminiFourth, #TicketToHeavenEP1) and astrology — minimal real AI-tooling signal today [1][3][5][24].
- A coding-model preference ranking put Codex GPT-5.5 first, Claude Opus 4.8 second, Composer 2.5 third, ahead of manual code and Gemini [11].
- China API price war intensified: DeepSeek made its 75% API price cut permanent and Xiaomi cut API costs up to 99% to match [39].
- 'MCP is dead?' engineering blog drew 336 comments, signaling an active debate on Model Context Protocol's role in agent stacks [40].
- Market framing: Anthropic now valued above Walmart and OpenAI above JPMorgan per a markets post; Jim Cramer flagged index-rebalance volatility risk from these private valuations [50][34].

## What happened
Most items in this feed are not about AI tooling: they cover a Thai actor/series promotion (Gemini–Fourth, #TicketToHeavenEP1) and horoscope content [1][2][5][7][24][25]. The genuine AI signal is thin. A developer posted a personal coding-assistant ranking favoring Codex GPT-5.5 over Claude Opus 4.8 and Composer 2.5 [11]. On pricing, DeepSeek made a 75% API cut permanent and Xiaomi reportedly cut API prices up to 99% [39]. A blog titled 'MCP is dead?' generated heavy discussion about the Model Context Protocol [40]. Finance-adjacent posts noted that Anthropic and OpenAI now exceed Walmart and JPMorgan in valuation, with warnings about volatility from index rebalancing [50][34], and Musk reiterated concerns about truthfulness in Gemini and ChatGPT [56].

## Why it matters (reasoning)
For studio AI workflows, the actionable content today is limited to pricing and protocol direction, not concrete new repos or skills. Chinese providers cutting API prices 75–99% [39] pressures incumbent per-token costs and could lower the cost of background/agentic tasks if quality holds — relevant to budget-sensitive batch work. The 'MCP is dead?' debate [40] matters because the studio's tool-integration choices (Claude/Cursor plugins, agent connectors) depend on whether MCP remains the default integration layer; a 336-comment thread suggests unsettled consensus, so committing heavily to MCP-specific plumbing now carries some rework risk. Model rankings like [11] are single-user opinion, not benchmarks, and should not drive tool switches. The valuation/market items [34][50] are macro context, not operational.

## Possibility
Likely: continued downward pressure on API pricing as DeepSeek and Xiaomi anchor low, prompting price or tier responses elsewhere [39]. Plausible: MCP keeps evolving rather than dying — the volume of debate [40] indicates engagement, not abandonment, but expect competing integration patterns to appear. Unlikely (from this feed): any of the named coding-model rankings [11] reflects a stable, reproducible quality ordering; it is one person's preference. No source provides numeric probabilities, so none are asserted.

## Org applicability — NDF DEV
1) Read the 'MCP is dead?' article before expanding any MCP-based integrations, to decide whether to standardize on MCP or stay adapter-agnostic — effort: low [40]. 2) Evaluate DeepSeek/Xiaomi pricing for non-critical, high-volume tasks (e.g., bulk asset captioning, test generation) with a small quality spot-check; do not move production-critical code work — effort: med [39]. 3) Treat the coding-model ranking as a prompt to run your own quick A/B on a real studio task rather than acting on it — effort: low [11]. Skip: the actor/horoscope items [1][2][5][7][24][25] (irrelevant), the '20k free credits' link [38] (unverified, likely scam — do not enter credentials), and the $GOBLIN/crypto lore [21].

## Signals to Watch
- Whether DeepSeek/Xiaomi price cuts trigger matching moves from US providers [39].
- Outcome of the MCP-relevance debate and any emerging alternative integration patterns [40].
- Independent benchmarks for Codex GPT-5.5 / Claude Opus 4.8 / Composer 2.5 beyond single-user rankings [11].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **kristapsdz/openrsync** — Openrsync: An implementation of rsync, by the OpenBSD team | radar | <https://github.com/kristapsdz/openrsync> |
| **mplsllc/macsurf** — Macsurf, "modern" web browser for macOS 9 | radar | <https://github.com/mplsllc/macsurf> |
| **harry0703/MoneyPrinterTurbo** — 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. MoneyPrinterTurbo 💸 简体中文 / Engl | rss | <https://github.com/harry0703/MoneyPrinterTurbo> |
| **microsoft/markitdown** — Python tool for converting files and office documents to Markdown.MarkItDown Important MarkItDown pe | rss | <https://github.com/microsoft/markitdown> |
| **EveryInc/compound-engineering-plugin** — Official Compound Engineering plugin for Claude Code, Codex, Cursor, and moreCompound Engineering AI | rss | <https://github.com/EveryInc/compound-engineering-plugin> |
| **twentyhq/twenty** — The open alternative to Salesforce, designed for AI. The #1 Open-Source CRM Website · Documentation  | rss | <https://github.com/twentyhq/twenty> |
| **anthropics/claude-code** — Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and he | rss | <https://github.com/anthropics/claude-code> |
| **Leonxlnx/taste-skill** — Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop Taste Skil | rss | <https://github.com/Leonxlnx/taste-skill> |
| **cursor/plugins** — Cursor plugin specification and official pluginsCursor plugins Official Cursor plugins for popular d | rss | <https://github.com/cursor/plugins> |
| **run-llama/liteparse** — A fast, helpful, and open-source document parserLiteParse / / / / / / Docs Looking for LiteParse V1? | rss | <https://github.com/run-llama/liteparse> |
| **galilai-group/stable-worldmodel** — A platform for reproducible world model research and evaluationstable-worldmodel A platform for repr | rss | <https://github.com/galilai-group/stable-worldmodel> |
| **byoungd/English-level-up-tips** — An advanced guide to learn English which might benefit you a lot 🎉 . 离谱的英语学习指南/英语学习教程/英语学习/学英语简体中文 / | rss | <https://github.com/byoungd/English-level-up-tips> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | geminiscity | ^5685 c10 | [4️⃣: [talks] ♊️: Keep going. I like listening to you talk. 4️⃣: [continues talki](https://x.com/geminiscity/status/2060703541661200394) |
| x | justalesky | ^3508 c7 | [https://t.co/0653ggwHBV P’Aof : “This is what Gemini and I had to deal with when](https://x.com/justalesky/status/2060734944792731708) |
| x | _iamjamila | ^3223 c70 | [Happy 30th Birthday to me the leader of the Gemini Supremacy Movement ♊️♊️♊️♊️ S](https://x.com/_iamjamila/status/2060698074972840192) |
| x | geminiscity | ^2881 c1 | [♊️: [talks about Tanrak who's reserved like Fourth when he first entered the ind](https://x.com/geminiscity/status/2060696629255274515) |
| x | mylifegemfourth | ^2084 c1 | [GEMINI CHANGED THE LYRICS FROM "that person must be you" TO "that person must be](https://x.com/mylifegemfourth/status/2060708154628002048) |
| x | aydellch | ^1984 c1 | [[ talking about how their feelings (while filming) coming from inside ] 🎤: And G](https://x.com/aydellch/status/2060698841205358890) |
| x | nongsiii | ^1878 c2 | [twenty years later, he comes back. from someone who once lost his faith in God, ](https://x.com/nongsiii/status/2060748869517144087) |
| x | aydellch | ^1847 c8 | [[ sing คนนั้นต้องเป็นเธอ by Win Metawin ] 4️⃣: That person must be... you~ ♊️: (](https://x.com/aydellch/status/2060707752729870807) |
| x | fotgems | ^1176 c3 | [gemini as barth is genuinely the best thing that has ever happened. #TicketToHea](https://x.com/fotgems/status/2060734775946887466) |
| x | aydellch | ^1145 c12 | [From giggling bcs Fourth could describe Gemini's golden body so detailed to feel](https://x.com/aydellch/status/2060700741665439981) |
| x | rezoundous | ^1095 c71 | [My personal ranking 1. Codex GPT-5.5 2. Claude Opus 4.8 3. Composer 2.5 4. Manua](https://x.com/rezoundous/status/2060707540795900216) |
| x | aydellch | ^1079 c13 | [I can't believe I got to see Gemini with gray hair 😭😭😭😭😭😭😭😭😭😭😭😭😭😭 GEMINIFOURTH T](https://x.com/aydellch/status/2060735782286139450) |
| x | nongsiii | ^1005 c3 | [4️⃣: Gemini is his golden form 😛😋 4️⃣: everyone’s drooling 😝 ♊️: crazy 😹 #Ticket](https://x.com/nongsiii/status/2060740055665393785) |
| x | justalesky | ^1005 c0 | [https://t.co/Dd3bKMYPHV P’Aof: “We don't have much time left... Gemini and Fourt](https://x.com/justalesky/status/2060714469966442914) |
| x | justalesky | ^962 c2 | [https://t.co/frWvx6JhPo ♊: “Everything you say turns into a spoiler at this poin](https://x.com/justalesky/status/2060710188039221580) |
| x | CChang20970 | ^878 c2 | [♊️Gemini: We have been waiting for two years, and today is finally the day. We d](https://x.com/CChang20970/status/2060713001146274035) |
| x | wetneptune | ^866 c3 | [the full moon in sagittarius is in opposition to uranus in gemini. this is a ful](https://x.com/wetneptune/status/2060709658398990477) |
| x | gemnuna | ^835 c1 | [never see gemini with this expression before he truly like a different person as](https://x.com/gemnuna/status/2060739373268873477) |
| x | gemfot_smile | ^788 c2 | [Gem : I don't understand why they had to hurt Tanrak's feelings that much. The p](https://x.com/gemfot_smile/status/2060696319254208672) |
| x | nongsiii | ^776 c1 | [#TicketToHeavenEP1 Fourth to Gemini 🥹🤍 4️⃣: i feel that for this series, he dedi](https://x.com/nongsiii/status/2060709288755257538) |
| x | MarcellxMarcell | ^641 c25 | [Over the past 24 hours OpenAI and its developers have reaffirmed the $GOBLIN lor](https://x.com/MarcellxMarcell/status/2060723307088117774) |
| x | nongsiii | ^628 c0 | [#TicketToHeavenEP1 Gemini to Fourth 🥹🤍 ♊️: as everyone knows, Fourth is a playfu](https://x.com/nongsiii/status/2060712928593215505) |
| x | justalesky | ^621 c1 | [https://t.co/VOxH0DKBvE (Discussion about the 6 levels of heaven, meanwhile Gemi](https://x.com/justalesky/status/2060702949177991457) |
| x | OneLuckyGirl_28 | ^597 c8 | [JUNE✨ Aries: Attract Money Taurus: Manifest Wealth Gemini: Big Glow Up Cancer: M](https://x.com/OneLuckyGirl_28/status/2060714998821683340) |
| x | YogmayaAstro5 | ^587 c47 | [Jupiter in Cancer ♋ is going to be very beneficial for Cancer ♋ Virgo ♍ Pisces ♓](https://x.com/YogmayaAstro5/status/2060693961115918586) |
| x | astroinrealtime | ^586 c11 | [your laugh is unforgettable, gemini.](https://x.com/astroinrealtime/status/2060708307648627114) |
| x | justalesky | ^553 c0 | [https://t.co/3y5ghC4qWF Mae Godji: "You're really not going to do cheek kiss,fir](https://x.com/justalesky/status/2060740621506355487) |
| x | levelsio | ^520 c44 | [It's a disease all over Europe](https://x.com/levelsio/status/2060766986523553929) |
| x | mylifegemfourth | ^508 c1 | [the way gemini entered at the end then sing with fourth "good time with you" 🥺🥺 ](https://x.com/mylifegemfourth/status/2060706622939562279) |
| x | DoseofTarot | ^504 c4 | [Mutable Signs Gemini , Pisces , Sagittarius , Virgo Job opportunities coming in ](https://x.com/DoseofTarot/status/2060746897573212412) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@geminiscity</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5685 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/geminiscity/status/2060703541661200394">View @geminiscity on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“4️⃣: [talks] ♊️: Keep going. I like listening to you talk. 4️⃣: [continues talking] 👤: Gemini hasn't talked. 4️⃣: Come on, Gemini. Talk. ♊️: I like it~ No, I just listen to Fourth and I enjoy it. #Tic”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan-account post clips a Thai BL show dialogue where a character named Gemini says they enjoy listening rather than talking, tagged with a drama episode hashtag.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/geminiscity/status/2060703541661200394" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@justalesky</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3508 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/justalesky/status/2060734944792731708">View @justalesky on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/0653ggwHBV P’Aof : “This is what Gemini and I had to deal with whenever Fourth was trying to manage his stress.” GEMINIFOURTH TTH PREMIERE #TicketToHeavenEP1”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan account posted a humorous caption referencing Thai actors Fourth and Aof alongside the Gemini name, unrelated to Google Gemini or any AI/dev topic.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/justalesky/status/2060734944792731708" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@_iamjamila</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3223 · 💬 70</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/_iamjamila/status/2060698074972840192">View @_iamjamila on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Happy 30th Birthday to me the leader of the Gemini Supremacy Movement ♊️♊️♊️♊️ Siri, play GROWN WOMAN 💫 https://t.co/klkj2MRpA2”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Twitter user is celebrating their 30th birthday and referencing a personal 'Gemini Supremacy Movement' based on their zodiac sign, with no technical content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/_iamjamila/status/2060698074972840192" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@geminiscity</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2881 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/geminiscity/status/2060696629255274515">View @geminiscity on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“♊️: [talks about Tanrak who's reserved like Fourth when he first entered the industry] 👤: Which meant Gemini likes Fourth since he entered the industry? ♊️: [coos] I just said like back then... 👤: So ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Thai BL drama fan account (@geminiscity) posts a playful exchange between actors Gemini and Fourth about their relationship, tagged to TicketToHeavenEP1 premiere.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/geminiscity/status/2060696629255274515" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@mylifegemfourth</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2084 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/mylifegemfourth/status/2060708154628002048">View @mylifegemfourth on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“GEMINI CHANGED THE LYRICS FROM &quot;that person must be you&quot; TO &quot;that person must be FOURTH&quot; 😭😭😭😭😭😭😭😭😭😭😭😭😭🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍 GEMINIFOURTH TTH PREMIERE #TicketToHeavenEP1 https://t.co/owkb0U1PmJ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan account reports that Thai celebrity Gemini changed song lyrics to reference bandmate Fourth during a live premiere event.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/mylifegemfourth/status/2060708154628002048" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aydellch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1984 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aydellch/status/2060698841205358890">View @aydellch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“[ talking about how their feelings (while filming) coming from inside ] 🎤: And Gemini, do you feel it too? ♊️: Can you hear it my heart ♊️: It's saying 'love, love ter (you)' now [ ♊️4️⃣ looking at eo”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan account live-tweets a Thai idol group (GeminiFourth) premiere event, quoting stage banter between members.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aydellch/status/2060698841205358890" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nongsiii</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1878 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nongsiii/status/2060748869517144087">View @nongsiii on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“twenty years later, he comes back. from someone who once lost his faith in God, he returns believing again. the way gemini portrayed old barth in this scene… there’s not a single trace of “gemini nora”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Thai drama fan praises an actor's performance in episode 1 of Ticket to Heaven, noting Gemini Norawit's transformation into the character Barth.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nongsiii/status/2060748869517144087" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aydellch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1847 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aydellch/status/2060707752729870807">View @aydellch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“[ sing คนนั้นต้องเป็นเธอ by Win Metawin ] 4️⃣: That person must be... you~ ♊️: (must be) Fourth~ // OMGGGGG, OKAY GEMINI GEMINIFOURTH TTH PREMIERE #TicketToHeavenEP1 https://t.co/DO6McqrrmE”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan post reacting to actor Win Metawin singing at a TV show premiere (#TicketToHeavenEP1), with no technical content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aydellch/status/2060707752729870807" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
