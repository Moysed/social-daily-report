---
type: social-topic-report
date: '2026-05-28'
topic: devops-cloud
lang: th
pair: devops-cloud.en.md
generated_at: '2026-05-28T03:35:17+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- reddit
- x
regions:
- global
post_count: 133
salience: 0.82
sentiment: mixed
confidence: 0.7
tags:
- cloudflare
- vercel
- supabase
- edge-functions
- cost-optimization
- feature-flags
thumbnail: https://pbs.twimg.com/media/HJOFQH6a8AAIcNV.jpg
translated_by: claude-sonnet-4-6
---

# DevOps & Cloud — 2026-05-28

## TL;DR
- ช่องว่างด้านต้นทุนระหว่าง Cloudflare กับ Vercel คือสัญญาณที่ดังที่สุดในวันนี้: ทีมหนึ่งลดบิลจาก $25k เหลือ $2k/เดือนด้วยการย้ายมาใช้ [3]; อีกทีมย้ายออกจาก Vercel free tier ไป CF Pages ตอนโหลดพุ่ง [53]
- Cloudflare เปิดตัว Flagship feature flags (public beta) บน Workers [11] และ Voice SDK [51]; sandbox-sdk v0.10.2 เพิ่ม CF Tunnels + R2 mounts [26]
- Reliability theater: Vercel anomaly detection จับสัญญาณ GitHub outage ได้ก่อน status page 16 นาที [2]; Cloudflare ออก RCA ภายใน <24h ขณะที่คู่แข่งใช้เวลาเป็นสัปดาห์ [6]
- Ghost CMS CVE-2026-26980 (unauth SQLi) กระทบเว็บไซต์กว่า 700 แห่งรวมถึง Harvard/Oxford — Admin API key ถูก exfil [5] ตรวจสอบทุก CMS ที่ studio ดูแลอยู่
- Supabase local dev flow ถูกย้ำอีกครั้งว่าเป็นแนวทางที่ถูกต้องสำหรับ prod parity [43]; consensus ของ solo-stack ยังคงเป็น Supabase+Vercel+Stripe+Resend [41][44]

## สิ่งที่เกิดขึ้น
ต้นทุนและ lock-in ครองวาระหลักของวันนี้ ผู้ก่อตั้งรายหนึ่งรายงานต่อสาธารณะว่าการย้ายจาก Vercel ไป Cloudflare ทำให้ค่าใช้จ่ายรายเดือนลดจาก $25k เหลือ $2k [3] สอดคล้องกับการย้ายออกจาก Vercel free tier เมื่อ traffic พุ่ง [53] และ DHH โอ้อวดว่า Omarchy serve traffic 600TB/เดือนผ่าน Cloudflare [4] Cloudflare ยังขยาย platform อีก ได้แก่ Flagship feature flags ใน public beta บน Workers [11], Voice SDK [51], sandbox-sdk v0.10.2 พร้อม Tunnels + R2 mounts และ isolated exec [26] และ post-quantum ครอบคลุมกว่า 50% ของ traffic เว็บจากมนุษย์แล้ว [20] วาทกรรมด้าน reliability เอียงมาทาง CF/Vercel — anomaly detection ของ Vercel นำหน้า status page ของ GitHub 16 นาที [2] และ CF ออก RCA ภายใน 24h ขณะที่ Coinbase และคู่แข่งใช้เวลาเป็นสัปดาห์ [6]

## ทำไมจึงสำคัญ (เหตุผล)
สำหรับ studio ขนาดเล็กที่รัน Next.js + Supabase เส้นโค้งราคา bandwidth/function-invocation ของ Vercel จะโหดขึ้นมากเมื่อโปรเจกต์เติบโต; CF Pages/Workers + R2 egress-free คือทางออกที่ชัดเจน [3][4][53] แต่เรื่องราวการย้ายนั้นเลือกนำเสนอแค่บางด้าน — Vercel ยังคง ship DX ได้ดี (preview deploys, ISR, marketplace integrations อย่าง Firecrawl [56]) ที่ CF Pages ยังตามไม่ทัน และ CF Workers มีกับดักอย่างเรื่อง DB connection reuse semantics ที่กัด Postgres users [27] ผลกระทบรอบสอง: feature flags ที่ย้ายเข้ามาใน edge runtime [11] หมายถึง SaaS line item ที่น้อยลงหนึ่งรายการ (LaunchDarkly/Statsig); CF Voice SDK [51] ทำให้ realtime audio เข้าถึงได้โดยไม่ต้องพึ่ง Twilio/LiveKit ด้านความเสี่ยง Ghost CMS unauth SQLi [5] เตือนให้ระลึกว่า self-hosted CMS = SOC problem ของคุณเอง

