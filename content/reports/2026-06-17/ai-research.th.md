---
type: social-topic-report
date: '2026-06-17'
topic: ai-research
lang: th
pair: ai-research.en.md
generated_at: '2026-06-17T15:32:11+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- radar
- rss
- x
regions:
- global
post_count: 204
salience: 0.6
sentiment: mixed
confidence: 0.5
tags:
- glm-5.2
- open-weights
- gemini
- benchmarks
- model-adoption
- interpretability
thumbnail: https://pbs.twimg.com/media/HK8INEZaEAAffC_.jpg
translated_by: claude-sonnet-4-6
---

# AI Research — 2026-06-17

## TL;DR
- GLM-5.2 ถูกรายงานว่าเป็น open-weights model อันดับหนึ่งบน Artificial Analysis's Intelligence Index โดยมีคะแนน GDPval-AA v2 ที่ 1524 [8][39][41]
- Google ติด tag 'Gemini 3.5 Pro coming soon' บน model card ของ Gemini 3.1 Pro — ยังไม่มี benchmark หลุด แต่สัญญาว่าจะ launch ภายในเดือนนี้ [1][10]
- การ self-host โมเดล SOTA ต้องการทรัพยากรสูง: มีแหล่งอ้างอิงระบุว่าต้องใช้ RAM ~400GB สำหรับ SOTA LLM ปี 2026 ซึ่งเป็นตัวชี้วัดสำคัญในการเปรียบเทียบ hosted API กับ local [24][7]
- มีงานวิจัยสองชิ้นที่เกี่ยวข้องกับ reproducibility: ข้อจำกัดด้าน state tracking ของ transformers [51] และ ICML 2026 paper ว่าด้วยสาเหตุที่ sparse-autoencoder features จำนวนมากตาย [29]
- หลายโพสต์อ้างว่า GLM-5.2 และ 'V4-Pro' ปิดช่องว่างด้าน theory-of-mind เทียบกับเวอร์ชันก่อน แต่หลักฐานเป็นเพียง X chatter ไม่ใช่ published evals [43][19][47]

## What happened
สัญญาณ AI research ของวันนี้เวียนอยู่รอบสองเหตุการณ์หลัก อย่างแรก GLM-5.2 (เชื่อมโยงกับ Zhipu/Tsinghua [25]) ขึ้นเป็นอันดับหนึ่ง open-weights บน Artificial Analysis รวมถึงตัวเลข GDPval-AA v2 ที่ 1524 [8][39][41] พร้อมคอมเมนต์ระบุว่า RL ของมันแข็งแกร่งที่สุดในบรรดา Chinese labs [11] อย่างที่สอง Google ดูเหมือนใกล้ปล่อย Gemini 3.5 Pro: พบ tag 'coming soon' บน model card ของ Gemini 3.1 Pro แม้ยังไม่มีข้อมูล performance หลุดออกมา และ launch ถูกสัญญาไว้ในเดือนนี้ [1][10] กระแสรอบข้างเปรียบเทียบ GLM-5.2, 'V4.1/V4-Pro,' Qwen 3.7 Max และ DeepSeek บน benchmark และ theory-of-mind prompts ซึ่งส่วนใหญ่เป็นการทดสอบส่วนตัวและการคาดเดาที่ยังไม่ได้รับการยืนยัน [19][43][47][40][58]

## Why it matters (reasoning)
สำหรับ studio ที่กำลังเลือกโมเดล สัญญาณที่จับต้องได้คือ GLM-5.2 นำ open weights บน public index [8][39] ซึ่งขยายตัวเลือกที่น่าเชื่อถือนอกเหนือจาก closed APIs แต่ต้นทุน self-hosting คือปัจจัยบล็อค: ~400GB RAM สำหรับโมเดล SOTA [24] หมายความว่าการรันในเครื่องตัวเองต้องอาศัย GPU infrastructure เช่นบริการที่กล่าวถึงใน [7] ดังนั้นสำหรับทีมส่วนใหญ่ hosted endpoint ยังคงถูกกว่าต่อ task สัญญาณ Gemini 3.5 Pro [1][10] บ่งชี้ว่าควรชะลอการผูกมัด Gemini 3.1 ในระดับ production จนกว่า evals และ pricing ของตัวต่อไปจะเผยแพร่ อีกชั้น: งานวิจัยมีนัยต่อการวางแผน reliability — จุดอ่อนด้าน state tracking ของ transformers [51] บ่งชี้ว่าจะเกิดความผิดพลาดในงาน multi-step agent/stateful (เกี่ยวข้องกับ game logic และ tutoring flow) ส่วน SAE dead-feature finding [29] เป็น interpretability plumbing ที่ยังไม่ใช่ input สำหรับผลิตภัณฑ์ในระยะใกล้ การเปรียบเทียบโมเดลส่วนใหญ่ที่พบในชุดนี้มาจาก X posts และการทดสอบส่วนตัว [19][43][47] ซึ่งยังไม่ถึงเกณฑ์สำหรับการตัดสินใจ adoption

