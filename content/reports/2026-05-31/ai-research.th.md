---
type: social-topic-report
date: '2026-05-31'
topic: ai-research
lang: th
pair: ai-research.en.md
generated_at: '2026-05-31T16:11:42+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- radar
- x
regions:
- global
post_count: 152
salience: 0.3
sentiment: mixed
confidence: 0.5
tags:
- ai-evaluation
- benchmarks
- governance
- retrieval
- image-to-video
- agents
thumbnail: https://pbs.twimg.com/media/HJhS2KkWYAUErj_.jpg
translated_by: claude-sonnet-4-6
---

# AI Research — 2026-05-31

## TL;DR
- Amazon ปิด leaderboard ภายใน 'KiroRank' หลังพนักงานเผา token เพื่อปีนอันดับ; ผู้บริหารสื่อสารชัดว่า 'อย่าใช้ AI เพื่อใช้ AI' [1][5][6]
- Grok Imagine Video 1.5 Preview ขึ้น #1 image-to-video บน Arena AI leaderboard นำหน้า Seedance 2.0 และ Veo 3.1 [28]
- ColBERTv2 ทะลุ 20M downloads/เดือน ทั้งที่เป็น model ตั้งแต่ Oct-2021; ผู้เขียนแนะให้ migrate ไป late-interaction ColBERT รุ่นใหม่ [32]
- นักปฏิบัติบ่นว่า public eval benchmarks สำหรับ coding agents 'เล็กเกินไป' และ benchmark บางตัวใน model card ไม่แสดงความก้าวหน้า [59][47]
- สัญญาณ AI research จริงๆ วันนี้บางมาก — feed เต็มไปด้วยสัญญาณรบกวนจาก 'red team' สายกีฬาและ offensive-security tooling ไม่ใช่ paper หรือ eval suite [2][8][11][12][30][56]

## What happened
รายการที่ถูก engage สูงสุดส่วนใหญ่ไม่ตรงกับ AI research: คำว่า 'red team' อ้างถึงฟุตบอล/กีฬาเป็นหลัก [2][8][11][12][16][44] และกลุ่ม security post ครอบคลุม offensive pentest tooling กับ XRPL AI red-team effort [17][26][30][31][34][50][51][56] ไม่ใช่ model evaluation สำหรับ signal จริงด้าน model/eval: Amazon ยุติ internal leaderboard 'KiroRank' หลังพนักงานพองตัวเลข token เพื่อปีนอันดับ ผู้บริหารเตือนไม่ให้ใช้ AI เพื่อประโยชน์ของมันเอง [1][5][6] Grok Imagine Video 1.5 Preview ขึ้น #1 image-to-video บน Arena AI leaderboard เหนือ Seedance 2.0 และ Veo 3.1 [28] หมายเหตุด้าน retrieval ชี้ว่า ColBERTv2 (Oct 2021) มี 20M monthly downloads และเร่งให้ migrate ไป late-interaction model รุ่นใหม่กว่า [32] LangChain เปิดตัว GEPA integration สำหรับ optimizing chains [22] และมี write-up จาก AWS/LangSmith เรื่องการ evaluate long-horizon 'deep' agents [60]

## Why it matters (reasoning)
theme หลักคือ governance ไม่ใช่ capability: ความล้มเหลวของ leaderboard ของ Amazon [1][5][6] แสดงให้เห็นว่าการวัด AI adoption ด้วยปริมาณการใช้งานก่อให้เกิดความสูญเปล่า เพราะ incentive ตอบแทนการเผา token ไม่ใช่ผลลัพธ์ สำหรับ studio ข้อนี้ชี้ว่าควรวัดผลงานที่ ship ออกไป ไม่ใช่กิจกรรมการใช้เครื่องมือ ด้าน capability ข้อมูลที่ตรวจสอบได้และเกี่ยวข้องกับการนำไปใช้มีเพียง leaderboard ranking [28] และการเตือนเรื่อง dependency ที่ล้าสมัย [32] — มีประโยชน์แต่แคบ คำบ่นซ้ำๆ จากนักปฏิบัติว่า coding-agent benchmarks เล็กเกินไปและ metric บางตัวใน model card หยุดนิ่ง [47][59] หมายความว่าตัวเลขที่เผยแพร่ไม่ควรใช้แทน workload จริง; internal eval สำคัญกว่าก่อนนำ model ไปใช้ secondary: ความนิยมของ retrieval model ที่เก่าหลายปี [32] บ่งชี้ว่าทีมต่างๆ ดูแล AI dependency น้อยเกินไป ซึ่งเป็นความเสี่ยงด้านความเชื่อถือได้และคุณภาพที่แฝงอยู่ใน RAG pipeline

