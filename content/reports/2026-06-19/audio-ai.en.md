---
type: social-topic-report
date: '2026-06-19'
topic: audio-ai
lang: en
pair: audio-ai.th.md
generated_at: '2026-06-19T03:51:06+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 85
salience: 0.55
sentiment: mixed
confidence: 0.5
tags:
- tts
- voice-cloning
- music-generation
- copyright
- elevenlabs
- multilingual
thumbnail: https://pbs.twimg.com/media/HLHMUUhbsAA1r6D.jpg
---

# Audio AI — 2026-06-19

## TL;DR
- Grok TTS topped Vapi's blind Humaneness Index at 96, reported as 4 points below the human reference, ranking it the top AI voice model in that chart [3][29].
- The Atlantic published a searchable database of copyrighted songs used to train Suno/Udio; artists report catalogs scraped without consent — Quadeca cited at 295 grabs across 8 datasets, another artist reports 22 songs incl. unreleased tracks [1][4][6][8][21][59].
- Poland's state, via Vinci (BGK Group), took an equity stake in ElevenLabs (reported ~$11M) alongside Sequoia, a16z and ICONIQ, part of a push to make Warsaw a European AI hub [2][19].
- Rumik AI's Silk Mulberry 1.5 (India) claims ₹0.40/min (~95% cheaper than ElevenLabs) with Hindi/English mid-sentence code-switching [10]; Lovable added built-in TTS/STT and Cartesia is being adopted for production voice [17][60].
- Caveat: a large share of high-engagement items here are TimeSoul ($TTS) crypto-mindfulness spam, unrelated to text-to-speech; genuine Audio AI signal is narrower than raw counts suggest, and no item demonstrates Thai-language support.

## What happened
Two distinct threads dominate the real Audio AI signal. On voice synthesis, Grok TTS is reported at the top of Vapi's blind Humaneness Index with a score of 96, with blind-test anecdotes claiming it was indistinguishable from a human [3][29]. ElevenLabs received a state-backed equity investment from Poland (~$11M via Vinci/BGK), joining a round with Sequoia, a16z and ICONIQ [2][19], and one news roundup claims ElevenLabs now matches Suno on music generation [27]. Lower-cost and developer-facing options surfaced: Rumik AI's Silk Mulberry 1.5 at ₹0.40/min with Hindi/English code-switching [10], Lovable adding TTS/STT to its app builder [17], and Cartesia being chosen over OpenAI/Gemini/ElevenLabs for a production voice product [60]. ElevenLabs also appears inside hobby agent pipelines [54].

## Why it matters (reasoning)
The copyright thread is the most consequential for a studio shipping commercial games and edutech. The Atlantic's leaked, searchable training database [21] plus multiple artists documenting scraped catalogs [1][4][6][8][59] turns the licensing question for Suno/Udio music from theoretical to evidenced — which is a direct commercial-use risk for any music dropped into client deliverables, cinematics, or e-learning soundscapes. On the voice side, the combination of a credible quality leader (Grok TTS [3]), aggressive price compression (Silk Mulberry at ~95% below ElevenLabs [10]), and easy integration paths (Lovable [17], Cartesia [60]) means TTS is becoming a commoditized, multi-vendor decision rather than a single-provider lock-in. A second-order effect: state capital entering ElevenLabs [19] signals voice AI is now treated as strategic infrastructure, which tends to accelerate funding and competition — good for buyers on price and choice. Content-policy refusals for branded creative work [5] are a smaller but real friction when scripting voiced characters.

## Possibility
Likely: legal and reputational pressure on Suno/Udio intensifies given documented, searchable evidence of scraped catalogs [8][21][59]; expect tighter scrutiny of music-gen licensing terms. Plausible: Grok TTS sustains a top-tier position in blind quality tests and ships an API at competitive pricing, given the leaderboard result [3] and a corporate parent with distribution. Plausible: price compression continues as cheaper code-switching models appear [10] and app builders bundle voice [17]. Unlikely (on current evidence): any of these providers demonstrably support Thai at production quality — no item shows it, so treat Thai/EN multilingual claims as unverified until tested. No source gives numeric probabilities, so none are asserted here.

