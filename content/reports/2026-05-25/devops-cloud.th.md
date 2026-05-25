---
type: social-topic-report
date: '2026-05-25'
topic: devops-cloud
lang: th
pair: devops-cloud.en.md
generated_at: '2026-05-25T08:44:42+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- reddit
- x
regions:
- global
post_count: 90
salience: 0.78
sentiment: mixed
confidence: 0.74
tags:
- supabase
- cloudflare-r2
- vercel
- egress-cost
- rls-security
- nextjs-stack
thumbnail: https://pbs.twimg.com/media/HI_lY1ZaIAA9sam.jpg
translated_by: claude-sonnet-4-6
---

# DevOps & Cloud — 2026-05-25

## TL;DR
- ตรวจสอบต้นทุนจริง: Postbridge ที่ MRR $35K กำลังจ่าย egress ให้ Supabase ราว $700/เดือน ขณะที่ R2 คิด egress $0 [5][38][14]; Postiz ที่ MRR $105K รันบน Railway $200 + R2 $160 [22]
- R2 ครองตลาดเพิ่มขึ้นเรื่อยๆ — วิดีโอ 4K ขนาด 15TB ในราคา $2.18 [25] พร้อม pattern temp-share บน R2+Durable Objects [27] และ R2 sync connectors [23]
- จุดอ่อน Supabase: anonymous sign-in สร้างช่องโหว่ด้านความปลอดภัยนาน 3 สัปดาห์ เป็น edge case ของ RLS ที่คนส่วนใหญ่พลาด [54]
- ท่าที Vercel: โพสต์ครบ 10 ปี [9], อ้าง 'ไม่มีพนักงานคนไหนเขียนโค้ดด้วยมือแล้ว' [18], เร่ง hiring [45] — platform เสถียร, workflow พัฒนาแบบ AI-native กลายเป็นเรื่องปกติ
- เสียงรบกวนฝั่ง Cloudflare: Discord ถูกสแกมรุมเนื่องจากยุบ community champions [56]; แรงกดดันจาก ADL/Kiwi Farms + ข้อพิพาทกับ Chamath เพิ่มความเสี่ยงด้านชื่อเสียง [2][4][55]

## สิ่งที่เกิดขึ้น
วันนี้มี case study ต้นทุนที่เป็นรูปธรรมสองชิ้นออกมา: Jack Friks เปิดเผย stack ของ Postbridge ที่ MRR $35K และพบว่า egress ของ Supabase storage อย่างเดียวอยู่ที่ ~$700/เดือน เทียบกับโมเดล zero-egress ของ R2 [5][38] โดยมี Levelsio ออกมาล้อเรื่องค่า DB ด้วย [14] ส่วน Postiz เปิด infra ที่ MRR $105K: Railway ~$200, R2 ~$160 และ X API คือตัวดูดเงินตัวจริงที่ $1,000 [22] Cloudflare R2 มีช่วงเวลาไวรัลหลายครั้ง — วิดีโอ 4K 15TB ในราคา $2.18 [25], pattern resumable file-share ด้วย R2+Durable Objects+Turnstile [27] และ demo sync ผ่าน S3/R2 connector [23]

ฝั่ง platform มี war-story ของ Supabase โผล่มาเปิดเผยช่องโหว่ RLS จริงตอนใช้ anonymous sign-in ที่ไม่มีใครสังเกตนาน 3 สัปดาห์ [54] สัญญาณฝั่ง Vercel ส่วนใหญ่เป็นเรื่อง culture/hiring [9][18][45] บวกกับโพสต์วิศวกรรม domain-search ที่ถูก tease ไว้ [32] เสียงรบกวนเชิง operational รอบ Cloudflare รวมถึงปัญหาสแกมใน Discord ที่ไม่มีคนดูแล [56] และแรงกดดันด้าน ADL/deplatforming ที่ยังดำเนินต่อ [2][4] การพูดถึงการเลือก stack ('Next.js + Supabase + Stripe' เป็น default) ยืนยันว่า stack ของ studio อยู่ใน mainstream แล้ว [34][47][49][42]