## Possibility
Likely: องค์กรอื่นจะเดินตาม Amazon โดยถอยจาก usage-based metrics มาสู่ outcome metrics เพราะ cost framing [5][6] Plausible: อันดับ image-to-video leaderboard จะวนเปลี่ยนทุกเดือน ดังนั้นสถานะ #1 [28] ไม่ใช่สัญญาณการนำไปใช้ที่ยั่งยืน Plausible: แรงกดดันให้มี coding-agent eval suite ที่ใหญ่ขึ้นและเป็น public จะเพิ่มขึ้นเมื่อนักปฏิบัติยังคงบ่นต่อไป [59] Unlikely (จาก feed นี้): จะมี arXiv paper หรือ open eval suite ที่ reproduce ได้เกิดขึ้น — แทบไม่มีเลย ดังนั้นความเชื่อมั่นในการอ้างแนวโน้ม research อยู่ในระดับต่ำ

## Org applicability — NDF DEV
1) นำ outcome-based metrics มาใช้วัด AI ภายในองค์กร ไม่ใช่ token/usage leaderboard — หลีกเลี่ยงความผิดพลาดของ Amazon (low effort) [1][5][6] 2) ถ้าใช้ ColBERT/RAG ในฟีเจอร์ edutech หรือ search ให้ audit หา ColBERTv2 ที่ล้าสมัยและทดสอบ late-interaction model รุ่นใหม่ก่อน ship (med effort) [32] 3) ก่อนนำ model ไปใช้โดยอิง published benchmarks ให้สร้าง internal eval เล็กๆ บน Unity/XR/edutech task จริงของตัวเอง — public benchmarks ไม่น่าเชื่อถือตามนักปฏิบัติ (med effort) [47][59] 4) ถ้าประเมิน multi-step agent features ให้ดู LangSmith/AWS deep-agent eval approach และ GEPA chain-optimization PR (low effort, evaluation only) [60][22] 5) สำหรับการทดลอง image-to-video asset อาจลอง Grok Imagine แต่ให้ถือ ranking #1 เป็นแค่ snapshot ไม่ใช่เหตุผลในการจัดซื้อ (low effort) [28] ข้าม: post 'red team' สายฟุตบอล [2][8][11][12][16][44] และ offensive-security pentest thread [30][51][56] — ไม่เกี่ยวกับการนำ model/method ไปใช้

