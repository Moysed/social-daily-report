---
type: social-topic-report
date: '2026-06-19'
topic: multimodal-ai
lang: en
pair: multimodal-ai.th.md
generated_at: '2026-06-19T03:46:29+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 221
salience: 0.6
sentiment: mixed
confidence: 0.55
tags:
- multimodal-ai
- video-generation
- image-generation
- midjourney
- seedance
- production-pipeline
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2067417890098499584/img/MFFwG8qdfYbJALQD.jpg
---

# Multimodal AI — 2026-06-19

## TL;DR
- Midjourney announced a hardware pivot — "Midjourney Medical" and a full-body ultrasonic CT "Scanner" claiming MRI-quality 3D scans in ~60s via ~358,000 on-chip transducers and water, no radiation [1][2][4][16]; this dominated engagement but is off-focus for asset pipelines.
- Real production signal is in video gen: a body-physics comparison pitted Grok Imagine 1.5, ByteDance Seedance 2.0, Google Gemini Omni Flash, and Kling 3.0 Pro against each other [28]; Seedance 2.0 (mini) shipped via Dreamina/Higgsfield [36][48][42].
- Midjourney V8.1 added a big-batch draft mode: 24 low-res images at half the price of a standard 4-image job [18].
- Pipeline tooling moved: Runway API "Recipes" expose prebuilt generative-media endpoints in one call [58]; ComfyUI showed a motion-data-driven video rebuild [43]; Photoshop AI Assistant does context-aware text edits [60].
- Midjourney is described as VC-free, ~$500M revenue, <200 staff, funding R&D from its image product [6][22] — relevant to whether its image/video cadence continues.

## What happened
The day's volume centered on Midjourney's hardware announcement: "Midjourney Medical" and a full-body ultrasonic computational-tomography "Scanner" claiming MRI-quality 3D imaging in ~60 seconds using sound and water instead of radiation or magnets, with ~358,000 on-chip transducers and a stated goal of 50,000 units doing a billion scans/month [1][2][3][4][16][53]. Most high-score items are reaction/speculation rather than data [5][9][13][19][24][32][51], and at least one clinician noted little hard technical data was available [37]. The company was repeatedly described as community-funded, ~$100M revenue in 9 months rising past $500M, under 200 employees [6][22].

## Why it matters (reasoning)
For NDF DEV's pipelines (games, XR scenes, edutech visuals), the Midjourney Medical story is not actionable — it is a healthcare hardware bet, not asset generation, and the bulk of its traction is sentiment, not verified capability [5][9][13][37]. The usable signal is the video-gen competition: multiple labs shipping comparable models within the same window [28][36] plus aggressive pricing (half-price draft batches [18], unlimited monthly plans via Higgsfield [42]) lowers the cost of concept frames, animatics, and edutech b-roll. Runway Recipes [58] and the ComfyUI motion workflow [43] matter specifically because they target pipeline integration rather than one-off demos, which fits the brief's preference for production-feeding tools. A second-order risk: Midjourney is publicly redirecting attention toward medical for the next six months by its CEO's own framing [14], while its image product funds that R&D [6] — so its image/video feature cadence could slow even though revenue is healthy.

## Possibility
Continued, fast video-model iteration is likely — four named competitors were compared in a single test and several shipped near-simultaneously [28][36][48]. An open-weight model matching or beating Fable is plausible but unproven; item [27] frames it only as a hypothetical, not a release. Midjourney's 50,000-scanner / billion-scans-a-month fleet is unlikely on any near-term horizon — it is an aspirational target with no shipped-device data and skeptical clinical commentary [4][37], and "MRI-quality" remains a marketing claim, not a validated result [11][16][37]. No source gives a numeric probability, so none is asserted here.

## Org applicability — NDF DEV
Actions: (1) Run a short bake-off of Seedance 2.0, Kling 3.0, and Grok Imagine 1.5 for edutech b-roll and game-trailer shots, using the published body-physics comparison as a starting filter [28][36][57] — effort low. (2) Use Midjourney V8.1 big-batch draft mode for cheap concept ideation before committing to high-res renders [18] — low. (3) Prototype Runway API Recipes if you need hosted generative endpoints inside a content tool or web/mobile app [58] — med. (4) Evaluate the ComfyUI motion-data workflow for animation/XR previz where you already have motion capture [43] — med. (5) Trial Photoshop AI Assistant for consistency-preserving asset cleanup [60] — low. Skip: Midjourney Medical and all scanner coverage [1][2][3][4][9][16][53] — irrelevant to your pipelines; and discount unverified "MRI-quality" / fleet claims [11][37]. Drop any plan that depends on the open-weight-beats-Fable scenario until a model actually ships [27].