## Possibility
**Likely:** Gemini 3.5 Pro จะ ship ภายในไม่กี่สัปดาห์ เมื่อดูจาก model-card tag และ deadline ที่ระบุไว้ [1][10] ความสามารถที่แท้จริงยังไม่รู้จนกว่า card/benchmark จะออก **Plausible:** ความนำของ GLM-5.2 ใน open weights บน index จะยืนได้ในระยะใกล้และคู่แข่ง (DeepSeek, Qwen) จะตอบสนอง เพราะ thread เดียวกันคาด DeepSeek จะตามหลังหรือต่ำกว่า GLM-5.2 [47][40] **Plausible:** GLM multimodal จะมาใน 5.x release ถัดไป [58] แต่ยังไม่พร้อมใช้ตอนนี้ **Unlikely (near-term):** การ self-host โมเดลระดับ SOTA จะถูกลงสำหรับ studio เล็ก เมื่อดู footprint ~400GB ที่อ้างถึง [24] ไม่มีแหล่งใดระบุตัวเลข probability ดังนั้นจึงไม่ได้ระบุไว้

## Org applicability — NDF DEV
1) รัน eval เล็กที่ reproduce ได้บน GLM-5.2 ผ่าน hosted endpoint (ไม่ใช่ local) สำหรับงาน coding-assist และ content/edutech text โดยเทียบคะแนนกับโมเดลปัจจุบันบน prompt ของตัวเอง — effort med [8][39][7] 2) อย่าผูกงาน production ใหม่กับ Gemini 3.1 Pro pricing/limits จนกว่า model card ของ Gemini 3.5 Pro จะออก แล้วค่อย test ใหม่ — effort low [1][10] 3) สำหรับ agentic/stateful feature (game NPC logic, multi-step tutoring) ให้เพิ่ม external state อย่างชัดเจนแทนการพึ่งพา context memory ของโมเดล ตามข้อจำกัด state-tracking — effort med [51] 4) สำหรับ product/marketing copy ใน edutech apps หลีกเลี่ยงการเน้น 'AI' เป็นจุดขายหลัก เมื่อดูข้อมูลที่บ่งชี้ว่าผู้บริโภคไม่ชอบ — effort low [5] **ข้าม:** self-hosting โมเดล SOTA บน hardware ตัวเอง (ต้นทุน) [24]; SAE/mech-interp papers [29][36][18][44] และ protein/binder และ smart-contract papers [48][49] (นอก scope ของ studio); ถือว่า theory-of-mind และ X head-to-head claims ยังไม่ถึงระดับตัดสินใจ [19][43][47]

