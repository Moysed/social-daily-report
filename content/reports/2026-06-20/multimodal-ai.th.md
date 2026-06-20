---
type: social-topic-report
date: '2026-06-20'
topic: multimodal-ai
lang: th
pair: multimodal-ai.en.md
generated_at: '2026-06-20T15:43:44+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 173
salience: 0.45
sentiment: mixed
confidence: 0.5
tags:
- video-generation
- comfyui
- open-weights
- production-pipeline
- model-comparison
- midjourney
thumbnail: https://pbs.twimg.com/media/HLLmjWXXEAAKcY8.jpg
translated_by: claude-sonnet-4-6
---

# Multimodal AI — 2026-06-20

## TL;DR
- มีการสาธิต pipeline วิดีโอในเครื่องแบบฟรี: NVIDIA Studio + ComfyUI + LTX (ltx_io) render CG short ทั้งเรื่องบนเครื่องส่วนตัว [13]
- มีการแชร์ production stack ที่ใช้งานจริง — ComfyUI/After Effects/Photoshop ร่วมกับ Wan 2.2 I2V+T2V, Krea 2, GPT Image 2.0, Grok Image และ Florence2 [11]
- ตลาด hosted video model แข่งขันเข้มข้น: Seedance 2.0, Kling 3.0 Pro, Gemini Omni Flash, Grok Imagine 1.5 รวมถึง Veo3 และ Runway โดย Seedance 2.1/2.5 คาดว่าจะปล่อยสัปดาห์หน้า [21][28][36][54][56]
- ข้อบกพร่องที่รู้จักกันดียังคงอยู่: ฉากต่อสู้หลายตัวละคร/หลายฝ่ายและการเคลื่อนไหวละเอียด (tongue rotation) ยังทำให้ video model พัง [21][28]
- Midjourney ประกาศหันมาทำ medical hardware (เครื่อง full-body ultrasound) พร้อมอ้างว่า 'เลิก' ทำ image generation — ครองการมีส่วนร่วมสูงสุด แต่ไม่เกี่ยวกับ production asset tooling และมีแหล่งข้อมูลเดียว [29][38][43][44]

## What happened
รายการที่ได้รับความสนใจสูงส่วนใหญ่เกี่ยวกับการประกาศของ Midjourney ว่าจะเปิดแผนกการแพทย์และพัฒนาเครื่อง full-body ultrasound scanner [29][38][43] ซึ่งเป็นเรื่อง hardware/medical ไม่ใช่ generative image/video tooling มีคำตอบหนึ่งระบุว่า scanner เป็นโปรเจกต์แยกที่ยังไม่มี AI [44] สัญญาณที่ตรงประเด็นจริงๆ มีน้อยกว่านั้น demo ที่ NVIDIA Studio สปอนเซอร์แสดงการ render CG short ในเครื่องแบบฟรีผ่าน ComfyUI โดยใช้ LTX [13] creator รายหนึ่งโพสต์ stack หลายเครื่องมือที่ชัดเจน: ComfyUI + After Effects + Photoshop ขับเคลื่อน Wan 2.2 (image-to-video และ text-to-video), Krea 2, GPT Image 2.0, Grok Image และ Florence2 [11] ComfyUI ไฮไลต์การ rebuild การแสดงกลองสดด้วย motion data แทนที่จะ generate แบบสุ่ม [14]

