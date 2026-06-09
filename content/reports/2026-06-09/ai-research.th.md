---
type: social-topic-report
date: '2026-06-09'
topic: ai-research
lang: th
pair: ai-research.en.md
generated_at: '2026-06-09T03:28:39+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- radar
- rss
- x
regions:
- global
post_count: 194
salience: 0.42
sentiment: mixed
confidence: 0.5
tags:
- ai-research
- model-eval
- on-device-ai
- local-llm
- coding-models
- benchmarks
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2063651111664250880/img/mTeN_Ym3Mzdr3KVd.jpg
translated_by: claude-sonnet-4-6
---

# AI Research — 2026-06-09

## TL;DR
- Apple เปิดเผย AI architecture ที่สร้างรอบ Google Gemini models [8] และปล่อย Core AI framework developer docs [16] — เส้นทาง on-device/platform ที่เกี่ยวข้องกับแอป iOS, mobile, และ XR
- Xiaomi ประกาศ MiMo-v2.5-Pro-UltraSpeed อ้างเป็น model ขนาด 1T param ที่รัน 1000 tokens/sec [4]; NVIDIA Nemotron 3 Nano วางตำแหน่งเป็น local model สำหรับ 24GB / CPU+RAM [51] — ทั้งคู่เป็น vendor claims ยังไม่มี independent benchmarks ในฟีด
- สัญญาณเรื่อง eval hygiene: Amazon ยกเลิก AI leaderboard หลังต้นทุนพุ่ง [30] และมีการถกเถียงว่า 'benchmaxxing' แบบ static กำลังเปลี่ยนไปใช้ suite ที่อัปเดตต่อเนื่องอย่าง LiveCodeBench [42]
- สัญญาณเสี่ยงในการ adoption: มี 30B coding model ที่ไม่มีชื่อปรากฏขึ้นโดยไม่มี model card หรือข้อมูลใดเลย [46]; string ของ Anthropic ชื่อ claude-oceanus-v1-p รั่วออกมาใน Console แต่ยังไม่มีการยืนยัน [33]
- ฟีดส่วนใหญ่วันนี้ออกนอกเรื่อง (การเมือง, กีฬา 'red/blue team', ภูมิรัฐศาสตร์); signal ด้าน AI research จริงๆ มีน้อยและส่วนใหญ่เป็น social posts ไม่ใช่ papers หรือ reproducible evals

## What happened
Platform news: Apple เปิดเผย AI architecture ที่จัดระบบรอบ Google Gemini models [8] และส่ง Core AI framework documentation ให้นักพัฒนา [16] มี vendor claims เรื่อง model/inference ใหม่: MiMo-v2.5-Pro-UltraSpeed ของ Xiaomi (1T params, ~1000 tok/s) [4], NVIDIA Nemotron 3 Nano สำหรับ low-end GPU หรือ CPU+RAM (24GB) พร้อม pipeline 'PRISM' [51] และ FrontierCode coding ของ Cognition [32] มีการโพสต์ unnamed 30B coding model โดยไม่มี model card [46] และพบ Anthropic model string (claude-oceanus-v1-p) ใน Console โดยผู้โพสต์ระบุว่าเรื่องราวส่วนใหญ่ยังเป็นการคาดเดา [33]

## Why it matters (reasoning)
สำหรับการตัดสินใจ adoption สิ่งที่ลงมือทำได้จริงคือเรื่อง provenance และ evaluation ไม่ใช่การ hype capability ดิบๆ vendor claims เรื่องความเร็ว/ขนาด [4][51] ยังไม่มี independent benchmarks จึงยังใช้เลือก model ไม่ได้ signal ด้าน eval infrastructure สำคัญกว่า: Amazon ถอน leaderboard เพราะต้นทุน [30] และการย้ายไปใช้ benchmark ที่อัปเดตต่อเนื่องและป้องกัน contamination [42] ล้วนสนับสนุนให้ไม่เชื่อ static public leaderboard เมื่อเลือก model 30B coding model ที่ไม่มี model card [46] คือตัวอย่างชัดของ release ที่ไม่ควร adopt โดยไม่มีข้อมูล training data, license, และ eval ที่บันทึกไว้ Apple architecture ที่ใช้ Gemini [8] บวก Core AI docs [16] คือ second-order effect ที่เป็นรูปธรรมที่สุด: กำหนดทิศทาง on-device AI สำหรับ iOS/mobile และอาจรวม XR ด้วย พร้อมผูก stack ของ Apple กับ Google model dependency งานวิจัยด้าน interpretability [49][60] ยังเร็วเกินไปและยังไม่เกี่ยวกับ adoption ความสงสัยในภาพรวม (บทความของ Zitron 'AI is slowing down' [6]) เป็นความคิดเห็น ไม่ใช่หลักฐานของ method หรือ model ที่ควรดำเนินการ