## ทำไมถึงสำคัญ (เหตุผล)
สำหรับโปรเจกต์ NDF DEV บน Next.js + Supabase สัญญาณที่นำไปใช้ได้มากที่สุดคือเรื่อง egress [38]: egress ของ Supabase Storage อาจขึ้นครองบิลแบบเงียบๆ ทันทีที่ผลิตภัณฑ์มี media/asset ในปริมาณหนึ่ง ขณะที่ R2 ไม่คิด egress เลย Postbridge จ่ายค่า storage มากกว่าค่า DB ถึง ~7 เท่า ผลกระทบระดับที่สอง: ถ้า studio apps รองรับ user uploads, วิดีโอ หรือแม้แต่ bundled assets ผ่าน Supabase Storage รูปแบบบิลแบบเดียวกันจะปรากฏเมื่อ scale ขึ้น การย้าย bucket หนักไปที่ R2 (หรือการ front Supabase Storage ด้วย Cloudflare cache) จึงกลายเป็น lever ควบคุมต้นทุน ไม่ใช่แค่การ optimize

ช่องโหว่ security ของ Supabase anonymous-auth [54] มีความสำคัญเพราะ anon sign-in มักถูกเปิดเพื่อ onboarding ที่ไม่ยุ่งยาก และ RLS policies ที่เขียนสำหรับ authenticated users มักพลาด anonymous role — นี่คือ bug แบบเงียบๆ ที่ hit production หลายสัปดาห์ต่อมาพอดี ปัญหาสแกมใน Cloudflare Discord [56] เป็นหมายเหตุ hygiene เล็กน้อยแต่จริง: อย่าเชื่อ DM/ลิงก์ในช่องนั้น การที่ Vercel วาง positioning เรื่อง 'โค้ดที่ agent เขียน' [18] สัญญาณว่า frontend hosting จะถูก commoditize เพิ่มขึ้น — ราคาและ DX จะยังแข่งขันได้ แต่ lock-in ผ่าน fluid compute/agent runtimes จะแน่นขึ้น

## ความเป็นไปได้
น่าจะเกิด (70%): R2-as-storage-tier จะกลายเป็นคำแนะนำมาตรฐานสำหรับทุกโปรเจกต์ Supabase ที่มี media ไม่น้อย โดย community tooling (R2 connectors [23], rclone-style sync) จะ mature ใน 3-6 เดือน น่าจะเกิด (60%): Supabase จะปล่อย guard-rails หรือคำเตือนที่ชัดขึ้นเกี่ยวกับ anonymous-role RLS ตอบสนองต่อ war stories ที่ซ้ำๆ [54] อาจเกิด (40%): adapter หรือ template 'Supabase + R2 storage' จะกลายเป็น pattern ที่แนะนำ ลดต้นทุนการ migrate โอกาสน้อย (25%): เสียงรบกวนด้านชื่อเสียง/operational ของ Cloudflare [2][4][56] ส่งผลจริงต่อ enterprise procurement; สำหรับสเกล indie/studio ไม่กระทบ การรวมตัวของ Vercel/Supabase ใน indie stack [34][47][49] จะยิ่ง entrench มากขึ้น — switching cost เพิ่มขึ้น