## Signals to Watch
- องค์กรต่างๆ จะเผยแพร่ outcome-based AI metrics หลัง Amazon ปิด leaderboard หรือไม่ [5]
- Arena image-to-video rankings เดือนหน้าว่า Grok Imagine ยังรักษา #1 ไว้ได้หรือเปล่า [28]
- การนำ late-interaction ColBERT รุ่นใหม่มาใช้แทน legacy v2 [32]
- public coding-agent eval suite ที่ใหญ่ขึ้นจะตอบสนองต่อการบ่นเรื่อง 'benchmarks เล็กเกินไป' หรือไม่ [59]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Pirat_Nation | ^2389 c85 | [Amazon reportedly shut down an internal AI leaderboard after employees started u](https://x.com/Pirat_Nation/status/2060618209733362132) |
| x | HuskerCPF | ^900 c6 | [The Red Team is rollin' and so is the work at Bowlin. The state-of-the-art Hella](https://x.com/HuskerCPF/status/2060414805484208290) |
| radar | aaronbrethorst | ^750 c444 | [Domain expertise has always been the real moat](https://www.brethorsting.com/blog/2026/05/domain-expertise-has-always-been-the-real-moat/) |
| x | F1BigData | ^450 c1 | [LEASON: Never fully trust a red team](https://x.com/F1BigData/status/2060798697982566640) |
| x | interesting_aIl | ^450 c35 | [Amazon has axed their internal AI leaderboard as costs have skyrocketed "Please ](https://x.com/interesting_aIl/status/2060444204556320949) |
| x | CodeByNZ | ^442 c8 | [Bad week for AI. &gt; Amazon scrapped its AI leaderboard after costs spiraled &g](https://x.com/CodeByNZ/status/2060408820111691833) |
| x | teortaxesTex | ^406 c27 | [In the last 12-18 months, a divergence has began among the global cognitive elit](https://x.com/teortaxesTex/status/2060876931927507139) |
| x | Musafirr_hu_yar | ^365 c21 | [Blue team defeated red team https://t.co/BS6RG66nTb](https://x.com/Musafirr_hu_yar/status/2060800023236137239) |
| radar | aleda145 | ^347 c40 | [Shantell Sans (2023)](https://shantellsans.com/process) |
| radar | k1m | ^337 c135 | [The Website Specification](https://specification.website/) |
| x | academy_dinda | ^332 c8 | [Btw in yesterday's Final, the Red Team lost and the Blue team won the UCL Trophy](https://x.com/academy_dinda/status/2061040774528352725) |
| x | TimnasXtra | ^322 c7 | [🚨 White Team defeated Red Team 5-4 in Indonesia's internal training match earlie](https://x.com/TimnasXtra/status/2060693059361493027) |
| x | beffjezos | ^299 c36 | [Stephen Wolfram educating everyone @CIMCAI on computational irreducibility Wolfr](https://x.com/beffjezos/status/2060862470974267819) |
| radar | ksec | ^289 c130 | [The AV2 Video Standard Has Released (Final v1.0 Specification)](https://av2.aomedia.org) |
| x | teortaxesTex | ^232 c21 | [Where the fck are Indian brains meant to move to? Sarvam? It's like 50 people. E](https://x.com/teortaxesTex/status/2060839226166374464) |
| x | SonaricDragon | ^228 c6 | [Lock in or lock out for sombr endings Red team asf as fuck: https://t.co/uwr7ztt](https://x.com/SonaricDragon/status/2060844307511140405) |
| x | msvadari | ^228 c13 | [We're two months into our AI red team effort for the XRP Ledger. Here's a real l](https://x.com/msvadari/status/2060413883571970142) |
| radar | zeristor | ^191 c93 | [London's Free Roof Terraces](https://diamondgeezer.blogspot.com/2026/05/londons-free-roof-terraces.html) |
| x | MIT_CSAIL | ^190 c4 | ["Anyone who has lost track of time when using a computer knows the propensity to](https://x.com/MIT_CSAIL/status/2060753160566706188) |
| radar | Muhammad523 | ^145 c17 | [Mechanical Pencil: An illustrated celebration of the engineering around us](https://mechanical-pencil.com/) |
| radar | HypnoticOcelot | ^144 c77 | [Cloudflare Turnstile requiring fingerprintable WebGL](https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting) |
| x | hwchase17 | ^128 c13 | [LangChain🤝GEPA shout out to @bryonkuchML for contributing a PR to the GEPA repo ](https://x.com/hwchase17/status/2060732843282850276) |
| x | teortaxesTex | ^120 c6 | [Dario is probably sweating from spicy Italian food, if at all. he's just closed ](https://x.com/teortaxesTex/status/2060832083140915652) |
| x | teortaxesTex | ^117 c7 | [whining about steel and shipment dates sounds so quaint now, after the absolute ](https://x.com/teortaxesTex/status/2060840118001291757) |
| radar | birdculture | ^112 c60 | [I Put a Datacenter GPU in My Gaming PC for £200](https://blog.tymscar.com/posts/v100localllm/) |
| x | ja_akinyele | ^111 c4 | [Major shoutout to the AI Red team at @RippleXDev and the engineers helping secur](https://x.com/ja_akinyele/status/2060462435279208923) |
| x | teortaxesTex | ^111 c11 | [&gt; - it costs $2-4B to train a current gen model I'd like to see the mafs on t](https://x.com/teortaxesTex/status/2060845526845653387) |
| x | mark_k | ^109 c36 | [Grok Imagine by @xai is now actually the best image-to-video model in the world.](https://x.com/mark_k/status/2061019472748564498) |
| x | teortaxesTex | ^108 c4 | [Cluster A LLM psychosis: "gwahaha my 11th Claude-MAX-20X sub will surely Ratatou](https://x.com/teortaxesTex/status/2060899720378163548) |
| x | VivekIntel | ^105 c2 | [AI-Powered Red Team — 28 Specialized Agents for Offensive Security 🤖🔥 Turn Claud](https://x.com/VivekIntel/status/2060900694622937345) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2389 · 💬 85</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2060618209733362132">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Amazon reportedly shut down an internal AI leaderboard after employees started using large amounts of AI tokens just to climb the rankings. The leaderboard, called KiroRank, tracked how much employees”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Amazon ปิด leaderboard ภายใน KiroRank หลังพนักงานรัน AI agents กับงานที่ไม่จำเป็นเพื่อเพิ่ม token count ส่งผลให้ค่าใช้จ่ายพุ่งโดยไม่เกิด value จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>วัด AI adoption ด้วย token volume ดึงแรงจูงใจผิดทาง — ต้องวัดจาก output จริง (tasks ที่เสร็จ, เวลาที่ประหยัด) ไม่ใช่ปริมาณการใช้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า studio วัด AI adoption ภายใน ให้นิยาม success ด้วย output จริง เช่น PRs, bugs, หรือชั่วโมงที่ประหยัดได้ ไม่ใช่จำนวน token หรือ API calls</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2060618209733362132" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@HuskerCPF</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 900 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/HuskerCPF/status/2060414805484208290">View @HuskerCPF on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Red Team is rollin' and so is the work at Bowlin. The state-of-the-art Hellas turf installation is officially underway for @HuskerSoftball. 🚧🥎 https://t.co/W8IcEoTVmk”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>บัญชี Nebraska athletics รายงานว่ากำลังติดตั้งสนามหญ้าเทียม Hellas ใหม่ให้กับทีม Husker Softball</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/HuskerCPF/status/2060414805484208290" target="_blank" rel="noopener">เปิดบน x →</a>
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
      <dd>@F1BigData โพสต์ประโยคเดียวสะกดผิด 'LEASON: Never fully trust a red team' โดยไม่มี context หรือข้อมูลใดเพิ่มเติม</dd>
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
    <span class="ndf-author">@interesting_aIl</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 450 · 💬 35</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/interesting_aIl/status/2060444204556320949">View @interesting_aIl on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Amazon has axed their internal AI leaderboard as costs have skyrocketed “Please don’t use AI for the sake of using AI” https://t.co/A6vi15JkQY”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Amazon ปิด internal AI leaderboard หลัง cost พุ่ง พร้อมออก directive ให้ทีมหยุดใช้ AI โดยไม่มีเหตุผลทางธุรกิจที่ชัดเจน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ใช้ AI เพราะ 'มีให้ใช้' โดยไม่มี outcome วัดผล ทำให้ cost ควบคุมไม่ได้ — แม้แต่ Amazon ระดับ scale ยังโดน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทุก AI feature ที่ studio จะสร้าง ให้กำหนด cost ceiling และ success metric ก่อน build ไม่ใช่รอดูบิล</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/interesting_aIl/status/2060444204556320949" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CodeByNZ</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 442 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CodeByNZ/status/2060408820111691833">View @CodeByNZ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Bad week for AI. &amp;gt; Amazon scrapped its AI leaderboard after costs spiraled &amp;gt; Uber burned billions chasing AI ROI &amp;gt; Starbucks’ AI lost a fight against coffee cups HUMANITY LIVES ANOTHER WEEK. ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ viral รวม 3 ความล้มเหลวของ AI ในสัปดาห์เดียว: Amazon ปิด AI leaderboard, Uber ขาดทุนจาก AI, Starbucks' AI ทำงานพื้นฐานไม่ผ่าน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CodeByNZ/status/2060408820111691833" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@teortaxesTex</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 406 · 💬 27</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/teortaxesTex/status/2060876931927507139">View @teortaxesTex on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“In the last 12-18 months, a divergence has began among the global cognitive elite; both, I fear, have passed their respective point of no return. Group A can no longer be productive without AI. Group ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิจารณ์ชี้ว่า knowledge workers แบ่งเป็นสองกลุ่มถาวรใน 18 เดือนที่ผ่านมา: กลุ่มที่พึ่ง AI จนขาดไม่ได้ กับกลุ่มที่ปฏิเสธ AI และกำลังตกหลัง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/teortaxesTex/status/2060876931927507139" target="_blank" rel="noopener">เปิดบน x →</a>
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
      <dd>โพสต์ระบุแค่ 'Blue team defeated red team' พร้อมลิงก์ ไม่มีรายละเอียดเครื่องมือ ผลการวิจัย หรือเหตุการณ์ใดๆ</dd>
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
    <span class="ndf-author">@academy_dinda</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 332 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/academy_dinda/status/2061040774528352725">View @academy_dinda on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Btw in yesterday’s Final, the Red Team lost and the Blue team won the UCL Trophy💀 https://t.co/XxR9GLIG5M”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผลฟุตบอล UCL รอบชิงชนะเลิศ: ทีมสีน้ำเงินชนะทีมสีแดงคว้าแชมป์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/academy_dinda/status/2061040774528352725" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
