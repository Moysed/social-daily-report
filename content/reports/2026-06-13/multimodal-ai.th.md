---
type: social-topic-report
date: '2026-06-13'
topic: multimodal-ai
lang: th
pair: multimodal-ai.en.md
generated_at: '2026-06-13T03:42:49+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 157
salience: 0.6
sentiment: mixed
confidence: 0.5
tags:
- video-generation
- image-generation
- comfyui
- open-weights
- text-to-video
- asset-pipeline
thumbnail: https://pbs.twimg.com/media/HKi1tA1XgAAF1Qp.jpg
translated_by: claude-sonnet-4-6
---

# Multimodal AI — 2026-06-13

## TL;DR
- Midjourney ยก V8.1 เป็น default ให้ผู้ใช้ทุกคน, กำหนด deprecate V8 ใน 2 สัปดาห์, และระบุว่า V8.2 กำลังเข้าสู่การทดสอบ 'extremely soon' [7]; แยกอีกโพสต์รายงาน 20M registered vs ~1M paying, มี 19M ที่หายไปหลังยุติ free tier [19].
- โมเดลวิดีโอ hosted ราคาต่ำกำลังเข้ามาบรรจบกัน: Varya (Avataar) จากอินเดียอ้าง $0.01/วินาที และใช้เพียง 4 inference steps แทน 50 [17][44], ส่วนหลายโพสต์แพร่ข่าวลือ Dreamina 'Seedance 2.0 mini' ราคาถูกจะออกภายในหนึ่งสัปดาห์ [32][37][40][60].
- ComfyUI คือ production-pipeline layer ที่ถูกพูดถึงซ้ำๆ: workflow LLM-to-bounding-box/JSON สำหรับตั้งค่าภาพ [10] และ workflow 'Playblast → finished shot' โดยใช้ Seedance 2.0 โดยไม่ผ่าน render pipeline แบบเดิม [13].
- LTX 2.3 เพิ่ม Multiple Subject Reference (สูงสุด 5 ภาพ เช่น 2 ตัวละคร + พื้นหลัง) โดยอ้างว่าไม่มี face-mixing [29] — สำคัญเพราะ LTX เปิด open weights.
- Runway ขยายความร่วมมือกับ Lionsgate สู่โปรแกรมพัฒนา original IP ร่วมกัน [5][22] และจัด AI Festival ที่ Lincoln Center เต็มทุกที่นั่ง [21][34]; image/video stack ที่ creators อ้างถึงในปัจจุบันคือ GPT Image 2, Nano Banana 2, Veo 3.1 Fast และ Ray 3.14 [27][33].

## What happened
ฝั่งภาพ Midjourney โปรโมท V8.1 เป็น default, กำหนด deprecate V8 ใน 2 สัปดาห์ และส่งสัญญาณว่า V8.2 จะเข้าทดสอบเร็วๆ นี้ [7]; อีกโพสต์ระบุ registered users 20M, paying ~1M และ 19M หลุดออกหลังยุติ free tier [19]. โมเดลภาพที่ creators อ้างถึงคือ GPT Image 2, Google's Nano Banana 2 และ Midjourney [11][27][35] โดย Adobe เปิด free daily tier (5 ภาพ, 2 วิดีโอ) ครอบคลุม Nano Banana 2, GPT Image 2, Veo 3.1 Fast และ Ray 3.14 [33]. ฝั่งวิดีโอ โมเดลราคาต่ำครองการสนทนา: Varya จาก Avataar ชูจุดขาย $0.01/วินาที และลด step จาก 50 เหลือ 4 [17][44], Kling 3.0 ถูกโปรโมทสำหรับสร้าง UGC ad ปริมาณสูง [16][26][57] และหลายบัญชีขยายข่าวลือ Dreamina Seedance 2.0/mini ราคาถูกจะออกสัปดาห์หน้า [32][37][40][60].