## Org applicability — NDF DEV
1) Benchmark TTS for edutech narration and in-game character voice across Grok TTS [3], ElevenLabs [54] and Cartesia [60] on quality, latency, and — critically — Thai output, which no item confirms (effort: med). 2) For fast voice-feature prototypes in web/mobile apps, trial Lovable's built-in TTS/STT before wiring a raw provider [17] (effort: low). 3) For cost-sensitive or code-switching narration, evaluate cheaper models like Silk Mulberry 1.5, but verify Thai support and commercial license terms before any commitment [10] (effort: low-med). 4) Treat Suno/Udio-generated music as a commercial-license risk: require documented provenance/licensing or use cleanly licensed music for cinematics and e-learning; do not ship Suno output in paid client work without written license clarity [1][6][8][21] (effort: med). 5) Pre-test any voice/creative provider for content-policy refusals on branded scripts before relying on it [5] (effort: low). Skip: all TimeSoul/$TTS crypto items (not audio) and the generic '80+/120 AI tools' listicles [23][48][50][55][56].

## Signals to Watch
- Grok TTS leaderboard standing [3] — watch for an actual API, pricing, and explicit commercial-use/license terms before adoption.
- The Atlantic training-data database leak [21] — watch whether it triggers litigation or forced licensing that reshapes music-gen terms.
- Cheaper code-switching TTS like Silk Mulberry [10] — watch for similar low-cost models adding Southeast Asian / Thai voices.
- Single-source claim that ElevenLabs now matches Suno on music generation [27] — verify independently before relying on it for soundscapes.

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Rishhie | ^2982 c16 | [Apparently an AI music generation software has been trained on my music and 3 so](https://x.com/Rishhie/status/2067589593029820498) |
| x | Polymarket | ^1843 c127 | [JUST IN: Poland invests $11 million in ElevenLabs as Warsaw pushes to become a m](https://x.com/Polymarket/status/2067521698371379419) |
| x | XFreeze | ^1480 c195 | [Grok TTS is already sounding insanely human In Vapi’s blind voting Humaneness In](https://x.com/XFreeze/status/2067658361487921484) |
| x | DJSTTDJ | ^1117 c5 | [to everyone who thought my music sounded like ai slop, did you ever think it was](https://x.com/DJSTTDJ/status/2067512823513514294) |
| x | Timcast | ^868 c152 | [One big problem i find with AI is that as the owner of a large publicly visible ](https://x.com/Timcast/status/2067635844672799228) |
| x | hyphen_c_ | ^804 c29 | [An overwhelming chunk of Quadeca’s catalog was scraped for training sets for Sun](https://x.com/hyphen_c_/status/2067506727277232362) |
| x | Chappytoa | ^581 c55 | [why? It’s a glorified slop channel that just summarizes horror movies. Barely an](https://x.com/Chappytoa/status/2067452300931870923) |
| x | oralon | ^524 c9 | [Suno &amp; other AI models are reportedly being used to scrape music catalogs as](https://x.com/oralon/status/2067606379322384702) |
| x | kellyeld | ^417 c25 | [This song is about people who just love to hear themselves talk. Lyrics by me. I](https://x.com/kellyeld/status/2067213904015417568) |
| x | VaibhavSisinty | ^328 c2 | [This Indian AI lab built a voice model 95% cheaper than ElevenLabs. And it switc](https://x.com/VaibhavSisinty/status/2067608358551695632) |
| x | tomvcns | ^310 c37 | [corny ass lyrics, suno ai production, vocals stuck way in the back of her throat](https://x.com/tomvcns/status/2067125675169927664) |
| x | uthykinging | ^300 c174 | [A lot of Web3 products are designed to optimize capital, trading activity, or on](https://x.com/uthykinging/status/2067503088244592921) |
| x | Coinmaster100x | ^235 c86 | [A new chapter for @timesoulcom is unfolding. What if mindfulness was more than j](https://x.com/Coinmaster100x/status/2067551334212243526) |
| x | pocox40036 | ^228 c65 | [Finding balance in the digital age is more important than ever That’s why I’m ex](https://x.com/pocox40036/status/2067470457859936420) |
| x | Hey_karl | ^218 c66 | [late night rabbit hole and ended up checking @timesoulcom again. what caught my ](https://x.com/Hey_karl/status/2067279206585893116) |
| x | 0xZephh | ^215 c119 | [Your portfolio gets tracked. Your screen time gets tracked. Your steps get track](https://x.com/0xZephh/status/2067610143777546635) |
| x | Lovable | ^205 c12 | [Your app talks back. Lovable now supports text-to-speech and-speech-to-text, so ](https://x.com/Lovable/status/2067608317392732617) |
| x | IParvel56536 | ^204 c108 | [I have seen plenty of projects talk about wellness but @timesoulcom is actually ](https://x.com/IParvel56536/status/2067563678678081915) |
| x | mati | ^197 c13 | [The Polish state is taking a stake in @ElevenLabs. Through Vinci, part of the BG](https://x.com/mati/status/2067613148052406692) |
| x | DrPengu6 | ^176 c181 | [been following @timesoulcom for a while, and what makes me interested is how sim](https://x.com/DrPengu6/status/2067401831186088338) |
| x | LinesofLogic | ^168 c3 | [The Atlantic leaked a searchable database tracking the exact copyrighted music u](https://x.com/LinesofLogic/status/2067614487104884940) |
| x | evrendag1284 | ^163 c153 | [What interests me about @timesoulcom is that it doesn't present meditation or pe](https://x.com/evrendag1284/status/2067579189050433863) |
| x | Aqib__786Ai | ^158 c51 | [🚀 80+ AI Tools That Can Save You Hundreds of Hours Why spend months on tasks whe](https://x.com/Aqib__786Ai/status/2067427603846500699) |
| x | wsdg79 | ^154 c0 | [@mail1010101010 @subtoconnorpls now we need an ai tts to summarise the movie](https://x.com/wsdg79/status/2067403630324641992) |
| x | jvstme_ophyxial | ^153 c139 | [What I find interesting about @timesoulcom is that it focuses less on motivation](https://x.com/jvstme_ophyxial/status/2067319968991969658) |
| x | Musty_hasheedu | ^143 c147 | [Good morning One thing I learned while exploring @timesoulcom today: Time is our](https://x.com/Musty_hasheedu/status/2067453003997553140) |
| x | YellowRobotXYZ | ^138 c6 | [AI News - June 2026. New generation of LLMs for local use. Elevenlabs now as goo](https://x.com/YellowRobotXYZ/status/2067687865287319852) |
| x | vikktorrrre | ^126 c58 | [this creator spends over $3,500 a month on ai models to maximise his content qua](https://x.com/vikktorrrre/status/2067555985913164065) |
| x | XFreeze | ^125 c17 | [Yesterday on a blind audio test, I couldn't tell if it was a human or AI, and it](https://x.com/XFreeze/status/2067323310384505057) |
| x | Bency1749379 | ^124 c123 | [GM GM I am seeking an effective method to cultivate positive habits and alleviat](https://x.com/Bency1749379/status/2067486663429730410) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Rishhie</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2982 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Rishhie/status/2067589593029820498">View @Rishhie on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Apparently an AI music generation software has been trained on my music and 3 songs I never even released to streaming platforms. Genuinely so disgusting”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An artist reports that an AI music generation tool was trained on their music, including 3 unreleased tracks never published to streaming platforms.</dd>
      <dt>Why interesting</dt>
      <dd>This highlights that AI training data can include non-public audio, raising legal and ethical risk for studios that use AI-generated music in game or e-learning projects.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Before using AI music generation tools in any project, the studio should verify each tool's training data policy and licensing terms to avoid IP liability.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Rishhie/status/2067589593029820498" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Polymarket</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1843 · 💬 127</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Polymarket/status/2067521698371379419">View @Polymarket on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“JUST IN: Poland invests $11 million in ElevenLabs as Warsaw pushes to become a major European AI hub.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Poland's government committed $11M to ElevenLabs as part of a bid to position Warsaw as a leading European AI hub.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Polymarket/status/2067521698371379419" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@XFreeze</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1480 · 💬 195</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/XFreeze/status/2067658361487921484">View @XFreeze on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Grok TTS is already sounding insanely human In Vapi’s blind voting Humaneness Index, Grok TTS ranked as the top AI voice model in the chart with a humaneness score of 96.....just 4 points below the re”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Grok TTS scored 96/100 on Vapi's blind Humaneness Index, ranking first among all AI voice models — 4 points below the real human benchmark.</dd>
      <dt>Why interesting</dt>
      <dd>Near-human TTS at low latency reduces reliance on recorded voice actors for e-learning narration and game NPC dialogue.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test Grok TTS via Vapi API on the next e-learning or XR project that currently budgets for voice recording sessions.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/XFreeze/status/2067658361487921484" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DJSTTDJ</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1117 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DJSTTDJ/status/2067512823513514294">View @DJSTTDJ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“to everyone who thought my music sounded like ai slop, did you ever think it was because Suno was using a dataset that contained 22 of my songs? it’s funny how there were no accusations of my music so”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Artist @DJSTTDJ publicly confirms that Suno used 22 of their original songs in its training dataset without consent, causing the artist's own music to be mislabeled as AI-generated.</dd>
      <dt>Why interesting</dt>
      <dd>Suno's dataset dispute is now documented by named artists — any studio shipping AI audio from contested tools faces real legal and reputational exposure.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Audit every AI audio tool in the studio's pipeline for dataset licensing status; replace Suno with an open-licensed alternative (e.g. Meta AudioCraft) for any client-facing work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DJSTTDJ/status/2067512823513514294" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Timcast</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 868 · 💬 152</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Timcast/status/2067635844672799228">View @Timcast on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One big problem i find with AI is that as the owner of a large publicly visible company I cannot use it for creative works GPT for instance sometimes refuses to create content for my company saying it”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Tim Pool (Timcast) found that GPT and Suno block him from generating content using his own brand because their IP filters recognize his public company, while smaller unknown companies face no such block.</dd>
      <dt>Why interesting</dt>
      <dd>As a studio's brand grows publicly visible, AI creative tools may start refusing to generate on-brand assets — a real ops risk that hits exactly when the team needs those tools most.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run smoke tests on AI creative tools (image, music, video gen) using the studio's actual brand name and assets now, before any client or product pipeline depends on them.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Timcast/status/2067635844672799228" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@hyphen_c_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 804 · 💬 29</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/hyphen_c_/status/2067506727277232362">View @hyphen_c_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“An overwhelming chunk of Quadeca’s catalog was scraped for training sets for Suno and other Gen-AI models, presumably against his will 295 grabs across 8 known data sets from various releases, snippet”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Quadeca's catalog was scraped 295 times across 8 known datasets to train Suno and other audio Gen-AI models, reportedly without consent, with lyrics also pulled from Genius.</dd>
      <dt>Why interesting</dt>
      <dd>This case exposes copyright risk in AI audio tools like Suno — studios using them for commercial output may inherit IP liability from uncleared training data.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio should avoid Suno or similar tools for any commercial audio deliverable until training data licensing is legally resolved.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/hyphen_c_/status/2067506727277232362" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Chappytoa</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 581 · 💬 55</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Chappytoa/status/2067452300931870923">View @Chappytoa on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“why? It’s a glorified slop channel that just summarizes horror movies. Barely any higher quality than those movie recap channels that use AI text to speech voices.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user criticizes an unnamed content channel for using AI text-to-speech to auto-summarize horror movies, calling it low-effort 'slop'.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Chappytoa/status/2067452300931870923" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@oralon</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 524 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/oralon/status/2067606379322384702">View @oralon on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Suno &amp;amp; other AI models are reportedly being used to scrape music catalogs as training sets against artists’ wills. (via The Atlantic) Independent artists such as Quadeca, Jane Remover, Lucy Bedroq”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Suno and other AI music generators are accused of scraping independent artists' catalogs without consent for model training; named artists include Quadeca, Jane Remover, and Backxwash.</dd>
      <dt>Why interesting</dt>
      <dd>Studios using AI audio tools for game or e-learning content now carry concrete legal risk if training data copyright claims advance in court.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Audit AI-generated audio in active projects and flag content from tools with unverified training data provenance before shipping to clients.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/oralon/status/2067606379322384702" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
