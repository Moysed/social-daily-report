---
type: social-topic-report
date: '2026-06-04'
topic: devops-cloud
lang: th
pair: devops-cloud.en.md
generated_at: '2026-06-04T03:45:55+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- x
regions:
- global
post_count: 172
salience: 0.6
sentiment: mixed
confidence: 0.55
tags:
- cloudflare
- vercel
- supabase
- ddos
- observability
- security
thumbnail: https://pbs.twimg.com/media/HJ46_MmXwAAguKX.jpg
translated_by: claude-sonnet-4-6
---

# DevOps & Cloud — 2026-06-04

## TL;DR
- ช่องโหว่ DoS ระยะไกลชื่อ "HTTP/2 Bomb" ถูกรายงานว่าให้ client รายเดียวดึง memory ได้ถึง 32GB ภายใน ~10–20 วินาที กระทบ nginx, Apache httpd, IIS, Envoy, และ Cloudflare Pingora โดยเครดิตการค้นพบมอบให้ OpenAI Codex [5][25][27]
- RPCS3 รับ request กว่า 3 ล้านครั้งและบล็อก Tencent ASN 132203 หลังถูก AI scraping ต่อเนื่องจนโครงสร้างพื้นฐานล่ม [1][4]
- Cloudflare รวม identity/billing: เพิ่ม Grok เข้า AI Gateway พร้อมเก็บเงินผ่าน Cloudflare [7] รวมถึงเปิดตัว "Login with Cloudflare" [16] และ OAuth clients แบบ self-managed ผ่าน Wrangler [29]
- Supabase เก็บ SQL snippets ในเครื่องไว้ที่ไดเรกทอรี supabase/snippets ที่ commit ได้ เพื่อให้ทีม share กัน [49] พร้อมรับ Flutter SDK engineer โดยเฉพาะ [17]
- Vercel Sandboxes ถูกนำไปใช้รัน parallel coding agents จากภายนอกแบบ remote (Conductor) [47] ท่ามกลางการลาออกของผู้นำ v0 [31]

## What happened
สัญญาณที่น่าเชื่อถือที่สุดคือการเปิดเผยช่องโหว่ "HTTP/2 Bomb" ซึ่งอ้างว่า client เพียงรายเดียวสามารถดึง memory ได้ ~32GB ภายใน 10–20 วินาที กระทบ nginx, Apache httpd, Microsoft IIS, Envoy, และ Cloudflare Pingora โดยตัวเลขเวลาไม่ตรงกันในแต่ละรายงาน (10s [5] กับ ~20s [25]) และให้เครดิตแก่ Codex [5][27] ในทางขนาน RPCS3 แจ้งว่าได้รับ request กว่า 3 ล้านครั้งและบล็อก Tencent ASN 132203 หลังถูก AI scraping อย่างต่อเนื่องจนโครงสร้างพื้นฐานรับไม่ไหว [1][4] ข่าว platform ส่วนใหญ่เป็นของ Cloudflare: เพิ่ม Grok (LLM/audio/image/video) เข้า AI Gateway เก็บเงินผ่าน Cloudflare [7], ความร่วมมือกับ OpenAI และการ host ES-module แบบ Worker-compatible [14][18][21], "Login with Cloudflare" [16], OAuth clients แบบ self-managed สำหรับ Wrangler [29], Sandboxes over Tunnel [35], Browser Run remote tabs [39], และ Email Sending named recipients [53]

