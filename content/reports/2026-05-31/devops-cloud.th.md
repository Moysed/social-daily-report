---
type: social-topic-report
date: '2026-05-31'
topic: devops-cloud
lang: th
pair: devops-cloud.en.md
generated_at: '2026-05-31T04:27:44+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 100
salience: 0.55
sentiment: mixed
confidence: 0.58
tags:
- vercel
- cloudflare
- supabase
- cost-optimization
- observability
- security
thumbnail: https://pbs.twimg.com/media/HJgHDctXcAcja_F.png
translated_by: claude-sonnet-4-6
---

# DevOps & Cloud — 2026-05-31

## TL;DR
- Vercel Sandbox รัน Docker container แบบ full isolation ได้แล้ว — ครอบคลุม database, test suite, แอปเต็มรูปแบบ พร้อม persist installs/images ข้ามเซสชัน [14][36]
- แรงกดด้านต้นทุนของ managed PaaS ดังที่สุดในสัปดาห์นี้: มีม '$5 VPSification of Vercel' [13], เรียกร้องให้ Vercel มี tier แบบ EC2 [55], ร้องเรียนเรื่อง invoice [33] — ตรงข้ามกับผู้ใช้ Cloudflare ที่รายงานค่าใช้จ่าย $0 [58] และ free tier ครอบคลุมทั้ง project [31][34]
- Cloudflare Durable Objects ใช้งานได้ผ่าน SST แล้ว [21] และ Cloudflare กำลังสร้าง Web Search สำหรับ Workers/agents [16]
- สัญญาณความปลอดภัย: Ghost CMS มีช่อง SQL injection ที่ให้ผู้โจมตีระยะไกลขโมย admin API key, แก้ไขโพสต์, และฝัง JS ได้ [26]; ชื่อเสียงของ Supabase เรื่อง 'ถูกแฮก' ยังคงวนเวียนเป็น joke ซ้ำๆ [49]
- ผลลัพธ์ด้าน observability ชัดเจน: การเชื่อม Claude เข้ากับ trace ของ observability พบ bottleneck 5 วินาที และเร่งความเร็ว Platzi ได้ [9]; Expo เปิด beta สำหรับ mobile observability [20]

## สิ่งที่เกิดขึ้น
ฝั่ง deploy/runtime — Vercel ส่ง Docker container support เข้า Sandbox รองรับ isolated build, database, และ test suite พร้อม persist image [14][36] และถูก position ไว้สำหรับ conversational/Slack workflow และ AI Gateway [43][11] กระแสเรื่องต้นทุนไหลแรงตลอดฟีด: มีม '$5 VPSification of Vercel' [13], คำขอ Vercel EC2 alternative [55], คำร้องเรียนในรูปแบบ invoice ก้อนใหญ่ [33] และคำชม Cloudflare เรื่อง $0/free-tier [58][31][34] ที่ตรงกันข้าม Railway ครอง engagement แต่ส่วนใหญ่เป็นโพสต์ brand/meme (การตั้งชื่อ CDN POP ว่า 'shupo') ไม่ใช่ข่าวเชิงเทคนิค [2][4][6][12] Cloudflare Durable Objects เข้า SST แล้ว [21], Cloudflare กำลังสร้าง Web Search สำหรับ Workers/agents [16] และมีการสาธิต edge/WASM PDF parsing (LiteParse) บน Workers [19][29]

## ทำไมถึงสำคัญ
สำหรับ studio ที่ใช้ Next.js + Supabase เรื่องต้นทุนคือสิ่งที่ต้องลงมือทำ บทสนทนา VPSification [13][55] และโพสต์ Cloudflare $0-bill [58][34] สะท้อนทีมจริงที่กำลังย้าย stateless/low-traffic workload ออกจาก per-invocation managed pricing ไปสู่ flat-rate compute (Hetzner/Railway/Coolify [3][2][5]) เพื่อลดค่า runtime Vercel Docker-in-Sandbox [14][36] ลดความจำเป็นในการมี CI box แยกหรือ local Docker สำหรับ ephemeral test/build environment ซึ่งช่วยให้ CI/CD เรียบง่ายขึ้น ด้าน reliability — กรณี Platzi [9] แสดงให้เห็นว่า AI-assisted trace analysis หา latency bottleneck ที่การ review แบบ manual พลาด ซึ่งตรงกับการลด alert กลางดึก ส่วนเรื่องความปลอดภัย: Ghost CMS SQLi [26] คือ CVE-class issue ที่ยังมีชีวิตหากมี marketing site รัน Ghost อยู่ และมีม Supabase 'ถูกแฮก' [49] เตือนว่า Supabase row-level-security misconfiguration คือความล้มเหลวที่ production จริงพบบ่อย ไม่ใช่เรื่องแปลกใหม่

