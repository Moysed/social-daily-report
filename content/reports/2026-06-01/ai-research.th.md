---
type: social-topic-report
date: '2026-06-01'
topic: ai-research
lang: th
pair: ai-research.en.md
generated_at: '2026-06-01T04:10:16+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- radar
- rss
- x
regions:
- global
post_count: 177
salience: 0.25
sentiment: neutral
confidence: 0.55
tags:
- ai-research
- evaluation
- benchmarks
- leaderboards
- prompt-injection
- model-cards
thumbnail: https://pbs.twimg.com/media/HJhS2KkWYAUErj_.jpg
translated_by: claude-sonnet-4-6
---

# AI Research — 2026-06-01

## TL;DR
- รายการ 'Red Team' ที่ engagement สูงวันนี้ส่วนใหญ่เป็นสัญญาณรบกวนจากกีฬา/ไอดอล (cricket RCB vs GT [1], UCL final [7][8], ฟุตบอลอินโดนีเซีย [10], KLP48 [38]) — ไม่ใช่งานวิจัย AI
- Amazon ปิด leaderboard ภายใน 'KiroRank' หลังพนักงานเผา token จำนวนมากเพื่อไต่อันดับ [2] — ตัวอย่างสดของ Goodhart's law ที่เกิดจากการออกแบบ metric ที่บกพร่อง
- ประเด็นหลักที่แท้จริงคือความน่าเชื่อถือของ eval: คำวิจารณ์ benchmark อิ่มตัว/หมดอายุและคะแนนที่ขยับแค่ 0.2% [50], ความไม่คืบหน้าที่เห็นชัดใน model card ของ OpenAI [37], และ Minimax M3 ที่ไม่เปิดเผยจำนวน param/token [39]
- สัญญาณการนำไปใช้งาน: คู่มือ LangSmith+AWS สำหรับ evaluate 'deep agents' แบบ long-horizon [29]; exploit ขโมยข้อมูลที่บันทึกไว้ใน ChatGPT-for-Google-Sheets [28]; การสร้างภาพ local แบบ 1-bit (Bonsai 4B) [13]
- Grok Imagine Video 1.5 Preview อ้างว่าอยู่อันดับ 1 บน Arena image-to-video leaderboard เหนือ Seedance 2.0 และ Veo 3.1 [20][49] — การจัดอันดับด้วย preference vote ไม่ใช่ controlled benchmark

## What happened
engagement ถูกครอบงำโดยโพสต์กีฬา/บันเทิง 'red team' [1][7][8][9][10][11][16][38][57] และ thread เกี่ยวกับ offensive-security tooling [25][27][30][48][59] ซึ่งทั้งหมดไม่มี research signal รายการวิจัย AI ที่แท้จริงมีน้อย Amazon ปิด leaderboard ภายใน (KiroRank) หลังพนักงานเล่นเกมโดยใช้ token เพื่อไต่อันดับ [2] นักปฏิบัติหลายคนวิจารณ์การ evaluate ในปัจจุบัน: การรายงานคะแนนที่ขยับเล็กน้อยบน benchmark อิ่มตัวถูกมองว่าไร้ประโยชน์ [50], benchmark ใน model card ของ OpenAI แสดงให้เห็นว่าไม่มีความคืบหน้าข้ามรุ่น [37], และ lab ถูกกดดันให้เปิดเผยจำนวน training token และ parameter (Minimax M3) [39] ในแง่ความสามารถ Grok Imagine Video 1.5 Preview รายงานว่าอยู่อันดับ 1 บน Arena image-to-video leaderboard เหนือ Seedance 2.0 และ Veo 3.1 [20][49]

## Why it matters (reasoning)
กลุ่มที่สำคัญต่อการนำไปใช้คือความน่าเชื่อถือของ eval ไม่ใช่ SOTA ใหม่ [2] แสดงว่า leaderboard ที่ผูกกับ incentive จะถูกเล่นเสมอ — ตรงประเด็นกับวิธีที่ studio จะ score การทดสอบ model ภายใน [50] และ [37] ชี้ว่าตัวเลข benchmark หลักอิ่มตัวหรือหยุดนิ่งมากขึ้น ดังนั้น delta เล็กน้อยที่รายงานไม่สามารถพยากรณ์ประสิทธิภาพงานจริง; [39] เสริมว่า model card ที่ไม่โปร่งใสทำให้ตรวจสอบ capability claim ได้ยาก ผลลัพธ์รอง: ทีมที่เลือก model โดยดูอันดับ leaderboard เพียงอย่างเดียว (เช่น Arena video claim [20][49] ซึ่งเป็น human-preference voting ที่บิดเบือนได้ง่ายจาก update เดียว) เสี่ยงเลือกบนสัญญาณรบกวน ในขณะเดียวกัน [28] เตือนอย่างเป็นรูปธรรมว่า LLM-in-product integration มีความเสี่ยง data exfiltration ผ่าน prompt injection ซึ่งเป็น adoption blocker โดยไม่ขึ้นกับคุณภาพของ model