## Signals to Watch
- Whether a Chinese open-weight model actually beats Fable on benchmarks and feel, beyond the hypothetical [27].
- Seedance 2.0 pricing and quota durability on Higgsfield's unlimited offer [42][48].
- Runway Recipes API rollout and which endpoints become production-ready [58].
- Whether Midjourney's image/video feature cadence slows as Medical absorbs focus for the next ~6 months [14][6].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | midjourney | ^32439 c2080 | [Announcing a new division of Midjourney called "Midjourney Medical" https://t.co](https://x.com/midjourney/status/2067421950314688759) |
| x | midjourney | ^25306 c1101 | [A technical dive inside our new "Midjourney Scanner" https://t.co/wJBHz2O7ro](https://x.com/midjourney/status/2067422898407837797) |
| x | Pirat_Nation | ^5341 c99 | [Midjourney, the company behind the popular AI image generator, has unveiled what](https://x.com/Pirat_Nation/status/2067517672120787395) |
| x | nickfloats | ^4175 c133 | [Full body ultrasonic computational tomography Our goal is to build a fleet of 50](https://x.com/nickfloats/status/2067423587540123853) |
| x | aakashgupta | ^3524 c103 | [Let me explain why an AI art company just built a full-body medical scanner, bec](https://x.com/aakashgupta/status/2067579580622528913) |
| x | nickfloats | ^3497 c86 | [What Midjourney is: - No investors, fully community-funded research lab - Revenu](https://x.com/nickfloats/status/2067445022484529282) |
| x | midjourney | ^3287 c752 | [We're gonna do a Midjourney Medical AMA (ask me anything ) right here all aftern](https://x.com/midjourney/status/2067688872944025975) |
| x | amazingzeros | ^3267 c10 | [sonic fan pissing their pants about fortnite as if sora ai getting deleted didn’](https://x.com/amazingzeros/status/2067666616700334555) |
| x | afshineemrani | ^3149 c105 | [I'm a cardiologist. Something just happened today that I genuinely did not see c](https://x.com/afshineemrani/status/2067630924108538083) |
| x | levelsio | ^2629 c86 | [I don't know if it's obvious information or not but if you talk to random people](https://x.com/levelsio/status/2067662326082498899) |
| x | digijordan | ^2377 c143 | [Midjourney just shocked the world: They’re building the Midjourney Scanner…a ful](https://x.com/digijordan/status/2067495206459519338) |
| x | is_OwenLewis | ^1987 c81 | [I did not see this one coming. BREAKING NEWS folks! Midjourney, yes the AI image](https://x.com/is_OwenLewis/status/2067467282180370447) |
| x | _sholtodouglas | ^1642 c53 | [If deployed widely - I bet this will save the US healthcare system at least 100x](https://x.com/_sholtodouglas/status/2067473495920140363) |
| x | ZeffMax | ^1602 c13 | [Loved Midjourney CEO David Holz's answer on what to make of the company now: “We](https://x.com/ZeffMax/status/2067479376518902219) |
| x | itsandrewgao | ^1342 c22 | [. @midjourney Scanner interactive 3d model I made! fun piece of trivia: I intern](https://x.com/itsandrewgao/status/2067513003227148579) |
| x | AdrianDittmann | ^941 c68 | [This is so cool! Midjourney Medical built a full body Ultrasonic CT scanner. You](https://x.com/AdrianDittmann/status/2067574011626946587) |
| x | Prolotario1 | ^868 c79 | [Quite The Eventful Day It Has Been: New Air Force 1 New GTA 6 Promo New Midjourn](https://x.com/Prolotario1/status/2067768517613551818) |
| x | midjourney | ^833 c29 | [We've released a new big-batch draft mode for V8.1. This new mode lets you gener](https://x.com/midjourney/status/2067292710063800483) |
| x | peer_rich | ^797 c15 | [we were promised AI to solve cancer by big tech and its a tiny AI bootstrapped f](https://x.com/peer_rich/status/2067493323015655566) |
| x | cignificants | ^786 c10 | [so hey, aside from midjourney and gemini what other generative AI program do you](https://x.com/cignificants/status/2067644406728135033) |
| x | midjourney | ^734 c47 | [t-minus 3 hours! we will drop a Livestream link soon. keep watch 🫡](https://x.com/midjourney/status/2067367868837322980) |
| x | dcbruck | ^631 c14 | [0 VC funding. $500M(+) in revenue. Less than 200 employees. And now they're rein](https://x.com/dcbruck/status/2067599482519216293) |
| x | BrianRoemmele | ^603 c44 | [Electronic Medicine is the future: Sound waves vs. Radiation. Currents and frequ](https://x.com/BrianRoemmele/status/2067619864370634919) |
| x | pronounced_kyle | ^589 c16 | [I'm calling it: this is the start of a new era in tech. First tangible example o](https://x.com/pronounced_kyle/status/2067595725404590439) |
| x | Scobleizer | ^571 c41 | [Congrats @midjourney and @DavidSHolz. It has been a while since a new product in](https://x.com/Scobleizer/status/2067489364725412345) |
| x | tomhfh | ^525 c20 | [This is so cool. A full-body ultrasound using no radiation and no magnets. Thank](https://x.com/tomhfh/status/2067550047483437079) |
| x | EMostaque | ^447 c102 | [How would you change your priors if a Chinese lab released an open model that be](https://x.com/EMostaque/status/2067610502826463409) |
| x | YourAlphaMom | ^404 c51 | [New body-physics test for the best AI video tools: The newly released Grok Imagi](https://x.com/YourAlphaMom/status/2067296958797025677) |
| x | swyx | ^391 c43 | [my notes from the @midjourney medical launch - @Scobleizer compared this to the ](https://x.com/swyx/status/2067468331918242127) |
| x | beffjezos | ^368 c27 | [Midjourney using its image gen AI expertise for next-gen imaging of the human bo](https://x.com/beffjezos/status/2067472148202184958) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@midjourney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 32439 · 💬 2080</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2067421950314688759">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Announcing a new division of Midjourney called &quot;Midjourney Medical&quot; https://t.co/c14YcO6yaU”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney is launching a dedicated division called Midjourney Medical, applying its generative image AI to the medical sector.</dd>
      <dt>Why interesting</dt>
      <dd>Midjourney entering a regulated vertical shows multimodal AI moving beyond creative tools into medical simulation and training content — a space adjacent to XR e-learning.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Track Midjourney Medical's visual output as a reference for medical simulation asset pipelines if the studio pursues health-sector e-learning or XR work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/midjourney/status/2067421950314688759" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@midjourney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 25306 · 💬 1101</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2067422898407837797">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A technical dive inside our new &quot;Midjourney Scanner&quot; https://t.co/wJBHz2O7ro”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney published a technical deep-dive into their new 'Midjourney Scanner' system, detailing its internal architecture and how it works.</dd>
      <dt>Why interesting</dt>
      <dd>A studio using Midjourney for asset generation benefits from knowing how their scanning pipeline works — especially for content safety and quality control.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Read the technical article to check if the scanner's approach to image analysis can inform the studio's own AI asset validation workflow.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/midjourney/status/2067422898407837797" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5341 · 💬 99</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2067517672120787395">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Midjourney, the company behind the popular AI image generator, has unveiled what it says is the world’s first full-body ultrasound CT scanner. &gt;The technology aims to make full-body imaging safer and ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney (the AI image-gen company) has revealed a full-body ultrasound CT scanner that images 25+ organs in ~1 min with no radiation, targeting FDA approval and market launch by end of 2027.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2067517672120787395" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nickfloats</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4175 · 💬 133</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nickfloats/status/2067423587540123853">View @nickfloats on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Full body ultrasonic computational tomography Our goal is to build a fleet of 50,000 of these scanners capable together of doing a billion scans a month. Enough to bring full body imaging to everyone ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney Medical announced a goal to deploy 50,000 full-body ultrasonic computational tomography scanners capable of one billion scans per month worldwide.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nickfloats/status/2067423587540123853" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aakashgupta</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3524 · 💬 103</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aakashgupta/status/2067579580622528913">View @aakashgupta on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Let me explain why an AI art company just built a full-body medical scanner, because almost everyone is reading this as a random pivot. Ultrasonic CT works by firing sound through your body and record”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney repurposed its image reconstruction model to solve ultrasonic CT's inverse-scattering problem, producing full-body 3D scans in 60 seconds with sub-millimeter resolution, deployed inside spas.</dd>
      <dt>Why interesting</dt>
      <dd>It confirms that a generative model's core skill — mapping ambiguous noisy input to coherent output — transfers across modalities, not just text-to-image.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">For XR or sensor-heavy projects, evaluate whether the studio's existing AI reconstruction pipelines can ingest new input types (audio, depth, IMU) before building separate models.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aakashgupta/status/2067579580622528913" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nickfloats</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3497 · 💬 86</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nickfloats/status/2067445022484529282">View @nickfloats on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“What Midjourney is: - No investors, fully community-funded research lab - Revenue from image generation product funds all R&amp;D - ~$100M in first 9 months, $200M by month 12, still growing - 8 active pr”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney is bootstrapped to ~$200M annual revenue with no investors, run by David Holz (Leap Motion + Northstar AR headset founder), and is shipping 2 consumer hardware products soon alongside 4 software projects.</dd>
      <dt>Why interesting</dt>
      <dd>Holz's core thesis — human-technology interaction is the bottleneck, not compute — maps directly to XR/VR UX design priorities, and his hardware pedigree makes the 2 mystery consumer devices worth watching.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Monitor Midjourney's 2 consumer hardware product announcements — if they are input or sensing devices, evaluate them for the studio's XR/VR prototyping pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nickfloats/status/2067445022484529282" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@midjourney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3287 · 💬 752</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2067688872944025975">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We're gonna do a Midjourney Medical AMA (ask me anything ) right here all afternoon. Post your questions below and we'll try to answer as many as we can! ❤️”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney announced a live medical-topic AMA on X with no product details, release notes, or technical content — just an open Q&amp;A invite.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/midjourney/status/2067688872944025975" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@amazingzeros</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3267 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/amazingzeros/status/2067666616700334555">View @amazingzeros on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“sonic fan pissing their pants about fortnite as if sora ai getting deleted didn’t set their games back by 20 years”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user mocks Sonic fans over Fortnite discourse while making an offhand hyperbolic jab that 'Sora AI getting deleted set games back 20 years' — no factual claim about any AI product.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/amazingzeros/status/2067666616700334555" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
