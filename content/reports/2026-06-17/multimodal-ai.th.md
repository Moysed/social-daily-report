---
type: social-topic-report
date: '2026-06-17'
topic: multimodal-ai
lang: th
pair: multimodal-ai.en.md
generated_at: '2026-06-17T15:46:07+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 176
salience: 0.68
sentiment: mixed
confidence: 0.55
tags:
- multimodal-ai
- video-generation
- comfyui
- open-weights
- cost-efficiency
- vfx-pipeline
thumbnail: https://pbs.twimg.com/media/HK31G4lXcAAVteI.jpg
translated_by: claude-sonnet-4-6
---

# Multimodal AI — 2026-06-17

## TL;DR
- ComfyUI open-model VFX pipeline คือสัญญาณ production ที่แข็งแกร่งที่สุด: face swap ผ่าน Florence 2 → SAM2 → WAN [19], de-aging ผ่าน Flux 2 Klein → Wan 2.2 Fun Control [28], sky/atmosphere replacement แบบ animated [43], และ robotic compositing นำทางด้วย face paint กับ Wan 2.2 Animate [6] — ทั้งหมดอ้างว่า temporally consistent และประกอบได้จาก open weights
- ByteDance Seedance 2.0 Mini (Dreamina) เน้น cost/speed มากกว่า fidelity ตอนนี้ขับ CapCut อยู่ โดยอ้างว่าเร็วกว่า Seedance 2.0 Fast ถึง 2× [29][23][57]; CapCut ยังเปิดตัว 'Director Mode' สำหรับ AI filmmaking [34]
- Sora รายงานว่าทำรายได้รวมเพียง ~$2.1M ขณะที่ cost 'millions a day' ถูกมองว่า 'ร่วงจากอันดับหนึ่งสู่ความตายใน six months' [45][11] — single-source, ยังไม่ verified แต่สอดคล้องกับ narrative เรื่อง cost-over-hype
- Z.ai ฝึก stack บน Huawei Ascend (ไม่มี Nvidia) ประมาณ ~$25M ตามหลัง leading models ~3 เดือน และถูกกว่า ~90% ตามที่ผู้วิจารณ์รายหนึ่งระบุ [16][10] — เป็น claim จาก China cost-stack ยังไม่ได้รับการยืนยันอิสระ
- Midjourney เตรียมประกาศ hardware project แรก 6/17 6pm PT [2]; Grok Imagine Video 1.5 image-to-video เปิดตัวพร้อม generation ที่เร็วขึ้น [58]; Runway ใช้งานได้ภายใน ChatGPT แล้ว [17][59]

## What happened
ปริมาณเนื้อหาวันนี้ส่วนใหญ่คือการพูดถึง image/video generation แต่แกนหลักที่ใช้งาน production จริงมีน้อย ComfyUI workflow ที่ผสม open model สำหรับงาน VFX ปรากฏซ้ำ: face replacement/de-aging [19][28], sky/atmosphere replacement [43], และ stylized compositing กับ Wan 2.2 Animate [6] รวมถึง mini-PC ในบ้านที่รัน Flux + Mistral Small 3.2 [54] ด้าน hosted video ByteDance Seedance 2.0 Mini วางตัวด้านต้นทุนและความเร็ว พร้อม integrate เข้า CapCut [23][29][30][57] ซึ่งเพิ่ม 'Director Mode' [34] ข่าว model อื่น: Grok Imagine Video 1.5 [58], Runway ฝังใน ChatGPT [17][59], Kling 3.0 [48], Veo 3.1 และ Nano Banana 2 อ้างถึงใน stills/animatics workflows [27][39][40]