## Possibility
มีแนวโน้ม: แรงต้านด้าน eval integrity ดำเนินต่อไปและ eval suite เฉพาะงานแบบ private กลายเป็น default สำหรับการตัดสินใจ adoption จริงจัง [50][37][39] เป็นไปได้: Arena-style preference leaderboard ยังคงผลิต claim อันดับ 1 ที่ผันผวนและพลิกทุก release ดังนั้นการจัดอันดับใดก็ตาม (เช่น Grok video [20][49]) อยู่ได้ไม่นาน เป็นไปได้: exploit prompt-injection/exfiltration ที่ถูกบันทึกใน LLM integration ที่ ship ออกไปแล้วจะตามมาอีก [28] ไม่น่าเป็นไปได้ (ไม่มีหลักฐานรองรับ): benchmark เดียวจะตัดสิน model choice ได้ — รายการทั้งหมดชี้ทิศทางตรงข้าม ไม่มีแหล่งข้อมูลใดระบุตัวเลขความน่าจะเป็น จึงไม่มีการระบุไว้

## Org applicability — NDF DEV
1) สร้าง eval set ส่วนตัวขนาดเล็กจาก NDF DEV task จริง (Unity/edutech prompts, RAG answers) และ score candidate model บนนั้นแทน public leaderboard — ความพยายามต่ำ ได้แรงบันดาลใจโดยตรงจาก [50][37][2] 2) ก่อน ship LLM tool/integration ใดก็ตาม (Sheets-like connectors, agent actions) ให้รัน injection/exfiltration check — ความพยายามปานกลาง ได้แรงบันดาลใจจาก [28] 3) ถ้า evaluate agent features สำหรับแอป ให้อ่าน LangSmith deep-agent eval write-up สำหรับการออกแบบ datapoint/evaluator บน long-horizon task — ความพยายามต่ำ [29] 4) ติดตาม 1-bit/local image generation (Bonsai 4B) สำหรับการใช้งาน on-device หรือ offline ใน edutech/mobile แต่ตรวจสอบคุณภาพก่อน commit — ความพยายามปานกลาง [13] ข้าม: รายการ 'red team' กีฬา/ไอดอลทั้งหมด [1][7][8][9][10][11][16][38], thread ภูมิรัฐศาสตร์ [19][41]-[47][54]-[56], และการใช้ Grok video #1 claim [20][49] เป็นพื้นฐานจัดซื้อ — จดบันทึกไว้แต่อย่าดำเนินการบน preference-vote ranking อย่าใช้ 'Qwen3.5-27B-Claude-4.6-Opus' VLM [34]; ชื่อดูเหมือนสร้างขึ้น/เสียดสีและยังไม่ได้รับการยืนยัน