## Possibility
มีแนวโน้มสูง: Apple Core AI + Gemini [8][16] จะกลายเป็นสิ่งที่ต้องพิจารณาจริงสำหรับ feature iOS/edu/XR ภายในไม่กี่เดือน เพราะตอนนี้ ship เป็น developer-facing docs แล้ว เป็นไปได้: local models ขนาดเล็กอย่าง Nemotron 3 Nano [51] จะดีพอสำหรับ edu features แบบ offline หรือ privacy-sensitive แต่ต้องรอ independent eval ยืนยัน vendor claims ก่อน เป็นไปได้: public leaderboards จะสูญเสียความน่าเชื่อถือต่อเนื่อง เพราะปัญหาต้นทุนและ contamination [30][42] ดัน team ไปใช้ private/held-out evals ไม่น่าจะเกิด (ระยะสั้น): Anthropic model string ที่รั่ว [33] หรือ 30B model ไร้ card [46] จะ adopt ได้อย่างปลอดภัยตอนนี้ — ทั้งคู่ขาด specs หรือ documentation ที่ยืนยันได้ ไม่มีแหล่งข้อมูลใดให้ตัวเลขความน่าจะเป็น จึงไม่ระบุไว้

## Org applicability — NDF DEV
1) อ่าน Apple's Core AI framework docs และ note เรื่อง Gemini architecture ก่อน scope iOS/mobile/XR AI feature ใหม่ — effort ต่ำ [16][8] 2) สร้าง internal eval harness ขนาดเล็กบน held-out tasks ของตัวเอง (coding, edu content generation) แทนการเชื่อ public leaderboards — effort ปานกลาง สมเหตุสมผลจาก signal เรื่องต้นทุน/contamination [30][42] 3) ถ้าต้องการ offline/on-device inference สำหรับ edu apps ทดสอบ Nemotron 3 Nano บนเครื่อง 24GB และวัดคุณภาพเองก่อนตัดสินใจ — effort ต่ำถึงปานกลาง claims ยังไม่ได้รับการยืนยัน [51] 4) กำหนดกฎตายตัว: ไม่ adopt model ใดที่ขาด model card / license / eval data (เช่น unnamed 30B coder) — effort ต่ำ [46] ข้ามไปก่อน: MiMo 1T speed claim จนกว่าจะมี independent benchmarks [4], Anthropic leak [33] และการถกเถียง macro 'bubble/slowdown' [6][7][29] — ไม่มีอะไรเปลี่ยนการตัดสินใจ build วันนี้