## Why it matters (reasoning)
สองแรงกำลังมาบรรจบกันสำหรับ studio อย่าง NDF DEV แรกแรก layer ที่ใช้งานได้จริงกำลังเปลี่ยนจาก closed demo ไปสู่ open-weight model ที่ orchestrate ผ่าน ComfyUI [6][19][28][43] — รันในเครื่อง ไม่มีค่า per-seat และให้ผล temporally consistent edit ที่เหมาะกับ game cinematics, XR backplates และ edutech visuals ประการที่สอง สัญญาณเชิงพาณิชย์ (ขาดทุนที่รายงานของ Sora [45][11]; Seedance Mini กับ CapCut แข่งกันด้านต้นทุน/ความเร็ว [23][29][30]; claim การฝึกราคาต่ำจาก China [16]) ชี้ว่า price collapse คือ trend ที่แท้จริง ไม่ใช่การก้าวกระโดดด้าน fidelity [46][35] ผลกระทบลำดับสอง: การผูกติด pipeline กับ closed API ราคาแพงตัวเดียวคือความเปราะบาง — การร่วงหกเดือนที่รายงานของ Sora [45] คือตัวอย่างเตือนใจ — ขณะที่ open WAN/Flux pipeline บวก hosted fallback ราคาถูก (Seedance/Kling/Veo) ให้ optionality การย้ายของ talent ไปสู่ 'real-world'/world models [13][15][20] บ่งชี้ว่าคลื่นวิจัยถัดไปมุ่ง physical/3D consistency แต่วันนี้ยังไม่มีสิ่งใดที่ shippable จากแนวนั้น

## Possibility
น่าจะเกิด: การแข่งขัน price/speed ระหว่าง hosted video model (Seedance Mini, Kling 3.0, Veo 3.1, Grok Imagine) ยังคงผลักให้ต้นทุนต่อ clip ลดลง [23][29][58][48] ทำให้ animatics คร่าว ๆ iterate ได้ถูกลง น่าจะเกิด: ComfyUI ยังคงเป็น integration hub ที่ใช้งานได้จริงสำหรับ open video/image model ใน production VFX [6][19][28][43] เป็นไปได้: China non-Nvidia stack แคบช่องว่างต้นทุนตามที่อ้าง [16][10] ขยายตัวเลือก open ที่ราคาจับต้องได้ — แต่อิงผู้วิจารณ์เพียงรายเดียว ยังไม่ยืนยัน เป็นไปได้: Midjourney hardware [2] เป็น consumer/creative device มากกว่าสิ่งที่ studio ต้องการ รอดู launch จริงก่อน ไม่น่าจะเกิดจากหลักฐานวันนี้: เครื่องมือ 3D/mesh/scene generation ที่ใช้งานได้สำหรับ game/XR pipeline — แทบไม่มีสัญญาณ 3D ในรายการเหล่านี้เลย

## Org applicability — NDF DEV
1) ทดลอง ComfyUI VFX pipeline กับ asset ภายในชิ้นเล็ก (face swap/de-aging, sky/atmosphere replacement, Wan 2.2 motion transfer) ใช้ open WAN/Flux weights — effort ต่ำ/กลาง รันในเครื่อง ไม่มีต้นทุน per-seat เหมาะกับ edutech visuals และ game cinematics [6][19][28][43] 2) bake-off ต้นทุน/คุณภาพระหว่าง Seedance 2.0 Mini vs Kling 3.0 vs Veo 3.1 สำหรับ storyboard/animatic generation — effort ต่ำ hosted [23][27][29][48] 3) ประเมิน local inference box (Flux + small LLM) สำหรับ on-prem image gen หากจำเป็นด้าน data sensitivity หรือปริมาณงาน — effort กลาง [54] 4) สำหรับ voiceover ใน edutech ทดสอบ open Chatterbox (Resemble AI) เทียบ paid TTS ก่อนผูกสัญญา subscription — effort ต่ำ [60] ข้าม: การทำให้ closed video app ราคาแพงเป็น core dependency (เศรษฐกิจ Sora [45]); แพลตฟอร์ม affiliate 'free unlimited' [27][42]; และโพสต์ bookmark/tool-list [33][36][37][49] — ไม่มีคุณค่า production หมายเหตุ: อย่าคาดหวัง 3D asset-gen solution จาก batch นี้ ใช้ 3D pipeline ปัจจุบันต่อไป