## ความเป็นไปได้
น่าจะเกิด (~70%): CF กินส่วนแบ่ง Vercel ในกลุ่ม price-sensitive สำหรับ static + edge-compute heavy workloads ต่อไป ขณะที่ Vercel รักษาฐาน Next.js-native + AI-SDK shops ไว้ได้ ปานกลาง (~40%): Flagship + Voice + Sandbox bundle กดดัน niche SaaS (LaunchDarkly, ElevenLabs-on-API, E2B) ต่ำ (~20%): outage ระดับ studio-scale บน CF Workers จะจุดกระแสต่อต้าน เมื่อพิจารณาจากดราม่า PR เรื่องเลิกจ้างที่เกิดขึ้นเร็วๆ นี้ [7][19] และความเสี่ยงจาก concentration [16][29][48] จับตาดูว่า Supabase Edge Functions จะแข่งขันกับ Workers + Hyperdrive สำหรับ Postgres-fronted apps ได้ต่อเนื่องหรือไม่

## ความเกี่ยวข้องกับองค์กร — NDF DEV
แนวทางที่ลงมือได้เลยสำหรับ NDF DEV: (1) ตรวจสอบต้นทุน Next.js prod app ทุกตัว — ถ้าโปรเจกต์ไหนเกิน ~$200/เดือน บน Vercel ให้ลอง prototype CF Pages + Workers + Hyperdrive บน branch แล้ว benchmark ดู [3][27] (2) สมัคร CF Startup $10k credits [17] — runway ฟรีสำหรับ HR/edutech web apps (3) แทนที่การ toggle env-flag แบบ ad-hoc ด้วย Flagship beta ใน release ถัดไป [11]; ลองง่าย ถอยก็ง่าย (4) ใช้ Supabase local dev flow [43] ทุก repo — ลด prod-only bugs (5) ข้าม CF Voice SDK [51] ไปก่อนจนกว่าจะมี use case edutech จริงๆ (เช่น pronunciation practice) (6) เพิ่ม CVE-2026-26980 ใน security checklist ถ้า client site ไหนใช้ Ghost [5] ควรทำ: ข้อ 1, 3, 4, 6 เลื่อนไปก่อน: 2 (เฉพาะถ้า eligible), 5

