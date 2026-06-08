---
type: social-topic-report
date: '2026-06-08'
topic: multimodal-ai
lang: th
pair: multimodal-ai.en.md
generated_at: '2026-06-08T15:45:42+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 119
salience: 0.55
sentiment: mixed
confidence: 0.45
tags:
- multimodal-ai
- video-generation
- open-weights
- comfyui
- content-pipeline
- provenance-risk
thumbnail: https://pbs.twimg.com/tweet_video_thumb/HKPInRwWoAADWy1.jpg
translated_by: claude-sonnet-4-6
---

# Multimodal AI — 2026-06-08

## TL;DR
- โมเดลที่ปรากฏซ้ำในโพสต์ workflow จริง: Midjourney V8.1 [7][14][53][57][59], GPT Image 2 [7][14][31] และโมเดลวิดีโอ Seedance 2.0 [7][14][24][46]; โมเดลวิดีโอ hosted ที่ถูกกล่าวถึง ได้แก่ Veo 3.1, Kling, Runway, Grok [3][10][24][35]
- ตัวเลือก open-weights ที่ตรงกับทิศทาง NDF มีบ้างแต่น้อย: Stable Diffusion 3.5 Large [22] และ Qwen Image 2512 รันผ่าน ComfyUI [34]; ที่เหลือเป็น closed/hosted ทั้งหมด
- รูปแบบที่ใช้จริงคือ multi-tool chain — LLM เขียน script/scene, image model สร้าง keyframe, video model ใส่ motion [3][7][14]; creator อ้างรายได้ด้วยตัวเอง ($8,217/เดือนจากช่อง anime [3], $1,500 จาก 2 frame + วิดีโอ 8 วินาที [43])
- สัญญาณต้านกระแส: หลายกระทู้บอกว่า AI hype เริ่มเย็นลง — เครื่องมือที่เคยดังหายไปจากการพูดถึง [33][39][44] — บวกกับความกังวลเรื่อง deepfake/scam [13], ข้อพิพาทข้อมูล training ของ GPT-4o [8] และมีม Sora watermark ที่เย้ยหยัน AI ในเกม [1][11][25]
- 3D generative AI แทบไม่ปรากฏในชุดนี้ (มีเพียง [48] ที่เกี่ยวโดยอ้อม); image→video คือ lane ที่สมบูรณ์แล้ว, 3D asset gen ยังไม่ขึ้นมา

## What happened
ปริมาณเนื้อหา multimodal AI สูง แต่ถูกครอบงำด้วยเนื้อหาสาระน้อย: listicle '120 AI tools' [2][20][27][29][38][42][49][50][60] และโพสต์สร้างรายได้สำหรับ creator [3][5][12][19][30][43] ในโพสต์ workflow จริง เครื่องมือกลุ่มเล็กปรากฏซ้ำข้ามกัน: Midjourney V8.1 สำหรับภาพนิ่ง [7][14][53][57][59], GPT Image 2 สำหรับแก้ไข/สร้างภาพ [7][14][31] และ Seedance 2.0 สำหรับวิดีโอ/animation [7][14][24][46] โมเดลวิดีโอ hosted ที่ถูกกล่าวถึง ได้แก่ Veo 3.1, Kling, Runway และ Grok [3][10][24][35] เส้นทาง open-weights ปรากฏเพียงสองครั้ง: Stable Diffusion 3.5 Large [22] และ Qwen Image 2512 ผ่าน ComfyUI [34] เครื่องมือตัดต่อวิดีโอชื่อ 'Omni' ถูกใช้สำหรับ projection-mapping บนตึกและเอฟเฟกต์ reverse/Tenet [6][9][23]

