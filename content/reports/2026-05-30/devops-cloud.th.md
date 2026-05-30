---
type: social-topic-report
date: '2026-05-30'
topic: devops-cloud
lang: th
pair: devops-cloud.en.md
generated_at: '2026-05-30T18:46:59+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 122
salience: 0.5
sentiment: mixed
confidence: 0.6
tags:
- vercel
- cloudflare
- supabase
- observability
- ci-cd
- cost
thumbnail: https://pbs.twimg.com/media/HJgHDctXcAcja_F.png
translated_by: claude-sonnet-4-6
---

# DevOps & Cloud — 2026-05-30

## TL;DR
- Vercel ปล่อย CLI ในรูปแบบ signed native binary: เล็กลง ~80%, startup เร็วขึ้น, เก็บ credential ใน OS keychain ปลอดภัยกว่าเดิม [30][31][55]
- Vercel Sandbox รองรับ Docker containers แล้ว (databases, test suites, FUSE, VPNs) แบบ isolation — feature ที่ถูกขอมากที่สุด [17][47]
- แรงกดด้านต้นทุนของ Vercel/Supabase ชัดเจนขึ้น: กระแส '$5 VPSification', self-hosting ด้วย Hetzner+Tailscale และ Coolify เป็น open-source hosting [16][4][6]
- ClickHouse ขยับขึ้น up-stack เพื่อแข่งกับ Datadog ด้าน analytics/observability ซึ่งสะท้อนสัญญาณด้านค่า runtime [37]; Supabase Postgres best-practice guidance ถูกรวมใน Codex web-apps plugin แล้ว [53]
- สัญญาณด้าน security และ vendor: Ghost CMS มี SQL injection ให้ผู้โจมตีขโมย admin API keys และฝัง JS ได้ [35]; Cloudflare ประกาศลดพนักงาน ~20% [59]

## สิ่งที่เกิดขึ้น
Vercel ผลัก platform changes หลายอย่าง: CLI แบบ native binary แบบ experimental (opt-in ผ่าน @vercel/vc-native) เล็กลง ~80% startup เร็วขึ้น พร้อม signing บน macOS/Windows เพื่อเก็บ credential อย่างปลอดภัย [30][31][55], Docker support ใน Vercel Sandbox [17][47] และ 'Vercel Agent Infrastructure' (skills, plugin, CLI) [29] ฝั่ง Cloudflare หลักๆ อยู่กับ Workers/edge platform: Browser Run quick actions (screenshot, pdf, markdown, scrape, crawl) [11], Web Search API สำหรับ agents/Workers ที่วางแผนไว้ [25], Durable Objects ที่ landing ใน SST [26], R2 object storage [50], Access SSO สำหรับ internal apps [49] และรายงานการลดพนักงาน ~20% [59] Supabase ปล่อย Postgres Best Practice skill ใน Codex 'Build Web Apps' plugin [53] และเพิ่ม NodeOps เข้า ecosystem [54]

## ทำไมถึงสำคัญ (เหตุผล)
สำหรับทีมที่ใช้ Next.js + Supabase ประโยชน์จริงอยู่ที่ด้าน operational ไม่ใช่ความแปลกใหม่ Vercel CLI binary แบบ signed ที่ไม่มี dependency ช่วยลดความเสี่ยง supply-chain และ credential-leak ใน CI/CD และเร่ง agent-driven deploys [30][31] Docker ใน Vercel Sandbox ทำให้ ephemeral DBs/test suites รันใกล้ deploy platform ได้โดยไม่ต้องใช้ infra แยก [17][47] กระแสเรื่องต้นทุน — '$5 VPSification', Hetzner+Tailscale, Coolify — สะท้อนการที่ทีมต่างๆ ต้านค่าใช้จ่าย managed platform ซึ่งเป็น tradeoff เดียวกับที่ studio เผชิญ [16][4][6] ClickHouse เล็งไปที่ Datadog บอกว่าราคา observability สามารถถูกท้าทายได้ ซึ่งเกี่ยวข้องถ้า monitoring spend เพิ่มขึ้น [37] Ghost SQLi เตือนอย่างชัดเจนว่า self-hosted CMS layer ขยายพื้นที่โจมตี [35] และการลดพนักงานของ Cloudflare เป็นข้อมูล vendor stability ที่ควรพิจารณาก่อนพึ่งพาเพิ่ม [59]