## Why it matters (reasoning)
มีสองแนวโน้มสำคัญต่อ production pipeline. ประการแรก orchestration layer กำลังรวมศูนย์ที่ ComfyUI: การ prompt ด้วย structured JSON/bounding-box [10] และการ render playblast-to-finished-shot ด้วย Seedance 2.0 [13] แสดงให้เห็นว่าโมเดลวิดีโอ/ภาพถูกต่อเข้ากับ workflow แบบ deterministic และทำซ้ำได้ ไม่ใช่แค่ chat demo ครั้งเดียว — ซึ่งเป็นรูปแบบที่ใช้งานได้จริงสำหรับ game และ XR asset. ประการที่สอง video generation กำลังถูกกดราคาอย่างต่อเนื่อง ทั้ง per-second pricing ที่ชัดเจน ($0.01/s [17][44]) และข่าวลือโมเดลราคาถูก [40][60]; หากเป็นจริงจะลดต้นทุนสร้าง edutech motion visual และ animatic ได้มาก. ตัวเลข churn ของ Midjourney [19] เป็นสัญญาณเตือน: การยุติ free tier ทำให้ฐานผู้ใช้ลดลง ~20 เท่า บ่งชี้ว่าการยึดติดกับ hosted tool นั้นเปราะบาง และตัวเลือก open-weights (LTX 2.3 [29], เครื่องมือ local ที่อ้าง 117k stars รองรับภาพ/วิดีโอ/3D/เสียง [41]) ควรเก็บไว้เป็น fallback. ปริมาณส่วนใหญ่ในฟีดคือ marketing claim, ข่าวลือ และรายการ '100+ tools' แบบทั่วไป [23][36][39][45][55] ไม่ใช่การ release ที่ยืนยันแล้ว.

## Possibility
การลดราคา/step ของวิดีโอต่อเนื่องมีแนวโน้มสูง เนื่องจากมีสัญญาณราคาต่ำหลายแหล่งที่อิสระจากกัน ([17][44] เป็น launch claim ที่ยืนยันแล้ว; [40][60] เป็นข่าวลือ) — อย่างไรก็ตามกำหนดเวลาของ Dreamina/Seedance ยังไม่ผ่านการยืนยัน ควรถือเป็น plausible ไม่ใช่ certain. LTX 2.3 open-weights multi-subject video reference [29] ที่ใช้กับตัวละคร/ฉากที่ต้องคงรูปใน pipeline จริงมีความเป็นไปได้ เพราะเปิด weights แทนที่จะเป็นแค่ closed demo. การกลับมาของ Midjourney free/cheap tier มีความเป็นไปได้จากปัญหา churn 19M [19] ที่ระบุไว้ แต่ยังไม่มีแหล่งใดยืนยัน. Marketing claim อย่าง Kling 3.0 '$1/video, 550/day' [16][26] ไม่น่าจะคงคุณภาพนั้นได้เมื่อทดสอบจริง เพราะไม่มี benchmark อิสระใดรองรับ.

## Org applicability — NDF DEV
1) ประเมิน ComfyUI เป็น orchestration layer สำหรับ asset generation ใน Unity/XR — node graph ที่ emit structured JSON/bounding box [10] และ flow playblast-to-render [13] รองรับ concept art, background และ animatic; effort ปานกลาง. 2) ทดสอบ LTX 2.3 open weights สำหรับความสม่ำเสมอของตัวละคร/ฉาก (สูงสุด 5 references, อ้างไม่มี face-mixing [29]) — ใช้ได้กับ edutech character ที่ต้องคง model เดิมข้ามช็อต; effort ปานกลาง. 3) ทดลอง hosted video ราคาถูกสำหรับ edutech visual — benchmark Varya ที่ $0.01/s [17][44] เทียบกับ Veo 3.1 Fast และ Ray 3.14 จาก Adobe free tier [33]; effort ต่ำ (hosted API). 4) ใช้ Midjourney V8.1 ต่อสำหรับ concept art แต่ทดสอบ prompt/sref library ใหม่ตอนนี้ เพราะ V8 deprecate ใน 2 สัปดาห์ [7]; effort ต่ำ. ข้ามไป: UGC ad-farm pipeline [16][26][57], รายการ '100+/120+ AI tools' ทั่วไป [23][36][39][45][55][58] และข่าวลือ Seedance [32][37][40][60] จนกว่าจะมี API/pricing page จริง.