## Why it matters (reasoning)
stack สำหรับ image→video กำลังหลอมรวม (image: Midjourney/GPT Image 2/SD 3.5/Qwen; video: Seedance 2.0/Veo 3.1/Kling/Runway) และรูปแบบ chain [3][7][14] คือวิธีที่คนใช้จริงในการส่งงาน previz, animation และ marketing clip สำหรับงาน edutech visual และ XR scene mockup ของ NDF, open-weights image model [22][34] คือตัวเลือกที่ควบคุมได้และมีต้นทุนคาดเดาได้ เหมาะกับ ComfyUI pipeline ในองค์กร; closed video model เหมาะกับ marketing/previz ไม่เหมาะกับ licensed asset pipeline ความเสี่ยงลำดับสองมีความชัดเจน: ข้อพิพาทแหล่งที่มาของ training data (#Keep4o, GPT-4o system card [8]) และความกังวล deepfake/scam [13] ก่อให้เกิดความเสี่ยงด้าน IP/consent ในงานสื่อ AI ที่ส่งมอบลูกค้า และมีม Sora watermark [1][11][25] สะท้อนความระแวงของผู้บริโภคต่อ asset ที่มองออกว่า AI ในเกม — เกี่ยวข้องกับวิธีที่ NDF ติดป้ายเนื้อหา AI ในชื่อเกมของตัวเอง กระทู้ hype-cooling [33][39][44] เป็นข้อเตือนใจไม่ให้ผูกกับ hosted tool รายเดียว

## Possibility
น่าจะเป็น: image→video chain และ Seedance 2.0 ยังคงเป็น workflow หลักของ creator จากการกล่าวถึงซ้ำอิสระ [7][14][24][46] เป็นไปได้: open-weights image model (SD 3.5 [22], Qwen Image 2512 [34]) ยังคงเป็นตัวเลือกจริงสำหรับทีมที่ต้องการ local control ผ่าน ComfyUI เป็นไปได้: attention churn ยังดำเนินต่อ — หลายโพสต์บันทึกว่าเครื่องมือที่เคยฮอตสูญเสียความนิยม [33][39][44] จึงเสี่ยงหากผูกกับ tool ใดเป็นพิเศษ ไม่น่าจะเป็น (ไม่มีแหล่งอ้างอิงรองรับ): ความก้าวหน้าของ 3D asset generation ในระยะใกล้จากชุดนี้; 3D ไม่ปรากฏเลย ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น; ตัวเลขรายได้เช่น [3] และ [43] เป็นข้อมูลรายงานตนเองและยังไม่ได้รับการยืนยัน

## Org applicability — NDF DEV
ความพยายามน้อย: ทดลอง ComfyUI + Qwen Image 2512 [34] และ Stable Diffusion 3.5 Large [22] ในเครื่องสำหรับภาพประกอบ edutech และ XR concept board — open weights, ไม่มีค่า API per-image ความพยายามน้อย/กลาง: ทดสอบ Seedance 2.0 [7][14][46] และ Veo 3.1/Kling [10][24] สำหรับ previz สั้นและ explainer clip จำกัดการใช้ภายในและงานที่ไม่ต้องการ license จนกว่าจะชัดเรื่อง provenance ความพยายามกลาง: ใช้ chain LLM→image-keyframe→video-motion [3][7][14] เป็น SOP ภายในสำหรับ storyboard/previz ความพยายามน้อย (governance): กำหนดนโยบายเรื่อง AI watermark ที่มองเห็นได้และ consumer perception สำหรับเกมที่ส่งมอบ [1][11][25] และ checklist IP/consent สำหรับสื่อ AI ในงานลูกค้า จากข้อพิพาท training data [8] และความเสี่ยง deepfake [13] ข้ามได้: listicle 'X AI tools' [2][20][27][29][38][42][49][50] และโพสต์ hustle/income [5][12][19][30] — ไม่มีเนื้อหาเชิง engineering — และข้าม closed black-box demo ตามที่กำหนดไว้

## Signals to Watch
- Seedance 2.0 ปรากฏซ้ำข้าม creator ที่ไม่เกี่ยวข้องกัน [7][14][24][46] — ติดตาม open weights หรือ API pricing ที่เปิดเผย
- Qwen Image 2512 ใน ComfyUI [34] — ติดตามในฐานะ open-weights image model เหมาะกับ local pipeline
- 'Omni' video editor สำหรับ projection-mapping และ reverse effect [6][9][23] — niche แต่เป็นมุมใหม่ด้าน scene control สำหรับ XR
- Meta-thread hype-cooling [33][39][44] — เตือนอยู่เสมอไม่ให้ lock-in กับ vendor รายเดียว

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | AmityBlight6777 | ^3610 c8 | [When I'm playing Sonic frontiers 2 and I see the Sora AI watermark on the corner](https://x.com/AmityBlight6777/status/2063713637852688524) |
| x | Rajesh992510253 | ^3142 c75 | [120 + Mind blowing AI tools 🔥 1. Ideas - Claude - ChatGPT - Bing Chat - Perplexi](https://x.com/Rajesh992510253/status/2063808629619532180) |
| x | 0x_fokki | ^1146 c56 | [🚨a 22-year-old makes $8,217/month from an anime channel he built in one weekend ](https://x.com/0x_fokki/status/2063309212353007843) |
| x | Suhail | ^707 c22 | [All my bad VC stories mostly just make me sound like a wuss so I'll just share a](https://x.com/Suhail/status/2063324620946821552) |
| x | frankyecom | ^475 c19 | [5.2 AI UGC sneak peek. $2 for this video, change persona + script, generate in 1](https://x.com/frankyecom/status/2063639886372966889) |
| x | fofrAI | ^383 c13 | [Make the building dance to music https://t.co/M9FwjQv1CH](https://x.com/fofrAI/status/2063337624505385422) |
| x | 0xInk_ | ^327 c28 | [just having fun making animation with my 2 cats in the real life : Googoo and Ga](https://x.com/0xInk_/status/2063327425308856633) |
| x | Blue_Beba_ | ^255 c15 | [#Keep4o #OpenSource4o 🚨 GPT-4o was trained on OUR data. OpenAI's own System Card](https://x.com/Blue_Beba_/status/2063357998613910005) |
| x | fofrAI | ^243 c5 | [Start with an image of a building and prompt for a projection mapping with Omni.](https://x.com/fofrAI/status/2063330900759200017) |
| x | SeharShinwari | ^201 c0 | [If you're creating AI content in 2026, these platforms are hard to ignore: • Cha](https://x.com/SeharShinwari/status/2063665962097000896) |
| x | segabysleep | ^172 c2 | [@lilifying frontiers two developed entirely using sora ai with focus m writing #](https://x.com/segabysleep/status/2063695964204913032) |
| x | 0xSpivach | ^161 c8 | [A student built a whole faceless passive business by creating AI backyards. I ke](https://x.com/0xSpivach/status/2063557288732803283) |
| x | badboyfoxy | ^156 c91 | ["we are all getting scammed in our 40s because of Ai " why ? AI is get way to sc](https://x.com/badboyfoxy/status/2063565506381046089) |
| x | aimikoda | ^147 c14 | [Midjourney + GPT Image 2 + Seedance 2.0 - Prompt Share Ash vs Borg Sometimes, wh](https://x.com/aimikoda/status/2063565204848324825) |
| x | fabianstelzer | ^131 c6 | [this is extremely cool for stuff that otherwise is hard to prompt with just text](https://x.com/fabianstelzer/status/2063634999174213793) |
| x | AndrewBolis | ^128 c42 | [AI is replacing people without the right skills. Build AI skills to future-proof](https://x.com/AndrewBolis/status/2063580489890611540) |
| x | fofrAI | ^126 c6 | [He can juggle anything https://t.co/Q1PplzkvAc](https://x.com/fofrAI/status/2063387602099581241) |
| x | Artedeingenio | ^122 c9 | [I think this is one of the best animation styles I've ever created. If you'd lik](https://x.com/Artedeingenio/status/2063535024272539982) |
| x | imrollandex | ^120 c3 | [FRAMEWORK 2: FANVUE Fanvue has established itself as the absolute best platform ](https://x.com/imrollandex/status/2063636671199846723) |
| x | RamSingh_369 | ^117 c25 | [100+ AI Tools That Help You Get Hours of Work Done in Minutes ⏱️ 1. Presentation](https://x.com/RamSingh_369/status/2063655343968899394) |
| x | gurniaiart | ^116 c0 | [Knight art #AIArt #AIイラスト #midjourney #AIgirl #knight #aiGallery https://t.co/hp](https://x.com/gurniaiart/status/2063537435519135800) |
| x | HuggingModels | ^115 c4 | [Stable Diffusion 3.5 Large is here, and it's a game changer for text-to-image ge](https://x.com/HuggingModels/status/2063372866687824120) |
| x | fofrAI | ^114 c8 | [I'm having fun reversing videos and editing them with Omni. Putting forwards thi](https://x.com/fofrAI/status/2063324626579513525) |
| x | chrisdadiva | ^111 c7 | [2 New Free AI Video Generators with Google Veo 3.1, Grok & Seedance 2.0 In this ](https://x.com/chrisdadiva/status/2063513170547732705) |
| x | funkin03 | ^110 c0 | [@_defnotnormal When you beat Sonic Frontiers 2 and you see "In Loving Memory of ](https://x.com/funkin03/status/2063734261815894051) |
| x | _VVSVS | ^109 c16 | [For everyone asking about the frameworks, methods, and tools behind my work: I p](https://x.com/_VVSVS/status/2063306802465243646) |
| x | ElizabethA77617 | ^108 c28 | [Over 80 AI tools to finish months of work in mere minutes🪄 1. 𝐑𝐞𝐬𝐞𝐚𝐫𝐜𝐡 - ChatGPT](https://x.com/ElizabethA77617/status/2063454925452173485) |
| x | deedydas | ^106 c21 | [This is the best scene in Hell Grind, an entirely AI-made movie, the flashback. ](https://x.com/deedydas/status/2063854357234557082) |
| x | Bhanusinghyede | ^105 c16 | [🚀 𝟏𝟐𝟎 𝐌𝐢𝐧𝐝-𝐁𝐥𝐨𝐰𝐢𝐧𝐠 𝐀𝐈 𝐓𝐨𝐨𝐥𝐬 𝐘𝐨𝐮 𝐒𝐡𝐨𝐮𝐥𝐝 𝐊𝐧𝐨𝐰 𝐢𝐧 𝟐𝟎𝟐𝟔 Most people know 5–10 tools…](https://x.com/Bhanusinghyede/status/2063585678454305225) |
| x | insomnia_vip | ^96 c23 | [This kid is making $10,000 a month posting completely fake AI animal videos on Y](https://x.com/insomnia_vip/status/2063570805120721176) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AmityBlight6777</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3610 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AmityBlight6777/status/2063713637852688524">View @AmityBlight6777 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“When I’m playing Sonic frontiers 2 and I see the Sora AI watermark on the corners of my screen https://t.co/RxpizSGMwY”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้โพสต์ล้อเล่นว่าเห็น watermark ของ Sora AI ตอนเล่น Sonic Frontiers 2 บอกเป็นนัยว่าเกมใช้หรือดูคล้าย AI-generated video</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AmityBlight6777/status/2063713637852688524" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Rajesh992510253</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3142 · 💬 75</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Rajesh992510253/status/2063808629619532180">View @Rajesh992510253 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“120 + Mind blowing AI tools 🔥 1. Ideas - Claude - ChatGPT - Bing Chat - Perplexity - Copilot 2. Website - Dora - 10Web - Framer - Unicorn - Style AI 3. Writing - Jasper - HIX AI - Longshot - Textblaze”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ viral บน X รวม AI tools 120+ ตัวใน 20 หมวด (writing, video, UI/UX, automation, SEO ฯลฯ) หมวดละ 5 ตัว — เป็น directory snapshot รวบรวมจาก crowd</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>list นี้รวมตื้นๆ ไม่มีข้อมูล pricing, คุณภาพ หรือ fit — ส่วนใหญ่รู้จักอยู่แล้วหรือมีตัวใหม่แทนแล้ว ไม่มี curation</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Rajesh992510253/status/2063808629619532180" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@0x_fokki</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1146 · 💬 56</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/0x_fokki/status/2063309212353007843">View @0x_fokki on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨a 22-year-old makes $8,217/month from an anime channel he built in one weekend → Claude: script and scene description. 10 minutes. → Midjourney: every frame. 20 minutes. → Runway: movement, breathing”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Creator สร้าง anime channel อัตโนมัติด้วย Claude+Midjourney+Runway+ElevenLabs+Suno+Make รายงานรายได้ $8,217/เดือน จากงานรวมแค่ ~3 ชั่วโมง/สัปดาห์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Pipeline ครบทุก layer ตั้งแต่ script, ภาพ, motion, voice, เพลง ถึง auto-publish ด้วย tool ที่ studio เข้าถึงได้อยู่แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Studio ลอง pilot stack นี้สำหรับ animated short promo โดยใช้ Claude เขียน script, Runway ทำ motion และ Make จัดการ auto-publish</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/0x_fokki/status/2063309212353007843" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Suhail</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 707 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Suhail/status/2063324620946821552">View @Suhail on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“All my bad VC stories mostly just make me sound like a wuss so I'll just share a good one: One time I crashed an Allen&amp;Co event since it meant I could pitch 4 investors in one day in the same location”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Founder @Suhail เล่าเรื่องส่วนตัวเรื่องการบุกเข้างาน Allen &amp; Co เพื่อ pitch นักลงทุน และได้รับ termsheet จาก a16z หลัง pitch Marc Andreessen กับ Ben Horowitz แบบเย็นชา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Suhail/status/2063324620946821552" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@frankyecom</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 475 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/frankyecom/status/2063639886372966889">View @frankyecom on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“5.2 AI UGC sneak peek. $2 for this video, change persona + script, generate in 15 minutes. Systemized the entire process and have a complete 54,000+ character prompt engine ready to drop. (Which every”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Creator โชว์ pipeline สร้างวิดีโอ AI UGC — สลับ persona + script ได้ ราคา ~$2/คลิป ใช้เวลา 15 นาที ขับเคลื่อนด้วย prompt engine 54,000 ตัวอักษรที่สร้างมาตั้งแต่ยุค Sora</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Prompt engine ที่ standardize output วิดีโอ AI ต้นทุนต่ำแบบนี้ใช้ได้โดยตรงกับ e-learning avatar content หรือคลิปการตลาดของ studio</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม e-learning ลอง pilot ใช้ pipeline persona-swap นี้แทนหรือเสริม segment วิดีโอ instructor ที่ต้องถ่ายจริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/frankyecom/status/2063639886372966889" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@fofrAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 383 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/fofrAI/status/2063337624505385422">View @fofrAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Make the building dance to music https://t.co/M9FwjQv1CH”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@fofrAI โชว์ demo AI ที่ animate อาคารให้เคลื่อนไหวตาม music — เป็น audio-driven video generation จาก input เดียว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Audio-reactive generative visual ใช้ได้ตรงกับ environment animation ใน Unity game และ XR scene ที่ต้องการ visual ตอบสนอง sound</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity/XR team ลองใช้เทคนิคนี้เป็น reference สำหรับ audio-reactive animation ใน background environment</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/fofrAI/status/2063337624505385422" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@0xInk_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 327 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/0xInk_/status/2063327425308856633">View @0xInk_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“just having fun making animation with my 2 cats in the real life : Googoo and Gaga reference images made on Midjourney V8.1 and fixed with GPT Image2 prompt made with Claude, animation on Seedance2 ht”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้สาธิต pipeline 4 ตัว: Midjourney V8.1 สร้าง reference image, GPT Image2 แก้ภาพ, Claude เขียน prompt, Seedance2 สร้างอนิเมชัน จากรูปแมวจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>pipeline นี้แสดงวิธีแปลง reference photo จริงเป็น animated character ด้วย AI tools สำเร็จรูป — ใช้ได้กับ prototype asset เกมหรือ character ใน e-learning</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีมลองใช้ Midjourney → GPT Image2 → Seedance2 สร้าง prototype animated character ก่อนเข้า production จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/0xInk_/status/2063327425308856633" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Blue_Beba_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 255 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Blue_Beba_/status/2063357998613910005">View @Blue_Beba_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“#Keep4o #OpenSource4o 🚨 GPT-4o was trained on OUR data. OpenAI's own System Card confirms it.🚨 From the official GPT-4o System Card: &quot;Pre-trained using data sourced from a wide variety of materials in”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ viral นำข้อมูลจาก GPT-4o System Card ของ OpenAI มาเล่าใหม่ — web crawl, ดีล Reddit/Stack Overflow, Shutterstock, และ paywalled content — แต่เป็นข้อมูลที่เปิดเผยอยู่แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Blue_Beba_/status/2063357998613910005" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