## ความเป็นไปได้
**Likely:** Vercel native CLI จะ graduate จาก experimental สู่ default เพราะมีเหตุผลด้าน security ชัดเจน (signing, keychain storage) [31][55] **Plausible:** studio มากขึ้นจะแยก workload — ใช้ Next.js บน Vercel แต่ย้าย object storage, background jobs หรือ low-traffic apps ไปที่ Cloudflare R2/Workers หรือ VPS ราคาถูกเพื่อลดค่าใช้จ่าย [16][41][50] **Plausible:**ค่าใช้จ่ายด้าน observability จะถูกทบทวนเมื่อ ClickHouse-based options พัฒนาขึ้นมาเทียบกับ Datadog [37] **Unlikely ระยะสั้น:** migration ออกจาก Supabase/Vercel ทั้งหมดสำหรับ production app ที่กำลังใช้งาน — claim ว่า 'replace your whole stack' [38] เป็น marketing ไม่ใช่ข้อมูลที่ผ่านการพิสูจน์ ไม่มีแหล่งใดให้ตัวเลข probability

## การนำไปใช้สำหรับ NDF DEV
นำ Vercel native CLI binary เข้า CI lane ที่ไม่ใช่ production และประเมิน keychain credential storage (low effort) [55][31] ทดลอง Docker-in-Vercel-Sandbox สำหรับ ephemeral integration tests / throwaway Postgres แทน standing infra (med) [17][47] นำ Supabase Postgres Best Practice skill เข้า Codex/agent setup ของทีมเพื่อ standardize schema และ query patterns (low) [53] Audit Ghost/CMS instances ทุกตัวและ patch SQLi ทันที; rotate admin API keys ถ้า exposed (low–med) [35] สำหรับ internal tools traffic ต่ำ ลองต้นแบบ Cloudflare Access SSO + R2 เป็น host ที่ถูกกว่า always-on Vercel (med) [49][50][41] บันทึก Cloudflare layoffs ไว้เป็น vendor-risk item ก่อนขยายการพึ่งพา (low) [59] **ข้ามได้:** product pitch ประเภท 'replace Supabase/Vercel ทั้งหมด' [38], GTM-engineering และ VC-story threads [8][10] และ noise ที่ไม่มีสัญญาณทุกประเภท [1][7][9][18][33][58]