## Why it matters (reasoning)
สำหรับ stack ที่ใช้ Next.js + Supabase ช่องโหว่ HTTP/2 Bomb มีผลตรงส่วนที่ terminate proxy เอง แอปที่อยู่หลัง managed edge ของ Vercel หรือ Cloudflare เป็นความรับผิดชอบของ vendor แต่ nginx/Envoy ที่ self-host (internal tools, streaming, custom gateways) คือความเสี่ยงของทีม [5][25][27] ยังควรถือว่าข้อมูลนี้น่าเชื่อถือแต่ยังไม่ verified เพราะหมุนเวียนผ่านบัญชี security มือสองที่ตัวเลขไม่สอดคล้องกัน และไม่มี patch advisory ยืนยันในรายงานเหล่านี้ ให้ตรวจสอบกับ CVE ของ vendor ก่อนดำเนินการ [25][27] คลื่น scraping จาก Tencent เป็นปัญหาด้านต้นทุนและความเสถียร ไม่ใช่แค่ความรำคาญ: bot flood ทำให้ egress, edge invocations, และ Postgres read load พุ่ง และอาจปลุกออนคอลตี 3 โดยไม่ต้องมีการโจมตีแบบ targeted [1][4] การรวม identity/billing ของ Cloudflare (AI Gateway billing, Login with Cloudflare, OAuth clients) ลด friction ในการ integrate แต่เพิ่มการพึ่งพา vendor รายเดียว; billing แบบรวมศูนย์ที่สะดวกยังทำให้ค่าใช้จ่าย AI เริ่มง่ายแต่ trace ต้นทางต่อแอปยากขึ้น [7][16][29]

## Possibility
**Likely:** vendor ออก patch/CVE advisories สำหรับ HTTP/2 Bomb เร็ว เพราะมีชื่อ server ห้าตัวและได้รับความสนใจมาก ทำให้ managed edge (Vercel, Cloudflare) แก้เองได้ ขณะที่ self-hosted proxies ล่าช้ากว่า [5][27] **Likely:** traffic จาก AI scraper เพิ่มต่อเนื่อง ดันให้ทีมต่างๆ ต้องตั้ง bot-management rules และบล็อกแบบ per-ASN มากขึ้น [1][4] **Plausible:** Cloudflare AI Gateway กลายเป็น default สำหรับ AI billing/observability เพราะผูกกับ Grok และ OpenAI ไว้แล้ว [7][14] **Plausible:** ความปั่นป่วนของ Vercel รอบ v0 บ่งชี้การจัดโครงสร้างใหม่ ไม่ใช่ platform ไม่เสถียร [31][19] **Unlikely** (จากรายการนี้): partnership ฝั่ง marketing [2][3] ไม่มีผลต่อต้นทุน runtime หรือความเสถียรของ studio ในชีวิตจริง

## Org applicability — NDF DEV
1) ตรวจสอบ exposure จาก HTTP/2 Bomb: รวบรวม nginx/Envoy/reverse proxies ที่ manage เองทั้งหมดที่อยู่หน้าแอป และเช็คสถานะ patch/CVE ของ vendor; ส่วน managed edge ของ Vercel/Cloudflare ให้รอ vendor แก้ [5][25][27] (effort: low/med) 2) ขันน็อต bot/rate-limit rules ของ Cloudflare บน endpoints ที่ใช้ Supabase เพื่อจำกัด egress และ Postgres read load จาก scraper; พิจารณาบล็อกระดับ ASN สำหรับ scraper ที่ abusive [1][4] (effort: low) 3) ถ้าจะเพิ่มฟีเจอร์ AI ให้ประเมิน Cloudflare AI Gateway สำหรับ billing + observability แบบรวมศูนย์ แต่ต้อง tag ค่าใช้จ่ายต่อแอปไว้เพื่อไม่ให้ trace ต้นทางไม่ได้ [7] (effort: low to evaluate) 4) ใช้ Supabase git-committed SQL snippets เพื่อให้ migrations/queries ถูก share และ review ได้ทั้งทีม [49] (effort: low) 5) ทดลอง Vercel Sandboxes สำหรับ remote coding-agent หรือ preview workloads [47] (effort: med) ข้ามไปก่อน: โพสต์ marketing/partnership [2][3][14][18], merch [6], YES-CODE/hype threads [13][44][60], และ observability startups ใหม่ [32] จนกว่าจะมีปัญหาชัดเจน (ต้นทุนหรือ incident) ที่ justify การ migrate จาก tooling เดิม

