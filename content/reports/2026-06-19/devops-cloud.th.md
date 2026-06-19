---
type: social-topic-report
date: '2026-06-19'
topic: devops-cloud
lang: th
pair: devops-cloud.en.md
generated_at: '2026-06-19T03:41:49+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- x
regions:
- global
post_count: 215
salience: 0.6
sentiment: mixed
confidence: 0.55
tags:
- vercel
- supabase
- observability
- cloud-cost
- ci-cd
- cloudflare
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2067216339781955584/img/4mEk1DIO42vji-6Q.jpg
translated_by: claude-sonnet-4-6
---

# DevOps & Cloud — 2026-06-19

## TL;DR
- Vercel Ship ครองวันนี้: เปิดตัว agent framework 'eve' [1][12], 'Bring Your Own Cloud' สำหรับรัน Vercel Compute ในบัญชี AWS ของตัวเอง [18], Vercel Connect สำหรับ short-lived scoped tokens [19], และ enterprise tier พร้อม identity/access/audit [46]
- Supabase แตะ 10 ล้าน developer แล้ว โดย 3 ล้านคนเพิ่งเข้ามาใน 3 เดือน [13][40] — สัญญาณดีสำหรับ Postgres backend ของ studio
- กระแส observability ชัดเจนว่า 'instrument ตั้งแต่วันแรก ไม่ใช่หลังเกิด incident' [26][34][60]; มีผู้ใช้รายหนึ่งลด log volume ใน production ลงราว 50% ด้วยการให้ Claude Code ชี้ไปที่ Grafana Cloud CLI [35]
- Cloudflare เปิด Agents SDK เป็น runtime และส่ง Cloudflare One agent skills แต่ก็โดน Corey Quinn เปิด bug-report thread สาธารณะ [15][41][43]
- ผลสำรวจจาก CTO/CIO/CSO กว่า 300 คน พบ 93% กังวลเรื่อง vibe-coded apps ที่ไม่รู้จักในองค์กรตัวเอง [52] — ตรงกับความเสี่ยงที่ Vercel Passport [18] เล็งแก้

## What happened
engagement ส่วนใหญ่มาจากงาน Vercel Ship. Vercel ปล่อย 'eve' ซึ่งเป็น agent framework ที่ถูกอธิบายว่า 'เหมือน Next.js แต่สำหรับ agents' [1] พร้อมกับ Agent Stack (AI SDK, AI Gateway, Workflow SDK, Sandbox, Chat SDK, Vercel Connect) [12]. นอกจากเรื่อง agents ยังมี 'Bring Your Own Cloud' สำหรับรัน Vercel Compute ในบัญชี AWS ของลูกค้า [18], Vercel Connect ที่ออก short-lived precisely-scoped tokens สำหรับเข้าถึงข้อมูลภายนอก [19], Vercel Passport สำหรับควบคุม shadow/vibe-coded apps [18], และ enterprise tier ที่เพิ่ม identity, access และ audit [46]. นักวิจารณ์ตั้งข้อสังเกตว่า eve ผูกกับ Vercel เท่านั้นและต้องเดิมพันกับ stack ของพวกเขาเต็มๆ [10] พร้อมกับเสียงวิจารณ์ที่คมกว่านั้นต่อ launch นี้ [7]

## Why it matters (reasoning)
สำหรับเป้าด้าน reliability และ cost ของ studio, release Vercel ที่เกี่ยวข้องจริงๆ ไม่ใช่ eve แต่คือ BYOC [18] กับ Connect [19]. BYOC อาจย้ายค่า compute และ egress ไปอยู่ในบัญชี AWS ของ studio เอง ทำให้มองเห็น cost และควบคุม data residency ได้ ซึ่ง Vercel platform มาตรฐานซ่อนสิ่งเหล่านี้ไว้ — แม้ pricing และ operational overhead ยังไม่เปิดเผย. Short-lived scoped tokens ของ Connect ลดความเสี่ยงจากการเปิด long-lived secrets บน production integrations [19]. กระแส observability [26][34][60] ยืนยันแนวปฏิบัติที่ชัดเจน: ใส่ instrumentation ใน Next.js + Supabase ก่อนเกิด incident ถูกกว่าต้องสร้างใหม่ตอนวิกฤต ซึ่งตรงกับเป้าลด 3am pages โดยตรง. ตัวอย่างการลด log volume ด้วย Grafana CLI [35] แสดงว่า log volume ซึ่งเป็น bill line ตรงๆ ของ runtime — ลดได้จริง. การเติบโตของ Supabase [13][40] ลดความเสี่ยงจากการพึ่งพา. สัญญาณตรงข้ามคือ platform lock-in: eve และส่วนใหญ่ของ agent stack รันได้เฉพาะบน Vercel [10], และ Cloudflare โดยร้องเรียนเรื่อง reliability ต่อสาธารณะ [43] ดังนั้น การพึ่งพา vendor เดียวมีความเสี่ยงจริง