## Signals ที่ต้องติดตาม
- Vercel native binary CLI เดินหน้าสู่ signed default — ตรวจอีกครั้งก่อน standardize deploy tooling [55][31]
- ClickHouse vs Datadog ด้านต้นทุน observability — จับตา self-hostable monitoring ที่ลดค่าใช้จ่าย [37]
- Cloudflare ~20% layoffs — ติดตาม service/SLA impact ก่อนพึ่งพาเพิ่ม [59]
- momentum ของ cheap-host (Coolify, Hetzner+Tailscale, '$5 VPS') ในฐานะ Vercel cost hedge [6][4][16]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bluntsmokr45 | ^28299 c22 | [im a cloudflare rapper](https://x.com/bluntsmokr45/status/2060342648146190621) |
| x | Railway | ^6311 c149 | [https://t.co/PLdn2N1GK8 https://t.co/nHw363jtqc](https://x.com/Railway/status/2060411091725832643) |
| x | lennysan | ^1482 c188 | [Fascinating results + Anthropic running away with it right now + So many people ](https://x.com/lennysan/status/2060105044494872879) |
| x | catalinmpit | ^1387 c139 | [I've deployed my Hermes agent on a Hetzner VPS. The security measures I've taken](https://x.com/catalinmpit/status/2060351831826628650) |
| x | fayazara | ^814 c18 | [One of my favorite UI elements from the Cloudflare dashboard is now available fo](https://x.com/fayazara/status/2060120859311034675) |
| x | theo | ^773 c44 | [First donation is up, just gave $2,000 to @heyandras to support open source alte](https://x.com/theo/status/2060494740433571955) |
| x | Railway | ^540 c0 | [@zeroxdayz Not hacked- shupo Hikari is the name of one of the high-speed Shinkan](https://x.com/Railway/status/2060566138522599464) |
| x | immad | ^526 c24 | [Every VC had a reason Vercel shouldn't exist. Guillermo Rauch heard a different ](https://x.com/immad/status/2060466505251197435) |
| x | Railway | ^461 c0 | [@rv32e shupo](https://x.com/Railway/status/2060486690351812987) |
| x | fin465 | ^405 c27 | [Vercel replaced their 10 person sales team with 1 GTM engineer (managing AI agen](https://x.com/fin465/status/2060128443304657091) |
| x | fayazara | ^394 c14 | [Quick Actions in Cloudflare Browser Run - screenshot - content - pdf - markdown ](https://x.com/fayazara/status/2060077571694624782) |
| x | freddier | ^384 c21 | [Claude made Platzi 10x faster. Platzi's dev team connected Claude to our observa](https://x.com/freddier/status/2060481390874148878) |
| x | xai | ^365 c16 | [It's also available via OpenRouter and Vercel AI Gateway, as well as in Cursor, ](https://x.com/xai/status/2060392251520594105) |
| x | arpit_bhayani | ^328 c23 | [Everyone talks about agent intelligence. Then agents reach production - or face ](https://x.com/arpit_bhayani/status/2060717906296803457) |
| x | Railway | ^326 c3 | [We're in good company https://t.co/RdcAnhDKnZ](https://x.com/Railway/status/2060473943799062840) |
| x | jacobmparis | ^320 c9 | [the $5 VPSification of vercel is well underway](https://x.com/jacobmparis/status/2060447494924902547) |
| x | vercel_dev | ^315 c14 | [Run Docker inside Vercel Sandbox. ▪︎ Build and run containers in full isolation ](https://x.com/vercel_dev/status/2060443240902627388) |
| x | CharlesMullins2 | ^300 c19 | [🚨 SCIENTISTS MAY HAVE FOUND A CHEAPER PATH TO QUANTUM COMPUTERS AND IT LOOKS LIK](https://x.com/CharlesMullins2/status/2060424341268164706) |
| x | DivesTech | ^280 c11 | [Palantir,Datadog..Innodata..Snowflake..CRM (Agentforce)…now MongoDB…AI across da](https://x.com/DivesTech/status/2060092916723257405) |
| x | freeCodeCamp | ^270 c2 | [Building a basic RAG system is one thing. Making it secure, scalable, and produc](https://x.com/freeCodeCamp/status/2060572170988761187) |
| x | jerryjliu0 | ^263 c3 | [Parse PDFs in the browser, or the edge, in milliseconds Our LiteParse WASM packa](https://x.com/jerryjliu0/status/2060395856860455265) |
| x | evilrabbit_ | ^255 c18 | [Part of the Vercel Design Team in SF! https://t.co/3o92Rz4QgE](https://x.com/evilrabbit_/status/2060180320742510670) |
| x | Railway | ^250 c0 | [@disk_writes shupo](https://x.com/Railway/status/2060486704427848062) |
| x | expo | ^225 c7 | [🆕 Today we open up the beta for our new mobile Observability service. If you've ](https://x.com/expo/status/2060423327781700091) |
| x | CherryJimbo | ^219 c12 | [Cloudflare is working on Web Search, giving AI agents and Workers real-time acce](https://x.com/CherryJimbo/status/2060717359979958513) |
| x | vimtor | ^190 c9 | [hate them or love them: they are inevitable @cloudflare durable objects are now ](https://x.com/vimtor/status/2060372357001175392) |
| x | DennisAdriaans | ^187 c3 | [Introducing DashboardStack Beta Schema-driven Dashboard Primitives: - DB - Auth ](https://x.com/DennisAdriaans/status/2060332236986036469) |
| x | Umesh__digital | ^187 c33 | [Top tech skills to have in your CV in 2026 1. Distributed Caching : Redis, Memca](https://x.com/Umesh__digital/status/2060253161525584137) |
| x | MelkeyDev | ^177 c16 | [Skills, plugin, CLI and more Vercel Agent Infrastructure https://t.co/jnvCHAaNtT](https://x.com/MelkeyDev/status/2060203066776060308) |
| x | rauchg | ^168 c22 | [Vercel CLI as a self-updating binary with zero external dependencies. Our CLI is](https://x.com/rauchg/status/2060105470460010993) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bluntsmokr45</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 28299 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bluntsmokr45/status/2060342648146190621">View @bluntsmokr45 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“im a cloudflare rapper”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ X โพสต์ว่า 'im a cloudflare rapper' — เป็นแค่การเล่นคำ ไม่มีเนื้อหาเชิงเทคนิค</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bluntsmokr45/status/2060342648146190621" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Railway</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 6311 · 💬 149</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Railway/status/2060411091725832643">View @Railway on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/PLdn2N1GK8 https://t.co/nHw363jtqc”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Railway เปิด CDN edge layer ใหม่ codename 'hikari' v0.1.2 มี PoP ที่สิงคโปร์ (sin1) รองรับ WebSockets และ SSE เป็นส่วนหนึ่งของแผนขยาย datacenter อีก 4 regions เพื่อลด latency ในเอเชียและอเมริกาใต้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>PoP สิงคโปร์ทำให้ app ที่ deploy บน Railway ได้ TTFB ต่ำลงสำหรับผู้ใช้ไทย โดยไม่ต้องตั้งค่าอะไรเพิ่ม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เปิด railway.com/.railway/cdn-trace บน project ที่ deploy อยู่บน Railway เพื่อเช็คว่า route ผ่าน sin1 แล้วหรือยัง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Railway/status/2060411091725832643" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@lennysan</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1482 · 💬 188</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/lennysan/status/2060105044494872879">View @lennysan on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Fascinating results + Anthropic running away with it right now + So many people want to start their own company + Google over OpenAI + Vercel, Linear, Every, PostHog overperforming A great list if you”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Lenny Rachitsky แชร์ผล survey 'ที่ทำงานยอดนิยม' โดย Anthropic มาแรงสุด, Google แซง OpenAI, และ Vercel/Linear/PostHog ติดอันดับสูงกว่าคาด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/lennysan/status/2060105044494872879" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@catalinmpit</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1387 · 💬 139</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/catalinmpit/status/2060351831826628650">View @catalinmpit on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I've deployed my Hermes agent on a Hetzner VPS. The security measures I've taken so far: - Installed Tailscale and restricted SSH access to Tailscale IPs only - Blocked all ports except 80 and 443 - R”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@catalinmpit แชร์ checklist hardening VPS บน Hetzner สำหรับ AI agent: SSH ผ่าน Tailscale เท่านั้น, UFW เปิดแค่พอร์ต 80/443 ให้ Cloudflare IP ranges, ปิด password login</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เป็น baseline security สำหรับ VPS ที่ทำตามได้ทันที ครอบทั้ง network perimeter, SSH, และ firewall ในที่เดียว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ใช้ stack เดียวกัน (Tailscale + UFW + Cloudflare allowlist + key-only SSH) กับ VPS ของ studio ที่ host backend, bot, หรือ internal tools</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/catalinmpit/status/2060351831826628650" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@fayazara</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 814 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/fayazara/status/2060120859311034675">View @fayazara on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One of my favorite UI elements from the Cloudflare dashboard is now available for everyone to use in Kumo UI https://t.co/ZcrZ8jMkHk https://t.co/8BRIglnjfa”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Fayaz Ara เพิ่ม UI component สไตล์ Cloudflare dashboard เข้าไปใน Kumo UI ซึ่งเป็น open-source component library ของเขา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Component dashboard สำเร็จรูปช่วยประหยัดเวลา design สำหรับงาน web และ admin panel</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู component ใหม่ใน Kumo UI แล้วประเมินว่าใช้กับงาน web หรือ admin panel ของ studio ได้ไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/fayazara/status/2060120859311034675" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 773 · 💬 44</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2060494740433571955">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“First donation is up, just gave $2,000 to @heyandras to support open source alternatives to Codex App and Claude Desktop 🫡 Also pumped that this can help with Coolify, the coolest open source hosting ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Theo บริจาค $2,000 เพื่อสนับสนุน open-source alternatives ของ Codex App และ Claude Desktop พร้อมชี้ให้เห็น Coolify ในฐานะ self-hosted hosting แทน Vercel</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Coolify เป็น self-hosted PaaS แทน Vercel ได้ — ควบคุม infra เองเต็มที่ ค่ารายเดือนต่ำกว่า</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลองประเมิน Coolify สำหรับ host web projects แทน Vercel เพื่อลด cost และ vendor lock-in</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2060494740433571955" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Railway</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 540 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Railway/status/2060566138522599464">View @Railway on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@zeroxdayz Not hacked- shupo Hikari is the name of one of the high-speed Shinkansen Hikari is also the codename of our fleet of CDN POPs around the world that makes our website super fast pic maybe re”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Railway ชี้แจงว่า 'Hikari' คือ codename ของ CDN POP fleet ทั่วโลก ไม่ใช่ถูก hack — ตั้งชื่อตามรถไฟชินคันเซ็น Hikari</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Railway/status/2060566138522599464" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@immad</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 526 · 💬 24</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/immad/status/2060466505251197435">View @immad on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Every VC had a reason Vercel shouldn't exist. Guillermo Rauch heard a different reason from every investor he spoke to when building Vercel, and he kept going anyway. He joined us live at Mercury HQ i”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Mercury จัด founder talk โดย Guillermo Rauch CEO ของ Vercel เล่าว่า investor แต่ละคนปฏิเสธด้วยเหตุผลต่างกัน และมองว่า consensus ที่บอกว่า 'ไม่' คือสัญญาณให้เดินหน้า</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/immad/status/2060466505251197435" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