## การนำไปใช้ — NDF DEV
สิ่งที่ทำได้เลยสำหรับ NDF DEV web stack:
1. Audit Supabase Storage egress ของทุกโปรเจกต์ production สัปดาห์นี้ — ดูรายการ invoice; ถ้า egress > DB cost ให้วางแผน migrate คุ้มค่าทันทีที่ bucket ใดมี egress >50GB/เดือน
2. ตั้งค่า default media buckets ให้เป็น Cloudflare R2 ในโปรเจกต์ใหม่; เก็บ Supabase Storage ไว้เฉพาะ artifact ขนาดเล็กที่ auth-gated ROI เห็นได้ทันทีเมื่อ scale [25][38]
3. ตรวจสอบ anonymous sign-in ในทุกโปรเจกต์ Supabase: ถ้าเปิดไว้ ให้ audit RLS policies เพื่อให้แน่ใจว่า role `anon` ถูก check ตรงๆ ไม่ใช่แค่ `authenticated` [54] งานหนึ่งชั่วโมง ป้องกัน bug แบบเปิดช่องโหว่หลายสัปดาห์
4. ใช้ pattern R2 + Durable Objects [27] สำหรับ feature upload/share ใน studio web apps — ประหยัดทั้งเวลา build และต้นทุน runtime เทียบกับการทำบน Supabase Storage เอง
5. อย่าใช้ Cloudflare Discord เป็นช่อง support [56]; ใช้ docs + GitHub issues แทน
ยังไม่คุ้มตอนนี้: ปรับ obs/CI tooling ให้รองรับ k6/Grafana [20][44] — overkill สำหรับสเกล studio ปัจจุบัน; ค่อยกลับมาดูเมื่อผลิตภัณฑ์ใดข้าม 10k DAU

