---
type: social-topic-report
date: '2026-06-20'
topic: multimodal-ai
lang: th
pair: multimodal-ai.en.md
generated_at: '2026-06-20T03:43:47+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 206
salience: 0.58
sentiment: mixed
confidence: 0.5
tags:
- multimodal-ai
- video-generation
- comfyui
- open-weights
- image-editing
- midjourney
thumbnail: https://pbs.twimg.com/media/HLEKRTNW4AAiGWG.jpg
translated_by: claude-sonnet-4-6
---

# Multimodal AI — 2026-06-20

## TL;DR
- Midjourney ประกาศ 'Midjourney Medical' — เครื่องสแกนอัลตราโซนิกเต็มตัว (~358,000 transducers บนชิป, ใช้น้ำแทนรังสี, ~60 วินาที) แต่เป็น hardware ที่รายงานว่า ยังไม่มี AI อยู่เลย [12][52][23] ไม่ใช่ multimodal AI release แม้จะครองยอด engagement ของวันนี้
- signal จริงในสายการผลิต: pipeline NVIDIA Studio + ComfyUI + LTX รัน CG shorts เต็มรูปแบบบน GPU ของตัวเองได้ฟรีบน local machine [21] และอีก ComfyUI workflow ที่สร้างวิดีโอจาก motion-capture data ของมือกลองจริง [19]
- ByteDance ปล่อย Dreamina Seedance 2.0 (mini) สำหรับ AI video; creator ต่างนำ prompt เดียวกันมาทดสอบเทียบกับ Kling 3.0 [26][45][46]
- ฝั่ง open weights: 'Boogu Image Edit' โมเดล open-source ขนาด 10B ขึ้น Hugging Face [50]; Adobe ปล่อย Photoshop AI Assistant แบบ context-aware ขับเคลื่อนด้วยข้อความ [42]; ComfyUI stack หนึ่งอ้างถึง Wan 2.2 I2V/T2V, Krea 2, GPT Image 2.0 และ Florence2 [16]
- Midjourney รายงานรายได้ ~$100M ใน 9 เดือนแรก และ ~$200M ภายในเดือนที่ 12 ระดมทุนจากชุมชนล้วน โดยรายได้จาก image-gen เป็นตัวหล่อเลี้ยง R&D [6]

## What happened
feed วันนี้แบ่งเป็นสองกลุ่ม กลุ่มที่ engagement สูงสุดคือ 'Midjourney Medical' และเครื่องสแกนอัลตราโซนิกเต็มตัว — ใช้น้ำแทนรังสี, ~358,000 transducers, สแกน ~60 วินาที อ้างว่าได้ภาพระดับ MRI [12][34][47][51] นี่คือ medical hardware ไม่ใช่ generative AI: แหล่งหนึ่งระบุว่า 'ไม่มี AI อยู่ในนั้นเลย' [52] และอีกแหล่งพบว่าไม่มีข้อมูล performance จริง [23] แยกจากนั้น ธุรกิจภาพของ Midjourney ถูกอ้างว่าระดมทุนจากชุมชนเองได้ ~$100M ใน 9 เดือน [6]

item ที่ตรงประเด็น multimodal AI จริงๆ คือการปล่อย tool และโมเดล: pipeline ComfyUI + LTX แบบ local ที่ NVIDIA Studio หนุนหลัง สำหรับ CG rendering บน GPU ตัวเองฟรี [21]; ComfyUI สร้างวิดีโอจาก motion data [19]; Dreamina Seedance 2.0 mini ของ ByteDance พร้อมการเปรียบกับ Kling 3.0 [26][45][46]; โมเดล Boogu Image Edit ขนาด 10B บน Hugging Face [50]; Adobe Photoshop AI Assistant [42]; Google Vids ที่เสริม AI avatar [10]; และ stack ที่รวม Wan 2.2, Krea 2, GPT Image 2.0, Grok Image, Florence2 และ Suno [16] การถกเถียง open-vs-closed model วิ่งอยู่ในหลายโพสต์ที่อ้างถึงโมเดล frontier ชื่อ 'Fable' และโมเดล open จากจีน [17][41][7][49]