## Signals to Watch
- HTTP/2 Bomb: จับตา CVE/patch advisories อย่างเป็นทางการที่ระบุชื่อ nginx, Envoy, และ Cloudflare Pingora เพื่อยืนยันผลกระทบจริงกับ claim ที่ยังไม่ verified [5][27]
- แรงกดดันจาก AI scraper bot (Tencent ASN 132203 และรายอื่น) ที่ดัน egress/DB load และนำไปสู่การบล็อกแบบ per-ASN [1][4]
- Cloudflare รวม identity + billing (AI Gateway billing [7], Login with Cloudflare [16], OAuth clients [29]) — ความสะดวกเทียบกับการพึ่งพา vendor รายเดียว
- ความปั่นป่วนด้าน product/leadership ของ Vercel รอบ v0 [31][19] — ติดตามการเปลี่ยนแปลง roadmap ของ Sandboxes/preview tooling [47]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **lnussbaum/incant** — incant: Incus frontend สำหรับ describe และ provision development environments | lobsters | <https://github.com/lnussbaum/incant> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | rpcs3 | ^11283 c95 | [PSA: @TencentGlobal is aggressively scraping the Internet to build yet another A](https://x.com/rpcs3/status/2061946000734888017) |
| x | elonmusk | ^8851 c1068 | [Grok on Cloudflare](https://x.com/elonmusk/status/2062346295256527350) |
| x | elonmusk | ^8663 c1380 | [Grok Imagine on Vercel](https://x.com/elonmusk/status/2062332654587118036) |
| x | Pirat_Nation | ^3896 c60 | [RPCS3 has announced that it is blocking traffic from Tencent ASN 132203 after re](https://x.com/Pirat_Nation/status/2062172954700505145) |
| x | calif_io | ^1744 c22 | [Introducing HTTP/2 Bomb: a remote DoS in nginx, Apache httpd, Microsoft IIS, Env](https://x.com/calif_io/status/2061891591741071765) |
| x | thomasgauvin | ^1203 c104 | [Ok but why does @Cloudflare merch go so hard https://t.co/O0EFBaKVPM](https://x.com/thomasgauvin/status/2061935227514052729) |
| x | CloudflareDev | ^959 c97 | [We're partnering with @xai to bring Grok to @Cloudflare AI Gateway. • Grok LLMs,](https://x.com/CloudflareDev/status/2062281694162629119) |
| x | ni5arga | ^798 c29 | [@cbseindia29 &gt; ddos just cloudflare it dude](https://x.com/ni5arga/status/2061764653559271577) |
| x | steipete | ^796 c26 | [It's been great working with Omar to get observability and verifiable workspaces](https://x.com/steipete/status/2061877813053907083) |
| x | dieworkwear | ^739 c11 | [Some things I saw recently that I think are cool: — Solbiati Art Du Lin linen an](https://x.com/dieworkwear/status/2061923175852888267) |
| x | _avichawla | ^708 c27 | [A harnessed LLM agent, clearly explained! Most people picture this as a model wi](https://x.com/_avichawla/status/2062082282878627946) |
| x | Maks_NAFO_FELLA | ^704 c10 | [❌ Russian messenger MAX removed from App Store, — Russian media Cloudflare previ](https://x.com/Maks_NAFO_FELLA/status/2062245810243273150) |
| x | rauchg | ^605 c61 | [YES-CODE An entire category of software, "no-code", was built under the presumpt](https://x.com/rauchg/status/2061934154732974376) |
| x | elithrar | ^525 c9 | [OpenAI 🤝 Cloudflare. super excited for this to roll out even more widely.](https://x.com/elithrar/status/2061860660456157607) |
| x | whoiskatrin | ^382 c29 | [🎈 we've just shipped agents sdk v0.14.0 you can now build agents with skills, me](https://x.com/whoiskatrin/status/2061757643471945948) |
| x | threepointone | ^377 c16 | [Big news. Login with Cloudflare is here.](https://x.com/threepointone/status/2062288961041506728) |
| x | spydon | ^373 c47 | [Yesterday I joined @supabase as an SDK Engineer (Flutter)! This is a dream job f](https://x.com/spydon/status/2061784593741611435) |
| x | chatsidhartha | ^364 c14 | [This is huge! @Cloudflare 🤝 @OpenAI](https://x.com/chatsidhartha/status/2061901342382178760) |
| x | nishimiya | ^359 c44 | [1 year at @vercel today i don't think words can fully capture what this year has](https://x.com/nishimiya/status/2061924518348689546) |
| x | InduTripat82427 | ^353 c19 | [10 GitHub repositories so good they shouldn't be free. 1. TradingAgents A full t](https://x.com/InduTripat82427/status/2062136258030350758) |
| x | dok2001 | ^333 c5 | [. @OpenAI has good taste. "Sites hosts projects that build Cloudflare Worker-com](https://x.com/dok2001/status/2061992513997578548) |
| x | perplexity_ai | ^309 c25 | [Perplexity Computer is for growing businesses. Computer connects to 400+ tools f](https://x.com/perplexity_ai/status/2062221423104704753) |
| x | LayoffAI | ^275 c19 | [ORACLE LAYOFFS OFFICIALLY BEGIN AMID COMPLAINTS OF TERRIBLE SEVERANCE TERMS The ](https://x.com/LayoffAI/status/2061890930526032297) |
| x | Surendar__05 | ^272 c57 | [How did he deploy facebook without vercel ? https://t.co/OLWWrGLbyK](https://x.com/Surendar__05/status/2061819081024794663) |
| x | TheHackersNews | ^254 c7 | [🚨 WARNING — New HTTP/2 Bomb exploit targets NGINX, Apache HTTPD, Microsoft IIS, ](https://x.com/TheHackersNews/status/2062091046922977340) |
| x | livingdevops | ^249 c8 | ["We use Prometheus for monitoring." I hear this in almost every interview. Then ](https://x.com/livingdevops/status/2061842632222056595) |
| x | The_Cyber_News | ^247 c5 | [🚨 HTTP/2 Bomb — Remote DoS Exploit Hits nginx, Apache, IIS, Envoy, and Cloudflar](https://x.com/The_Cyber_News/status/2062073588128305426) |
| x | unknown | ^238 c24 | [▲ + ❄️ Generating frontends on top of your business data is one of the killer ap](https://x.com/unknown/status/2062199585322529108) |
| x | CFchangelog | ^236 c13 | [Cloudflare now supports self-managed OAuth clients. Build third-party apps that ](https://x.com/CFchangelog/status/2062279751117439052) |
| x | pulkit_mittal_ | ^224 c1 | [Skills that can push your CTC to 50 LPA but you keep avoiding, as a senior engin](https://x.com/pulkit_mittal_/status/2061979932356722918) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rpcs3</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 11283 · 💬 95</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rpcs3/status/2061946000734888017">View @rpcs3 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“PSA: @TencentGlobal is aggressively scraping the Internet to build yet another AI slop chatbot, DDoSing many websites in the process. We've found that, as of last week, their scraping bots can now sol”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>บอต AI ของ Tencent ผ่าน Cloudflare challenge ได้แล้ว ไม่สน robots.txt ส่ง request สำเร็จกว่า 3M ใน 24 ชม. RPCS3 แนะนำให้ block ASN 132203</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>บอต scrape AI ที่ข้าม Cloudflare challenge ได้เป็นภัยจริงที่มีหลักฐาน ทีมที่รัน web service สาธารณะต้องมี firewall rule ระดับ ASN ไม่ใช่แค่ CAPTCHA</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทบทวน firewall rule ของ web service ที่เปิดสาธารณะ เพิ่ม ASN 132203 และ range ของ Tencent ที่ abusive ใน blocklist</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rpcs3/status/2061946000734888017" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@elonmusk</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 8851 · 💬 1068</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/elonmusk/status/2062346295256527350">View @elonmusk on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Grok on Cloudflare”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Elon Musk ยืนยัน Grok (LLM จาก xAI) พร้อมใช้งานบน Cloudflare แล้ว เข้าถึง inference ผ่าน edge ได้โดยไม่ต้อง self-host</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Cloudflare Workers AI อยู่ใน web stack อยู่แล้ว Grok เพิ่มเป็นตัวเลือก model เทียบกับ OpenAI และ Anthropic ได้ทันทีผ่าน billing เดิม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง swap Grok เข้า Cloudflare Workers AI call ที่มีอยู่ เพื่อเปรียบ output quality และ token cost กับ model ที่ใช้อยู่ก่อนตัดสินใจ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/elonmusk/status/2062346295256527350" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@elonmusk</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 8663 · 💬 1380</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/elonmusk/status/2062332654587118036">View @elonmusk on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Grok Imagine on Vercel”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>xAI เปิดให้ใช้ Grok Imagine (image generation) บน Vercel แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่ใช้ Vercel อยู่แล้วสามารถเพิ่ม AI image generation ได้เลยโดยไม่ต้องจัดการ inference endpoint แยก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลองเทียบ Grok Imagine บน Vercel กับ image-gen API ที่ใช้อยู่ในโปรเจกต์ web หรือ e-learning ที่ต้องสร้าง visual content</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/elonmusk/status/2062332654587118036" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3896 · 💬 60</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2062172954700505145">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“RPCS3 has announced that it is blocking traffic from Tencent ASN 132203 after reporting sustained high-volume scraping activity. According to the RPCS3 team, its infrastructure received more than 3 mi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>RPCS3 บล็อก Tencent ASN 132203 หลังถูก bot ส่ง request 3 ล้านครั้งใน 24 ชั่วโมง โดย bot สามารถ bypass Cloudflare challenge และเพิกเฉย robots.txt</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Cloudflare challenge ไม่ใช่กำแพงกั้น bot ที่เชื่อถือได้อีกต่อไป ทีมที่รัน public API หรือ asset server ควรเตรียม ASN-level blocking เป็น fallback</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เพิ่ม ASN-level firewall rule ใน public-facing services และตั้ง alert เมื่อ request volume จาก network range เดียวพุ่งผิดปกติ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2062172954700505145" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@calif_io</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1744 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/calif_io/status/2061891591741071765">View @calif_io on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing HTTP/2 Bomb: a remote DoS in nginx, Apache httpd, Microsoft IIS, Envoy, and Cloudflare Pingora. A single client pins 32GB of server memory in 10s. Found by Codex. Blog post: https://t.co/W”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>HTTP/2 Bomb คือช่องโหว่ DoS ระยะไกลที่เพิ่งเปิดเผย กระทบ nginx, Apache httpd, IIS, Envoy, Cloudflare Pingora — client เดียวดึง memory 32 GB ใน 10 วินาที พร้อม PoC สาธารณะแล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>studio ที่รัน nginx, Apache, หรือ Envoy มีความเสี่ยงทันที ไม่ต้องใช้ auth ในการโจมตี และ PoC เปิดสาธารณะแล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ระบุ server ทุกตัวที่รัน nginx, Apache httpd, IIS, หรือ Envoy แล้ว apply vendor security patch ก่อน expose สู่ public</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/calif_io/status/2061891591741071765" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@thomasgauvin</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1203 · 💬 104</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/thomasgauvin/status/2061935227514052729">View @thomasgauvin on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ok but why does @Cloudflare merch go so hard https://t.co/O0EFBaKVPM”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer advocate ของ Cloudflare โพสต์ชื่นชม merch แบรนด์ ไม่มีเนื้อหาเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/thomasgauvin/status/2061935227514052729" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CloudflareDev</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 959 · 💬 97</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CloudflareDev/status/2062281694162629119">View @CloudflareDev on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We're partnering with @xai to bring Grok to @Cloudflare AI Gateway. • Grok LLMs, audio, image, and video models are now available through AI Gateway • Billed directly through Cloudflare • No additiona”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Cloudflare AI Gateway รองรับ Grok จาก xAI แล้ว — ทั้ง text, audio, image, video — เรียกเก็บเงินผ่าน Cloudflare ไม่ต้อง manage API key แยก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่ใช้ AI Gateway อยู่แล้วเพิ่ม Grok ได้เลยโดยไม่ต้อง set up auth ใหม่ — ลด overhead การ manage หลาย provider</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้าใช้ Cloudflare AI Gateway อยู่แล้ว ลอง add xai/grok-* เข้า config ที่มีอยู่แล้วเทียบ output กับ model ปัจจุบันได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CloudflareDev/status/2062281694162629119" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ni5arga</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 798 · 💬 29</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ni5arga/status/2061764653559271577">View @ni5arga on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@cbseindia29 &amp;gt; ddos just cloudflare it dude”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>user ตอบกลับโพสต์บ่นเรื่อง DDoS ว่า 'just cloudflare it dude' — ไม่มีรายละเอียดทางเทคนิคหรือข้อมูลใหม่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ni5arga/status/2061764653559271577" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