## แนวโน้ม
Likely: แรงกดด้านต้นทุน managed-PaaS ดันทีมสู่ hybrid setup — คง Vercel ไว้สำหรับ Next.js frontend/edge, ย้าย always-on service ไป flat-rate VPS/container [13][55][58] Plausible: Vercel เพิ่ม longer-running/cheaper compute tier เพราะ demand ซ้ำๆ [55] และทิศทาง Docker Sandbox [14][36] Plausible: Cloudflare agent/Web Search และ Durable Objects [16][21][51] ทำให้มันเป็น backend ที่สมบูรณ์กว่าสำหรับ edge-first app — แต่ agentic-TPS claims [51] ยังเป็น vendor projection ไม่ใช่ capacity ที่ deliver ได้จริง ไม่น่าส่งผลต่อ studio ในระยะใกล้: รายการ quantum/honeycomb, WWE poster และ crypto/WorldID [17][39][46] — noise ทั้งหมด ไม่มีแหล่งใดให้ตัวเลขความน่าจะเป็นที่เชื่อถือได้ จึงไม่ระบุ

## การนำไปใช้ใน NDF DEV
1) ตรวจ Vercel + Supabase spend รายเดือน เทียบกับ flat-rate alternative สำหรับ always-on หรือ background workload — ย้ายเฉพาะ stateless/cron-style job, คง Next.js edge ไว้บน Vercel (med, [13][53][58]) 2) ทดลอง Vercel Docker Sandbox สำหรับ ephemeral integration test แทน CI runner แยก (low, [14][36]) 3) ทำ Supabase RLS + key-exposure review บน production project — pattern 'ถูกแฮก' อยู่ที่ config ไม่ใช่ platform (med, [49][28]) และนำ Supabase Postgres best-practice skill มาใช้ถ้าใช้ Codex/AI tooling (low, [28]) 4) หาก site ใดรัน Ghost CMS ให้ patch SQLi ทันทีและ rotate admin API key (low/urgent, [26]) 5) ทดลอง AI-over-traces หา latency บน production endpoint ที่ช้า ก่อนเพิ่ม dashboard ใหม่ (med, [9]) ข้าม: Railway brand meme [2][4][6], โพสต์ Cloudflare layoff/crypto/quantum/architecture [37][46][17][50] — ไม่มี action เชิง operational