## Why it matters (reasoning)
signal ที่มีความหมายสำหรับ production studio คือการรวมตัวของ open และ local video/image pipeline ไม่ใช่กระแส medical render path แบบ local LTX+ComfyUI ฟรี [21] บวกกับ open weights อย่าง Boogu [50] และ Wan 2.2 [16] ลดต้นทุนต่อ asset และตัดการพึ่งพา closed API กับ per-seat pricing — ตรงกับการสร้าง visual สำหรับ game, XR และ edutech ในปริมาณมากพร้อมควบคุม licensing การเปรียบ Seedance 2.0 vs Kling 3.0 [26][46] ชี้ว่าคุณภาพ hosted video ตัดสินจากการลองจริงแบบ side-by-side ไม่ใช่ spec sheet ดังนั้นควรทดสอบกับ prompt ของตัวเอง ส่วน pivot ด้านการแพทย์ของ Midjourney เป็นผลพลอยได้ลำดับสอง: ธุรกิจ image ที่ทำกำไรได้ [6] ใช้ทุนลงทุน hardware คนละสาย [4][48] ซึ่งดูดความสนใจแต่ไม่เปลี่ยน creative pipeline ใดๆ กรอบ 'ยุคใหม่' [15][27][36] คือ marketing โดยเฉพาะเมื่อยังไม่มีข้อมูลยืนยัน [23] และตัวเครื่องอาจไม่ได้ใช้ AI เลย [52]

## Possibility
**Likely:** open และ local image/video tooling ยังพัฒนาต่อเนื่องและแข่งกันสูสี — ComfyUI+LTX [21], Wan 2.2 [16] และ open editor อย่าง Boogu [50] บ่งชี้ว่ามี open weights ที่ใช้งานได้จริงออกมาสม่ำเสมอ **Plausible:** โมเดล open จากจีนตีเสมอหรือเหนือกว่า closed frontier ระดับ 'Fable' ทั้งใน benchmark และการใช้จริง [17][41] ซึ่งจะเป็นประโยชน์กับ studio ที่สร้างบน open model แบบเปลี่ยนได้ **Plausible:** ราคา hosted video ยังลดต่อเนื่องเมื่อ Seedance และ Kling แข่งกัน [26][45][46] แม้ตัวเลข '$1 ต่อวิดีโอ, 5 โฆษณาใน 5 นาที' [33] เป็น vendor marketing และยังไม่ได้ยืนยัน **Unlikely ที่จะกระทบ NDF DEV:** เครื่องสแกน Midjourney Medical เข้ามาเกี่ยวกับ creative pipeline — ยังเป็น hardware ที่ไม่ผ่านการพิสูจน์และไม่มีข้อมูลเผยแพร่ [23][52] ไม่มีแหล่งใดให้ตัวเลขความน่าจะเป็นที่น่าเชื่อถือ จึงไม่ยืนยันตัวเลขใดทั้งสิ้น

## Org applicability — NDF DEV
**ทำ:** (1) ทดลอง pipeline local ComfyUI + LTX บน studio GPU สำหรับสร้าง visual asset งาน XR-scene และ edutech [21] — effort med (2) รัน same-prompt bake-off ระหว่าง Dreamina Seedance 2.0 กับ Kling 3.0 สำหรับคลิป marketing/edutech สั้นก่อนผูก API ใดฝั่งหนึ่ง [26][46] — effort low (3) ทดสอบโมเดล Boogu image-edit ขนาด 10B สำหรับแก้ asset แบบ iterative ที่ต้องควบคุม weights/licensing [50] — effort low/med (4) เพิ่ม Wan 2.2 I2V/T2V เข้า ComfyUI workflow ภายในสำหรับ open text/image-to-video [16] — effort med (5) ทดลอง Google Vids AI avatars สำหรับวิดีโออธิบาย talking-head ใน e-learning [10] และ Photoshop AI Assistant สำหรับ batch edit แบบ context-aware [42] — effort low **ข้าม:** เครื่องสแกน Midjourney Medical [12][52], ข่าวลือ 'Fable' ban/DeepMind-discontent [49][7] (ยังไม่ยืนยัน) และตัวเลข cost/speed ที่มาจาก promo thread [33]