## Why it matters (reasoning)
สิ่งที่สำคัญสำหรับ production studio มีสองอย่าง อย่างแรก hosted video model iterate เร็วและแข่งกันโดยตรง (Seedance vs Kling vs Veo3 vs Runway) [21][28][36][56] หมายความว่า eval cycle สั้นและต้นทุนต่อ clip ที่ใช้ได้ลดลง แต่ก็หมายความว่าการเลือก vendor ใดเป็น default ถือเป็นการตัดสินใจชั่วคราว อย่างที่สอง เส้นทาง local/open กำลังสุกงอม: GPU vendor (NVIDIA) กำลังโปรโมต free local ComfyUI+LTX render pipeline [13] และ open-weight Wan 2.2 อยู่ใน stack จริงแล้ว [11] — ลดการพึ่งพา closed API สำหรับ previz และ asset draft การ pivot ทางการแพทย์ของ Midjourney ไม่ว่าจะดีแค่ไหน เป็นสัญญาณลำดับที่สอง: เครื่องมือ image ชั้นนำกำลังหันความสนใจไป hardware อย่างเปิดเผย [29][43] ดังนั้นการยึด Midjourney เป็น image pipeline หลักแบบมั่นคงจึงมีความเสี่ยงด้าน vendor จุดอ่อนที่ยังคงอยู่ในฉากหลายตัวละครและ fine motion [21][28] หมายความว่าเครื่องมือเหล่านี้ยังเป็นแค่ตัวช่วย draft/B-roll ไม่ใช่ตัว generate shot สำเร็จรูป

## Possibility
มีแนวโน้มสูง: release cadence ของ hosted video model ยังเดินหน้า โดยมีการอัปเดต Seedance อ้างว่าจะมาสัปดาห์หน้า [28] และการแข่งขัน Kling/Veo/Runway ที่ต่อเนื่อง [21][36][56] เป็นไปได้: local open pipeline (ComfyUI + LTX + Wan 2.2) จะเป็นตัวเลือกจริงสำหรับ studio previz และ asset draft เมื่อมี vendor backing และการใช้งานจริงอยู่แล้ว [11][13] เป็นไปได้ถึงไม่น่าจะเกิด: Midjourney ออกจาก image generation จริงๆ — มาจากโพสต์ hype และถูกหักล้างด้วย reply ที่บอกว่า scanner ไม่เกี่ยวกัน [43][44] ไม่น่าจะตรวจสอบได้: ข้ออ้างว่า 'Sora ถูกลบ' ซึ่งปรากฏแค่ในการพูดคุยผ่านๆ [2][10] ไม่มีแหล่งข้อมูลใดให้ตัวเลขความน่าจะเป็น จึงไม่อ้างไว้

## Org applicability — NDF DEV
1) ตั้ง local test bench ของ ComfyUI + Wan 2.2 + LTX สำหรับ game/XR previz และ edutech B-roll; Wan 2.2 มี open weights และ LTX local render path ฟรี — ความพยายามต่ำ/กลาง [11][13] 2) จัด internal bake-off สั้นของ hosted video model (Seedance, Kling, Veo3, Runway) บน shot edutech/marketing จริงหนึ่งหรือสองอย่างเพื่อเลือก default ปัจจุบันและ fallback — ความพยายามต่ำ [21][36][56] 3) กระจายออกจาก Midjourney ในฐานะแหล่ง image แหล่งเดียวเมื่อเห็น public pivot; คง alternative (Krea, GPT Image, Grok Image) ไว้ใน stack — ความพยายามต่ำ [11][29][43] 4) สำหรับ shot ที่มี motion หนักหรือหลายตัวละคร วางแผน motion-data/manual compositing แทน pure generation [14][28] ข้ามไปเลย: การถกเถียงเรื่อง medical scanner ของ Midjourney [1][3][9][16][23][31][49][58][60], listicle 'free AI tools' [26][37][45][51][52][59] และ thread ที่หา follower [22][39][48][55] — ไม่มีคุณค่าต่อ production