## Signals to Watch
- การตอบสนองของ Vercel ต่อ demand 'cheaper/longer-running compute' ซ้ำๆ — จับตา EC2-style หรือ flat tier [55][13]
- Cloudflare Web Search for Workers ถึง GA หรือยัง — สำคัญถ้ากำลังสร้าง agent feature [16]
- สถานะ patch Ghost CMS SQLi และรายงาน exploit-in-wild [26]
- ความสมบูรณ์ของ Cloudflare Durable Objects + SST ในฐานะ stateful-edge option สำหรับ Next.js backend [21]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bluntsmokr45 | ^29752 c27 | [im a cloudflare rapper](https://x.com/bluntsmokr45/status/2060342648146190621) |
| x | Railway | ^9367 c187 | [https://t.co/PLdn2N1GK8 https://t.co/nHw363jtqc](https://x.com/Railway/status/2060411091725832643) |
| x | catalinmpit | ^1481 c147 | [I've deployed my Hermes agent on a Hetzner VPS. The security measures I've taken](https://x.com/catalinmpit/status/2060351831826628650) |
| x | Railway | ^910 c2 | [@zeroxdayz Not hacked- shupo Hikari is the name of one of the high-speed Shinkan](https://x.com/Railway/status/2060566138522599464) |
| x | theo | ^860 c49 | [First donation is up, just gave $2,000 to @heyandras to support open source alte](https://x.com/theo/status/2060494740433571955) |
| x | Railway | ^693 c0 | [@rv32e shupo](https://x.com/Railway/status/2060486690351812987) |
| x | immad | ^562 c25 | [Every VC had a reason Vercel shouldn't exist. Guillermo Rauch heard a different ](https://x.com/immad/status/2060466505251197435) |
| x | arpit_bhayani | ^422 c25 | [Everyone talks about agent intelligence. Then agents reach production - or face ](https://x.com/arpit_bhayani/status/2060717906296803457) |
| x | freddier | ^408 c22 | [Claude made Platzi 10x faster. Platzi's dev team connected Claude to our observa](https://x.com/freddier/status/2060481390874148878) |
| x | Railway | ^406 c4 | [We're in good company https://t.co/RdcAnhDKnZ](https://x.com/Railway/status/2060473943799062840) |
| x | xai | ^377 c16 | [It's also available via OpenRouter and Vercel AI Gateway, as well as in Cursor, ](https://x.com/xai/status/2060392251520594105) |
| x | Railway | ^376 c0 | [@disk_writes shupo](https://x.com/Railway/status/2060486704427848062) |
| x | jacobmparis | ^355 c10 | [the $5 VPSification of vercel is well underway](https://x.com/jacobmparis/status/2060447494924902547) |
| x | vercel_dev | ^344 c14 | [Run Docker inside Vercel Sandbox. ▪︎ Build and run containers in full isolation ](https://x.com/vercel_dev/status/2060443240902627388) |
| x | freeCodeCamp | ^331 c2 | [Building a basic RAG system is one thing. Making it secure, scalable, and produc](https://x.com/freeCodeCamp/status/2060572170988761187) |
| x | CherryJimbo | ^312 c20 | [Cloudflare is working on Web Search, giving AI agents and Workers real-time acce](https://x.com/CherryJimbo/status/2060717359979958513) |
| x | CharlesMullins2 | ^302 c19 | [🚨 SCIENTISTS MAY HAVE FOUND A CHEAPER PATH TO QUANTUM COMPUTERS AND IT LOOKS LIK](https://x.com/CharlesMullins2/status/2060424341268164706) |
| x | 31Carlton7 | ^297 c31 | [just wrapped up my first week at @vercel and @aisdk initial thoughts: - pace is ](https://x.com/31Carlton7/status/2060804842868908427) |
| x | jerryjliu0 | ^275 c4 | [Parse PDFs in the browser, or the edge, in milliseconds Our LiteParse WASM packa](https://x.com/jerryjliu0/status/2060395856860455265) |
| x | expo | ^233 c7 | [🆕 Today we open up the beta for our new mobile Observability service. If you've ](https://x.com/expo/status/2060423327781700091) |
| x | vimtor | ^228 c10 | [hate them or love them: they are inevitable @cloudflare durable objects are now ](https://x.com/vimtor/status/2060372357001175392) |
| x | Umesh__digital | ^188 c33 | [Top tech skills to have in your CV in 2026 1. Distributed Caching : Redis, Memca](https://x.com/Umesh__digital/status/2060253161525584137) |
| x | DennisAdriaans | ^187 c3 | [Introducing DashboardStack Beta Schema-driven Dashboard Primitives: - DB - Auth ](https://x.com/DennisAdriaans/status/2060332236986036469) |
| x | QuinnyPig | ^151 c2 | [So @cloudflare has been saying they're an agentic cloud. Let's test the theory. ](https://x.com/QuinnyPig/status/2060523529494569023) |
| x | tobiaslins | ^147 c7 | [We've been using similar concepts when building Vercel Data Pipeline - Processin](https://x.com/tobiaslins/status/2060782772461973622) |
| x | Playerinthgame | ^129 c3 | [What does this mean? Ghost is a widely used CMS. A SQL injection flaw lets remot](https://x.com/Playerinthgame/status/2060397849305575536) |
| x | pythontrending | ^129 c1 | [awesome-harness-engineering - Awesome list for AI agent harness engineering: too](https://x.com/pythontrending/status/2060395787901702207) |
| x | supabase | ^121 c7 | [The official "Build Web Apps" plugin for Codex ships with the Supabase Postgres ](https://x.com/supabase/status/2060732268696555549) |
| x | llama_index | ^119 c8 | [When we say "LiteParse runs everywhere," we mean it. Our WASM package is lightwe](https://x.com/llama_index/status/2060392729910116830) |
| x | haider__anis | ^112 c30 | [Was scrolling through product launches today like I always do… Then I saw Enter ](https://x.com/haider__anis/status/2060332723752108152) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bluntsmokr45</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 29752 · 💬 27</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bluntsmokr45/status/2060342648146190621">View @bluntsmokr45 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“im a cloudflare rapper”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ล้อเล่นคำว่า 'cloudflare rapper' ไม่มีเนื้อหาเทคนิคใดๆ</dd>
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
    <span class="ndf-engagement">♥ 9367 · 💬 187</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Railway/status/2060411091725832643">View @Railway on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/PLdn2N1GK8 https://t.co/nHw363jtqc”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Railway ขยาย CDN เพิ่ม edge ใน Singapore (sin1) และเปิด endpoint /.railway/cdn-trace ให้ตรวจสอบว่า request ถูก route ผ่าน region และ node ไหน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Edge Singapore ลด latency สำหรับ user ในไทย/ASEAN — มีผลกับทุก project ที่ deploy บน Railway และมี target user ใน region นี้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง GET /.railway/cdn-trace บน app ที่ deploy บน Railway เพื่อเช็กว่า traffic route ผ่าน sin1 แล้วหรือยัง — ถ้าไม่ใช่ให้ดู region settings</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Railway/status/2060411091725832643" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@catalinmpit</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1481 · 💬 147</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/catalinmpit/status/2060351831826628650">View @catalinmpit on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I've deployed my Hermes agent on a Hetzner VPS. The security measures I've taken so far: - Installed Tailscale and restricted SSH access to Tailscale IPs only - Blocked all ports except 80 and 443 - R”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@catalinmpit แชร์ checklist hardening VPS บน Hetzner สำหรับ deploy AI agent: SSH ผ่าน Tailscale เท่านั้น, UFW เปิดแค่พอร์ต 80/443 และ allowlist เฉพาะ IP ของ Cloudflare พร้อมปิด password login</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>5 ขั้นนี้ครอบ attack vector หลักของ VPS สาธารณะได้โดยไม่ต้องใช้ tooling หนัก — เหมาะกับทีมเล็กที่ดูแล server เอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เอา stack นี้มาทำเป็น provisioning checklist มาตรฐานสำหรับทุก VPS project ก่อน go live</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/catalinmpit/status/2060351831826628650" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Railway</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 910 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Railway/status/2060566138522599464">View @Railway on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@zeroxdayz Not hacked- shupo Hikari is the name of one of the high-speed Shinkansen Hikari is also the codename of our fleet of CDN POPs around the world that makes our website super fast pic maybe re”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Railway ชี้แจงว่า 'Hikari' คือชื่อ codename ของ CDN POP fleet ทั่วโลก ตั้งตามชื่อรถไฟ Shinkansen หลังมีคนเข้าใจผิดว่าถูก hack</dd>
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
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 860 · 💬 49</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2060494740433571955">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“First donation is up, just gave $2,000 to @heyandras to support open source alternatives to Codex App and Claude Desktop 🫡 Also pumped that this can help with Coolify, the coolest open source hosting ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Theo บริจาค $2,000 เพื่อ open-source dev tools และแนะนำ Coolify เป็น self-hosted deployment แทน Vercel</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Coolify เป็น self-hosted platform ฟรีแทน Vercel/Netlify ลดต้นทุน hosting สำหรับ web projects หลายตัวได้จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดลอง Coolify กับ web project ที่ไม่ critical เพื่อเทียบ workflow และค่า hosting กับ Vercel ที่ใช้อยู่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2060494740433571955" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Railway</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 693 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Railway/status/2060486690351812987">View @Railway on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@rv32e shupo”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Account ของ Railway โพสต์ข้อความ '@rv32e shupo' ซึ่งไม่มีความหมายหรือบริบทใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Railway/status/2060486690351812987" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@immad</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 562 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/immad/status/2060466505251197435">View @immad on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Every VC had a reason Vercel shouldn't exist. Guillermo Rauch heard a different reason from every investor he spoke to when building Vercel, and he kept going anyway. He joined us live at Mercury HQ i”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Podcast Founders in Arms ของ Mercury ดึง Guillermo Rauch (CEO, Vercel) มาพูดถึง fundraising — ถ้า VC แต่ละคน reject ด้วยเหตุผลต่างกัน นั่นคือสัญญาณให้เดินหน้า ไม่ใช่หยุด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/immad/status/2060466505251197435" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@arpit_bhayani</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 422 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/arpit_bhayani/status/2060717906296803457">View @arpit_bhayani on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Everyone talks about agent intelligence. Then agents reach production - or face even the slightest bit of load - and suddenly the hard problems are: - memory management - concurrency - backpressure - ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Arpit Bhayani ชี้ว่า AI agents ที่ deploy จริงมักพังเพราะปัญหา infra พื้นฐาน เช่น memory, concurrency, backpressure, retries, timeouts, observability ไม่ใช่เรื่อง intelligence</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่ build agentic features เช่น Unity automation หรือ e-learning bots จะเจอปัญหาเหล่านี้จริง — distributed-systems hygiene สำคัญพอๆ กับ prompt design</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ก่อน deploy agent loop ทุกโปรเจกต์ กำหนด retry/timeout policy และเพิ่ม structured logging ก่อน — handle มันเหมือน async service ทั่วไป</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/arpit_bhayani/status/2060717906296803457" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