## Possibility
แนวโน้มสูง: Vercel ยังขยาย enterprise และ BYOC ต่อเนื่อง จากปริมาณ Ship announcements ที่มุ่งไปที่องค์กรขนาดใหญ่ [18][46]. เป็นไปได้: BYOC กลายเป็น lever จริงด้าน cost และ compliance สำหรับ studio ที่ค่า runtime เริ่มสูง แต่ต้องดูก่อนว่า pricing และ setup overhead สมเหตุสมผลหรือเปล่า — ยังไม่มีข้อมูลทั้งคู่ [18]. เป็นไปได้: ความกังวล 93% ของ CTO เรื่อง vibe-coded apps [52] ดัน demand ให้ governance tooling อย่าง Vercel Passport [18] และ scoped-token access [19]. เป็นไปได้: lock-in concerns [7][10] ชะลอการ adopt eve โดยเฉพาะในทีมที่ต้องการ portability. ไม่มี source ใดให้ตัวเลขความน่าจะเป็นนอกจากตัวเลขสำรวจ 93% [52]

## Org applicability — NDF DEV
1) ใส่ day-1 observability ใน production Next.js + Supabase apps — วาง dashboards, error tracking, และ alert thresholds ไว้ก่อนเกิด incident [26][34][60] (effort: med; ตรงเป้าลด 3am pages). 2) ทดลอง Grafana Cloud CLI + Claude Code วิเคราะห์ log เพื่อหาและตัด noisy/redundant production logs [35] (effort: low; ลด runtime bill โดยตรง). 3) ประเมิน Vercel BYOC เมื่อ/ถ้า monthly runtime bills โตพอที่จะคุ้มกับการย้าย compute เข้าบัญชี AWS ของ studio [18] (effort: high; ทำ cost comparison ก่อนตัดสินใจ). 4) ย้าย external-integration secrets ไปใช้ short-lived scoped tokens ผ่าน Vercel Connect ในงานใหม่ [19] (effort: low-med; security hardening). 5) ถือว่า Supabase ยังเป็นตัวเลือก Postgres ที่ปลอดภัยจากขนาด ecosystem [13][40] — ไม่ต้องทำอะไร แค่มั่นใจได้. ข้ามก่อน: eve และ agent stack ทั้งชุด [1][5][12] ซึ่ง Vercel-only [10] และตอบโจทย์การสร้าง agents ไม่ใช่ reliability/cost — กลับมาดูเมื่อโปรเจกต์ client ต้องการ agents จริงๆ. ข้าม Cloudflare Agents SDK [15], crypto/onchain stacks [27][28], recruiter skill lists [21][58], และ AI-engineering interview/stack threads [4][6][54]

