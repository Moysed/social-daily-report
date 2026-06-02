---
type: social-topic-report
date: '2026-06-02'
topic: multimodal-ai
lang: th
pair: multimodal-ai.en.md
generated_at: '2026-06-02T03:42:18+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 110
salience: 0.6
sentiment: mixed
confidence: 0.55
tags:
- multimodal-ai
- open-weights
- image-to-3d
- video-generation
- world-models
- comfyui
thumbnail: https://pbs.twimg.com/media/HJqUhLQa8AIb5qv.jpg
translated_by: claude-sonnet-4-6
---

# Multimodal AI — 2026-06-02

## TL;DR
- NVIDIA's Cosmos 3 ขึ้นอันดับ 1 ในกลุ่ม open-weights models ทั้ง text-to-image และ image-to-video บน Artificial Analysis leaderboards; NVIDIA, Runway และ labs อื่นๆ ร่วมก่อตั้ง 'Cosmos Coalition' เพื่อ open-source world models สำหรับ physical AI [13][9][46]
- TripoAI ปล่อย TripoSplat เป็น open-source image-to-3D Gaussian model พร้อม ComfyUI support วันแรก — รูป 2D หนึ่งภาพได้ 3D Gaussian asset เหมาะกับ stylized props และตัวละคร [41]
- ByteDance open-source Bernini framework สำหรับ video generation + editing (text prompts ผสม image/video references) พร้อม code สาธารณะ [16]
- ฝั่ง closed video ยังแข่งกันเข้มข้น: Grok Imagine Video 1.5 Preview ขึ้นอันดับ 1 image-to-video บน Arena leaderboard แซง Seedance 2.0, Veo 3.1 และ Vidu [23]; Runway ส่ง Aleph 2.0 compositing mattes สำหรับ subject isolation [24]
- ปริมาณมากของวันนี้เป็น listicles '80+ AI tools' [1][25][42] และ pipeline กลโกง dropshipping/UGC [5][10][17][35] — ไม่ใช่ signal ที่ใช้งานได้จริง

## What happened
มี release ที่จับต้องได้ 3 ตัวโดดเด่น NVIDIA's Cosmos 3 ซึ่งเป็นตระกูล omnimodal world models ขึ้นอันดับ 1 บน Artificial Analysis open-weights leaderboards ทั้ง text-to-image และ image-to-video [13] และ NVIDIA พร้อม Runway กับ labs อื่นๆ ประกาศ 'Cosmos Coalition' เพื่อ open-source world models สำหรับ physical AI [9][46] TripoAI ส่ง TripoSplat เป็น open-source single-image-to-3D Gaussian model พร้อม ComfyUI support วันแรก [41] ByteDance open-source Bernini framework สำหรับ video generation/editing ขับเคลื่อนด้วย text และ reference พร้อม code สาธารณะ [16] ฝั่ง closed, Grok Imagine Video 1.5 Preview รายงานว่าอยู่อันดับ 1 image-to-video บน Arena เหนือ Seedance 2.0, Veo 3.1 และ Vidu [23], Runway เพิ่ม Aleph 2.0 mattes [24] และ Adobe ประกาศ partnership กับ NVIDIA เพื่อ optimize Photoshop, Premiere และ Substance 3D [27]

## Why it matters (reasoning)
สำหรับ studio ที่สร้างเกม, XR scenes และ edutech visuals signal ที่ใช้ได้จริงคือ open-weight และ ComfyUI-native releases ไม่ใช่การแข่ง leaderboard TripoSplat เข้าตรงจุด bottleneck ของการผลิต 3D asset — แปลงรูป concept image ให้เป็น 3D asset — และ ComfyUI day-0 support [41] ทำให้ต่อเข้า local pipeline ที่ใช้ ComfyUI, Automatic1111, Fooocus และ InvokeAI อยู่แล้วได้ทันที [11][60] Open weights และ local hosting ยังหลีกเลี่ยงความเสี่ยง 2 อย่างที่เห็นในฟีด: ปัญหา watermark/provenance (การครอบ Sora watermarks [3]) และความกังวลด้าน IP recycling [2] ซึ่งสำคัญสำหรับงาน client และ edutech ที่ต้องการ licensing สะอาด Open weights ของ Cosmos 3 [13] เป็นทางเลือกแทน closed APIs แม้การวางตัวเป็น world models สำหรับ physical AI และการ pivot ของทีม Sora ไปสู่ robotics [6][21] หมายความว่าคุณค่าระยะใกล้อยู่ที่ 2D/3D generation มากกว่า scene simulation สำหรับ XR ตัวนำ closed (Grok, Kling 3.0, Seedance 2.0, Veo 3.1) เคลื่อนเร็วและหมุนเวียนอันดับ 1 [23][4][8] จึงควรระวังการผูก pipeline กับ hosted model ใดตัวเดียว

