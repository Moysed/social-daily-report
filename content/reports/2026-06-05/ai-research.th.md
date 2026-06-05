---
type: social-topic-report
date: '2026-06-05'
topic: ai-research
lang: th
pair: ai-research.en.md
generated_at: '2026-06-05T03:28:37+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- radar
- rss
- x
regions:
- global
post_count: 238
salience: 0.5
sentiment: mixed
confidence: 0.5
tags:
- ai-research
- open-models
- nemotron
- post-training
- inference-optimization
- agents
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2062515450425253888/img/ZYYAdfDVwXahZLOh.jpg
translated_by: claude-sonnet-4-6
---

# AI Research — 2026-06-05

## TL;DR
- NVIDIA ปล่อย Nemotron 3 Ultra บน Hugging Face — 550B พารามิเตอร์ทั้งหมด / 55B active, hybrid Mamba-2 MoE, context 1M token, อ้าง SOTA บน MMLU/code/long-context, ส่วนใหญ่ใช้ FP4 [56][49]
- On-policy distillation คือทิศทาง post-training สาย RL สำหรับ LLM ที่ถูกพูดถึงมากที่สุดในตอนนี้ — เหมาะกับ pipeline ขนาดใหญ่และ task model เล็ก [4][30]
- งานศึกษา self-improving agent (Adaptive Auto-Harness) รายงานว่าแม้แต่ agent ระดับ SOTA ที่ใช้ Opus ก็ล้มเหลวบน real-world task stream โดยมีรูปแบบ 'peak early then decline' [48]
- Huawei เผยแพร่ KVarN ซึ่งเป็น native vLLM backend สำหรับ KV-cache quantization เพื่อลดต้นทุน inference [32]
- การอ้าง 'AI research' หลายรายการที่ viral ยังไม่มีการยืนยัน — เช่น thread MIT ที่บอกว่า AI memory 'solved' แล้วโดยไม่มีแหล่งที่ตรวจสอบได้ [15] และโพสต์ประเภท bubble-burst [2][20]

## What happened
จากรายการที่จัดเรียงตาม engagement สัญญาณ research/model ที่เป็นเนื้อหาจริงมีน้อย NVIDIA ส่ง Nemotron 3 Ultra (550B total, 55B active, hybrid Mamba-2 MoE Transformer, context 1M, FP4) บน Hugging Face พร้อม SOTA ที่รายงานเองบน MMLU, code และ long-context [56][49] การอภิปรายด้าน post-training เน้นที่ on-policy distillation ในฐานะทิศทาง RL-for-LLM ที่กำลังเคลื่อนไหวอยู่ [4][30] ด้าน efficiency มี Huawei ปล่อย KVarN สำหรับ KV-cache quantization ใน vLLM [32] และงาน arXiv ศึกษาว่า transformer จำเป็นต้องมี QKV projection ครบทั้งสามหรือไม่ [35] ด้าน interpretability มีกลุ่มงานติดกัน ได้แก่ การอธิบาย subliminal-learning [11], Activation Oracles [22], CVPR talk เรื่อง neural geometry ของ vision model [45] และงาน protein mech-interp [43] สัญญาณต้านทาน: งาน Adaptive Auto-Harness พบว่า self-improving agent (รวมถึง Opus) เสื่อมประสิทธิภาพบน real task stream [48]

## Why it matters (reasoning)
ข้อเท็จจริงที่นำไปใช้จริงได้คือ base model open-weight ขนาดใหญ่ใหม่ (Nemotron 3 Ultra) และ post-training recipe ที่สุกขึ้น (on-policy distillation) FP4 + MoE sparsity [49][56] ลดต้นทุนการรัน model ใหญ่ แต่ 550B total ยังไกลเกินกว่าสตูดิโอเล็กจะ self-host ได้ ประโยชน์จริงอยู่ที่ variant ที่ distill หรือเล็กลงในอนาคต ซึ่งตรงกับสิ่งที่ on-policy distillation ทำได้ [4][30] ผลลัพธ์ agent-failure [48] เป็นคำเตือนที่มีประโยชน์ที่สุดที่นี่ — โต้แย้งตรงๆ กับเรื่องเล่า 'autonomous self-improving agent' [9][31] และชี้ว่าไม่ควร ship feature ที่พึ่งพา long-horizon self-improvement loop ส่วนใหญ่ของ feed คือ noise หรือ hype ที่ตรวจสอบไม่ได้ ([15] 'solved memory', [2][20] bubble claims, red-team meme thread) ดังนั้น benchmark claim อย่าง 'SOTA' ของ Nemotron [56] ควรมองเป็น vendor announcement จนกว่าจะมีการทดสอบอิสระ