## Signals to Watch
- Seedance 2.1/2.5 รายงานว่าจะปล่อยสัปดาห์หน้า — รัน video bake-off ใหม่เมื่อมาถึง [28]
- Wan 2.2 open weights ปรากฏใน stack จริง — ติดตามสำหรับ self-hosted I2V/T2V [11]
- NVIDIA โปรโมต free local ComfyUI+LTX rendering — ดู hardware-tier requirement และ quality ceiling [13]
- roadmap image-gen ของ Midjourney หลัง medical pivot — ยืนยันก่อนพึ่งพา [43][44]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | afshineemrani | ^9473 c318 | [I'm a cardiologist. Something just happened today that I genuinely did not see c](https://x.com/afshineemrani/status/2067630924108538083) |
| x | amazingzeros | ^7449 c19 | [sonic fan pissing their pants about fortnite as if sora ai getting deleted didn'](https://x.com/amazingzeros/status/2067666616700334555) |
| x | midjourney | ^4717 c897 | [We're gonna do a Midjourney Medical AMA (ask me anything ) right here all aftern](https://x.com/midjourney/status/2067688872944025975) |
| x | levelsio | ^3899 c112 | [I don't know if it's obvious information or not but if you talk to random people](https://x.com/levelsio/status/2067662326082498899) |
| x | synthwavedd | ^2873 c174 | [🚨 SCOOP: After the release of Fable 5 and with GPT-5.6 looming, the mood behind ](https://x.com/synthwavedd/status/2068000857757741251) |
| x | cignificants | ^1951 c14 | [so hey, aside from midjourney and gemini what other generative AI program do you](https://x.com/cignificants/status/2067644406728135033) |
| x | Prolotario1 | ^1894 c131 | [Quite The Eventful Day It Has Been: New Air Force 1 New GTA 6 Promo New Midjourn](https://x.com/Prolotario1/status/2067768517613551818) |
| x | ChanduThota | ^1609 c55 | [Video is an effective way to communicate, and we want to make it as easy as edit](https://x.com/ChanduThota/status/2067631530890113477) |
| x | matt_is_nice | ^1087 c46 | [Everyone arguing about whether the Midjourney Scanner can replace an MRI or CT i](https://x.com/matt_is_nice/status/2067796547400814608) |
| x | lanxre | ^744 c35 | [What does this change?😭✌🏾 shit looks like it's from Sora Ai](https://x.com/lanxre/status/2068170937401237893) |
| x | ingi_erlingsson | ^677 c18 | [take the wheel 🏁 make: ComfyUI, After Effects, Photoshop model: Wan 2.2 I2V + T2](https://x.com/ingi_erlingsson/status/2067756997756256650) |
| x | fabianstelzer | ^530 c23 | [this will be such a great movie. how do you even steal a EUV machine? https://t.](https://x.com/fabianstelzer/status/2067907362329907275) |
| x | mickmumpitz | ^464 c12 | [Paid partnership with @NVIDIAStudio - You can now render entire CG movies with l](https://x.com/mickmumpitz/status/2067976421687881962) |
| x | ComfyUI | ^443 c8 | [Most AI video work is just "generate and hope." This is different. Creator seung](https://x.com/ComfyUI/status/2067669239033717141) |
| x | javilopen | ^439 c48 | [Why didn't they call me to name this? What a wasted opportunity to call it... ME](https://x.com/javilopen/status/2067926942238540049) |
| x | heacockmd | ^359 c48 | [Apparently, yesterday @midjourney pivoted from AI image generation to...whole bo](https://x.com/heacockmd/status/2067638397804441634) |
| x | fofrAI | ^343 c24 | [Entrance to the new Midjourney spa https://t.co/vsnEIjM36P](https://x.com/fofrAI/status/2067635885370126556) |
| x | ai_explorer25 | ^338 c22 | [Best accounts to follow from each frontier lab to stay constantly up to date Ant](https://x.com/ai_explorer25/status/2068159401253327223) |
| x | MTSlive | ^297 c6 | [Why is the Midjourney team uniquely qualified to build medical hardware? @BeffJe](https://x.com/MTSlive/status/2067757811191447659) |
| x | askwhykartik | ^290 c21 | [A lot of people asked how I made this animation, so here's the process 👇 Honestl](https://x.com/askwhykartik/status/2067990215764148331) |
| x | YourAlphaMom | ^267 c29 | [New tongue-physics test for the best AI video models! Seedance 2.0, Kling 3.0 Pr](https://x.com/YourAlphaMom/status/2068046646085329212) |
| x | icreatelife | ^266 c121 | [I'm following 3,700 AI pioneers and I'd love to follow 300 more, to make it a ro](https://x.com/icreatelife/status/2067728865808519355) |
| x | KevInvestingYT | ^260 c19 | [I've initiated a position in $BFLY in response to the greatest medical imaging a](https://x.com/KevInvestingYT/status/2067684979098694058) |
| x | dreamingtulpa | ^259 c13 | [still can't get over how beautiful some of these shots are and the soundtrack 👌 ](https://x.com/dreamingtulpa/status/2067880684920643956) |
| x | abarrallen | ^250 c19 | [I just read a story about a runner I know who had leg pain for 3.5 years. Her di](https://x.com/abarrallen/status/2067978979668275486) |
| x | dharmvir_ | ^235 c43 | [GITHUB REPOS THAT FEEL ILLEGAL TO USE, THEY'RE KILLING $50 BILLION IN CORPORATE ](https://x.com/dharmvir_/status/2067873642038612343) |
| x | Rakib_Web3 | ^218 c16 | [i pay $0 for ai tools. literally zero. and i use all of them chatgpt, cursor, mi](https://x.com/Rakib_Web3/status/2068040519037616393) |
| x | aimikoda | ^214 c35 | [No matter how much we try, multiple-opponent scenes always seem to be challengin](https://x.com/aimikoda/status/2068139736242307295) |
| x | martinvars | ^212 c9 | [Midjourney announcing Midjourney Medical is a useful shock. An AI image company ](https://x.com/martinvars/status/2067628676955418990) |
| x | AntonHand | ^212 c10 | [All the AI bros saying things like "I know the Midjourney stuff might be bullshi](https://x.com/AntonHand/status/2068051953947660585) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@afshineemrani</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 9473 · 💬 318</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/afshineemrani/status/2067630924108538083">View @afshineemrani on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm a cardiologist. Something just happened today that I genuinely did not see coming — and it could change the future of preventive medicine more than anything I've written about on this platform. Mi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney เปิดตัวต้นแบบ full-body ultrasound scanner ใช้ transducer 500k ตัวในน้ำ สแกน 60 วินาที AI 2 petaflops สร้าง 3D anatomy ไม่ใช้รังสีหรือ MRI</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>บริษัท AI ด้านภาพผลิต hardware ทางการแพทย์จริง แสดงว่า multimodal AI (acoustic → 3D reconstruction) ออกจากงานวิจัยสู่ผลิตภัณฑ์ clinical ได้เร็วกว่าที่คาด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action ยังไม่มี SDK หรือ API — ติดตามเมื่อ studio สนใจ e-learning ด้านการแพทย์หรือ XR anatomy simulation</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/afshineemrani/status/2067630924108538083" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@amazingzeros</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7449 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/amazingzeros/status/2067666616700334555">View @amazingzeros on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“sonic fan pissing their pants about fortnite as if sora ai getting deleted didn’t set their games back by 20 years”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ล้อเลียนแฟน Sonic เรื่อง Fortnite พร้อมอ้างแบบไม่มีที่มาว่า 'Sora AI ถูกลบ' ทำให้วงการเกมถอยหลัง 20 ปี</dd>
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
    <span class="ndf-engagement">♥ 4717 · 💬 897</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2067688872944025975">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We're gonna do a Midjourney Medical AMA (ask me anything ) right here all afternoon. Post your questions below and we'll try to answer as many as we can! ❤️”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney ประกาศจัด Medical AMA แบบ live บน X ให้คนโพสต์คำถาม ไม่มีรายละเอียด product ใดๆ ในโพสต์นี้</dd>
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
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3899 · 💬 112</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2067662326082498899">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I don't know if it's obvious information or not but if you talk to random people in San Francisco the general thing they say is that software is commoditized cause so easy to make anything with AI fas”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>levelsio รายงาน consensus ใน SF ว่า software กลายเป็น commodity แล้ว — เขายกเลิก SaaS ทุกตัวแล้ว vibe-code ใช้เอง — คนเก่งเลยหันไปทำ hardware แทนเพราะเข้ายากกว่า</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้า client vibe-code เองได้ studio ที่ขายแค่ 'build app' จะกดราคาลำบาก งานที่ยังมี margin คืองาน XR, hardware-adjacent, และ integration ซับซ้อน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทบทวน service lineup แล้วเน้น XR, Unity, และงาน hardware-layer ใน pitch — พื้นที่ที่ vibe-coding ยังทำเองไม่ได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2067662326082498899" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@synthwavedd</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2873 · 💬 174</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/synthwavedd/status/2068000857757741251">View @synthwavedd on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 SCOOP: After the release of Fable 5 and with GPT-5.6 looming, the mood behind the scenes at Google DeepMind is increasingly one of frustration and broad discontent over the lab's perceived fall into”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แหล่งในของ DeepMind รายงานว่า model ดีที่สุดของ Google อยู่อันดับ 5 บน Artificial Analysis Intelligence Index แพ้ Anthropic, OpenAI และ Zhipu AI และ Gemini 3.5 Pro ที่จะออก 30 มิ.ย. ยังไม่พอแก้สถานการณ์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>สำหรับทีมที่กำลังเลือก AI API provider การที่ Gemini ตกไปอันดับ 5 เป็นสัญญาณให้ benchmark ทางเลือกอื่นก่อน lock-in integration</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เช็ค Gemini API integration ที่มีหรือวางแผนไว้ แล้ว benchmark กับ Anthropic หรือ OpenAI ก่อน commit budget</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/synthwavedd/status/2068000857757741251" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cignificants</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1951 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cignificants/status/2067644406728135033">View @cignificants on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“so hey, aside from midjourney and gemini what other generative AI program do you use? just curious https://t.co/vAU8YebeEj”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ Twitter ถามว่าใครใช้ generative AI ตัวไหนนอกจาก Midjourney กับ Gemini — ไม่มีข้อมูลหรือ tool ใหม่ใด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cignificants/status/2067644406728135033" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Prolotario1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1894 · 💬 131</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Prolotario1/status/2067768517613551818">View @Prolotario1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Quite The Eventful Day It Has Been: New Air Force 1 New GTA 6 Promo New Midjourney Tech- New AI Data Center Orbit Concepts New Apple Intelligence &amp; Siri AI Upgrades New Matrox Video Low-Latency Tech N”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>บัญชี Twitter รวมข่าวประมาณ 10 เรื่องที่ไม่เกี่ยวกัน — รองเท้า, GTA 6, Midjourney, Starlink, Neuralink ฯลฯ — เป็น roundup แบบไม่มีการวิเคราะห์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Prolotario1/status/2067768517613551818" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ChanduThota</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1609 · 💬 55</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ChanduThota/status/2067631530890113477">View @ChanduThota on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Video is an effective way to communicate, and we want to make it as easy as editing slides - that's why we created Google Vids (https://t.co/Z0lp7dvIRB). We are launching major enhancements to AI avat”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Google Vids อัปเดตใหญ่ — สร้าง AI avatar, voiceover 24 ภาษา, และแปลง Google Slides เป็นวิดีโอแบบอัตโนมัติ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมเล็กที่ต้องทำ presentation หรือ demo ให้ลูกค้าสามารถแปลง Slides เป็นวิดีโอได้เร็วขึ้นมากโดยไม่ต้องตัดต่อเอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลองใช้ Google Vids แปลง proposal deck หรือ e-learning slides เป็นวิดีโอก่อน deliver งานลูกค้าครั้งถัดไป</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ChanduThota/status/2067631530890113477" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