## Possibility
**Likely:** open-weight 3D และ world-model releases จะออกมาต่อเนื่อง เพราะมี multi-lab NVIDIA coalition หนุนหลังไม่ใช่ vendor รายเดียว [9][46][13] และ 3D tools เริ่ม land พร้อม ComfyUI integration วันแรก [41] **Plausible:** ByteDance Bernini กลายเป็น local video-edit step ที่ใช้งานได้จริงเมื่อ community นำไป package เพราะ code สาธารณะแล้ว [16] **Plausible:** อันดับ 1 image-to-video ฝั่ง closed จะหมุนเวียนระหว่าง Grok, Seedance, Veo และ Kling รอบสั้นต่อไป [23][4][8] อันดับวันนี้จึงไม่เสถียร **Unlikely:** listicles '80+ AI tools' [1][25][42] หรือ dropshipping pipelines [5][10][35] จะเป็น production tooling ที่ยั่งยืน — เป็นแค่ engagement bait ที่แทบไม่มีสาระตรวจสอบได้

## Org applicability — NDF DEV
1) ทดสอบ TripoSplat ใน ComfyUI กับ concept art จริงสำหรับ Unity/XR props และ stylized characters; วัด topology/usability ก่อนผูก pipeline (effort: med) [41] 2) Standardize local generation stack บน ComfyUI เป็น hub เพื่อให้ open models ใหม่ drop in ได้โดยไม่ต้อง rework มาก (effort: low) [11][41][60] 3) ทดลอง ByteDance Bernini สำหรับ prompt-driven video edits กับคลิป internal/edutech เมื่อ weights ได้รับการ package แล้ว (effort: med) [16] 4) ประเมิน Cosmos 3 open weights เป็น fallback ไม่มี watermark, self-hostable สำหรับงาน image และ image-to-video เพื่อหลีกเลี่ยงปัญหา provenance แบบ Sora [13][3][2]; ใช้ hosted leader (Grok/Kling/Seedance) เฉพาะเมื่อ speed เป็นปัจจัยชี้ขาด [23][4] (effort: med) 5) สำหรับ compositing ใน edutech/marketing cuts ให้พิจารณา Runway Aleph 2.0 mattes เป็นตัวเลือก subject-isolation ด่วน (effort: low) [24] **ข้าม:** listicle round-ups [1][25][42][52], dropshipping/UGC grift threads [5][10][17][35][36] และ commentary ด้าน philosophy/robotics-pivot [6][12][15][50] — ไม่มี production value ที่นำไปใช้ได้