## Signals to Watch
- Lab จะเริ่มเปิดเผย training-token และ parameter ใน model card เพื่อตอบสนองต่อแรงกดดันแบบ [39] หรือไม่
- ความเสถียรของอันดับ 1 ใน Arena image-to-video ข้าม Grok/Seedance/Veo update ครั้งถัดไป [20][49]
- exploit เพิ่มเติมใน shipped integration ที่ตามรูปแบบ Sheets exfiltration [28]
- การนำ eval suite แบบ private/เฉพาะงานไปใช้แทน public benchmark ที่อิ่มตัว [50][37]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **pewdiepie-archdaemon/odysseus** — Odysseus – self-hosted AI workspace | radar | <https://github.com/pewdiepie-archdaemon/odysseus> |
| **viggy28/streambed** — Show HN: Streambed – Stream Postgres to Iceberg on S3, Supports Postgres Wire | radar | <https://github.com/viggy28/streambed> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | zomato | ^4799 c18 | [Thank you for showing that the red team always delivers ♥️🏆 #RCBvsGT](https://x.com/zomato/status/2061145484274901120) |
| x | Pirat_Nation | ^2385 c85 | [Amazon reportedly shut down an internal AI leaderboard after employees started u](https://x.com/Pirat_Nation/status/2060618209733362132) |
| radar | HypnoticOcelot | ^552 c317 | [Cloudflare Turnstile requiring fingerprintable WebGL](https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting) |
| x | F1BigData | ^450 c1 | [LEASON: Never fully trust a red team](https://x.com/F1BigData/status/2060798697982566640) |
| radar | thunderbong | ^419 c207 | [Codex just found a "workaround" of not having sudo on my PC](https://twitter.com/i/status/2060746160558543217) |
| x | teortaxesTex | ^386 c16 | [@m0d8ye what do you mean, Google has shipped tons of models](https://x.com/teortaxesTex/status/2061250918595641773) |
| x | academy_dinda | ^373 c8 | [Btw in yesterday's Final, the Red Team lost and the Blue team won the UCL Trophy](https://x.com/academy_dinda/status/2061040774528352725) |
| x | Musafirr_hu_yar | ^365 c21 | [Blue team defeated red team https://t.co/BS6RG66nTb](https://x.com/Musafirr_hu_yar/status/2060800023236137239) |
| x | ToriTyson | ^352 c0 | [Im crying on the plane! Thank you @jordybahl for giving us alumna something to b](https://x.com/ToriTyson/status/2061193241584681268) |
| x | TimnasXtra | ^327 c7 | [🚨 White Team defeated Red Team 5-4 in Indonesia's internal training match earlie](https://x.com/TimnasXtra/status/2060693059361493027) |
| x | sopselinchen | ^323 c4 | [btw the team themself did not do this!!! People that work at Twitchcon did that,](https://x.com/sopselinchen/status/2061135263108075908) |
| x | beffjezos | ^315 c38 | [Stephen Wolfram educating everyone @CIMCAI on computational irreducibility Wolfr](https://x.com/beffjezos/status/2060862470974267819) |
| radar | modinfo | ^315 c109 | [1-Bit Bonsai Image 4B Image Generation for Local Devices](https://prismml.com/news/bonsai-image-4b) |
| radar | Eridanus2 | ^296 c468 | [United Airlines 767 returns to Newark after Bluetooth name sparks alert](https://simpleflying.com/united-airlines-767-returns-newark-bluetooth-name-alert/) |
| x | teortaxesTex | ^240 c4 | [a very good universal reply, almost took it personally https://t.co/sWUmUBKQ6T](https://x.com/teortaxesTex/status/2061200788748132557) |
| x | SonaricDragon | ^236 c6 | [Lock in or lock out for sombr endings Red team asf as fuck: https://t.co/uwr7ztt](https://x.com/SonaricDragon/status/2060844307511140405) |
| radar | grappler | ^184 c51 | [Restartable Sequences](https://justine.lol/rseq/) |
| radar | mindcrime | ^174 c104 | ['Backrooms' Stuns with $81M Debut](https://variety.com/2026/film/box-office/backrooms-box-office-record-opening-weekend-obsession-jumps-star-wars-crumbles-1236763355/) |
| x | teortaxesTex | ^162 c10 | [three months ago, Americans made the world a permanently shittier place to live ](https://x.com/teortaxesTex/status/2061254646442692898) |
| x | mark_k | ^154 c42 | [Grok Imagine by @xai is now actually the best image-to-video model in the world.](https://x.com/mark_k/status/2061019472748564498) |
| radar | tambourine_man | ^147 c230 | [Meta launches Instagram, Facebook, and WhatsApp subscriptions](https://techcrunch.com/2026/05/27/meta-officially-launches-instagram-facebook-and-whatsapp-subscriptions-with-more-to-come-including-ai-plans/) |
| radar | mooreds | ^132 c103 | [It's Not Just X. It's Y](https://mail.cyberneticforests.com/its-not-just-data-its-post-training/) |
| radar | Dzheky | ^132 c64 | [Odysseus – self-hosted AI workspace](https://github.com/pewdiepie-archdaemon/odysseus) |
| radar | mooreds | ^125 c66 | [The Speed of Prototyping in the Age of AI](https://darylcecile.net/notes/speed-of-prototyping-age-of-ai) |
| x | VivekIntel | ^120 c0 | [Syscalls in C# — Red Team Tradecraft Beyond Win32 APIs 💀🔴 A deep dive into how o](https://x.com/VivekIntel/status/2061007010917925189) |
| radar | thcipriani | ^111 c106 | [Chuwi Minibook X: the netbook we deserve](https://tylercipriani.com/blog/2026/05/28/chuwi-minibook-x/) |
| x | VivekIntel | ^107 c0 | [Claude-BugHunter — Turn Claude Code into a Senior Bug Hunter & Red Team Operator](https://x.com/VivekIntel/status/2061063109662662856) |
| radar | hackerBanana | ^107 c40 | [ChatGPT for Google Sheets exfiltrates workbooks](https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration) |
| x | hwchase17 | ^104 c11 | [🧑‍⚖️Evaluating Deep Agents with LangSmith on AWS Great deep dive blog with our f](https://x.com/hwchase17/status/2061085058384150904) |
| x | VivekIntel | ^102 c0 | [Cryptex OSS — Open-Source LLM Red-Team Lab in Your Browser 💀🔥 A powerful browser](https://x.com/VivekIntel/status/2060643637709635694) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@zomato</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4799 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/zomato/status/2061145484274901120">View @zomato on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Thank you for showing that the red team always delivers ♥️🏆 #RCBvsGT”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Zomato ทวีตเชียร์ทีม RCB ชนะ GT ในคริกเก็ต ไม่มีเนื้อหาด้านเทคโนโลยีใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/zomato/status/2061145484274901120" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2385 · 💬 85</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2060618209733362132">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Amazon reportedly shut down an internal AI leaderboard after employees started using large amounts of AI tokens just to climb the rankings. The leaderboard, called KiroRank, tracked how much employees”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Amazon ปิด leaderboard ภายใน KiroRank หลังพนักงานใช้ AI agent รัน task ไม่จำเป็นเพื่อเพิ่ม token count ทำให้ต้นทุนพุ่งโดยไม่ได้ผลลัพธ์จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>วัด AI adoption ด้วย token volume เป็น metric ที่ผิด — วัดการใช้งาน ไม่ใช่คุณค่า และจูงใจให้เกิดความสูญเปล่าโดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้าทำ dashboard วัดการใช้ AI ภายใน ให้ track ผลลัพธ์จริง เช่น PR merged, bug resolved, เวลาที่ประหยัด — ไม่ใช่ token count ดิบ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2060618209733362132" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@F1BigData</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 450 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/F1BigData/status/2060798697982566640">View @F1BigData on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“LEASON: Never fully trust a red team”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@F1BigData โพสต์ประโยคสั้นๆ ว่า 'Never fully trust a red team' ไม่มีบริบทหรือข้อมูลรองรับ — account นี้เน้น F1 analytics ดังนั้น 'red team' น่าหมายถึง Ferrari ไม่ใช่ adversarial AI testing</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/F1BigData/status/2060798697982566640" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@teortaxesTex</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 386 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/teortaxesTex/status/2061250918595641773">View @teortaxesTex on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@m0d8ye what do you mean, Google has shipped tons of models”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>reply บรรทัดเดียวปกป้องว่า Google ส่ง model มาเยอะแล้ว — ไม่มีรายละเอียด ตัวเลข หรือบริบทใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/teortaxesTex/status/2061250918595641773" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@academy_dinda</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 373 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/academy_dinda/status/2061040774528352725">View @academy_dinda on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Btw in yesterday’s Final, the Red Team lost and the Blue team won the UCL Trophy💀 https://t.co/XxR9GLIG5M”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์รายงานผลการแข่งขัน UCL รอบชิงชนะเลิศ ทีมน้ำเงินชนะทีมแดง ไม่มีเนื้อหาด้านเทคโนโลยีหรืออุตสาหกรรม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/academy_dinda/status/2061040774528352725" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Musafirr_hu_yar</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 365 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Musafirr_hu_yar/status/2060800023236137239">View @Musafirr_hu_yar on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Blue team defeated red team https://t.co/BS6RG66nTb”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ระบุแค่ 'Blue team defeated red team' พร้อมลิงก์ ไม่มีรายละเอียด actor, tool, หรือผลลัพธ์ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Musafirr_hu_yar/status/2060800023236137239" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ToriTyson</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 352 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ToriTyson/status/2061193241584681268">View @ToriTyson on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Im crying on the plane! Thank you @jordybahl for giving us alumna something to believe in 🥹♥️🌽 Red Team what an incredible run!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แสดงความรู้สึกชื่นชม 'Red Team' และขอบคุณบุคคลชื่อ Jordy Bahl ในบริบทที่ดูเหมือนเป็นกีฬาหรือมหาวิทยาลัย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ToriTyson/status/2061193241584681268" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TimnasXtra</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 327 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TimnasXtra/status/2060693059361493027">View @TimnasXtra on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 White Team defeated Red Team 5-4 in Indonesia's internal training match earlier today. Jens Raven scored a hat-trick, while Mitch Baker netted a brace 🎯 📸 @TimnasIndonesia https://t.co/AAaXE18yk2”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีมชาติอินโดนีเซียจัดซ้อมภายใน White Team ชนะ Red Team 5-4 Jens Raven ทำแฮตทริก Mitch Baker ยิง 2 ประตู</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TimnasXtra/status/2060693059361493027" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