## Signals to Watch
- Dreamina 'Seedance 2.0 mini' มีข่าวลือว่าจะออก ~ภายในหนึ่งสัปดาห์ — รอ API จริงและราคาต่อวินาที ไม่ใช่แค่โพสต์ leak [37][60].
- Midjourney V8.2 กำลังเข้าทดสอบ 'extremely soon' โดย V8 deprecate ใน 2 สัปดาห์ [7].
- Runway × Lionsgate โปรแกรมพัฒนา original IP ร่วมกัน — รูปแบบ licensed-studio สำหรับ generative video [5][22].
- LTX 2.3 Multiple Subject Reference (5 ภาพ, ไม่มี face-mixing) ในฐานะ open-weights option สำหรับ production consistency [29].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Suhail | ^12913 c69 | [My favorite @elonmusk quote that I often send friends: Do not fear losing. "You ](https://x.com/Suhail/status/2065476904543481907) |
| x | EMostaque | ^971 c22 | [So looks like @SpaceX will spend 2.5% of its market cap to buy @cursor_ai at 15x](https://x.com/EMostaque/status/2065514350090059901) |
| x | tan_stack | ^826 c31 | [TanStack AI is now in Beta! TanStack AI is no longer just a text-generation libr](https://x.com/tan_stack/status/2065102675390189916) |
| x | Suhail | ^624 c20 | [Priorities for high agency people are almost always communicated by the latency ](https://x.com/Suhail/status/2065127494014120056) |
| x | runwayml | ^343 c43 | [Today, we're deepening our partnership with Lionsgate with a slate of new initia](https://x.com/runwayml/status/2065072377596088525) |
| x | gurniaiart | ^297 c0 | [Knight art #AIArt #AIイラスト #midjourney #AIgirl #knight #aiGallery https://t.co/20](https://x.com/gurniaiart/status/2065067622610145360) |
| x | midjourney | ^280 c28 | [We've made V8.1 the new default model for all users on Midjourney. V8 will now b](https://x.com/midjourney/status/2064921117618557292) |
| x | Suhail | ^238 c7 | [SpaceX feels like a bet on rooting for humanity's grand ability to invent, thriv](https://x.com/Suhail/status/2065472394156773705) |
| x | bull_bnb | ^234 c33 | [AI data was big because models needed the internet. Robot data will be bigger be](https://x.com/bull_bnb/status/2065131071252103412) |
| x | hellorob | ^229 c8 | [The only thing worse than looking at a blank canvas is prompting with JSON. Here](https://x.com/hellorob/status/2065209723184676973) |
| x | AvelyrahnAI | ^215 c29 | [Created with GPT Image 2 on Chatgpt Prompt: Create image Here's a cleaner, optim](https://x.com/AvelyrahnAI/status/2065383336722493531) |
| x | Suhail | ^197 c13 | [I've enjoyed this prompt for learning more than I thought I would: Teach me this](https://x.com/Suhail/status/2065103647848157369) |
| x | ComfyUI | ^190 c7 | [Seedance Playblast 2 Render Demo: VFX artist @heydoughogan built a workflow in C](https://x.com/ComfyUI/status/2065217065490034775) |
| x | Endory2 | ^188 c5 | [KH4 sora is weirdly AI Upscaled btw. KH4 does not look like this. And I am not t](https://x.com/Endory2/status/2065176708836217258) |
| x | sunaiuse | ^174 c28 | [1 guy in China made $1,000,000 last year. No employees. No code. Just AI and a v](https://x.com/sunaiuse/status/2065183221135069232) |
| x | FynCas | ^171 c93 | [MakeUGC & Kling 3.0 = 550 videos/day Fully realistic UGC ads — cinematic lightin](https://x.com/FynCas/status/2065071656100298813) |
| x | kingofknowwhere | ^168 c13 | [India just launched it's first video AI model Varya. (@Avataar) It is marketted ](https://x.com/kingofknowwhere/status/2065352682328690689) |
| x | Tanaypawar27 | ^156 c31 | [Best accounts to follow from each frontier lab to stay constantly up to date Ant](https://x.com/Tanaypawar27/status/2064920550418645252) |
| x | ekinoks_26 | ^155 c160 | [Midjourney has 20 million registered users. Roughly 1 million pay. The other 19 ](https://x.com/ekinoks_26/status/2064950762715951536) |
| x | treyisforever | ^150 c0 | [@cihywastaken @ctrlkugi ai image generation has been around publicly since 2020 ](https://x.com/treyisforever/status/2065118866943176709) |
| x | c_valenzuelab | ^146 c16 | [Yesterday, we hosted our 4th Annual AI Festival at Lincoln Center in NYC, our bi](https://x.com/c_valenzuelab/status/2065417356986208632) |
| x | c_valenzuelab | ^145 c19 | [Excited to announce that we're expanding our partnership with Lionsgate through ](https://x.com/c_valenzuelab/status/2065081068630282541) |
| x | Bhanusinghyede | ^144 c21 | [🚀 𝟏𝟐𝟎 𝐌𝐢𝐧𝐝-𝐁𝐥𝐨𝐰𝐢𝐧𝐠 𝐀𝐈 𝐓𝐨𝐨𝐥𝐬 𝐘𝐨𝐮 𝐒𝐡𝐨𝐮𝐥𝐝 𝐊𝐧𝐨𝐰 𝐢𝐧 𝟐𝟎𝟐𝟔 Most people know 5–10 tools…](https://x.com/Bhanusinghyede/status/2065036535645470797) |
| x | kellyeld | ^143 c15 | ['Beautiful Pink Heart' Lyrics by me. About a tough time in my life many years ag](https://x.com/kellyeld/status/2065444518426734700) |
| x | GlitterPixely | ^142 c25 | ["Oh! it's you!"🤭I found the cutest sref so had to test it! Prompt below, too ₍ᐢ.](https://x.com/GlitterPixely/status/2065294658532442368) |
| x | spwfeijen | ^142 c79 | [Kling 3.0 = 550 videos per day Fully-realistic UGC ads — cinematic lighting, hum](https://x.com/spwfeijen/status/2065056560154370451) |
| x | churvikv | ^141 c53 | [Northern lights and neon reefs Created in @Somake_ai Model: Midjourney Experimen](https://x.com/churvikv/status/2065155683301917132) |
| x | avidseries | ^140 c21 | [A lot of people follow AI more closely than I do, but almost everything I'm read](https://x.com/avidseries/status/2065446869652652106) |
| x | sunbaolong_2001 | ^136 c2 | [LTX 2.3 just reached "Omni-Reference" level! 🎬🔥 The new MSR (Multiple Subject Re](https://x.com/sunbaolong_2001/status/2065098450333839446) |
| x | EMostaque | ^136 c8 | [Thanks @elder_plinius 😂 https://t.co/n6Ff9zJHyv](https://x.com/EMostaque/status/2065605506165518722) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Suhail</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 12913 · 💬 69</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Suhail/status/2065476904543481907">View @Suhail on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“My favorite @elonmusk quote that I often send friends: Do not fear losing. “You will lose,” Musk says. “It will hurt the first fifty times. When you get used to losing, you will play each game with le”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แชร์คำพูด Elon Musk เรื่องการยอมรับความล้มเหลวเพื่อกล้าเสี่ยงมากขึ้น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Suhail/status/2065476904543481907" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EMostaque</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 971 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EMostaque/status/2065514350090059901">View @EMostaque on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“So looks like @SpaceX will spend 2.5% of its market cap to buy @cursor_ai at 15x revenue 👀”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>EMostaque รายงานว่า SpaceX กำลังจะซื้อกิจการ Cursor AI ที่ราคา ~15 เท่าของรายได้ คิดเป็นราว 2.5% ของ market cap SpaceX</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Cursor เป็น AI coding tool หลักของทีม dev ทั่วไป การที่ SpaceX เข้าถือครองจะเปลี่ยนทิศทาง roadmap และ pricing</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตาม roadmap ของ Cursor หลังดีลปิด ถ้าเน้น enterprise มากขึ้น ให้ประเมิน Windsurf หรือ VS Code + Copilot แทน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EMostaque/status/2065514350090059901" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@tan_stack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 826 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/tan_stack/status/2065102675390189916">View @tan_stack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“TanStack AI is now in Beta! TanStack AI is no longer just a text-generation library with extras bolted on. TanStack AI has first-class dev experience for: ✅ Text and Streaming Structured Data ✅ Tool C”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>TanStack AI เข้า Beta เป็น library JS/TS ที่รวม generative AI ครบวงจร — text, tool calls, image/video/audio gen, realtime voice, MCP hosting และ orchestration พร้อม per-model type-safety</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>library ตัวเดียวครอบ AI ทั้งหมดตั้งแต่ text ถึง multimodal และ voice ไม่ต้องต่อ SDK หลายตัวใน web หรือ e-learning project ที่มี AI</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง TanStack AI เป็น AI layer ใน web project ถัดไป โดยเฉพาะโปรเจกต์ที่ scope multimodal output หรือ voice chat ไว้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/tan_stack/status/2065102675390189916" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Suhail</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 624 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Suhail/status/2065127494014120056">View @Suhail on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Priorities for high agency people are almost always communicated by the latency of their response.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้เขียนบอกว่าคนที่ agency สูงสื่อสาร priority ผ่านความเร็วในการตอบกลับ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Suhail/status/2065127494014120056" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@runwayml</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 343 · 💬 43</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/runwayml/status/2065072377596088525">View @runwayml on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Today, we’re deepening our partnership with Lionsgate with a slate of new initiatives, including a joint development program focused on creating original IP together. Learn more at the link below. htt”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Runway ML กับ Lionsgate ขยายความร่วมมือจากแค่ใช้ tools ไปสู่ร่วม develop original IP ด้วยกันโดยตรง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/runwayml/status/2065072377596088525" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gurniaiart</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 297 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gurniaiart/status/2065067622610145360">View @gurniaiart on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Knight art #AIArt #AIイラスト #midjourney #AIgirl #knight #aiGallery https://t.co/20cs9inIha”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ X โพสต์ภาพ AI-generated อัศวินสร้างด้วย Midjourney ติด tag #AIArt / #aiGallery ได้ 297 likes</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gurniaiart/status/2065067622610145360" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@midjourney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 280 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2064921117618557292">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We've made V8.1 the new default model for all users on Midjourney. V8 will now be deprecated in 2 weeks. V8.2 will start testing extremely soon.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney ตั้ง V8.1 เป็น default model ให้ทุก user แล้ว, V8 จะถูก deprecated ใน 2 สัปดาห์ และ V8.2 จะเริ่ม test เร็วๆ นี้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>workflow หรือ script ที่ pin V8 ไว้จะพังใน 2 สัปดาห์ V8.1 output style ต่างออกไปและอาจเปลี่ยน result ของ concept art หรือ asset ที่ generate ไว้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู Midjourney API call และ saved prompt ทั้งหมดที่ระบุ V8 แล้วอัปเป็น V8.1 ก่อนครบ 2 สัปดาห์</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/midjourney/status/2064921117618557292" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Suhail</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 238 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Suhail/status/2065472394156773705">View @Suhail on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“SpaceX feels like a bet on rooting for humanity's grand ability to invent, thrive, and far surpass our wildest imaginations. Bravo to you all that made this happen.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@Suhail โพสต์ยกย่อง SpaceX สำหรับความสำเร็จที่ไม่ระบุรายละเอียด โดยมองว่าเป็นชัยชนะของมนุษยชาติ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Suhail/status/2065472394156773705" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