## Signals to Watch
- ComfyUI ในฐานะ integration layer สำหรับ open video model (Florence 2/SAM2/WAN/Flux chains) — จับตา template ที่ stable และนำกลับมาใช้ได้ [6][19][28][43]
- การแข่งขัน cost/speed ใน hosted video: Seedance 2.0 Mini + CapCut Director Mode vs Kling/Veo/Grok [29][34][48][58]
- China non-Nvidia training-cost claims (Z.ai บน Huawei Ascend) — ยืนยันอิสระก่อนนำไปใช้ [16][10]
- การย้าย talent ไปสู่ 'real-world'/world models (การย้ายจาก ex-Meta, ex-xAI; video model journal club) เป็น leading indicator สำหรับ 3D/physical consistency [13][15][20]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | foalymatripony | ^110806 c360 | [Holy shit. It's fully Sora Ai](https://x.com/foalymatripony/status/2066952666031308979) |
| x | midjourney | ^4415 c513 | [Midjourney will be announcing its first hardware project tomorrow (Wednesday 6/1](https://x.com/midjourney/status/2066994481770213697) |
| x | Sigmaskibidi282 | ^1354 c6 | [@foalymatripony It's not ai but damn it does look like the average Sora ai Disne](https://x.com/Sigmaskibidi282/status/2067015976072425543) |
| x | javilopen | ^1201 c42 | [I'd forgotten about "Primer". The most complex movie I've ever seen. You know wh](https://x.com/javilopen/status/2066577399832097002) |
| x | c_valenzuelab | ^713 c171 | [Imagine waking up and realizing that your full time job entails using a digital ](https://x.com/c_valenzuelab/status/2066922813466779876) |
| x | 8bit_e | ^663 c23 | [Painted sections of my face with face paint and used them to guide where the AI ](https://x.com/8bit_e/status/2066907375894688183) |
| x | ShamiWeb3 | ^615 c126 | [This is what happens when World Cup energy meets e-commerce storytelling ⚽ Fast ](https://x.com/ShamiWeb3/status/2067048483279057062) |
| x | NapoleonBonabot | ^518 c15 | [Is it just me or does this look like Sora AI?](https://x.com/NapoleonBonabot/status/2067066960081223881) |
| x | EMostaque | ^496 c14 | [With the acquisition of @cursor_ai the AI run rate of $SPCX will actually go abo](https://x.com/EMostaque/status/2066856395463344526) |
| x | EMostaque | ^457 c40 | [I think it's increasingly clear that if Chinese AI labs can get enough compute t](https://x.com/EMostaque/status/2067208860020924573) |
| x | signulll | ^411 c20 | [the entire sora chase kinda cost openai twice. on the supply side it bled comput](https://x.com/signulll/status/2066665563150237834) |
| x | Rogito211 | ^408 c0 | [@ToonHive You could tell me this is Sora Ai and I'd believe you](https://x.com/Rogito211/status/2067042901758976378) |
| x | _rohitgirdhar_ | ^406 c24 | [After almost 7 incredible years at Meta, I'm excited to share that I'll be joini](https://x.com/_rohitgirdhar_/status/2066846769204347142) |
| x | strawbrrysugrr | ^383 c1 | [@foalymatripony so no this is just disney's style lately, sora stole it because ](https://x.com/strawbrrysugrr/status/2067019746688581933) |
| x | zeeshanp_ | ^379 c16 | [Personal update: I joined @PrometheusInc six months ago to help build the Artifi](https://x.com/zeeshanp_/status/2066616272230760503) |
| x | EMostaque | ^379 c19 | [Important to note @Zai_org train on @Huawei Ascend chips, no NVIDA (!) So you ha](https://x.com/EMostaque/status/2067208281727054123) |
| x | runwayml | ^354 c35 | [Use Runway inside ChatGPT to generate and edit video and images. No tab-switchin](https://x.com/runwayml/status/2066596138824696214) |
| x | EMostaque | ^324 c56 | [At what valuation of SpaceX does Elon merge Tesla into it?](https://x.com/EMostaque/status/2066829123754799194) |
| x | ComfyUI | ^322 c9 | [Face Replacement and De-aging Demo: VFX artist @heydoughogan built a fully autom](https://x.com/ComfyUI/status/2066635313062277337) |
| x | DengHokin | ^310 c3 | [I am super excited to share that I launch a weekly Video Model Journal Club. Eve](https://x.com/DengHokin/status/2066692387397927329) |
| x | probnstat | ^306 c4 | [The Calculus of Randomness: How Itô's Integral Tamed the Chaos of the Universe T](https://x.com/probnstat/status/2066612639049101355) |
| x | fabianstelzer | ^286 c60 | [a really strange behaviour I'm observing with many high end Chinese models is se](https://x.com/fabianstelzer/status/2067146927058124952) |
| x | AIwithJessica | ^277 c27 | [The next wave of AI video isn't about bigger demos, it's about faster production](https://x.com/AIwithJessica/status/2066731121354977703) |
| x | mdmadeit | ^257 c33 | [Azuki Zanbato Dance Made with midjourney, chatgpt and seedance Prompt on the nex](https://x.com/mdmadeit/status/2066722279376195963) |
| x | EMostaque | ^255 c28 | [are they going to rename it CodeX](https://x.com/EMostaque/status/2066989372017090669) |
| x | AleRVG | ^252 c19 | [💡One of the biggest issues I've faced with short-form video is the constant repe](https://x.com/AleRVG/status/2066871328263574014) |
| x | Atenov_D | ^242 c26 | [FREE 1 month Plus subscription. Seedance 2.0, Kling 3.0, Veo 3.1, WAN. No card, ](https://x.com/Atenov_D/status/2066905977278886246) |
| x | ComfyUI | ^234 c4 | [Creator lecovictor ( IG ) built this workflow to explore what's possible at the ](https://x.com/ComfyUI/status/2066947693629608183) |
| x | zahra4sure | ^213 c43 | [CapCut's new AI video update is a big one for anyone who moves fast. With Dreami](https://x.com/zahra4sure/status/2066803186267312219) |
| x | DoctorAmna11 | ^209 c34 | [CapCut's new AI video update is a good reminder that the best tool is not always](https://x.com/DoctorAmna11/status/2066808807326400704) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@foalymatripony</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 110806 · 💬 360</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/foalymatripony/status/2066952666031308979">View @foalymatripony on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Holy shit. It’s fully Sora Ai”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้โพสต์ประโยคสั้นแสดงความตื่นเต้นเกี่ยวกับ Sora AI โดยไม่มีรายละเอียดว่าอะไรเปลี่ยนแปลง ฟีเจอร์อะไร หรือเวอร์ชันอะไร</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/foalymatripony/status/2066952666031308979" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@midjourney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4415 · 💬 513</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2066994481770213697">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Midjourney will be announcing its first hardware project tomorrow (Wednesday 6/17) at 6pm PT. Stay tuned for a livestream of our in-person launch event in San Francisco. If you're in town and want an ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney เปิดตัว hardware ตัวแรกที่งาน live event ใน San Francisco วันนี้ (17 มิ.ย.) เวลา 6 pm PT พร้อม livestream สาธารณะ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Midjourney ก้าวเข้าสู่ hardware หมายความว่ามีผลิตภัณฑ์ใหม่ที่อาจเกี่ยวกับ spatial computing หรือ creative tools — ตรงกับงาน XR/VR และ AI asset</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู livestream วันนี้ 6 pm PT แล้วค่อยประเมินว่า hardware นี้เข้ากับ pipeline XR/VR หรืองาน AI asset ของสตูดิโอได้แค่ไหน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/midjourney/status/2066994481770213697" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Sigmaskibidi282</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1354 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Sigmaskibidi282/status/2067015976072425543">View @Sigmaskibidi282 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@foalymatripony It's not ai but damn it does look like the average Sora ai Disney style video”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้คอมเมนต์ว่าวิดีโอหนึ่งดูคล้าย output สไตล์ Disney จาก Sora แต่ยืนยันว่าไม่ได้สร้างด้วย AI</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Sigmaskibidi282/status/2067015976072425543" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@javilopen</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1201 · 💬 42</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/javilopen/status/2066577399832097002">View @javilopen on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'd forgotten about &quot;Primer&quot;. The most complex movie I've ever seen. You know when people say, &quot;Let me draw you a diagram&quot;? Well, this movie is so complicated it actually needs one. It's going to blow”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้แนะนำหนัง 'Primer' (2004) ว่าซับซ้อนมากจนต้องใช้ diagram อธิบาย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/javilopen/status/2066577399832097002" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@c_valenzuelab</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 713 · 💬 171</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/c_valenzuelab/status/2066922813466779876">View @c_valenzuelab on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Imagine waking up and realizing that your full time job entails using a digital cinema camera with a 65mm large format CMOS sensor fabricated on a sub-20nm semiconductor process, capturing 16-bit line”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@c_valenzuelab ชี้ว่า pipeline ภาพยนตร์มืออาชีพฝัง ML denoising, NeRF, optical flow, photogrammetry ไว้นานแล้ว การบอกว่า AI imagery เพิ่งมาถึงจึงไม่ถูกต้อง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคโนโลยีที่ระบุ — NeRF, photogrammetry, LiDAR, ML denoising, PBR — ตรงกับ workflow XR/VR และ Unity asset production ที่ทีมใช้อยู่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ใช้ framing นี้ตอน client ต้านทาน AI tools — ชี้ว่าเทคนิคเหล่านี้เป็น standard ใน visual production มืออาชีพมานานแล้ว</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/c_valenzuelab/status/2066922813466779876" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@8bit_e</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 663 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/8bit_e/status/2066907375894688183">View @8bit_e on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Painted sections of my face with face paint and used them to guide where the AI effect would appear. Using Wan 2.2 Animate in ComfyUI, I turned those areas into a robotic endoskeleton while leaving mu”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักสร้างใช้สีทาหน้าเป็น region mask ทางกายภาพใน ComfyUI (Wan 2.2 Animate) เพื่อให้ AI ใส่ VFX โรบอทเฉพาะจุดที่ทา โดยไม่แตะ footage ส่วนที่เหลือ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>สีทาหน้าแทน rotoscoping ได้เลย — selective AI compositing ไม่ต้องทำ mask ในซอฟต์แวร์ ใช้ได้ดีกับงาน previs และ XR concept</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลองเทคนิคนี้ใน ComfyUI สำหรับงาน XR หรือ previs ที่ต้องการ selective AI VFX บน live footage โดยไม่ต้องมี rotoscoping pipeline</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/8bit_e/status/2066907375894688183" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ShamiWeb3</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 615 · 💬 126</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ShamiWeb3/status/2067048483279057062">View @ShamiWeb3 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is what happens when World Cup energy meets e-commerce storytelling ⚽ Fast lifestyle cuts and stadium-level football energy shaping a premium Speedcat OG Pelé Yellow – PUMA Black film. From handh”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Creator สร้าง commercial video ให้ PUMA ด้วย GPT Image 2 + Seedance 2.0 ผ่าน EaseMate AI ผสม UGC-style กับ macro product shot และ hero moment โดยไม่ใช้กองถ่ายจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Pipeline นี้ผลิต commercial video คุณภาพ broadcast จาก prompt อย่างเดียว — ใช้ได้จริงสำหรับ game trailer หรืองาน promo ของ client</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ pipeline GPT Image 2 + Seedance 2.0 ผ่าน EaseMate AI กับ game trailer หรือ promo ภายในก่อน แล้วค่อยเสนอ client</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ShamiWeb3/status/2067048483279057062" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NapoleonBonabot</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 518 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NapoleonBonabot/status/2067066960081223881">View @NapoleonBonabot on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Is it just me or does this look like Sora AI?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้โพสต์คำถามคลุมเครือว่ามีบางอย่างดูเหมือน output จาก Sora AI โดยไม่มีภาพ บริบท หรือข้อมูลใดประกอบ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NapoleonBonabot/status/2067066960081223881" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