## Possibility
มีแนวโน้มสูง: model ที่ distill มาจาก Nemotron หรือ FP4 model ขนาดเล็กจะใช้งาน self-host ได้ภายในไม่กี่เดือน เพราะทั้ง base และ distillation method กำลังวนเวียนอยู่อย่างแข็งขัน [4][49][56] เป็นไปได้: KV-cache quantization อย่าง KVarN [32] กลายเป็น lever มาตรฐานในการลดต้นทุน inference บน vLLM deployment เป็นไปได้แต่ยังไม่พิสูจน์: รูปแบบ 'peak-early-then-decline' ของ agent [48] ขยายผลในวงกว้าง ทำให้ autonomy ที่เชื่อถือได้ยังอยู่นอกเอื้อมในระยะใกล้ แม้จะมีกระแส self-improvement [9][31] ไม่น่าเป็นไปได้: การอ้าง 'AI memory solved' [15] จะยืนหยัดได้ตามที่กล่าวอ้าง — ไม่มีแหล่งอ้างอิงที่ตรวจสอบได้

## Org applicability — NDF DEV
1) อ่านหน้า Gaussian Point Splatting SIGGRAPH 2026 [21] สำหรับ XR/Unity asset และ rendering pipeline — effort ต่ำ ตรง lane ของ NDF DEV โดยตรง 2) ติดตาม Nemotron 3 Ultra ในแง่ variant เล็ก/distilled และ FP4 deployment มากกว่าการ self-host 550B [56][49] — effort ต่ำในการติดตาม แต่ effort/ต้นทุนสูงมากถ้าจะ deploy ตอนนี้ 3) ถ้า fine-tune task model สำหรับ edutech/in-game NPC ให้ดู on-policy distillation เป็น recipe ที่แนะนำในปัจจุบัน ก่อนยึดติดกับ SFT/RLHF เดิม [4][30] — effort ปานกลางในการประเมิน 4) เมื่อ self-host บน vLLM ให้ทดสอบ KV-cache quantization (KVarN) เพื่อลดต้นทุน inference [32] — effort ปานกลาง 5) อย่า build feature บน autonomous self-improving agent loop เลย [48] แสดงว่าเกิดการเสื่อมประสิทธิภาพแม้กับ Opus ข้าม: bubble-burst thread [2][20], red-team meme post [5][8][10], listicle 'learn AI' [3][19][28] และ claim 'solved memory' ที่ไม่มีการยืนยัน [15]