## สัญญาณที่ต้องจับตา
- การตอบสนองของ Vercel ด้านราคาต่อกรณี $25k→$2k ที่เป็นข่าวใหญ่ — bandwidth tier ใหม่หรือส่วนลด fluid-compute [3]
- Flagship GA + ราคาเทียบกับ LaunchDarkly/Statsig [11]
- ความสมบูรณ์ของ CF Workers + Hyperdrive สำหรับ Supabase Postgres connection reuse [27]
- ความถี่ของ Cloudflare-side incidents/RCA ในอีก 90 วันข้างหน้า เมื่อพิจารณาผลกระทบจากการเลิกจ้าง [6][7]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | vxunderground | ^3154 c49 | [Someone on social media was bragging they got a CSAM website taken offline. They](https://x.com/vxunderground/status/2059142741255168059) |
| x | rauchg | ^2208 c116 | [Every time GitHub has an outage our team is paged. Incidents at Vercel get autom](https://x.com/rauchg/status/2059612940307714540) |
| x | nooriefyi | ^1657 c145 | [Our Vercel bill was $25k per month. We just switched to Cloudflare and our spend](https://x.com/nooriefyi/status/2059135988107284905) |
| x | dhh | ^815 c29 | [Omarchy traffic keeps surging. In the past 30 days, 600 terrabyte of traffic was](https://x.com/dhh/status/2059638719305371835) |
| x | IntCyberDigest | ^737 c16 | [‼️🚨 Over 700 Ghost CMS sites, including Harvard, Oxford, and Auburn, were compro](https://x.com/IntCyberDigest/status/2059367678096359507) |
| x | GergelyOrosz | ^661 c36 | [How is it that Cloudflare publishes RCAs within 24 hours of a massive outage, an](https://x.com/GergelyOrosz/status/2059598189053747372) |
| x | theallinpod | ^519 c43 | [Chamath Rips Cloudflare CEO's Layoff Memo: "Shut the f**k up. You suck at this."](https://x.com/theallinpod/status/2059287103561687410) |
| x | __morse | ^448 c18 | [introducing holocron it's an open source alternative to Mintlify, as a self host](https://x.com/__morse/status/2059384382448611729) |
| x | atomicbot_ai | ^434 c33 | [We released iOS app for Hermes Agent 📱 Connect to your self-hosted agent over Ta](https://x.com/atomicbot_ai/status/2059427131252171068) |
| x | PuthingAround | ^403 c1 | [@patternrecoggni That's just the god damn server error message for Cloudflare](https://x.com/PuthingAround/status/2059315270808703433) |
| x | kristianfreeman | ^346 c13 | [cloudflare now has a built-in feature flag service 🏁 flagship enters public beta](https://x.com/kristianfreeman/status/2059282992673988957) |
| x | lukepierceops | ^336 c20 | [We've built systems for 85+ companies. The order you build in matters more than ](https://x.com/lukepierceops/status/2059254933539451104) |
| x | testingcatalog | ^317 c14 | [Atomic Bot released an iOS app for Hermes Agent, bringing mobile control to a se](https://x.com/testingcatalog/status/2059428197670719958) |
| x | marclou | ^313 c69 | [🚨 Ruby on Rails has taken over NextJS 🚨 and Vercel is still just above Cloudflar](https://x.com/marclou/status/2059616890063085632) |
| x | GCNDiscs_ | ^262 c2 | [@nonbatnary Cloudflare turnstile security on cobalt when you even think about do](https://x.com/GCNDiscs_/status/2059274243209347411) |
| x | immanuel_vibe | ^239 c7 | [eBPF is kinda insane and nobody talks about it enough Netflix uses it to trace f](https://x.com/immanuel_vibe/status/2059143155707007463) |
| x | IanLandsman | ^222 c22 | [If you're a bootstrapped startup Cloudflare will give you $10k in credits https:](https://x.com/IanLandsman/status/2059289714264273337) |
| x | _cantemizyurek | ^221 c44 | [Excited to share that today is my first day @vercel. I'll be joining the CDN tea](https://x.com/_cantemizyurek/status/2059348736585699381) |
| x | NewsArenaIndia | ^214 c5 | ["AI to replace middle management, measurer roles." - Cloudflare CEO Matthew Prin](https://x.com/NewsArenaIndia/status/2059377409431163285) |
| x | 0xRiRoyal | ^203 c115 | [good morning quip networks fam crypto is debating something the rest of the inte](https://x.com/0xRiRoyal/status/2059496008921522673) |
| x | ayushagarwal027 | ^181 c3 | [A Rust dev built a Python compiler in 90 days. 13K lines of no_std Rust. ~170KB ](https://x.com/ayushagarwal027/status/2059711362109001817) |
| x | 5harath | ^155 c7 | [OK @Cloudflare team cooked with their startup program landing page https://t.co/](https://x.com/5harath/status/2059349223829807133) |
| x | JaredSleeper | ^151 c17 | [This has now gotten to fairly considerable n. Share of saying AI is good for eac](https://x.com/JaredSleeper/status/2059276904197128250) |
| x | TheGlobalMinima | ^151 c3 | [Wanna start building Agentic applications ? Learn backend engineering and design](https://x.com/TheGlobalMinima/status/2059602050259034248) |
| x | noor36758 | ^141 c35 | [Popular Frameworks and the Company Behind Them 🌍 • ⚛️ React — 🇺🇸 Meta • 💚 Vue — ](https://x.com/noor36758/status/2059266575300256110) |
| x | whoiskatrin | ^139 c4 | [we just shipped sandbox-sdk v0.10.2 today 🎈 - cloudflare tunnels support - mount](https://x.com/whoiskatrin/status/2059675264968179816) |
| x | AdamRackis | ^138 c22 | [Anyone here smart about Cloudflare workers? Is re-using / keeping open a db conn](https://x.com/AdamRackis/status/2059742697414418762) |
| x | brandonjcarl | ^127 c4 | [Out of every company I've seen, @Cloudflare has cracked the agent-platform of th](https://x.com/brandonjcarl/status/2059624598644109363) |
| x | CloudflareRadar | ^125 c8 | [Cloudflare Radar observed a notable increase in activity (DNS queries and traffi](https://x.com/CloudflareRadar/status/2059385635333636294) |
| x | CruzzCtrl1 | ^119 c17 | [Every tool you need to become a DevOps engineer costs $0. - Linux ✓ - Docker ✓ -](https://x.com/CruzzCtrl1/status/2059132470126129651) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vxunderground</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3154 · 💬 49</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vxunderground/status/2059142741255168059">View @vxunderground on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Someone on social media was bragging they got a CSAM website taken offline. They illustrated this by showing a CloudFlare report. The report shows the domain this person reported. CloudFlare clearly s”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>คนโพสต์อวดว่าแจ้ง Cloudflare แล้วเว็บ CSAM โดนปิด แต่เว็บยังอยู่เพราะ report แค่ส่งสืบสวน ไม่ใช่ takedown — โพสต์ 782K views กลายเป็นโฆษณาฟรีให้เว็บนั้น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Cloudflare abuse report = ส่งสืบสวน ไม่ใช่ปิดทันที — ต่างกันสำคัญมาก. โพสต์ viral เกี่ยวกับเว็บผิดกฎหมายที่ยังอยู่สร้าง Streisand effect ขนาดใหญ่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตอน studio ใช้ Cloudflare ต้องจด SOP ไว้ว่า abuse report ≠ takedown. ห้าม post public เรื่อง security หรือ legal incident จนกว่าจะปิดได้จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vxunderground/status/2059142741255168059" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2208 · 💬 116</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2059612940307714540">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Every time GitHub has an outage our team is paged. Incidents at Vercel get automatically filed by anomaly detection systems. We just detected an outage 16 minutes before their status page changed. Dep”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>CEO ของ Vercel เล่าว่า anomaly detection ของพวกเขาจับ GitHub outage ได้ก่อน status page ของ GitHub ถึง 16 นาที และย้ำว่า software infrastructure ยังยากมากแม้จะมี AI</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แม้แต่ GitHub ที่ทำ Copilot ออกมายังหนีปัญหา infrastructure ไม่พ้นด้วย AI พิสูจน์ว่า observability และ anomaly detection ขาดไม่ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม web stack ควรตั้ง anomaly alert บน Vercel projects เลย เช่น deployment dip — รอ user complaint หรือ status page ช้าเกินไป</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2059612940307714540" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nooriefyi</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1657 · 💬 145</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nooriefyi/status/2059135988107284905">View @nooriefyi on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Our Vercel bill was $25k per month. We just switched to Cloudflare and our spend is $2k per month. This is your sign to switch to Cloudflare https://t.co/H8BdmiVDYp”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีมลดค่า hosting จาก $25k เหลือ $2k/เดือน โดย switch จาก Vercel ไป Cloudflare</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ลดค่าใช้จ่าย 92% บน production จริง พิสูจน์ว่า Vercel pricing แตกที่ scale — ไม่ใช่ edge case</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Next.js stack ของ studio deploy บน Cloudflare Pages/Workers ได้เลย — ตรวจ Vercel spend ปัจจุบันแล้วทดสอบ deploy บน Cloudflare ก่อน project ขยายตัว</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nooriefyi/status/2059135988107284905" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@dhh</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 815 · 💬 29</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/dhh/status/2059638719305371835">View @dhh on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Omarchy traffic keeps surging. In the past 30 days, 600 terrabyte of traffic was served by our awesome hosts at @cloudflare. Up 13% month/month!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>DHH รายงาน Omarchy มี traffic 600 TB ผ่าน Cloudflare ใน 30 วันที่ผ่านมา เพิ่มขึ้น 13% month-over-month</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Cloudflare รับ 600 TB พร้อม growth 13% MoM พิสูจน์ว่าใช้งานได้จริงเป็น CDN และ DDoS layer สำหรับ project ที่โต fast โดยไม่ต้องมีทีม infra</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Web apps Next.js ของ studio ควร route traffic ทั้งหมดผ่าน Cloudflare — รับ spike ได้โดยไม่ต้อง scale origin server และ free tier รองรับ load ส่วนใหญ่ได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/dhh/status/2059638719305371835" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@IntCyberDigest</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 737 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/IntCyberDigest/status/2059367678096359507">View @IntCyberDigest on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“‼️🚨 Over 700 Ghost CMS sites, including Harvard, Oxford, and Auburn, were compromised through an unauthenticated SQL injection (CVE-2026-26980). Attackers pulled Admin API Keys and turned every site i”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Ghost CMS กว่า 700 เว็บ รวมถึง Harvard และ Oxford โดน SQL injection ไม่ต้อง authenticate (CVE-2026-26980) — Admin API Keys หลุด เว็บถูกเปลี่ยนเป็น ClickFix malware delivery แพตช์ออก 19 ก.พ. แต่ส่วนใหญ่ไม่ได้อัปเดต</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ช่องโหว่ CMS ที่ไม่แพตช์ทำให้ domain ที่น่าเชื่อถือกลายเป็นอาวุธได้ — ปัญหาคือการแพตช์ช้า ไม่ใช่ zero-day แปลว่าป้องกันได้ 100%</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Studio ใช้ Next.js + Supabase ไม่ได้ใช้ Ghost แต่ทุก CMS หรือ dependency ต้องมี automated update monitoring — เปิด Dependabot แล้วตั้ง rule แพตช์ภายใน 7 วัน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/IntCyberDigest/status/2059367678096359507" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GergelyOrosz</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 661 · 💬 36</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GergelyOrosz/status/2059598189053747372">View @GergelyOrosz on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“How is it that Cloudflare publishes RCAs within 24 hours of a massive outage, and no other company of similar size comes close? Waiting almost 3 weeks for the one Coinbase promised publicly (their glo”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Cloudflare ออก RCA ภายใน 24 ชั่วโมงหลัง outage ใหญ่ ขณะที่คู่แข่งอย่าง Coinbase รอ 3 สัปดาห์แล้วยังเงียบ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>RCA เร็วและตรงไปตรงมา = trust signal ทีมที่ทำได้จะได้ client confidence และบังคับให้เกิด blameless culture จริงๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Studio ควร template RCA (timeline, root cause, fix, prevention) และ commit กับ client ว่าจะส่งภายใน 48 ชั่วโมงหลัง production outage ทุกครั้ง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GergelyOrosz/status/2059598189053747372" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theallinpod</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 519 · 💬 43</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theallinpod/status/2059287103561687410">View @theallinpod on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Chamath Rips Cloudflare CEO’s Layoff Memo: “Shut the f**k up. You suck at this.” @Jason: “Matthew Prince, who is the CEO of Cloudflare, said, ‘Two weeks ago, I laid off more than 20% of my workforce. ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Chamath วิจารณ์ memo ไล่พนักงานของ CEO Cloudflare ว่าการเรียกคนถูกปลดว่า 'measurers' คือ PR แย่มาก และทำลาย reputation พนักงานในตลาดงานระยะยาว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>วิธี label การปลดพนักงานสาธารณะติดตัวคนออก — คำเดียวใน memo อาจทำให้ ex-employee ถูกมองแบบนั้นทั้ง industry</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า studio ต้องปรับ structure ให้สื่อสารในแง่ scope ของ role และทิศทาง business — อย่า reduce คนเป็น label function ที่ติดตัวพวกเขาออกไปถึง interview งานถัดไป</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theallinpod/status/2059287103561687410" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@__morse</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 448 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/__morse/status/2059384382448611729">View @__morse on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“introducing holocron it's an open source alternative to Mintlify, as a self hostable Vite plugin. it supports the same exact docs.json config you can deploy it to Vercel, Cloudflare, Docker or anywher”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Holocron คือ Vite plugin open-source ที่ใช้แทน Mintlify ได้ รองรับ docs.json format เดิม deploy ได้ทั้ง Vercel, Cloudflare, Docker</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่จ่าย Mintlify อยู่สามารถเลิก subscription แล้ว self-host ได้เลย โดยไม่ต้องแก้ config — ใช้ docs.json เดิมได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">web stack ใช้ Vercel อยู่แล้ว — เปลี่ยนมาใช้ Holocron แทน Mintlify เพื่อลดค่า subscription และเก็บ docs ไว้ใน repo เดียวกับ Next.js</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/__morse/status/2059384382448611729" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