## Signals to Watch
- ติดตาม official model card และ benchmark ของ Gemini 3.5 Pro — tag ปัจจุบันยังไม่มีข้อมูล performance [1][10]
- ติดตาม Artificial Analysis ว่า GLM-5.2 จะรักษาความนำใน open weights ได้นานแค่ไหนเมื่อ DeepSeek/Qwen ตอบสนอง [39][47]
- ติดตาม GLM multimodal/vision support ใน 5.x release ถัดไปก่อนพิจารณาใช้กับงาน image [58]
- ติดตามการถกเถียงด้าน alignment/eval เรื่อง sandbagging classification ซึ่งเกี่ยวกับความน่าเชื่อถือของ model self-reports ในการทดสอบ [54]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **rxi/microui** — MicroUI – A tiny, portable, immediate-mode UI library written in ANSI C | radar | <https://github.com/rxi/microui> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | pankajkumar_dev | ^942 c50 | [Gemini 3.5 Pro Leaks: Launch Is Getting Closer - Google has started hinting at G](https://x.com/pankajkumar_dev/status/2066879784458887545) |
| radar | Cider9986 | ^911 c476 | [GrapheneOS has been ported to Android 17](https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon) |
| x | jxmnop | ^667 c23 | [endlessly fascinating how a traditional machine learning background is basically](https://x.com/jxmnop/status/2067061000994795764) |
| x | LLMJunky | ^596 c48 | [I do not believe GPT 5.6 will receive the same level of scrutiny as Fable 5 for ](https://x.com/LLMJunky/status/2066606543164850671) |
| radar | thm | ^507 c259 | [Sixty percent of US consumers say 'AI' in brand messaging is a turnoff](https://wpvip.com/future-of-the-web-2026/) |
| radar | mrshu | ^497 c215 | [TIL: You can make HTTP requests without curl using Bash /dev/TCP](https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/) |
| x | abacusai | ^466 c25 | [🚨 Host Your Own Local LLM On The Abacus AI SuperComputer Stop being sad about Fa](https://x.com/abacusai/status/2066734555202248728) |
| radar | himata4113 | ^463 c251 | [GLM-5.2 is the new leading open weights model on Artificial Analysis](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index) |
| x | jxmnop | ^410 c41 | [There is a simple reason why Gemini is so much worse than GPT or Claude engineer](https://x.com/jxmnop/status/2067068156410278385) |
| x | haider1 | ^365 c13 | [gemini 3.5 pro seems close to release, given that it already mentioned in the ge](https://x.com/haider1/status/2066626801678311931) |
| x | teortaxesTex | ^327 c7 | [This is a really troublesome benchmark for open models yeah I think they have th](https://x.com/teortaxesTex/status/2067025557162697056) |
| radar | denysvitali | ^320 c78 | [Humiliating IIS servers for fun and jail time](https://mll.sh/humiliating-iis-servers-for-fun-and-jail-time/) |
| x | sanghaviharsh | ^315 c1 | [Strengthening Gujarat's industrial growth, two major projects were inaugurated a](https://x.com/sanghaviharsh/status/2067097673099087881) |
| radar | lutr | ^309 c127 | [Want your images back? Sure... That'll be $5!](https://www.lutr.dev/want-your-images-back-sure-that-ll-be-5-dollars) |
| radar | headalgorithm | ^302 c93 | [Hacker News but for Independent Blogs](https://bubbles.town/) |
| x | TweetsByAmaka | ^209 c45 | [This girl is a weapon fashioned against the red team… or maybe a mole from the b](https://x.com/TweetsByAmaka/status/2066824084478992572) |
| radar | alok-g | ^198 c105 | [Wolfram Language and Mathematica version 15](https://writings.stephenwolfram.com/2026/06/launching-version-15-of-wolfram-language-mathematica-built-in-useful-ai-lots-of-new-core-functionality/) |
| x | SuryaGanguli | ^179 c7 | [Our new paper lead by @vedanglad w/@AToliasLab "Letting the neural code speak...](https://x.com/SuryaGanguli/status/2066963477445689678) |
| x | teortaxesTex | ^177 c23 | [I think V4.1 Pro will score closely to GLM 5.1, probably noticeably higher both ](https://x.com/teortaxesTex/status/2067047818070565319) |
| x | MrUn1k0d3r | ^172 c2 | [We often talk about EDR evasion, but what about honeypot detection. Nothing new ](https://x.com/MrUn1k0d3r/status/2066932236545355821) |
| x | peterli34923561 | ^168 c1 | [$PLTR --- $PLTR management aggressively raised full-year 2026 revenue guidance f](https://x.com/peterli34923561/status/2066784248032534603) |
| x | VivekIntel | ^165 c1 | [🦅 Claude-OSINT: Give Claude 90+ Recon Capabilities and Turn It Into an OSINT Ope](https://x.com/VivekIntel/status/2066905731295838585) |
| radar | schappim | ^154 c76 | [RFC 10008: The new HTTP Query Method](https://www.rfc-editor.org/info/rfc10008/) |
| x | mehulmpt | ^149 c11 | [Memory required to run video game in 1980s: 4KB Memory required to run SOTA LLM ](https://x.com/mehulmpt/status/2066612276204109951) |
| x | teortaxesTex | ^143 c11 | [Zhipu is basically Tsinghua btw They might have the deepest political goodwill o](https://x.com/teortaxesTex/status/2067236996511068214) |
| x | teortaxesTex | ^133 c14 | [Fr though. Le Chaton Fat memes aside, Europeans have 2 choices. - begin deployme](https://x.com/teortaxesTex/status/2067034152042467432) |
| x | Sauers_ | ^132 c15 | [Does anyone want to give the creator of Le Chaton Fat a A100 or H100 to research](https://x.com/Sauers_/status/2066679416827097561) |
| radar | esychology | ^132 c33 | [Show HN: High-Res Neural Cellular Automata](https://cells2pixels.github.io/) |
| x | james_y_zou | ^125 c2 | [Sparse autoencoders (SAEs) are foundational to much of mechanistic interpretabil](https://x.com/james_y_zou/status/2066626705020891525) |
| x | teortaxesTex | ^121 c7 | [OK. how does this help India compete in AGI?](https://x.com/teortaxesTex/status/2067043767488479300) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@pankajkumar_dev</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 942 · 💬 50</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/pankajkumar_dev/status/2066879784458887545">View @pankajkumar_dev on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gemini 3.5 Pro Leaks: Launch Is Getting Closer - Google has started hinting at Gemini 3.5 Pro, with a &quot;3.5 Pro coming soon&quot; tag appearing on the Gemini 3.1 Pro model card. - Expect stronger vision, be”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Google ใส่ tag '3.5 Pro coming soon' บน model card ของ Gemini 3.1 Pro บ่งชี้ว่าจะได้ vision, multimodal reasoning, และ SVG/frontend generation ที่ดีขึ้น แต่ราคาสูงกว่า 3.1 Pro</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>SVG และ frontend generation ที่ดีขึ้นช่วยงาน UI prototyping และ e-learning asset โดยตรง ถ้า fix laziness ในงานยาวได้ จะช่วย code gen งานซับซ้อนได้จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">รอ release จริง แล้ว benchmark Gemini 3.5 Pro ด้าน SVG output และ long-context coding เทียบ tool ปัจจุบันก่อนตัดสินใจจ่าย API ราคาสูงขึ้น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/pankajkumar_dev/status/2066879784458887545" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jxmnop</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 667 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jxmnop/status/2067061000994795764">View @jxmnop on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“endlessly fascinating how a traditional machine learning background is basically not that helpful for modern AI. we use deep NNs and do SGD with one of two losses. most day-to-day work lies in abstrac”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา AI ชี้ว่างาน AI สมัยใหม่ไม่ใช่ ML ทฤษฎีแบบเดิม แต่คือการ compose pipeline ของ data, model, rules — pre-training/RL/post-training เป็นแค่ topology ต่างกันของสามสิ่งนี้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ช่วย reframe งาน AI integration ให้เป็นโจทย์ systems/pipeline engineering ที่ทีม dev มีทักษะอยู่แล้ว ไม่ต้องการพื้นหลัง ML เชิงลึก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตอน scope งาน AI features ให้มองเป็น data/model/rules pipeline design แทน อย่า over-hire หา ML specialist โดยไม่จำเป็น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jxmnop/status/2067061000994795764" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LLMJunky</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 596 · 💬 48</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LLMJunky/status/2066606543164850671">View @LLMJunky on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I do not believe GPT 5.6 will receive the same level of scrutiny as Fable 5 for a litany of reasons, and no, they're not all political. The primary one being the fact that I suspect the guardrails on ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@LLMJunky ชี้ว่า GPT มี guardrails แข็งกว่า Fable/Opus/Sonnet โดยอ้าง OpenAI bounty $25,000 ที่ยังไม่มีใครเคลมได้ และไม่มี universal jailbreak สำเร็จบน GPT 5.5 ขณะที่ Fable กับ Opus 4.x ถูก liberate ตั้งแต่วันแรก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>สำหรับ LLM ที่ user เข้าถึงโดยตรง (e-learning, XR) ความแข็งแกร่งของ guardrails คือความเสี่ยงด้าน content moderation จริงๆ ไม่ใช่แค่ตัวเลข benchmark</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตอน evaluate LLM provider สำหรับ user-facing feature ให้เพิ่ม guardrail track record เป็น criterion อย่างเป็นทางการ ไม่ใช่แค่ดู capability score</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LLMJunky/status/2066606543164850671" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@abacusai</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 466 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/abacusai/status/2066734555202248728">View @abacusai on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 Host Your Own Local LLM On The Abacus AI SuperComputer Stop being sad about Fable and control your destiny by hosting your own LLM - host open source LLMs like Qwen and Gemma - create chat bots or a”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Abacus AI เปิดตัว SuperComputer ให้ host open-source LLMs (Qwen, Gemma) เป็น always-on API หรือ chatbot หลังจาก Anthropic ยกเลิก Fable</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การ host LLM เองบน managed compute ลด dependency กับ third-party model — ป้องกันงานสะดุดเมื่อ model ถูกยกเลิก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลองใช้ Abacus AI SuperComputer run LLM สำหรับ NPC dialogue, e-learning chatbot, หรือ internal tools โดยไม่ต้องพึ่ง external API</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/abacusai/status/2066734555202248728" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jxmnop</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 410 · 💬 41</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jxmnop/status/2067068156410278385">View @jxmnop on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“There is a simple reason why Gemini is so much worse than GPT or Claude engineers at OpenAI or Ant can read incoming user queries. all the data is visible but at Google there are tons of privacy restr”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ X รายหนึ่งตั้งสมมติฐานว่า Gemini ด้อยกว่า GPT และ Claude เพราะ Google ล็อก privacy เข้มจน engineer ไม่สามารถดู user query จริงได้ ทำให้พัฒนา model แบบไม่เห็น real-world data</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jxmnop/status/2067068156410278385" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@haider1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 365 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/haider1/status/2066626801678311931">View @haider1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“gemini 3.5 pro seems close to release, given that it already mentioned in the gemini 3.1 pro model card but i'm still curious because google promised it this month, so, strangely, there are no leaks y”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Gemini 3.5 Pro ใกล้ออกแล้ว — ถูก cite ใน model card ของ 3.1 Pro และ Google บอกว่าจะออกเดือนนี้ แต่ยังไม่มี leak เลย ต่างจาก release ก่อนหน้าที่มีข่าวล่วงหน้า 1-2 สัปดาห์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้า Gemini 3.5 Pro ออกเดือนนี้ cost/capability benchmark ที่ทีมใช้เลือก model สำหรับ AI integration จะต้องประเมินใหม่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">รอดู release และ pricing ของ Gemini 3.5 Pro ก่อนตัดสินใจ model tier สำหรับ AI feature ที่กำลังทำอยู่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/haider1/status/2066626801678311931" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@teortaxesTex</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 327 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/teortaxesTex/status/2067025557162697056">View @teortaxesTex on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is a really troublesome benchmark for open models yeah I think they have the best RL in China now, hard to admit but true GLM 5.2 also has… cheek. it even has COPE CAPACITY AGI at home? https://t”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>GLM 5.2 จาก Zhipu AI ทำคะแนนสูงในเกณฑ์วัดที่ยากสำหรับ open model — ผู้เขียนระบุว่าจีนนำหน้าด้าน RL training ตอนนี้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>GLM 5.2 เป็น open model ที่แข็งพอจะทดสอบเทียบกับ API ที่จ่ายเงินอยู่ โดยเฉพาะงาน inference</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ GLM 5.2 กับ inference task ที่ใช้อยู่ เปรียบคุณภาพและต้นทุนกับ paid model ปัจจุบัน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/teortaxesTex/status/2067025557162697056" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sanghaviharsh</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 315 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sanghaviharsh/status/2067097673099087881">View @sanghaviharsh on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Strengthening Gujarat’s industrial growth, two major projects were inaugurated and launched in the presence of Chief Minister Shri @Bhupendrapbjp Ji ▪️ Groundbreaking of Hitachi Energy’s new Power Tra”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>มุขมนตรีรัฐ Gujarat เปิดโรงงาน Power Transformer ของ Hitachi Energy (₹2,000 crore) และโรงงาน CPVC Resin ของ Lubrizol/Grasim ภายใต้นโยบาย Make in India</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sanghaviharsh/status/2067097673099087881" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
