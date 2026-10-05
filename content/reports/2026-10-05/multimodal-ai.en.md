---
type: social-topic-report
date: '2026-10-05'
topic: multimodal-ai
lang: en
pair: multimodal-ai.th.md
generated_at: '2026-10-05T03:27:47+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 108
salience: 0.5
sentiment: mixed
confidence: 0.45
tags:
- 3d-generation
- comfyui
- video-generation
- open-weights
- asset-pipeline
- kling
thumbnail: https://pbs.twimg.com/media/HTr8ShkbYAAWoAy.png
---

# Multimodal AI — 2026-10-05

## TL;DR
- Trellis2 combined with Pixal3D in ComfyUI is reported to generate watertight 3D meshes locally, with no holes, doubled-up surfaces or inner shells, at up to 2K resolution [4]. This is the most production-relevant item for game and XR assets today.
- MiniMax-H3 has a growing local ComfyUI toolchain: one user reports a 15s video made on an RTX 5070 with 12GB of VRAM [54], there is an X2-Detail VAE that adds detail and 2x upscaling [7], and an Extender continues existing clips using reference frames [28].
- Hosted video models compete on clip length and shot control: Kling 4.0 claims native 30-second generation and multi-keyframe control [26] and ships a Flash variant [47], and Seedance 2.5 is being pushed through free-credit promotions [27][32].
- A practitioner who works with 3D and AI professionally calls AI video the most costly, unreliable and time-wasting part of their pipeline, citing a 6:1 ratio [60]. Engagement posts do not show that cost.
- The top-engagement items are mostly NSFW deepfake promotions and tool listicles [1][3][9][10][14][8][12]. Little of today's volume is about real production tools.

## What happened
On the 3D side, a post reports that Trellis2 combined with Pixal3D in ComfyUI produces clean meshes that print or import without repair, at up to 2K resolution [4]. Another describes a workflow where the scene layout, AI-generated assets and camera are blocked out in Blender and then used to guide video generation [5]. On local video, MiniMax-H3 appears repeatedly. A specialised VAE for image-to-video adds detail and 2x upscaling [7], an Extender node continues an existing video with reference frames shown on clip cards [28], and users post image-to-video shorts [35], including a 15s clip run locally on a 12GB RTX 5070 with the model and LoRA shared [54]. A 7.3GB quantized Qwen3.8-27B vision-language model called Mitsuba was also released for ComfyUI, aimed at describing images [42].

Among hosted services, Kling 4.0 is promoted for realism, native 30s output and multi-keyframe control [26][47], and Kling will present on production at scale at Advertising Week New York on October 6 [45]. Seedance 2.5 [27][32], Midjourney v8.2 character style-mix prompts [31][38] and Gemini Omni for video [55] show up in creator showcases. One reply says Sora was discontinued about six months ago [46]; this is unverified. There are also signs of pushback: a professional reports a 6:1 cost ratio for AI video [60], consumers say they won't buy a game made with AI [25], there is an argument to ban image and video generation [58], and a debate over whether training is theft [13]. Most of the high-engagement posts are adult deepfake tool promotions and recycled 'websites that feel illegal' lists, which carry no technical signal [1][3][6][8][9][10][12][14][37].

## Why it matters (reasoning)
The useful shift is that local open pipelines are reaching output a studio can actually ship. Watertight meshes [4] remove the main cleanup cost of AI 3D output for Unity and XR scenes: holes and inner shells break collisions, lightmap UVs and Quest performance budgets. Running MiniMax-H3 on a 12GB consumer GPU [54] means video generation no longer requires renting cloud GPUs. Add-ons like the Extender and upscaling VAE [7][28] suggest a toolchain is forming around one model, as happened earlier with SD and Flux. Treat all of this as claims made on social media, not benchmarks: no item gives polycount, topology quality, UV quality or generation time.

Hosted video is competing on length and control, not just how realistic it looks [26]. That matters because control is what makes output reusable for edutech explainers and trailers. Still, the 6:1 cost report [60] is a better planning number than showcase clips, and the Blender-first approach [5] points the same way: the reliable approach is to fix the geometry and camera deterministically and use AI for appearance only. Two risks follow from the noise around this topic. First, deepfake and NSFW tooling dominates attention [1][3][9], and that drives regulatory and platform scrutiny of generative video. Second, buyers are visibly pushing back on AI-made games [25][58], so studios need to think about disclosure and art direction, especially for client and edutech work.

## Possibility
Likely: more ComfyUI nodes built around MiniMax-H3 (extension, upscaling, LoRAs), because three separate add-ons and several user showcases appeared within a day [7][28][35][54]. Likely: 3D-generation pipelines move toward printable, game-ready meshes as the baseline expectation, since watertightness is now being marketed as a feature [4]. Plausible: blocking out scenes in a 3D tool and then generating video becomes the standard way to get consistent multi-shot output, given multi-keyframe control in Kling 4.0 [26] and the Blender workflow in [5]. Plausible: Kling positions itself for agency and advertising production after its Advertising Week panel [45]. Unlikely in the near term: AI video becoming cheap or reliable enough to replace planned production, given the practitioner's 6:1 report [60].