## Signals to Watch
- Vercel BYOC pricing และ operational requirements เมื่อมีเอกสาร — ปัจจัยชี้ขาดว่าจะลด bill ได้จริงหรือเปล่า [18]
- ว่า constraint Vercel-only ของ eve จะจุด portability pushback หรือทำให้เกิด alternative frameworks [7][10]
- Cloudflare reliability follow-up หลัง bug thread ของ Corey Quinn ซึ่งเกี่ยวข้องถ้า studio ใช้ Workers/CDN [43]
- การ adopt governance tooling (Vercel Passport, scoped tokens) เพื่อตอบสนองต่อความกังวล 93% เรื่อง vibe-code apps [18][52]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | vercel | ^7050 c316 | [Introducing eve, an agent framework. 𝚊𝚐𝚎𝚗𝚝/ 𝚊𝚐𝚎𝚗𝚝.𝚝𝚜 𝚒𝚗𝚜𝚝𝚛𝚞𝚌𝚝𝚒𝚘𝚗𝚜.𝚖𝚍 𝚝𝚘𝚘𝚕𝚜/ 𝚜𝚔𝚒𝚕](https://x.com/vercel/status/2067180054979936413) |
| x | CaryKelly11 | ^2280 c74 | [Here's how to turn a $20 chuck roast into three meals that include two steak din](https://x.com/CaryKelly11/status/2067216702014730670) |
| x | Marmitex78 | ^2127 c9 | [Why do I have so much honeycomb? For my giant honey block house of course https:](https://x.com/Marmitex78/status/2067247797825593672) |
| x | techNmak | ^846 c13 | [Someone just dropped a 9-layer production AI architecture and it's the most hone](https://x.com/techNmak/status/2067276894291316896) |
| x | cramforce | ^794 c42 | [I've rarely seen a piece of technology "click" with people like eve. It went thr](https://x.com/cramforce/status/2067185809288007786) |
| x | ConsciousRide | ^750 c26 | [90% of AI Engineering interviews in 2026 come down to these 7 points. 1. LLM Fun](https://x.com/ConsciousRide/status/2067239474527166605) |
| x | IceSolst | ^744 c31 | [Vercel will vibecode a repo of markdown files like this and have a launch party ](https://x.com/IceSolst/status/2067443793322721457) |
| x | OndoFinance | ^657 c33 | [Big day for tokenization. Over 170 new tokenized stocks & ETFs are now onchain, ](https://x.com/OndoFinance/status/2067319932254114289) |
| x | build_canada | ^464 c33 | [Canadians have built tech empires. But most didn't do it at home. ✈️ @Uber, @Clo](https://x.com/build_canada/status/2067293966597316991) |
| x | FredKSchott | ^456 c31 | [some thoughts on eve, especially re: @flueai and the larger agent builder space.](https://x.com/FredKSchott/status/2067302366718947778) |
| x | maya_l39 | ^419 c43 | [first week at @vercel! stoked to be working in the office of the cto with @andre](https://x.com/maya_l39/status/2067309938406506723) |
| x | vercel | ^394 c13 | [Every agent needs streaming, models, durability, isolation, channels, and integr](https://x.com/vercel/status/2067176489641275824) |
| x | supabase | ^392 c28 | [Supabase is now used by 10 million developers worldwide! We want to thank the am](https://x.com/supabase/status/2067618668725305742) |
| x | AskYoshik | ^381 c12 | [A lot of juniors ask me if they should learn Rust. The reason companies like Ope](https://x.com/AskYoshik/status/2067526163342504043) |
| x | Cloudflare | ^345 c8 | [The Agents SDK is now a runtime any agent framework can build on. Today we're op](https://x.com/Cloudflare/status/2067332580400054593) |
| x | anishmoonka | ^295 c5 | [The metal ice tray in that video freezes water 30 to 50 percent faster than the ](https://x.com/anishmoonka/status/2067664892400668803) |
| x | Railway | ^282 c20 | [Railway, now in your pocket 📱🚄 https://t.co/jHHORL20c5](https://x.com/Railway/status/2067230889713475877) |
| x | cramforce | ^278 c13 | [We didn't only ship eve yesterday: Vercel BRING YOUR OWN CLOUD! Run Vercel Compu](https://x.com/cramforce/status/2067535959181181309) |
| x | vercel | ^270 c9 | [Vercel Connect makes accessing external data and systems simple and secure. It g](https://x.com/vercel/status/2067178169006973270) |
| x | Peersyst | ^232 c6 | [🧵1/8: Introducing the XRPL Network Monitoring &amp; Alerting Initiative We're ex](https://x.com/Peersyst/status/2067537808416240103) |
| x | devops_nk | ^226 c27 | [Dear recruiters, If you're looking for: • AWS, Azure, GCP • Kubernetes, Docker •](https://x.com/devops_nk/status/2067099667314454559) |
| x | rubenhassid | ^220 c18 | [Everyone's vibecoding the same (ugly) AI website. Here's the 7-step Claude Code ](https://x.com/rubenhassid/status/2067487480388166122) |
| x | idrwalerts | ^206 c10 | [Tejas Mk2 Achieves 75% Lower Frontal RCS Than Mk1A: India's Medium Weight Fighte](https://x.com/idrwalerts/status/2067086177749066018) |
| x | freeCodeCamp | ^206 c1 | [Learning Kubernetes isn't all about memorizing commands. It really clicks when y](https://x.com/freeCodeCamp/status/2067699130634285115) |
| x | SumitM_X | ^204 c6 | [Dear Java devs, How many of these skills are on your CV? 1. Distributed Caching ](https://x.com/SumitM_X/status/2067632672663552424) |
| x | montana_labs | ^184 c3 | [Adding observability after the first incident is the most expensive time to add ](https://x.com/montana_labs/status/2067653566987378847) |
| x | NKLinhzk | ^178 c180 | [gCNPY 🌿🌿🌿 just sat down with @CNPYNetwork latest take on the full dev stack. cur](https://x.com/NKLinhzk/status/2067532523174064170) |
| x | PodcastAlphaX | ^177 c5 | [If you hold $NET, this one changes an input. Gavin Baker @GavinSBaker of Atreide](https://x.com/PodcastAlphaX/status/2067341511105315039) |
| x | e_opore | ^175 c13 | [System Design Cheatsheet (Beginner to Advanced) Fundamentals of System Design → ](https://x.com/e_opore/status/2067129650187293164) |
| x | sp4rtan300 | ^175 c3 | [Minimum you have to know for DevOps or Platform Engineering Linux - OS Bash - Sc](https://x.com/sp4rtan300/status/2067762962581074050) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vercel</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7050 · 💬 316</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vercel/status/2067180054979936413">View @vercel on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing eve, an agent framework. 𝚊𝚐𝚎𝚗𝚝/ 𝚊𝚐𝚎𝚗𝚝.𝚝𝚜 𝚒𝚗𝚜𝚝𝚛𝚞𝚌𝚝𝚒𝚘𝚗𝚜.𝚖𝚍 𝚝𝚘𝚘𝚕𝚜/ 𝚜𝚔𝚒𝚕𝚕𝚜/ 𝚜𝚊𝚗𝚍𝚋𝚘𝚡/ 𝚜𝚌𝚑𝚎𝚍𝚞𝚕𝚎𝚜/ Like Next.js, for agents. https://t.co/ezUIGLkSqG”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Vercel เปิดตัว 'eve' framework สำหรับ agent ที่ใช้ file convention เหมือน Next.js — โครงสร้างมี agent.ts, instructions.md, tools/, skills/, sandbox/, schedules/</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Eve มี deploy path มาตรฐานสำหรับ agent บน Vercel โดยไม่ต้อง build architecture เอง — ตรงกับทีมที่ทำ AI feature บน Next.js</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง eve กับ internal tool หรือ chatbot feature ใน Next.js project สักอันก่อน แล้วค่อยตัดสินใจใช้กับ web stack ทั้งหมด</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vercel/status/2067180054979936413" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CaryKelly11</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2280 · 💬 74</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CaryKelly11/status/2067216702014730670">View @CaryKelly11 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here’s how to turn a $20 chuck roast into three meals that include two steak dinners. If you can learn how to recognize the chuck eye and the Denver steak, you’re in for some treats. The honeycomb mar”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Post ไวรัลสอนแล่เนื้อ chuck roast ให้ได้ Denver steak, chuck eye steak, และเนื้อบด — ไม่มีเนื้อหา tech</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CaryKelly11/status/2067216702014730670" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Marmitex78</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2127 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Marmitex78/status/2067247797825593672">View @Marmitex78 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Why do I have so much honeycomb? For my giant honey block house of course https://t.co/u7kD8K39tT”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์เกี่ยวกับการสะสม honeycomb ใน Minecraft เพื่อสร้างบ้านจาก honey block — ไม่เกี่ยวกับเทคโนโลยีหรือการพัฒนา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Marmitex78/status/2067247797825593672" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@techNmak</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 846 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/techNmak/status/2067276894291316896">View @techNmak on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Someone just dropped a 9-layer production AI architecture and it's the most honest breakdown I've seen. services/ - RAG pipeline, semantic cache, memory, query rewriter, router. Not one file. Five. ag”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา share โครงสร้าง production AI 9 layer: RAG pipeline, versioned prompts, security 3 ชั้น, golden-dataset eval และ per-stage cost tracing — เทียบกับ demo ไฟล์เดียวทั่วไป</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>layer evaluation (golden dataset + offline/online eval) และ observability (cost per query, per-stage tracing) คือสองส่วนที่ทีมส่วนใหญ่ข้ามเมื่อ ship AI feature เร็ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ใช้ folder structure นี้เป็น reference ตอน scaffold AI หรือ RAG feature ถัดไป โดยเฉพาะ prompts/ versioning และ evaluation/ layer</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/techNmak/status/2067276894291316896" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cramforce</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 794 · 💬 42</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cramforce/status/2067185809288007786">View @cramforce on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I've rarely seen a piece of technology &quot;click&quot; with people like eve. It went through a months long dogfooding and private beta phase and the agents that our customers shipped in minimal time were abso”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Vercel engineer @cramforce รายงานว่า 'eve' platform สำหรับ AI agents เปิด public หลัง dogfooding หลายเดือน มาพร้อม evals, observability, และ SDLC ตั้งแต่วันแรก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Platform ที่มี evals และ observability built-in ช่วยลด DevOps overhead เมื่อ studio ต้องการ ship AI agent features บน Vercel stack</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู docs ของ eve เทียบกับงาน agent ที่จะทำใน web stack ก่อนจะไปสร้าง eval หรือ observability pipeline เอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cramforce/status/2067185809288007786" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ConsciousRide</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 750 · 💬 26</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ConsciousRide/status/2067239474527166605">View @ConsciousRide on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“90% of AI Engineering interviews in 2026 come down to these 7 points. 1. LLM Fundamentals: tokenization, transformers &amp; attention, fine-tuning (LoRA/QLoRA), context management, model selection 2. RAG ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>คู่มือสัมภาษณ์ AI Engineer ปี 2026 สรุป 7 หมวดทักษะ: LLM fundamentals, RAG, agentic workflows, inference optimization, eval/observability, MLOps, และ production safety.</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>7 หมวดนี้ใช้เป็น skills-gap audit ได้เลย — inference optimization และ eval/observability คือจุดที่ทีมเล็กมักข้ามไป</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เอา 7 หมวดนี้มาเช็คงาน AI ที่ studio ทำอยู่ เพื่อหา gap ก่อน scope project หรือ hire คนเพิ่ม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ConsciousRide/status/2067239474527166605" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@IceSolst</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 744 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/IceSolst/status/2067443793322721457">View @IceSolst on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Vercel will vibecode a repo of markdown files like this and have a launch party over it, clown ass company https://t.co/uH342gPDjb”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev ล้อ Vercel ว่าใช้ AI vibe-code สร้าง repo ที่เป็นแค่ไฟล์ markdown แล้วจัด launch party ราวกับเป็นของใหญ่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/IceSolst/status/2067443793322721457" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@OndoFinance</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 657 · 💬 33</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/OndoFinance/status/2067319932254114289">View @OndoFinance on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Big day for tokenization. Over 170 new tokenized stocks &amp; ETFs are now onchain, many for the first time ever: ✅ Dell ✅ Flex ✅ EQT ✅ Jabil ✅ Ciena ✅ Nokia ✅ Nucor ✅ Atkore ✅ Rambus ✅ Cameco ✅ Corning ✅”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Ondo Finance เพิ่ม tokenized stocks และ ETFs กว่า 170 รายการบน Ondo Global Markets รวมทั้งหมด 430+ assets ครอบคลุมหุ้นเทค อุตสาหกรรม และ ETF หลากหลายกลุ่ม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/OndoFinance/status/2067319932254114289" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