## Signals to Watch
- การทดสอบ benchmark อิสระสำหรับ claim MMLU/code/long-context ของ Nemotron 3 Ultra [56]
- ว่า on-policy distillation ผลิต model เล็กที่ deploy ได้จริง ไม่ใช่แค่ทฤษฎี pipeline [4][30]
- ผลติดตามจากงาน Adaptive Auto-Harness เรื่อง agent-degradation และ mitigation ที่เป็นไปได้ [48]
- KV-cache quantization (KVarN) ที่กลายเป็น inference cost lever เสถียรบน vLLM [32]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **anthropics/defending-code-reference-harness** — framework open-source ของ Anthropic สำหรับค้นหาช่องโหว่ด้วย AI | radar | <https://github.com/anthropics/defending-code-reference-harness> |
| **huawei-csl/KVarN** — KVarN: native vLLM backend สำหรับ KV-cache quantization โดย Huawei | radar | <https://github.com/huawei-csl/KVarN> |
| **alibaba/open-code-review** — Open Code Review – CLI tool สำหรับ code review ด้วย AI | radar | <https://github.com/alibaba/open-code-review> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | septisum | ^2996 c46 | [Just asked GPT-5.5-Pro a hard math problem and in the chain of thought I can see](https://x.com/septisum/status/2062535352410407323) |
| x | kushika_twt | ^1355 c129 | [Microsoft pulled the plug on Claude. Starbucks' AI can't count cups. Uber burned](https://x.com/kushika_twt/status/2062164836365332560) |
| x | TheAhmadOsman | ^1248 c26 | [Step-By-Step LLM Engineering Projects Roadmap - Build a tokenizer - Learn embedd](https://x.com/TheAhmadOsman/status/2062343535144436073) |
| x | srush_nlp | ^1102 c18 | [On-Policy Distillation is the most active new research direction being explored ](https://x.com/srush_nlp/status/2062359839783657816) |
| x | zephyr_z9 | ^647 c14 | [This is so fucking funny Some Chinese hackers have either infiltrated Ant's syst](https://x.com/zephyr_z9/status/2062546115543863704) |
| radar | coloneltcb | ^585 c259 | [VoidZero Is Joining Cloudflare](https://blog.cloudflare.com/voidzero-joins-cloudflare/) |
| radar | mooreds | ^524 c199 | [Ian's Secure Shoelace Knot](https://www.fieggen.com/shoelace/secureknot.htm) |
| x | nicoruas | ^473 c0 | [i'm crying he's so happy to end up on the red team https://t.co/2rM9gtr5UQ](https://x.com/nicoruas/status/2062515536865681796) |
| radar | meetpateltech | ^360 c474 | [When AI Builds Itself: Our progress toward recursive self-improvement](https://www.anthropic.com/institute/recursive-self-improvement) |
| x | bunniewiju | ^320 c0 | [WHY IS RED TEAM TRYNA PLAY MIND GAMES WITH THEIR MAKNAE IM CRYING 🎮we can finall](https://x.com/bunniewiju/status/2062511252853657826) |
| x | NeelNanda5 | ^318 c11 | [I had a lot of fun working on this paper - we found an elegant story for why sub](https://x.com/NeelNanda5/status/2062260199822639314) |
| x | Huangyu58589918 | ^312 c15 | [Starting as a Student Researcher at @GoogleDeepMind on June 8! I'll be in NYC th](https://x.com/Huangyu58589918/status/2062229610390053154) |
| radar | binyu | ^297 c96 | [Anthropic's open-source framework for AI-powered vulnerability discovery](https://github.com/anthropics/defending-code-reference-harness) |
| radar | mawise | ^263 c178 | [Retro-Tech Parenting](https://havenweb.org/2026/05/28/retro-tech.html) |
| x | jackcoder0 | ^262 c50 | [MIT just made every AI company's billion dollar bet look embarrassing. They solv](https://x.com/jackcoder0/status/2062233782548333047) |
| radar | buchodi | ^248 c209 | [Meta's ships facial recognition on smart glasses](https://www.buchodi.com/meta-glasses-facial-recognition/) |
| x | RickMcCracken | ^243 c15 | [Great Cardano SPO Call today - Notes for June 4th 1. Van Rossem Hard Fork Prepar](https://x.com/RickMcCracken/status/2062565547762467027) |
| x | tom_doerr | ^231 c2 | [Curated offensive security skills to turn Claude into a context-aware red team o](https://x.com/tom_doerr/status/2062139149432344674) |
| x | Tanaypawar27 | ^213 c29 | [Stop wasting hours trying to learn AI. 📘📚 I have already done it for you. With o](https://x.com/Tanaypawar27/status/2062497282293969027) |
| x | nicrypto | ^189 c28 | [Last year: "Embrace AI or your job is at risk." This year: "Please stop, you're ](https://x.com/nicrypto/status/2062067713825267787) |
| radar | ibobev | ^180 c66 | [Gaussian Point Splatting](https://momentsingraphics.de/Siggraph2026.html) |
| x | celestepoasts | ^162 c10 | [New research from @japhba and I! Activation Oracles are a pretty cool interpreta](https://x.com/celestepoasts/status/2062604291978985806) |
| x | teortaxesTex | ^158 c12 | [I view the concept of "ghost towns" as one of the most embarrassing Western inve](https://x.com/teortaxesTex/status/2062685913667207611) |
| x | vikktorrrre | ^150 c75 | [did you know AI is older than your forefathers? you obviously don't, neither did](https://x.com/vikktorrrre/status/2062183220939047127) |
| x | VivekIntel | ^149 c0 | [Havoc Framework: Modern Open-Source C2 for Red Teams 💀🔥 Havoc is a post-exploita](https://x.com/VivekIntel/status/2062233186252533786) |
| radar | tristanj | ^149 c59 | [SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P](https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation) |
| x | Hey_Aditii | ^145 c17 | [🤖 𝟮𝟵 𝗖𝗟𝗔𝗨𝗗𝗘 𝗦𝗛𝗢𝗥𝗧𝗖𝗨𝗧𝗦 🔖 𝗦𝗔𝗩𝗘 𝗧𝗛𝗜𝗦 𝗕𝗘𝗙𝗢𝗥𝗘 𝗬𝗢𝗨 𝗙𝗢𝗥𝗚𝗘𝗧 If you're using AI and not u](https://x.com/Hey_Aditii/status/2062036557377527810) |
| x | SaurabhDub28465 | ^131 c9 | [Stop wasting hours trying to learn AI. I have already done it for you. With one ](https://x.com/SaurabhDub28465/status/2062500175994830990) |
| x | lateinteraction | ^127 c2 | [is that why they call it a dissertation](https://x.com/lateinteraction/status/2062361599701065826) |
| x | srush_nlp | ^119 c1 | [Didn't get a change to include citations, but OPD (https://t.co/NPofF2A89p) Self](https://x.com/srush_nlp/status/2062360762803253465) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@septisum</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2996 · 💬 46</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/septisum/status/2062535352410407323">View @septisum on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Just asked GPT-5.5-Pro a hard math problem and in the chain of thought I can see it reading teenvogue”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>chain of thought ของ GPT-5.5-Pro อ้างอิง Teen Vogue ระหว่างแก้โจทย์คณิตศาสตร์ยาก แสดงว่าโมเดลดึงข้อมูล training ที่ไม่เกี่ยวข้องระหว่าง reasoning</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>reasoning model ดึงแหล่งข้อมูล training ที่ไม่เกี่ยวข้องได้โดยไม่แจ้ง คำตอบที่ดูมั่นใจอาจมาจาก source ห่วย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตรวจ chain of thought ของ reasoning model ก่อนเชื่อผล โดยเฉพาะงาน code หรือ logic ที่ต้องการความแม่นยำ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/septisum/status/2062535352410407323" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@kushika_twt</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1355 · 💬 129</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/kushika_twt/status/2062164836365332560">View @kushika_twt on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Microsoft pulled the plug on Claude. Starbucks’ AI can't count cups. Uber burned billions on AI with little to show for it. Amazon shut down its AI leaderboard. the AI bubble will burst any minute now”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทวีตยกตัวอย่าง AI ล้มเหลวที่ Microsoft, Starbucks, Uber, Amazon แล้วสรุปว่า AI bubble กำลังจะแตก — ไม่มีข้อมูลหรือแหล่งอ้างอิง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/kushika_twt/status/2062164836365332560" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheAhmadOsman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1248 · 💬 26</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheAhmadOsman/status/2062343535144436073">View @TheAhmadOsman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Step-By-Step LLM Engineering Projects Roadmap - Build a tokenizer - Learn embeddings - Implement RoPE / ALiBi - Hand-wire attention - Build MHA - Build a Transformer block - Train a mini-former - Comp”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์บน X แชร์ roadmap LLM engineering 30 หัวข้อ ตั้งแต่ tokenizer, embeddings, attention, KV cache, FlashAttention, RLHF, quantization, RAG ไปจนถึง tool-use agents พร้อมเรียกร้องให้ open-source ผลงาน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เส้นทางนี้ช่วยให้ทีมศึกษา LLM internals ที่อยู่เบื้องหลัง AI tools ที่สตูดิโอใช้อยู่ ตั้งแต่ speculative decoding ไปถึง eval harnesses และ red-team suite</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ปักหมุด roadmap นี้เป็น reference ภายใน แล้วแจกหัวข้อ sprint ละ 1 ให้สมาชิกที่ทำงานด้าน AI feature</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheAhmadOsman/status/2062343535144436073" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@srush_nlp</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1102 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/srush_nlp/status/2062359839783657816">View @srush_nlp on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“On-Policy Distillation is the most active new research direction being explored in RL for LLMs. Had the chance to discuss how it works with Dwarkesh and why it fits so nicely into large-scale pipeline”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Sasha Rush (Cornell NLP) ชี้ว่า On-Policy Distillation คือการฝึก student LLM จาก output ที่ teacher สร้างระหว่าง RL rollout จริงของ student เอง และเป็น research direction ที่ active ที่สุดใน RL for LLMs ตอนนี้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>รู้ว่า training technique ไหนกำลัง active ช่วยทีมประเมินได้ว่า foundation model ที่ใช้อยู่จะดีขึ้นยังไงและเร็วแค่ไหน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู Dwarkesh x Sasha Rush เพื่อเข้าใจ On-Policy Distillation ก่อนที่ technique นี้จะกลาย standard ใน model releases ที่ทีมใช้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/srush_nlp/status/2062359839783657816" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@zephyr_z9</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 647 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/zephyr_z9/status/2062546115543863704">View @zephyr_z9 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is so fucking funny Some Chinese hackers have either infiltrated Ant's systems or are part of the red team and are selling Mythos access 🤣🤣🤣🤣🤣🤣🤣”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์เย้ยเรื่องที่ยังไม่มีการยืนยัน ว่ามีแฮกเกอร์หรือ insider แอบขาย access ระบบ 'Mythos' ของ Ant Group</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/zephyr_z9/status/2062546115543863704" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nicoruas</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 473 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nicoruas/status/2062515536865681796">View @nicoruas on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“i’m crying he’s so happy to end up on the red team https://t.co/2rM9gtr5UQ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แสดงอารมณ์ต่อการที่ใครบางคนเข้าร่วม red team โดยไม่มีรายละเอียดทางเทคนิคใด ๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nicoruas/status/2062515536865681796" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bunniewiju</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 320 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bunniewiju/status/2062511252853657826">View @bunniewiju on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“WHY IS RED TEAM TRYNA PLAY MIND GAMES WITH THEIR MAKNAE IM CRYING 🎮we can finally see what maki can do 👑it’s def going in, it’d be weird if it didn’t 🐶can u guys keep it down… 🐱it’s in such an easy sp”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนด้อม K-pop/เกม แสดงปฏิกิริยาต่อ moment ในทีม ไม่มีเนื้อหาด้าน tech หรืออุตสาหกรรมใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bunniewiju/status/2062511252853657826" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NeelNanda5</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 318 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NeelNanda5/status/2062260199822639314">View @NeelNanda5 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I had a lot of fun working on this paper - we found an elegant story for why subliminal learning happens! A key intuition in interpretability is that basically every interesting phenomena in LLMs boil”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีม Neel Nanda ตีพิมพ์ paper พิสูจน์ว่า subliminal learning ใน LLM (การเรียนรู้พฤติกรรมที่ไม่ได้ตั้งใจ) อธิบายได้ด้วยการบวก steering vector ใน activation space</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Steering vector เป็น mechanism สากล — พฤติกรรม LLM ที่ไม่ต้องการใน feature ที่ embed AI สามารถตรวจและแก้ได้โดยไม่ต้อง retrain</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า LLM ใน product มีพฤติกรรมผิดปกติ ลอง steering vector analysis ก่อน — ไม่ต้อง fine-tune</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NeelNanda5/status/2062260199822639314" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