## Org applicability — NDF DEV
1) Test Trellis2 + Pixal3D in ComfyUI on 5–10 prop concepts from a current Unity or XR project. Measure whether meshes are watertight, polycount after decimation, UV and texture usability, and Quest draw-call cost before adopting it (effort: med) [4]. 2) If a 12GB+ GPU is available, run MiniMax-H3 image-to-video locally for edutech intro and B-roll clips, and log hours spent per usable second to compare against the reported 6:1 ratio (effort: med) [54][60]. Try the Extender and X2-Detail VAE only after the base output is acceptable (effort: low) [7][28]. 3) For any client video, block out layout and camera in Blender before generating, so shots are repeatable and revisions stay cheap (effort: med) [5]. 4) When a hosted option is needed for longer single shots, trial Kling 4.0's 30s and multi-keyframe output on one storyboard before committing to a subscription (effort: low) [26][47]. 5) Write a short internal policy on disclosing AI-generated assets in games and edutech deliverables, given buyer pushback (effort: low) [25][58]. Skip: every deepfake, face-swap and 'uncensored' tool [1][3][9][10][14][37][53], because of legal and reputational risk and no production value. Skip the 'illegal websites' and '50 AI tools' listicles [8][12][30][56], and the kids-channel content-farm playbook [11].