## สัญญาณที่ต้องจับตา
- Supabase changelog สำหรับ guard-rail หรือ audit tool ของ anon-role RLS
- การเปลี่ยนแปลงราคาหรือ free-tier ของ R2 (cache hit, Class A/B ops)
- ประกาศราคา Vercel ที่ผูกกับ Fluid/agent runtimes
- โพสต์ติดตามผลของ Postbridge เรื่องตัวเลข R2 migration จริง — ข้อมูล before/after จริงๆ

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | bodhi3attva | ^7592 c136 | [Government block claim is misleading. Technical checks show: > Domain is on clie](https://x.com/bodhi3attva/status/2058118651505729733) |
| x | LayoffAI | ^2288 c88 | [CHAMATH TO CLOUDFLARE CEO: SHUT THE FUCK UP Literally. He just destroyed him on ](https://x.com/LayoffAI/status/2058558639460192708) |
| x | shortmagsmle | ^1814 c1 | ["No man you don't get it, my foreign co-founder is REALLY good at using Claude t](https://x.com/shortmagsmle/status/2058156142090506368) |
| x | KiwiFarmsDotNet | ^838 c20 | [Despite deplatforming the Kiwi Farms, 8chan, the Daily Stormer, and other websit](https://x.com/KiwiFarmsDotNet/status/2058609650472218969) |
| x | jackfriks | ^780 c195 | [my solo business @postbridge_ is at $35,000 USD monthly recurring revenue (MRR) ](https://x.com/jackfriks/status/2058198360691998942) |
| x | steipete | ^744 c63 | [Still limited by compute, so I built a thing that runs codex in the cloud, power](https://x.com/steipete/status/2058248513662697622) |
| x | DavidFrosdick | ^720 c59 | [I did it 👍 thanks @levelsio for sharing. Setup @Tailscale on my @Hetzner_Online ](https://x.com/DavidFrosdick/status/2058582571194187819) |
| x | rileybrown | ^584 c77 | [Supabase will likely be worth more than Lovable Replit and Bolt combined when it](https://x.com/rileybrown/status/2058330104988844348) |
| x | evilrabbit_ | ^542 c32 | [I'm about to hit 10 years at Vercel. You can't imagine the amount of memories I ](https://x.com/evilrabbit_/status/2058205185655423224) |
| x | asonflower | ^406 c28 | [Let's find the path in the first post in my feed today... Nicki Minaj just hijac](https://x.com/asonflower/status/2058156658371477966) |
| x | cramforce | ^309 c12 | [Before joining Vercel, in an effort to escape the Google technology bubble, I wr](https://x.com/cramforce/status/2058650289969025043) |
| x | bayendor | ^255 c8 | [i just asked my Hermes Agent what the 5 most used skills are in our multi-agent ](https://x.com/bayendor/status/2058284935895748880) |
| x | XJosh | ^222 c5 | [@KiwiFarmsDotNet @Cloudflare P.S. @eastdakota has both my account and the Kiwi F](https://x.com/XJosh/status/2058609831565472002) |
| x | levelsio | ^207 c7 | [@jackfriks @postbridge_ @supabase Please let me replace that db with $0 SQLite 😭](https://x.com/levelsio/status/2058206568370295044) |
| x | tech_twi | ^204 c9 | [So 25,000 GHC for a data system fee na Supabase subscription koraa y3 $25. NDC i](https://x.com/tech_twi/status/2058224880647131547) |
| x | RoundtableSpace | ^190 c15 | [SCRAPLING JUST MADE WEB SCRAPING 774X FASTER THAN BEAUTIFULSOUP WHILE BYPASSING ](https://x.com/RoundtableSpace/status/2058129561343463822) |
| x | Hi_Mrinal | ^184 c7 | [I actually love to build my side project using go, etcd, sysbench, toxiproxy, gr](https://x.com/Hi_Mrinal/status/2058557056941248789) |
| x | cramforce | ^177 c23 | [For a company like Vercel it is hard to say things like "100% of code is agent w](https://x.com/cramforce/status/2058549755169636673) |
| x | Mayurasfeathers | ^177 c6 | [#MLBS6SPOILERS the honeycomb pattern on her clothes the bee themed outfit for he](https://x.com/Mayurasfeathers/status/2058451461936189564) |
| x | Akintola_steve | ^167 c10 | [Don't just learn how to code, Learn tools. For load testing to see how your syst](https://x.com/Akintola_steve/status/2058221171007512795) |
| x | bykarthikreddy | ^165 c3 | [- The website's domain was put on "clientHold" status by its registrar (Hostinge](https://x.com/bykarthikreddy/status/2058154816564781474) |
| x | wickedguro | ^161 c33 | [Postiz is currently on $105k MRR. My infrastructure is actually very cheap: > Ra](https://x.com/wickedguro/status/2058398638653800492) |
| x | yoginth | ^160 c1 | [Shipped S3 and @Cloudflare R2 connector sync + realtime socket updates for https](https://x.com/yoginth/status/2058244142594195855) |
| x | ChrisElliottux | ^155 c21 | [@rauchg Built with Opus 4.6 and 4.7 hosted on Vercel. https://t.co/C4CIa8Nzpt](https://x.com/ChrisElliottux/status/2058294078240903511) |
| x | akinkunmi | ^149 c8 | [Delivering 15TB of 4K video with Cloudflare R2 for $2.18 https://t.co/EErHbKjidz](https://x.com/akinkunmi/status/2058646916779356339) |
| x | swapsk | ^129 c12 | [@openletteryt Clearly can see the domain NS was changed. This us due to Gov repo](https://x.com/swapsk/status/2058204202740990094) |
| x | acoyfellow | ^127 c2 | ["Share": temporary, resumable file transfers on @Cloudflare - Instant share link](https://x.com/acoyfellow/status/2058513529804587492) |
| x | gazeldav | ^127 c103 | [Wild honeycomb harvest from wooden barrel https://t.co/wxn6BdagNJ](https://x.com/gazeldav/status/2058794887424938048) |
| x | N4pstr | ^126 c12 | [just making sure but a cloudflare dns setup should be *good enough* to hide my I](https://x.com/N4pstr/status/2058254124399870319) |
| x | rgbdev | ^123 c1 | [Platform OS &amp; Linux Kernel Troubleshooting Networking Container K8s Cloud IA](https://x.com/rgbdev/status/2058506284761055408) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bodhi3attva</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7592 · 💬 136</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bodhi3attva/status/2058118651505729733">View @bodhi3attva on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Government block claim is misleading. Technical checks show: &gt; Domain is on clientHold status &gt; Public DNS resolvers like Google (8.8.8.8) and Cloudflare (1.1.1.1) now return NXDOMAIN &gt; Website earlie”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>การวิเคราะห์ DNS แสดงว่า domain ที่ขึ้น clientHold และ return NXDOMAIN บน public resolver คือ registrar/hosting ระงับบริการ ไม่ใช่รัฐบาลบล็อก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แยกชัดระหว่าง government block (DNS ยังแก้ได้แต่ ISP ตัด) กับ clientHold (DNS ดับเลย) — อ่านผิดทำให้ debug incident ผิดทิศ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เวลา domain หรือ app ที่ deploy ไม่ตอบสนอง ให้เช็ค DNS ที่ 8.8.8.8/1.1.1.1 และดู registrar status ก่อนเลย อย่าเพิ่ง escalate ไป hosting หรือ infra</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bodhi3attva/status/2058118651505729733" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LayoffAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2288 · 💬 88</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LayoffAI/status/2058558639460192708">View @LayoffAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“CHAMATH TO CLOUDFLARE CEO: SHUT THE FUCK UP Literally. He just destroyed him on the All-In podcast yesterday. Called his layoff op-ed &quot;from the PR school of retards.&quot; Hard to disagree with him on this”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Chamath Palihapitiya ออกมาโจมตี CEO ของ Cloudflare สดๆ ใน All-In podcast ว่า op-ed เรื่อง layoff ที่เขียนเป็นแค่ PR ลมๆ แล้งๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>CEO ของ cloud vendor ระดับโลกโดนประจาน live เพราะห่อ layoff ด้วยภาษา PR — สัญญาณว่า communicate ตรงๆ กลายเป็น baseline ไปแล้ว ไม่ใช่ bonus</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า studio ต้องปรับทีมหรือลดคน ข้ามรูปแบบ op-ed ไปเลย — แจ้งตรงๆ ภายในดีกว่า PR ขัดเงาเสมอสำหรับทีมเล็ก</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LayoffAI/status/2058558639460192708" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@shortmagsmle</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1814 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/shortmagsmle/status/2058156142090506368">View @shortmagsmle on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">““No man you don’t get it, my foreign co-founder is REALLY good at using Claude to connect Supabase to Vercel. America will never make it without him! Why, just last week he created a minimalist UI exp”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์เสียดสีการ hype การใช้ Claude ทำงานพื้นฐาน เช่น connect Supabase กับ Vercel และสร้าง to-do reminder UI แล้วนำเสนอราวกับเป็นทักษะหายาก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>มุกนี้แม่นเพราะงานพวกนี้เป็น entry-level จริงๆ สะท้อนว่า AI-assisted dev กลาย commodity แล้ว มูลค่าของงาน integration พื้นฐานลดลงชัดเจน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Web stack ของ studio ใช้ Next.js + Supabase อยู่แล้ว สัญญาณคือหยุด pitch งาน Supabase-Vercel wiring พื้นฐาน แล้วโฟกัส higher-value งานแทน เช่น real-time sync, RLS design, หรือ XR data pipeline</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/shortmagsmle/status/2058156142090506368" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KiwiFarmsDotNet</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 838 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KiwiFarmsDotNet/status/2058609650472218969">View @KiwiFarmsDotNet on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Despite deplatforming the Kiwi Farms, 8chan, the Daily Stormer, and other websites under pressure, @Cloudflare continues to be in the crosshairs of the ADL, which demands more effort to clamp down on ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Cloudflare ยังโดน ADL กดดันให้แบน site เพิ่ม แม้จะเคย deplatform Kiwi Farms, 8chan, Daily Stormer ไปแล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยืนยันว่า CDN/DDoS provider ตัด service ได้ทุกเมื่อถ้าโดนกดดัน — ความเสี่ยง vendor-lock ที่จริงมากสำหรับทุก project</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Studio ต้องไม่ใช้ Cloudflare เป็น single point. เตรียม fallback CDN (เช่น Bunny.net หรือ AWS CloudFront) พร้อม runbook ไว้ก่อนที่จะฉุกเฉิน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KiwiFarmsDotNet/status/2058609650472218969" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jackfriks</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 780 · 💬 195</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jackfriks/status/2058198360691998942">View @jackfriks on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“my solo business @postbridge_ is at $35,000 USD monthly recurring revenue (MRR) = ±$48,000 CAD for my canadian friends and me here is main breakdown of major costs to run atm - i'm wondering if i shou”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Solo founder @postbridge_ เปิด MRR $35K USD ค่า infra แค่ $1,950/เดือน (Supabase $860, Vercel $130, Trigger.dev $400, Unkey $250, X API $250) — gross margin ~94%, net ~88%</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>พิสูจน์จริงว่า Next.js + Supabase SaaS ไปถึง $35K MRR ได้ ค่า infra ไม่ถึง $2K — Supabase แพงสุดที่ $860 แต่ margin ยังอยู่ที่ ~94%</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Stack ของ studio ตรงกันเลย (Next.js + Supabase) — ใช้เป็น benchmark เรื่องค่าใช้จ่ายตาม scale ได้เลย อย่าไป optimize infra ตอน margin ดี เอาแรงไป ship feature เร็วขึ้นดีกว่า</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jackfriks/status/2058198360691998942" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 744 · 💬 63</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2058248513662697622">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Still limited by compute, so I built a thing that runs codex in the cloud, powered by @Cloudflare firecracker boxes (and since that's not beefy enough for larger projects, tests are run via crabbox) U”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete สร้าง cloud runner ให้ OpenAI Codex รันบน Cloudflare Firecracker microVMs โดย test หนักๆ ส่งไป 'crabbox' แยก, ใช้ Ghostty terminal ผ่าน WebAssembly — และ Codex แทบ replicate ตัวเองได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แยก compute แบบ hybrid — Firecracker microVM เบาสำหรับงาน interactive, box ใหญ่สำหรับ test — เป็น pattern ประหยัดที่ทีมเล็กลอกได้เลยบน Cloudflare หรือ infra คล้ายกัน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">studio ใช้ pattern นี้ใน CI ได้เลย: lint และ check เบาๆ รันบน microVM, full build/test suite ส่งไป runner ใหญ่กว่า — ลด idle cloud spend และ feedback loop เร็วขึ้น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2058248513662697622" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DavidFrosdick</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 720 · 💬 59</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DavidFrosdick/status/2058582571194187819">View @DavidFrosdick on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I did it 👍 thanks @levelsio for sharing. Setup @Tailscale on my @Hetzner_Online VPS 🙌 Installed @claudeai on VPS 🤞 All my sites run through @Cloudflare tunnels 😎 Got @TermiusHQ running locally on my M”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>คนที่ไม่ใช่ developer ตั้งระบบ self-hosted VPS ด้วย Tailscale, Hetzner, Cloudflare tunnels และ Claude AI ทำให้ manage โปรเจกต์ 25GB และ code ได้จาก iPhone ขณะออกไปข้างนอก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Stack นี้ทั้งหมด — VPS + Tailscale + Cloudflare tunnel + Claude AI + Termius — ค่าใช้จ่ายไม่ถึง $20/เดือน แต่ทำให้ deploy fix จาก phone ได้โดยไม่ต้องพกแล็ปท็อป</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Studio ทำ setup เดียวกันสำหรับ on-call web deploy ได้: Hetzner VPS ผ่าน Cloudflare tunnel, Tailscale สำหรับ SSH ปลอดภัย, Claude AI ช่วยใน terminal — ให้ทีม hotfix Next.js หรือ Supabase จาก phone ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DavidFrosdick/status/2058582571194187819" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rileybrown</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 584 · 💬 77</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rileybrown/status/2058330104988844348">View @rileybrown on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Supabase will likely be worth more than Lovable Replit and Bolt combined when it’s all said and done.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนาคาดว่า Supabase จะมี valuation สูงกว่า Lovable, Replit, และ Bolt รวมกัน — ชี้ว่าเป็น backend platform ที่ dominant ที่สุด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Supabase วางตัวเป็น core infrastructure ไม่ใช่ AI coding tool — ประเภทนี้ได้ valuation สูงกว่าและ enterprise ติด long-term มากกว่า</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Studio ใช้ Next.js + Supabase อยู่แล้ว ลงทุน skill ใน Edge Functions, Realtime, Vector ตอนนี้ก่อน platform โต แล้วค่าใช้จ่ายจะแพงขึ้น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rileybrown/status/2058330104988844348" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