## Signals to Watch
- Apple Core AI framework docs และ Gemini-backed architecture — ติดตามสำหรับ on-device mobile/XR AI [16][8]
- ความน่าเชื่อถือของ public leaderboard: leaderboard ที่ Amazon ยกเลิกและการย้ายไปใช้ benchmark ที่อัปเดตต่อเนื่อง [30][42]
- ความเป็นไปได้ของ local small-model สำหรับ offline edu features (Nemotron 3 Nano) [51]
- วินัยด้าน model card: การปล่อย coding model ที่ไม่มี card ในฐานะ pattern ความเสี่ยงต่อ adoption [46]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | overton_news | ^1497 c21 | [Jillian Michaels delivers a brutal reality check on the Democratic establishment](https://x.com/overton_news/status/2063652303307936081) |
| radar | lizhang | ^822 c162 | [Show HN: Performative-UI – A react component library of design tropes](https://vorpus.github.io/performativeUI/) |
| radar | 1vuio0pswjnm7 | ^572 c419 | [Anti-social: It's fads, not friends, which now dominate social media feeds](https://www.bbc.com/worklife/article/20260520-how-social-media-ceased-to-be-social) |
| radar | gainsurier | ^508 c360 | [MiMo-v2.5-Pro-UltraSpeed: 1T model with 1000 tokens per second](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) |
| radar | g0xA52A2A | ^445 c168 | [Surveillance is not safety: A statement on the UK's latest threat to privacy [pd](https://signal.org/blog/pdfs/2026-06-08-uk-surveillance-is-not-safety.pdf) |
| radar | crescit_eundo | ^433 c454 | [AI is slowing down](https://www.wheresyoured.at/ai-is-slowing-down/) |
| radar | martinald | ^430 c339 | [xAI is looking more like a datacentre REIT than a frontier lab](https://martinalderson.com/posts/xais-new-rental-business/) |
| radar | unclefuzzy | ^389 c340 | [Apple reveals new AI architecture built around Google Gemini models](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/) |
| x | jrosseruk | ^361 c25 | [Career update! I've joined @NeelNanda5's Language Model Interpretability team as](https://x.com/jrosseruk/status/2064076447099015630) |
| radar | hackerBanana | ^309 c231 | [Confidential submission of draft S-1 to the SEC](https://openai.com/index/openai-submits-confidential-s-1/) |
| radar | john-titor | ^262 c95 | [EU-banned pesticides found in rice, tea and spices](https://www.foodwatch.org/en/eu-banned-pesticides-found-in-rice-tea-and-spices) |
| x | SeanZCai | ^254 c14 | [RL environment companies were never meant to sell to labs forever. It is undenia](https://x.com/SeanZCai/status/2063655806181204029) |
| x | nathancgy4 | ^227 c3 | [have been recently thinking about why pretrain research matters among the seemin](https://x.com/nathancgy4/status/2064010906250711330) |
| x | Fightsriot | ^224 c1 | [red team vs blue team https://t.co/dgNAI1ko4R](https://x.com/Fightsriot/status/2063730535046819965) |
| x | probnstat | ^218 c4 | [Information Bottleneck Theory is a powerful framework introduced by Naftali Tish](https://x.com/probnstat/status/2063682362169278722) |
| radar | hmokiguess | ^213 c46 | [Apple Core AI Framework](https://developer.apple.com/documentation/coreai/) |
| x | teortaxesTex | ^210 c10 | [such insane cope The only reason USSR looked like it was doing great is that wyp](https://x.com/teortaxesTex/status/2063689614842294577) |
| x | viemccoy | ^198 c18 | [If anyone is interested in running experiments to help figure out why this happe](https://x.com/viemccoy/status/2063745485224186270) |
| x | probnstat | ^187 c2 | [Gaussian Process Deep Learning combines the uncertainty quantification of Gaussi](https://x.com/probnstat/status/2064008984353288311) |
| x | sripathiteja4 | ^185 c22 | [Stop wasting hours trying to learn AI. I have already done it for you. With one ](https://x.com/sripathiteja4/status/2063621526734471358) |
| x | teortaxesTex | ^172 c6 | [In WWIII, the Gigachad Coalition (Japan, online rightoids, a few Indians and way](https://x.com/teortaxesTex/status/2063809638374498666) |
| x | lateinteraction | ^169 c2 | [as usual from @yoonholeee, this is extremely well-written and a great way to org](https://x.com/lateinteraction/status/2064098415416344835) |
| x | deepfates | ^162 c28 | [humanistic interpretability. who's working on this](https://x.com/deepfates/status/2063656348731257020) |
| x | SimplyAnnisa | ^158 c50 | [GPT image 2 on ChatGPT Professional sports poster, football goalkeeper sitting i](https://x.com/SimplyAnnisa/status/2063625767167082849) |
| x | Vet_X0 | ^145 c7 | [How are we strengthening the XRP Ledger for the next wave of adoption? • Formal ](https://x.com/Vet_X0/status/2064029474019070238) |
| x | browser_use | ^135 c6 | [Introducing Browser Use 0.13.0 [beta] 🏴‍☠️ &gt; The old Browser Use was built fo](https://x.com/browser_use/status/2064114158191468613) |
| x | chewbacapalapa | ^129 c4 | [@BretWeinstein @B44Don Honey, Blue Team literally celebrates when red team is mu](https://x.com/chewbacapalapa/status/2064075495625593330) |
| x | gfodor | ^125 c5 | [I wish we had a legal federal mechanism to seed false red team voters who are on](https://x.com/gfodor/status/2063784025140199583) |
| x | teortaxesTex | ^123 c7 | [People are going insane. there's so much demand for a bubble the wildest thing i](https://x.com/teortaxesTex/status/2063691475091599593) |
| x | CodeByNZ | ^119 c7 | [Bad week for AI. &gt; Amazon scrapped its AI leaderboard after costs spiraled &g](https://x.com/CodeByNZ/status/2063899585064378479) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@overton_news</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1497 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/overton_news/status/2063652303307936081">View @overton_news on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Jillian Michaels delivers a brutal reality check on the Democratic establishment in California. She pointed out that incumbent Karen Bass should have run away with the race — and the fact that she has”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Jillian Michaels แสดงความเห็นเรื่องการเลือกตั้งนายกเทศมนตรี LA โดยชี้ว่าการที่ Karen Bass ยังไม่ชนะขาดทั้งที่ Democrat ลงทะเบียนมากกว่า Republican ถึง 2 เท่า สะท้อนความเปลี่ยนแปลงทางการเมืองในแคลิฟอร์เนีย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/overton_news/status/2063652303307936081" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jrosseruk</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 361 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jrosseruk/status/2064076447099015630">View @jrosseruk on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Career update! I've joined @NeelNanda5's Language Model Interpretability team as a contractor employed by Adecco, supporting @GoogleDeepMind! I'll be working on interp and data attribution! This comes”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@jrosseruk ประกาศเข้าร่วมทีม LM Interpretability ของ Neel Nanda ที่ Google DeepMind ในฐานะ contractor โดยจะทำงานด้าน interpretability และ data attribution หลังจากฝึกงานที่ Cohere</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jrosseruk/status/2064076447099015630" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SeanZCai</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 254 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SeanZCai/status/2063655806181204029">View @SeanZCai on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“RL environment companies were never meant to sell to labs forever. It is undeniable what cost economics will be produced by the unit cost of intelligence decreasing, but that it is still confined to a”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิเคราะห์ชี้ว่า vendor ด้าน AI infra มีความเสี่ยงจาก customer concentration สูง และ 80% ของ enterprise ที่ยังไม่ใช้ AI จะยังคงเป็นเช่นนั้น จนกว่า deployment cost จะลดลง เพราะ engineering cost ต่อ engagement ยังสูงเกินไปสำหรับงาน white-collar ทั่วไป</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>สำหรับ studio เล็กที่ขาย AI tools หรือ e-learning ตัวเลขนี้ยืนยันว่า bottleneck จริงคือ deployment cost ไม่ใช่ demand — packaging และ pricing จึงสำคัญกว่า feature ในตอนนี้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตอน pitch AI features ให้ลูกค้านอกวงการ tech ให้เสนอ model แบบ fixed-cost หรือ SaaS เพื่อตัด barrier เรื่อง per-engagement engineering cost ที่โพสต์นี้ชี้ให้เห็น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SeanZCai/status/2063655806181204029" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nathancgy4</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 227 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nathancgy4/status/2064010906250711330">View @nathancgy4 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“have been recently thinking about why pretrain research matters among the seemingly more crucial data/compute/rl bottlenecks and sharing my take here on what makes pretrain research (still!) vital: 1.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้เขียนชี้ว่า pretrain research ยังสำคัญ เพราะ architecture/optimizer improvements สะสมกัน — ประหยัด FLOP ได้ &gt;90% ด้วย hybrid/sparse attention และ compute กว่าครึ่งยังอยู่ที่ pretraining</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>รู้ว่า efficiency มาจาก architecture ไม่ใช่แค่ compute ช่วยทีมเลือก model ที่คุ้มค่าต่อ inference cost กว่า</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เลือก LLM สำหรับโปรเจกต์ ให้ดู model ที่ใช้ hybrid หรือ sparse attention เพราะ inference cost ต่ำกว่าชัดเจนที่ quality เดียวกัน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nathancgy4/status/2064010906250711330" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Fightsriot</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 224 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Fightsriot/status/2063730535046819965">View @Fightsriot on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“red team vs blue team https://t.co/dgNAI1ko4R”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์มีแค่ประโยค 'red team vs blue team' กับ link — ไม่มีข้อมูล, tool, หรือ finding ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Fightsriot/status/2063730535046819965" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@probnstat</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 218 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/probnstat/status/2063682362169278722">View @probnstat on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Information Bottleneck Theory is a powerful framework introduced by Naftali Tishby for understanding learning and representation in intelligent systems. The central idea is that a good representation ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Information Bottleneck Theory ของ Tishby นิยาม representation ที่ดีว่าต้องเพิ่ม I(T;Y) และลด I(T;X) — บีบอัด input เก็บแค่ข้อมูลที่จำเป็นต่อ task</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ช่วย design compact state representation สำหรับ RL agent และอธิบายว่าทำไม deep net ถึง generalize ได้ — ตรงกับงาน XR และ game AI</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตอน build RL game AI หรือ XR agent ใช้ information bottleneck เป็น criteria ตรวจว่า representation over-fit กับ input noise หรือเปล่า</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/probnstat/status/2063682362169278722" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@teortaxesTex</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 210 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/teortaxesTex/status/2063689614842294577">View @teortaxesTex on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“such insane cope The only reason USSR looked like it was doing great is that wypipos sympathized with bolsheviks and carried water for their propaganda. Objectively Soviets struggled to make toilet pa”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ Twitter โต้เถียงว่า ความสำเร็จของสหภาพโซเวียตเป็นแค่การโฆษณาชวนเชื่อที่ตะวันตกพยุงไว้ และเศรษฐกิจโซเวียตผลิตสินค้าอุปโภคพื้นฐานแทบไม่ได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/teortaxesTex/status/2063689614842294577" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@viemccoy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 198 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/viemccoy/status/2063745485224186270">View @viemccoy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“If anyone is interested in running experiments to help figure out why this happens, when it's harmful, and what we should do about it - DM me! The Red Team is always looking for new people. (High sign”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@viemccoy ประกาศรับสมัครนักวิจัยเข้า Red Team เพื่อศึกษาพฤติกรรม AI บางอย่าง (ไม่ระบุ) — เน้น PM/TPM แต่ไม่บังคับ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/viemccoy/status/2063745485224186270" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