## Signals to Watch
- ช่องว่างคุณภาพและราคาระหว่าง Seedance 2.0 กับ Kling 3.0 เมื่อ creator ลงผลเปรียบโดยตรงมากขึ้น [46]
- ความสมบูรณ์ของ local-first rendering (LTX + ComfyUI + NVIDIA Studio) ที่แทน hosted spend [21]
- ความถี่ของ open-weight image editor ที่ขึ้น Hugging Face เช่น Boogu 10B [50]
- โมเดล open จากจีนจะถึงระดับ closed frontier 'Fable' ในแง่ feel จริง ไม่ใช่แค่ benchmark [17][41]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | afshineemrani | ^9168 c307 | [I'm a cardiologist. Something just happened today that I genuinely did not see c](https://x.com/afshineemrani/status/2067630924108538083) |
| x | amazingzeros | ^7445 c19 | [sonic fan pissing their pants about fortnite as if sora ai getting deleted didn'](https://x.com/amazingzeros/status/2067666616700334555) |
| x | midjourney | ^4644 c886 | [We're gonna do a Midjourney Medical AMA (ask me anything ) right here all aftern](https://x.com/midjourney/status/2067688872944025975) |
| x | aakashgupta | ^3811 c110 | [Let me explain why an AI art company just built a full-body medical scanner, bec](https://x.com/aakashgupta/status/2067579580622528913) |
| x | levelsio | ^3762 c109 | [I don't know if it's obvious information or not but if you talk to random people](https://x.com/levelsio/status/2067662326082498899) |
| x | nickfloats | ^3633 c94 | [What Midjourney is: - No investors, fully community-funded research lab - Revenu](https://x.com/nickfloats/status/2067445022484529282) |
| x | synthwavedd | ^2486 c148 | [🚨 SCOOP: After the release of Fable 5 and with GPT-5.6 looming, the mood behind ](https://x.com/synthwavedd/status/2068000857757741251) |
| x | cignificants | ^1884 c14 | [so hey, aside from midjourney and gemini what other generative AI program do you](https://x.com/cignificants/status/2067644406728135033) |
| x | Prolotario1 | ^1816 c126 | [Quite The Eventful Day It Has Been: New Air Force 1 New GTA 6 Promo New Midjourn](https://x.com/Prolotario1/status/2067768517613551818) |
| x | ChanduThota | ^1431 c48 | [Video is an effective way to communicate, and we want to make it as easy as edit](https://x.com/ChanduThota/status/2067631530890113477) |
| x | matt_is_nice | ^1027 c43 | [Everyone arguing about whether the Midjourney Scanner can replace an MRI or CT i](https://x.com/matt_is_nice/status/2067796547400814608) |
| x | AdrianDittmann | ^1018 c72 | [This is so cool! Midjourney Medical built a full body Ultrasonic CT scanner. You](https://x.com/AdrianDittmann/status/2067574011626946587) |
| x | dcbruck | ^799 c15 | [0 VC funding. $500M(+) in revenue. Less than 200 employees. And now they're rein](https://x.com/dcbruck/status/2067599482519216293) |
| x | BrianRoemmele | ^763 c52 | [Electronic Medicine is the future: Sound waves vs. Radiation. Currents and frequ](https://x.com/BrianRoemmele/status/2067619864370634919) |
| x | pronounced_kyle | ^760 c23 | [I'm calling it: this is the start of a new era in tech. First tangible example o](https://x.com/pronounced_kyle/status/2067595725404590439) |
| x | ingi_erlingsson | ^595 c16 | [take the wheel 🏁 make: ComfyUI, After Effects, Photoshop model: Wan 2.2 I2V + T2](https://x.com/ingi_erlingsson/status/2067756997756256650) |
| x | EMostaque | ^526 c121 | [How would you change your priors if a Chinese lab released an open model that be](https://x.com/EMostaque/status/2067610502826463409) |
| x | fabianstelzer | ^503 c23 | [this will be such a great movie. how do you even steal a EUV machine? https://t.](https://x.com/fabianstelzer/status/2067907362329907275) |
| x | ComfyUI | ^413 c8 | [Most AI video work is just "generate and hope." This is different. Creator seung](https://x.com/ComfyUI/status/2067669239033717141) |
| x | javilopen | ^388 c43 | [Why didn't they call me to name this? What a wasted opportunity to call it... ME](https://x.com/javilopen/status/2067926942238540049) |
| x | mickmumpitz | ^382 c10 | [Paid partnership with @NVIDIAStudio - You can now render entire CG movies with l](https://x.com/mickmumpitz/status/2067976421687881962) |
| x | arian_ghashghai | ^359 c17 | [reminder that Midjourney has 0 VC funding imo this is maybe the most utopian swi](https://x.com/arian_ghashghai/status/2067616613507923983) |
| x | heacockmd | ^344 c46 | [Apparently, yesterday @midjourney pivoted from AI image generation to...whole bo](https://x.com/heacockmd/status/2067638397804441634) |
| x | fofrAI | ^343 c23 | [Entrance to the new Midjourney spa https://t.co/vsnEIjM36P](https://x.com/fofrAI/status/2067635885370126556) |
| x | MTSlive | ^297 c6 | [Why is the Midjourney team uniquely qualified to build medical hardware? @BeffJe](https://x.com/MTSlive/status/2067757811191447659) |
| x | redchilli50 | ^269 c41 | [Wondering how to unlock Dreamina Seedance 2.0 mini right inside Dreamina? 🧵 A ra](https://x.com/redchilli50/status/2067505955814686786) |
| x | DeryaTR_ | ^257 c14 | [I think many people have realized what a revolutionary medical advance the Midjo](https://x.com/DeryaTR_/status/2067598405069591012) |
| x | icreatelife | ^257 c119 | [I'm following 3,700 AI pioneers and I'd love to follow 300 more, to make it a ro](https://x.com/icreatelife/status/2067728865808519355) |
| x | dreamingtulpa | ^254 c13 | [still can't get over how beautiful some of these shots are and the soundtrack 👌 ](https://x.com/dreamingtulpa/status/2067880684920643956) |
| x | KevInvestingYT | ^253 c18 | [I've initiated a position in $BFLY in response to the greatest medical imaging a](https://x.com/KevInvestingYT/status/2067684979098694058) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@afshineemrani</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 9168 · 💬 307</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/afshineemrani/status/2067630924108538083">View @afshineemrani on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm a cardiologist. Something just happened today that I genuinely did not see coming — and it could change the future of preventive medicine more than anything I've written about on this platform. Mi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney ประกาศแผนก medical hardware พร้อม prototype เครื่องสแกนร่างกาย full-body ใช้ ultrasonic transducer ~500K ตัว + compute 2 petaflops สร้าง 3D anatomy ใน 60 วินาที ไม่มีรังสี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>บริษัท AI ภาพกระโดดเข้า medical hardware แสดงว่า AI volumetric reconstruction พร้อม production แล้ว — ติดกับงาน XR medical visualization และ simulation ของ studio โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า studio เล็ง medical e-learning หรือ XR simulation เริ่ม scope Unity pipeline รับ full-body 3D scan data ได้เลย — scanner นี้คือ data source ที่น่าเชื่อถือในอนาคตอันใกล้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/afshineemrani/status/2067630924108538083" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@amazingzeros</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7445 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/amazingzeros/status/2067666616700334555">View @amazingzeros on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“sonic fan pissing their pants about fortnite as if sora ai getting deleted didn’t set their games back by 20 years”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์บ่นเรื่อง fandom Sonic กับ Fortnite แล้วเปรียบกับการยกเลิก Sora AI — เป็น drama วัฒนธรรม gaming ไม่มีเนื้อหาเชิงเทคนิค</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/amazingzeros/status/2067666616700334555" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@midjourney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4644 · 💬 886</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2067688872944025975">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We're gonna do a Midjourney Medical AMA (ask me anything ) right here all afternoon. Post your questions below and we'll try to answer as many as we can! ❤️”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney จัด AMA สดบน X โฟกัสที่ use case ด้านการแพทย์ ตอบคำถาม community เกี่ยวกับการใช้ AI image generation ในงาน medical</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/midjourney/status/2067688872944025975" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aakashgupta</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3811 · 💬 110</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aakashgupta/status/2067579580622528913">View @aakashgupta on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Let me explain why an AI art company just built a full-body medical scanner, because almost everyone is reading this as a random pivot. Ultrasonic CT works by firing sound through your body and record”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney เอา AI reconstruction ที่ฝึกมากับการสร้างภาพ มาใช้กับ ultrasonic CT สแกนทั้งตัวใน 60 วินาที ความละเอียดต่ำกว่า 1 มม. ไม่มีรังสี และ deploy ที่สปา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Model ที่ฝึกแก้ inverse problem ด้านภาพ transfer ไปแก้ acoustic reconstruction ได้ — ลด scan time จาก 90 นาทีเหลือ 60 วินาที เทียบ MRI</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ก่อน build AI feature ใหม่ตั้งแต่ต้น ให้ดูก่อนว่า generation หรือ reconstruction model ที่มีอยู่ใน pipeline จะ transfer ไป input modality ใหม่ได้มั้ย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aakashgupta/status/2067579580622528913" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3762 · 💬 109</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2067662326082498899">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I don't know if it's obvious information or not but if you talk to random people in San Francisco the general thing they say is that software is commoditized cause so easy to make anything with AI fas”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@levelsio รายงานว่าคนใน SF มองว่า software ถูก commoditize แล้ว เพราะ AI ทำให้ใครก็สร้างทดแทนได้เร็ว (เขายกเลิก SaaS ทั้งหมด แล้ว vibe code แทนฟรี) คนเก่งจึงย้ายไป hardware</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ลูกค้าที่เคยซื้อ custom software เริ่มคิดว่าสร้างเองด้วย AI ได้ สตูดิโอต้องแสดงคุณค่าใน complexity, domain expertise, และ production quality ที่ solo builder ทำไม่ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ปรับ pitch เน้นสิ่งที่ solo builder + AI ทำไม่ได้ — XR/Unity integration, e-learning ระดับ production, และ deployment ข้ามแพลตฟอร์มในระดับ scale</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2067662326082498899" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nickfloats</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3633 · 💬 94</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nickfloats/status/2067445022484529282">View @nickfloats on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“What Midjourney is: - No investors, fully community-funded research lab - Revenue from image generation product funds all R&amp;D - ~$100M in first 9 months, $200M by month 12, still growing - 8 active pr”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney ทำรายได้ $200M ภายใน 12 เดือนโดยไม่มี investor ภายนอก และ David Holz (อดีต Leap Motion, Northstar AR) กำลังจะ ship hardware products สำหรับผู้บริโภค 2 รายการ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>พื้นหลัง XR ของ Holz (hand-tracking, AR headset) บอกว่า hardware ที่จะออกมาน่าเกี่ยวกับ spatial/creative input — ตรงกับงาน XR ของทีม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตาม Midjourney hardware announcement — ถ้า spatial-input device ออกมา ทีม XR ควรลองประเมินสำหรับ prototyping และ interaction design</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nickfloats/status/2067445022484529282" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@synthwavedd</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2486 · 💬 148</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/synthwavedd/status/2068000857757741251">View @synthwavedd on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 SCOOP: After the release of Fable 5 and with GPT-5.6 looming, the mood behind the scenes at Google DeepMind is increasingly one of frustration and broad discontent over the lab's perceived fall into”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>พนักงาน DeepMind รายงานว่า Gemini ตกมาอันดับ 5 ใน Artificial Analysis Intelligence Index ตามหลัง Anthropic, OpenAI และ Zhipu AI และ Gemini 3.5 Pro ที่กำลังจะออกก็ไม่ได้รับการมองว่าแข่งขันได้จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Gemini ตามหลัง Anthropic และ OpenAI อย่างชัดเจน — ทีมที่วางแผนใช้ Gemini ใน integration ควรตรวจ performance gap ก่อน commit</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Benchmark Gemini เทียบ Anthropic/OpenAI สำหรับ AI feature ที่วางแผนไว้ — อย่า assume ว่า Google ยังทัดเทียมจากการ eval รอบก่อน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/synthwavedd/status/2068000857757741251" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cignificants</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1884 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cignificants/status/2067644406728135033">View @cignificants on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“so hey, aside from midjourney and gemini what other generative AI program do you use? just curious https://t.co/vAU8YebeEj”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ X ถามว่าใช้ generative AI tool อะไรนอกจาก Midjourney กับ Gemini — ไม่มี announcement หรือข้อมูลใหม่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cignificants/status/2067644406728135033" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