## Signals to Watch
- ComfyUI day-0 support ในฐานะ distribution channel สำหรับ open 3D/video models ใหม่ — ติดตามว่าอะไรจะ land ต่อไป [41]
- ความถี่ output ของ Cosmos Coalition และเงื่อนไข licensing สำหรับ open world models [9][46][13]
- ByteDance Bernini จะได้ community ComfyUI nodes / usable weights จริงหรือแค่มี repo [16]
- ความผันผวนของ image-to-video leaderboard (Grok vs Seedance vs Veo vs Kling) เป็นสัญญาณว่า hosted API ไหนควรเช่าใช้ ไม่ใช่ผูกยาว [23][4][8]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Rajesh992510253 | ^1838 c59 | [80+ AI tools to finish months of work in minutes. 1. Research - ChatGPT - Copilo](https://x.com/Rajesh992510253/status/2061123080429429035) |
| x | fabianstelzer | ^1394 c2 | [@JoshRaby Gibberish is to avoid IP detection as they just run endlessly recycle ](https://x.com/fabianstelzer/status/2061083464439382108) |
| x | TheDivineNigga | ^1022 c10 | [@lowtierrogdaily Cropped the video so we couldn't see that sora ai watermark😂](https://x.com/TheDivineNigga/status/2061615794241343848) |
| x | underwoodxie96 | ^751 c19 | [I created this video using GPT Image 2.0 and Kling 3.0. I also tested Seedance 2](https://x.com/underwoodxie96/status/2061414477120016873) |
| x | RetroChainer | ^746 c37 | [> the pipeline behind "AI dancing girl" accounts: 1. find a viral tiktok dance, ](https://x.com/RetroChainer/status/2061100475160653900) |
| x | EMostaque | ^546 c23 | [Sora team became robotics team](https://x.com/EMostaque/status/2061131278091464906) |
| x | lanxre | ^487 c3 | [So the devs dissected and studied RDR2 camera work to give the motorcycle that c](https://x.com/lanxre/status/2061042824057868323) |
| x | 0xbisc | ^391 c20 | [FLAT OUT made with Midjourney V8.1 + Seedance 2 #DreaminaCPP @dreamina_ai Prompt](https://x.com/0xbisc/status/2061045166149116402) |
| x | runwayml | ^369 c37 | [Introducing the Cosmos Coalition A new global initiative with NVIDIA and leading](https://x.com/runwayml/status/2061315089869721682) |
| x | N01ennn | ^301 c23 | [a 21 year old makes $30,000/month. Pinterest photo. AI video. Shopify store. zer](https://x.com/N01ennn/status/2061201825035178298) |
| x | heyrimsha | ^288 c8 | [9 Best GitHub repos to generate AI images locally for free: 1. ComfyUI https://t](https://x.com/heyrimsha/status/2061067323944120457) |
| x | EMostaque | ^274 c28 | [My review of Claude Opus 4.8: We should worry less about being turned into paper](https://x.com/EMostaque/status/2061217853521400081) |
| x | ArtificialAnlys | ^242 c15 | [NVIDIA's Cosmos 3 lands at #1 among open weights models in both Text to Image an](https://x.com/ArtificialAnlys/status/2061494719998546206) |
| x | javilopen | ^239 c70 | [WTF? Nobody that is actually serious about AI film making actually believes this](https://x.com/javilopen/status/2061000718748692863) |
| x | EMostaque | ^218 c55 | [your upbringing is your system prompt](https://x.com/EMostaque/status/2061191607165038652) |
| x | aisearchio | ^199 c7 | [Bytedance drops an open-source Gemini Omni!!! Bernini is a new AI video generati](https://x.com/aisearchio/status/2061572022074020174) |
| x | 0xFrogify | ^188 c9 | [Should I have gatekept this? This guy just casually dropped how he made $20,000 ](https://x.com/0xFrogify/status/2061223490770936137) |
| x | hayalet_kadir | ^186 c0 | ["Prompt by Hayalet - Generated by Stable Diffusion DreamShaper XL" #SciFiArt htt](https://x.com/hayalet_kadir/status/2061324149822230964) |
| x | hayalet_kadir | ^185 c8 | ["Prompt by Hayalet - Generated by Stable Diffusion DreamShaper XL" #RobotDesign ](https://x.com/hayalet_kadir/status/2061232463033028638) |
| x | fabianstelzer | ^179 c4 | [Julian Jaynes' "The Origin of Consciousness in the breakdown of the bicameral mi](https://x.com/fabianstelzer/status/2060988844703371520) |
| x | haider1 | ^176 c29 | [openai has officially entered robotics i've always believed Sora was more of a s](https://x.com/haider1/status/2061233765368696901) |
| x | runwayml | ^160 c18 | [Today we're announcing London as Runway's new European headquarters and our newe](https://x.com/runwayml/status/2061450141614145621) |
| x | mark_k | ^156 c45 | [Grok Imagine by @xai is now actually the best image-to-video model in the world.](https://x.com/mark_k/status/2061019472748564498) |
| x | runwayml | ^155 c12 | [Create compositing mattes in seconds with Aleph 2.0 Mattes let you isolate a sub](https://x.com/runwayml/status/2061548752989753454) |
| x | Nayak__Ai | ^153 c38 | [Over 80 AI tools to finish months of work in mere minutes🪄 1. 𝐑𝐞𝐬𝐞𝐚𝐫𝐜𝐡 - ChatGPT](https://x.com/Nayak__Ai/status/2061093680396861892) |
| x | EMostaque | ^153 c78 | [Let's say half of OpenAI and Anthropic goes to the American people, $1 trillion ](https://x.com/EMostaque/status/2061461391303753992) |
| x | icreatelife | ^139 c33 | [Excited to share with you Adobe where I work full time partners with NVIDIA 🎉 Ad](https://x.com/icreatelife/status/2061497655289926143) |
| x | rosemoni18 | ^126 c22 | [100+ AI Tools to replace your tedious work: 1. Research - @ChatGPTapp - YouChat ](https://x.com/rosemoni18/status/2061193894080233980) |
| x | azed_ai | ^117 c18 | [Hope your morning is off to a great start my friends Newly created style on Midj](https://x.com/azed_ai/status/2061312815479292008) |
| x | fabianstelzer | ^117 c12 | [no introspection you say? https://t.co/8acgbLNcNs](https://x.com/fabianstelzer/status/2061318774255477071) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Rajesh992510253</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1838 · 💬 59</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Rajesh992510253/status/2061123080429429035">View @Rajesh992510253 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“80+ AI tools to finish months of work in minutes. 1. Research - ChatGPT - Copilot - Gemini - Abacus - Perplexity 2. Image - Fotor - Dalle 3 - Stability AI - Midjourney - Microsoft Designer 3. CopyWrit”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ viral บน X รวม AI tools 80+ ตัวใน 18 หมวด (research, video, automation, UI/UX, audio ฯลฯ) เป็น directory รวมเล่ม ไม่มี release ใหม่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ครอบคลุม categories ที่ทีมใช้จริง — UI/UX, video, automation — ดูเป็น checklist เทียบกับ tools ที่มีอยู่แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เอา หมวด automation กับ meeting (Make, Zapier, Fireflies, Otter) มา cross-check กับ workflow ทีมว่ามี gap ไหนที่ยังไม่ได้ใช้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Rajesh992510253/status/2061123080429429035" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@fabianstelzer</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1394 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/fabianstelzer/status/2061083464439382108">View @fabianstelzer on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@JoshRaby Gibberish is to avoid IP detection as they just run endlessly recycle copyrighted stuff”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@fabianstelzer อ้างว่า AI model จงใจสร้าง gibberish เพื่อหลบ IP detection ขณะนำ copyrighted data มาใช้ซ้ำ — ไม่มีหลักฐานอ้างอิง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/fabianstelzer/status/2061083464439382108" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheDivineNigga</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1022 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheDivineNigga/status/2061615794241343848">View @TheDivineNigga on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@lowtierrogdaily Cropped the video so we couldn't see that sora ai watermark😂”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้รายหนึ่งแฉว่าอีกบัญชีตัด watermark ของ Sora AI ออกจากวิดีโอเพื่อแอบอ้างว่าเป็นของตัวเอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheDivineNigga/status/2061615794241343848" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@underwoodxie96</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 751 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/underwoodxie96/status/2061414477120016873">View @underwoodxie96 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I created this video using GPT Image 2.0 and Kling 3.0. I also tested Seedance 2.0 and Google Omni. They're much faster for generating transformation videos, but in my tests there were often one or tw”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Creator เปรียบ GPT Image 2.0 + Kling 3.0 กับ Seedance 2.0 / Google Omni — workflow start-frame/end-frame แบบ multi-clip ใน CapCut ให้ผล cinematic กว่า single-shot generation</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Workflow start-frame/end-frame เป็นเทคนิคที่ใช้ได้จริงกับ AI video คุณภาพสูง — ตรงกับงาน XR, e-learning และ content ของ studio</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ใช้ workflow start-frame/end-frame ตอนทำ AI video transition สำหรับ e-learning หรือ XR demo แทน single-shot generation</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/underwoodxie96/status/2061414477120016873" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RetroChainer</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 746 · 💬 37</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RetroChainer/status/2061100475160653900">View @RetroChainer on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“&gt; the pipeline behind &quot;AI dancing girl&quot; accounts: 1. find a viral tiktok dance, download it 2. screenshot frame 1 → chatgpt writes the prompt 3. generate your model from it (freepik) 4. wavespeed → kl”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Post เปิด pipeline จริงของบัญชี AI influencer: ChatGPT เขียน prompt → Freepik สร้าง model → WaveSpeed + Kling 2.6 motion control โอนท่าเต้น TikTok ใส่ตัวละครที่ gen ขึ้นมา แล้ว post วันละ 2 ครั้งขาย Fanvue</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Kling 2.6 motion control โอน movement จาก reference video ใส่ตัวละคร generated ได้เลย — ใช้กับ cinematic ใน Unity หรือ XR prototype โดยไม่ต้องมี mocap rig</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Kling 2.6 motion control โดยใช้ reference clip + generated character เพื่อดูว่าใช้กับ XR หรือ cinematic prototype ของ studio ได้จริงไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RetroChainer/status/2061100475160653900" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EMostaque</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 546 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EMostaque/status/2061131278091464906">View @EMostaque on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Sora team became robotics team”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีม Sora ของ OpenAI (video generation) ถูกโยกไปทำ robotics แทน — บ่งชี้ว่า OpenAI ลดน้ำหนัก video AI ลงอย่างชัดเจน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่วางแผนใช้ Sora ใน video pipeline ควรคาดว่า feature ใหม่จะช้าลง เพราะ OpenAI ย้าย resource ออกไปแล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้าทีมวางแผนใช้ Sora ใน video workflow ให้ประเมิน Runway หรือ Kling เป็น alternative หลักแทนได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EMostaque/status/2061131278091464906" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@lanxre</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 487 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/lanxre/status/2061042824057868323">View @lanxre on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“So the devs dissected and studied RDR2 camera work to give the motorcycle that cinematic feel, instead of just feeding prompts into sora Ai like that train game does for its presentation? https://t.co”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีม dev ถอดแบบระบบ camera ของ RDR2 เพื่อสร้าง cinematic feel ให้เกม motorcycle ขณะที่เกม train อีกตัวเลือกใช้ Sora AI แทน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เห็น design fork ชัดเจน: ศึกษา camera ด้วยมือ vs ใช้ AI generate — ทั้งคู่ ship ได้ แต่ผลลัพธ์และ skill ที่ต้องลงทุนต่างกัน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ก่อนทำ in-game camera หรือ cutscene ให้ Unity team ดู reference จากเกมที่ ship แล้วก่อน ค่อยพิจารณา AI video tools</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/lanxre/status/2061042824057868323" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@0xbisc</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 391 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/0xbisc/status/2061045166149116402">View @0xbisc on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“FLAT OUT made with Midjourney V8.1 + Seedance 2 #DreaminaCPP @dreamina_ai Prompt below ↓ https://t.co/OrtLek61oC”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้โพสต์แสดงวิดีโอที่สร้างด้วย Midjourney V8.1 ต่อเข้า Seedance 2 ของ Dreamina เป็น pipeline image-to-video ที่ใช้งานได้จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Midjourney V8.1 + Seedance 2 ทำ image-to-video ได้โดยไม่ต้องเขียนโค้ด เหมาะใช้ทำ concept previz สำหรับงาน game หรือ XR โดยไม่ต้องมี animator</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ pipeline Midjourney V8.1 → Seedance 2 สำหรับทำ concept art หรือ previz environment ของงาน XR ก่อนเข้าสู่ขั้นตอนผลิต asset จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/0xbisc/status/2061045166149116402" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