## Signals to Watch
- Independent tests of Trellis2 + Pixal3D topology and UV quality, beyond the original claim [4]
- Whether MiniMax-H3's licence allows commercial use, and how its ComfyUI node ecosystem grows [7][28][54]
- Announcements from Kling's Advertising Week panel on October 6 about production or API pricing [45]
- Practitioner cost data on AI video versus traditional production, as a check on showcase hype [60]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | rexsooo | ^1798 c19 | [ANOTHER FREE AI DEEPFAKE TOOL (UNCENSORED, 18+) https://t.co/avsebJkD1N • AI fac](https://x.com/rexsooo/status/2106244384933245002) |
| x | sauda_coder | ^1174 c20 | [10 GitHub repos that seem "illegal" but are perfectly legal 1. yt-dlp → https://](https://x.com/sauda_coder/status/2106273288091840602) |
| x | Forhanvv | ^1079 c5 | [ANOTHER FREE AI DEEPFAKE TOOL 👀 18+ only. https://t.co/JAxSHu5B1O lets you: • AI](https://x.com/Forhanvv/status/2106449748257575324) |
| x | philippsieben | ^825 c12 | [The best local 3D AI can now generate 100% watertight meshes. Trellis2 + Pixal3D](https://x.com/philippsieben/status/2106314260707958945) |
| x | deweytn | ^792 c20 | [3D AI + Blender Gives Full Scene Control for Video Generation Your AI video shou](https://x.com/deweytn/status/2106499269322559970) |
| x | codi_fyy | ^769 c28 | [35 WEBSITES GOOGLE DOESN'T WANT YOU TO KNOW 1. Explee .com — sends cold emails o](https://x.com/codi_fyy/status/2106659778068189561) |
| x | HuggingModels | ^684 c6 | [New AI model alert! MiniMax-H3-X2-Detail-VAE is here to supercharge your image-t](https://x.com/HuggingModels/status/2106486704127586704) |
| x | Orion_Vers7x | ^658 c36 | [30 Websites That Feel "Illegal" But Are Perfectly Legal 1. https://t.co/ZhGRKvIw](https://x.com/Orion_Vers7x/status/2106343200755487136) |
| x | rexsooo | ^597 c5 | [FOUND ANOTHER AI ADULT CONTENT GENERATOR (only for 18+) https://t.co/fU8PNkedvv ](https://x.com/rexsooo/status/2106343629316817161) |
| x | rexsooo | ^586 c4 | [UNCENSORED AI VIDEO GENERATOR IN YOUR BROWSER 😋 (18+) https://t.co/18Qt1Ld2G7 le](https://x.com/rexsooo/status/2106801572877602956) |
| x | 0xForce_ | ^554 c22 | [THIS IS F**KING INSANE She claims $69K/month from Shorts. She never starts from ](https://x.com/0xForce_/status/2106564034870771766) |
| x | malagojr | ^480 c4 | [30 Websites That Feel "Illegal" But Are Perfectly Legal 1. https://t.co/D7s9IKZw](https://x.com/malagojr/status/2106606418555965901) |
| x | ArturoWolff1 | ^373 c65 | [AI doesn't steal. It learns. https://t.co/bH76BKDlaT](https://x.com/ArturoWolff1/status/2106527397243662683) |
| x | melophile0646 | ^331 c0 | [🚨 ANOTHER FREE AI DEEPFAKE TOOL JUST DROPPED 👀 for 18 plus only. https://t.co/bn](https://x.com/melophile0646/status/2106633776009011437) |
| x | aynellex | ^301 c69 | [A little rain, a little kindness, and one tiny garden miracle. ☔🌱 Created with A](https://x.com/aynellex/status/2106251845437898892) |
| x | Kanthaswam80359 | ^273 c10 | [This video was actually made with KLING - an Indigenous Chinese AI generation so](https://x.com/Kanthaswam80359/status/2106591117223534906) |
| x | lovescapeai | ^266 c0 | [she asked for breakfast 🍼 #nsfw #thicc #wataa https://t.co/PKHnlPDTr3](https://x.com/lovescapeai/status/2106719123581603865) |
| x | stevencoder9 | ^222 c35 | [🤖 AI TOOLS WORTH KNOWING IN 2026 Productivity Notion Taskade ClickUp Motion Recl](https://x.com/stevencoder9/status/2106322884000186800) |
| x | Forhanvv | ^220 c1 | [FOUND ANOTHER AI ADULT CONTENT GENERATOR 👀 18+ only. https://t.co/i211tddOp1 let](https://x.com/Forhanvv/status/2106449075399020909) |
| x | thomasfbloom | ^210 c51 | [I find it bizarre that, despite the clear incredible capabilities of AI in e.g. ](https://x.com/thomasfbloom/status/2106448844711972986) |
| x | himanshubuildss | ^195 c8 | [Here's the stack for building a site like this with AI (save this 🔖) 𝗦𝘁𝗮𝗿𝘁 𝗵𝗲𝗿𝗲 ](https://x.com/himanshubuildss/status/2106449317406056903) |
| x | lucastohdev | ^183 c34 | [Heads up, I'm not being pessimistic or overly negative. It's just my realistic v](https://x.com/lucastohdev/status/2106561500223877626) |
| x | Romi2656 | ^179 c57 | [How advanced has AI video generation become? 🤯 Look at how insanely realistic an](https://x.com/Romi2656/status/2106256445801107596) |
| x | Jeremybtc | ^169 c110 | [Current AI subscriptions I’m paying for: 5x ChatGPT Pro 500 7x Claude Max 20x 4x](https://x.com/Jeremybtc/status/2106812545432687061) |
| x | Sora4Fortnite | ^161 c6 | [@Genki_JPN AI game, we're not buying @AkihiroHino 💔](https://x.com/Sora4Fortnite/status/2106414909944668249) |
| x | Mekarly | ^157 c40 | [AI video generation is moving from simple prompts to real creative direction Tha](https://x.com/Mekarly/status/2106864291588493611) |
| x | KevinVailAI | ^156 c37 | [Testing the limits of AI video generation with smooth motion and high-tech visua](https://x.com/KevinVailAI/status/2106610102505463813) |
| x | princedoesai | ^146 c0 | [MiniMax H3 Extender now lets ComfyUI continue an existing video, and I like that](https://x.com/princedoesai/status/2106473826049782101) |
| x | icreatelife | ^145 c50 | [Ask ChatGPT to create a tarot card based on your interests Here’s mine. A creato](https://x.com/icreatelife/status/2106801148304781570) |
| x | malagojr | ^131 c10 | [50 AI tools that can save you hundreds of hours in 2026. 1. Claude — tackle comp](https://x.com/malagojr/status/2106410818304675868) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rexsooo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1798 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rexsooo/status/2106244384933245002">View @rexsooo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“ANOTHER FREE AI DEEPFAKE TOOL (UNCENSORED, 18+) https://t.co/avsebJkD1N • AI face swap • AI image generation • AI video generation • image-to-video • one-click workflow you can start for free ⚠️ only ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An X post promotes a free, uncensored 18+ AI tool for face swap, image and video generation, and image-to-video, with a one-line note to use only your own face or a consenting person's.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rexsooo/status/2106244384933245002" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sauda_coder</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1174 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sauda_coder/status/2106273288091840602">View @sauda_coder on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“10 GitHub repos that seem &quot;illegal&quot; but are perfectly legal 1. yt-dlp → https://t.co/a9DYvZNrRO Downloads videos from any platform. YouTube Premium charges 16 dollars a month to do less 2. Ollama → ht”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral X post lists 10 open-source GitHub repos (yt-dlp, Ollama, Fooocus, Whisper, Plausible, AppFlowy, Penpot, n8n, Cal.com) as free self-hosted alternatives to paid SaaS tools.</dd>
      <dt>Why interesting</dt>
      <dd>Ollama, Whisper and Fooocus cover local LLM, transcription and image generation, and Plausible, Penpot and n8n replace paid analytics, design and automation tools.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Pick one paid SaaS subscription the studio uses, such as analytics or automation, and trial its self-hosted alternative (Plausible or n8n) on a small server.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sauda_coder/status/2106273288091840602" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Forhanvv</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1079 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Forhanvv/status/2106449748257575324">View @Forhanvv on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“ANOTHER FREE AI DEEPFAKE TOOL 👀 18+ only. https://t.co/JAxSHu5B1O lets you: • AI face swap • AI image generation • AI video generation • image-to-video • one-click workflow You can start generating fo”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An X post promotes a free web tool offering AI face swap, image and video generation, and image-to-video, and says to use only your own face or a consenting person's.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Forhanvv/status/2106449748257575324" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@philippsieben</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 825 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/philippsieben/status/2106314260707958945">View @philippsieben on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The best local 3D AI can now generate 100% watertight meshes. Trellis2 + Pixal3D in ComfyUI creates meshes with no holes, doubled-up surfaces or inner shells, at up to 2K resolution with stunning deta”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Trellis2 plus Pixal3D in ComfyUI generates watertight 3D meshes (no holes, doubled surfaces or inner shells) at up to 2K resolution, running locally and free on your own GPU.</dd>
      <dt>Why interesting</dt>
      <dd>Watertight meshes are what 3D printing, physics colliders and game-engine import need, so local image-to-3D output may need less manual cleanup.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Have the Unity team run the linked ComfyUI workflow on a local GPU with a few concept images, then check mesh quality and collider fit in-engine.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/philippsieben/status/2106314260707958945" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@deweytn</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 792 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/deweytn/status/2106499269322559970">View @deweytn on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“3D AI + Blender Gives Full Scene Control for Video Generation Your AI video shouldn’t be a guessing game. With 3D AI + Blender, you can build a scene, add AI-generated assets, and set the layout, came”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The post describes a workflow where a scene is built in Blender with AI-generated 3D assets, with layout, camera and composition set before video generation, using MCP and API automation.</dd>
      <dt>Why interesting</dt>
      <dd>Fixing layout and camera in a 3D scene first makes AI video output predictable, which cuts the retry cycles that burn time on prompt-only generation.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/deweytn/status/2106499269322559970" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@codi_fyy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 769 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/codi_fyy/status/2106659778068189561">View @codi_fyy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“35 WEBSITES GOOGLE DOESN'T WANT YOU TO KNOW 1. Explee .com — sends cold emails on autopilot https://t.co/Wb8ppu6CBi 2. NoteGPT — turns docs into podcasts https://t.co/5guI12zfQG 3. Napkin AI — turns t”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A 35-item X list of AI tools, with the first 18 visible: Cursor and v0 for code/UI, Suno, Kling and ElevenLabs for media generation, and Perplexity for search, each with a one-line pitch.</dd>
      <dt>Why interesting</dt>
      <dd>Most of these tools are well known, so the list is a quick catalogue of AI media and coding tools rather than new information. The 'Google doesn't want you to know' framing is clickbait.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/codi_fyy/status/2106659778068189561" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@HuggingModels</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 684 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/HuggingModels/status/2106486704127586704">View @HuggingModels on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“New AI model alert! MiniMax-H3-X2-Detail-VAE is here to supercharge your image-to-video game. It's a specialized VAE for ComfyUI that adds insane detail and x2 upscaling. Perfect for creators who want”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>HuggingModels posted MiniMax-H3-X2-Detail-VAE, a ComfyUI VAE that adds detail and 2x upscaling to image-to-video output generated from a single reference image.</dd>
      <dt>Why interesting</dt>
      <dd>A drop-in VAE for ComfyUI image-to-video workflows could raise output resolution without a separate upscaling pass, useful for trailers and XR/e-learning clips.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio already runs ComfyUI, test this VAE on one image-to-video workflow and compare detail and render time against the current setup.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/HuggingModels/status/2106486704127586704" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Orion_Vers7x</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 658 · 💬 36</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Orion_Vers7x/status/2106343200755487136">View @Orion_Vers7x on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“30 Websites That Feel &quot;Illegal&quot; But Are Perfectly Legal 1. https://t.co/ZhGRKvIwAD — Free unlimited AI image generation, quality rivals Midjourney 2. https://t.co/FrNru9C05N — Real-time AI image gener”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An X post lists 30 AI web tools (image generation, upscaling, voice cloning, video generation, code assistants, site builders) as free, with unverified claims like 'quality rivals Midjourney' and the list cut off at item 15.</dd>
      <dt>Why interesting</dt>
      <dd>It is a link roundup with marketing claims and no testing or pricing detail, though it shows which free multimodal tool categories are circulating.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Orion_Vers7x/status/2106343200755487136" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
