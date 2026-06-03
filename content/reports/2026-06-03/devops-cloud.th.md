---
type: social-topic-report
date: '2026-06-03'
topic: devops-cloud
lang: th
pair: devops-cloud.en.md
generated_at: '2026-06-03T06:58:56+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- x
regions:
- global
post_count: 168
salience: 0.6
sentiment: mixed
confidence: 0.55
tags:
- cloudflare
- security
- observability
- cost
- vercel
- supabase
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2061452121648865280/img/hS8gE8pxV4lWpSMx.jpg
translated_by: claude-sonnet-4-6
---

# DevOps & Cloud — 2026-06-03

## TL;DR
- HTTP/2 Bomb: client เดียวล็อก memory ได้ 32GB ใน ~10 วินาที บน nginx, Apache httpd, IIS, Envoy, และ Cloudflare Pingora — remote DoS ที่พบผ่าน Codex [15].
- Cloudflare ประกาศราคา R2 SQL, R2 Data Catalog, และ Pipelines; ยังไม่เปิดเก็บเงิน มีเวลา 30 วันก่อนระบบเริ่ม [31].
- Grafana ปิดการสอบสวนภายใน ยืนยันไม่มีการเข้าถึง customer production หรือ Grafana Cloud โดยไม่ได้รับอนุญาต และดึง Mandiant เข้ามา; แยกกัน มี Grafana CVEs เพิ่มเติมโผล่ [47][28].
- AI scraping load เพิ่มขึ้น — มีรายงาน Tencent bots DDoS sites ขณะ scrape [1] — bot/DDoS controls ยังคงเป็นประเด็นที่ต้องติดตาม [5].
- Serverless reference stack ชัดเจนออกมาแล้ว: Caltext บน Vercel ใช้ Hono บน Nitro, Upstash Redis, และ Vercel Workflows [3]; Cloudflare Agents SDK v0.14.0 เพิ่ม durable workflows และ schedules [14].

## What happened
ด้าน reliability มีการเปิดเผย remote DoS ชื่อ HTTP/2 Bomb กระทบ nginx, Apache httpd, Microsoft IIS, Envoy, และ Cloudflare Pingora — client เดียวล็อก memory ได้ 32GB ในราว 10 วินาที พบโดย Codex [15]. แรงกดดันจาก AI scraping ก็ชัดขึ้น มีรายงาน Tencent bots DDoS sites ระหว่าง scrape [1] และปฏิกิริยาแบบเดิมคือ 'แค่เอา Cloudflare วางไว้หน้า' [5]. Grafana แถลงว่าการสอบสวนภายในไม่พบการเข้าถึง customer production systems หรือ Grafana Cloud โดยไม่ได้รับอนุญาต และดึง Mandiant เข้ามา [47] ขณะที่อีก post หนึ่งแจ้ง Grafana CVEs เพิ่มเติม [28].

## Why it matters (reasoning)
สำหรับ shop ที่ใช้ Next.js + Supabase + Cloudflare/Vercel นั้น HTTP/2 Bomb [15] คือรายการที่โยงตรงไปหา 3am pages: managed edges (Cloudflare, Vercel) น่าจะได้รับ patch จาก provider แล้ว แต่ origin ที่ self-host บน nginx/Apache/Envoy ยังเสี่ยงอยู่จนกว่าจะ patch และการที่ Pingora ถูกระบุชื่อหมายความว่า edge layer อยู่ใน scope ด้วย ไม่ใช่แค่ origin. AI scraping traffic ที่เพิ่มขึ้น [1] ดัน baseline request volume และ bandwidth สูงขึ้น ทั้งกระทบ reliability และเพิ่ม runtime bills — ซึ่งเป็นทิศทางเดียวกับ cost focus ของ brief นี้. การ finalize ราคา R2 ของ Cloudflare [31] สำคัญเพราะเปลี่ยน data path ที่เคยฟรี/ทดลองใช้ให้กลายเป็น metered; 30 วันคือ planning window ก่อนที่บรรทัด storage/query จะเริ่มปรากฏ. Grafana incident บวก CVE ใหม่ [47][28] เตือนว่า observability layer เองก็เป็น attack surface และเป็น dependency ที่ต้องติดตาม ไม่ใช่แค่ dashboard ที่ passive.

## Possibility
มีแนวโน้มสูง: provider จะ patch HTTP/2 Bomb ที่ edge รวดเร็วเพราะมีชื่อ vendor ที่ได้รับผลกระทบ แต่ origin ที่ดูแลเองตามหลัง — ยังเสี่ยงอยู่ตรงที่ studio รัน nginx/Apache/Envoy ของตัวเอง [15]. มีแนวโน้มสูง: Cloudflare เปิด R2 billing หลังแจ้ง 30 วันตามที่ระบุ ทำให้การใช้ R2 SQL/Data Catalog/Pipelines กลายเป็น line item [31]. เป็นไปได้: AI scraping volume เพิ่มต่อเนื่อง ดันให้ทีมมากขึ้นหันมาจัดการ bot management และ rate limiting [1]. เป็นไปได้: observability market แตกกระจายมากขึ้นจาก entrants ใหม่ (Sazabi [32]) และการปรับราคา (Honeycomb uncapping [4]) กดดัน incumbent อย่าง Datadog/Sentry/Grafana. ไม่มี source ใดให้ตัวเลข probability จึงไม่ระบุ.

## Org applicability — NDF DEV
1) รวบรวม nginx/Apache/Envoy ที่ self-host บน origins หรือ internal tooling และ patch/verify กับ HTTP/2 Bomb; ยืนยันว่า Cloudflare/Vercel edge ได้รับ patch จาก provider แล้ว (low) [15]. 2) ตรวจ Cloudflare bot/DDoS และ rate-limit settings บน production sites เพราะ scraping พุ่งขึ้น (low) [1][5]. 3) ถ้าใช้หรือวางแผนใช้ R2 (R2 SQL, Data Catalog, Pipelines) ให้คำนวณราคา workload ตอนนี้และตั้ง reminder สำหรับ 30-day billing-enable window (low) [31]. 4) ถ้า observability รันบน Grafana Cloud ให้อ่าน Mandiant follow-up และ patch CVEs ที่ระบุ; ถ้า self-host Grafana ให้ prioritize CVE updates (low) [47][28]. 5) สำหรับ serverless builds ใหม่ ให้ใช้ Caltext เป็น reference สำหรับ Vercel-native stack (Hono on Nitro, Upstash Redis, Vercel Workflows) และเปรียบกับ Cloudflare Agents SDK durable workflows ก่อนตัดสินใจ (med) [3][14]. ข้ามได้: agent-demo hype [18][44], vendor personnel/merch/office posts [20][23][34][35][33], gaming/DLSS [6][27], และ no-code/yes-code commentary [12] — ไม่มี operational signal สำหรับ production reliability หรือ cost.

## Signals to Watch
- การ rollout ของ HTTP/2 Bomb patch และ Cloudflare Pingora advisory — ยืนยันว่า edge exposure ถูกปิดแล้วหรือยัง [15].
- วันที่ Cloudflare เปิด R2 billing หลัง 30-day notice — trigger สำหรับ storage/query costs ใหม่ [31].
- ผลการสอบสวนของ Mandiant สำหรับ Grafana และจังหวะ patch CVE — ความเสี่ยงของ dependency ใน observability layer [47][28].
- การเปลี่ยนแปลงราคา/entrant ใหม่ใน observability (Honeycomb uncapping, Sazabi) ที่อาจลด monitoring spend [4][32].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **lnussbaum/incant** — incant: Incus frontend สำหรับอธิบายและ provision development environments | lobsters | <https://github.com/lnussbaum/incant> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | rpcs3 | ^7353 c60 | [PSA: @TencentGlobal is aggressively scraping the Internet to build yet another A](https://x.com/rpcs3/status/2061946000734888017) |
| x | contextkingceo | ^1885 c230 | [Introducing HydraDB. The graph native context infrastructure for agents. Purpose](https://x.com/contextkingceo/status/2061452631298752790) |
| x | pontusab | ^1269 c56 | [Introducing Caltext, open-source calorie tracking in iMessage. Built with: • Bun](https://x.com/pontusab/status/2061410279922282556) |
| x | delvieero | ^833 c793 | [Honeycomb uncapping 👏🏻 🍯 🐝 ❤️ https://t.co/9x3NdAz0rf](https://x.com/delvieero/status/2061576021405503791) |
| x | ni5arga | ^738 c27 | [@cbseindia29 &gt; ddos just cloudflare it dude](https://x.com/ni5arga/status/2061764653559271577) |
| x | NVIDIAGeForce | ^653 c36 | [DLSS 4.5 is powering today's hits &amp; tomorrow's releases including: 🟢 Phantom](https://x.com/NVIDIAGeForce/status/2061485433314250932) |
| x | steipete | ^614 c18 | [It's been great working with Omar to get observability and verifiable workspaces](https://x.com/steipete/status/2061877813053907083) |
| x | rauchg | ^561 c30 | [Beautiful example of a full-stack agent on @vercel. Great learning material!](https://x.com/rauchg/status/2061415178298937365) |
| x | dieworkwear | ^555 c11 | [Some things I saw recently that I think are cool: — Solbiati Art Du Lin linen an](https://x.com/dieworkwear/status/2061923175852888267) |
| x | awscloud | ^512 c48 | [Now generally available, @OpenAI GPT-5.5, GPT-5.4, and Codex on Amazon Bedrock. ](https://x.com/awscloud/status/2061564484523524302) |
| x | elithrar | ^471 c9 | [OpenAI 🤝 Cloudflare. super excited for this to roll out even more widely.](https://x.com/elithrar/status/2061860660456157607) |
| x | rauchg | ^449 c41 | [YES-CODE An entire category of software, "no-code", was built under the presumpt](https://x.com/rauchg/status/2061934154732974376) |
| x | awscloud | ^436 c20 | [(1/2) Your most sensitive code deserves AI that never leaves your network. https](https://x.com/awscloud/status/2061523521331671423) |
| x | whoiskatrin | ^358 c28 | [🎈 we've just shipped agents sdk v0.14.0 you can now build agents with skills, me](https://x.com/whoiskatrin/status/2061757643471945948) |
| x | calif_io | ^353 c4 | [Introducing HTTP/2 Bomb: a remote DoS in nginx, Apache httpd, Microsoft IIS, Env](https://x.com/calif_io/status/2061891591741071765) |
| x | cjc | ^348 c15 | [Only missed out on these tiny startups: - Anthropic - Cursor - Perplexity - Sier](https://x.com/cjc/status/2061627852186169544) |
| x | PeterDiamandis | ^328 c52 | [Tech companies are laying off people by the thousands, doing so without an ounce](https://x.com/PeterDiamandis/status/2061484183441305965) |
| x | RoundtableSpace | ^315 c36 | [THIS GUY GAVE CLAUDE CODE A $1,000 BUDGET, WENT TO SLEEP, AND WOKE UP TO 4 AGENT](https://x.com/RoundtableSpace/status/2061572245923999815) |
| x | ai_trade_pro | ^296 c0 | [Quietly one of the most important AI updates of the month, and it's not a benchm](https://x.com/ai_trade_pro/status/2061479694361395504) |
| x | thomasgauvin | ^293 c29 | [Ok but why does @Cloudflare merch go so hard https://t.co/O0EFBaKVPM](https://x.com/thomasgauvin/status/2061935227514052729) |
| x | StockMKTNewz | ^292 c74 | [All these stocks hit new 52 WEEK HIGHS at some point today Micron $MU Broadcom $](https://x.com/StockMKTNewz/status/2061533276821479572) |
| x | spydon | ^280 c38 | [Yesterday I joined @supabase as an SDK Engineer (Flutter)! This is a dream job f](https://x.com/spydon/status/2061784593741611435) |
| x | nishimiya | ^279 c35 | [1 year at @vercel today i don't think words can fully capture what this year has](https://x.com/nishimiya/status/2061924518348689546) |
| x | chatsidhartha | ^270 c11 | [This is huge! @Cloudflare 🤝 @OpenAI](https://x.com/chatsidhartha/status/2061901342382178760) |
| x | LayoffAI | ^246 c19 | [ORACLE LAYOFFS OFFICIALLY BEGIN AMID COMPLAINTS OF TERRIBLE SEVERANCE TERMS The ](https://x.com/LayoffAI/status/2061890930526032297) |
| x | 0xJuliechen | ^241 c11 | [sf bros when they say they're building an agent: "a stateful agent with full obs](https://x.com/0xJuliechen/status/2061562085910155387) |
| x | NVIDIAGeForce | ^222 c16 | [Explore, adapt, and survive Sota7 with #RTXOn. Honeycomb: The World Beyond arriv](https://x.com/NVIDIAGeForce/status/2061531530514575769) |
| x | Zierax_x | ^214 c1 | [now Grafana Final Scanner have more CVEs 🥳🥳🥳 https://t.co/l9K3DyIYcz https://t.c](https://x.com/Zierax_x/status/2061466550385639587) |
| x | Surendar__05 | ^209 c47 | [How did he deploy facebook without vercel ? https://t.co/OLWWrGLbyK](https://x.com/Surendar__05/status/2061819081024794663) |
| x | PopPunkOnChain | ^207 c20 | [Pumpcade is now a Tier 1 @Cloudflare startup. We just recieved $350,000 in credi](https://x.com/PopPunkOnChain/status/2061449233153057214) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rpcs3</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7353 · 💬 60</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rpcs3/status/2061946000734888017">View @rpcs3 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“PSA: @TencentGlobal is aggressively scraping the Internet to build yet another AI slop chatbot, DDoSing many websites in the process. We've found that, as of last week, their scraping bots can now sol”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>RPCS3 รายงาน bot ของ Tencent ผ่าน Cloudflare challenge ได้แล้ว ส่ง request สำเร็จกว่า 3 ล้านครั้งใน 24 ชม. แนะให้ block ASN 132203</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Cloudflare challenge อย่างเดียวหยุด AI scraper ไม่ได้แล้ว ต้องเพิ่ม firewall rule ระดับ IP ด้วย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตรวจ firewall rule บน web service และ API ของ studio แล้ว block ASN 132203 บนที่เจอ traffic spike ผิดปกติ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rpcs3/status/2061946000734888017" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@contextkingceo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1885 · 💬 230</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/contextkingceo/status/2061452631298752790">View @contextkingceo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing HydraDB. The graph native context infrastructure for agents. Purpose built to deliver precise context &amp; observability into why agents act the way they do. We've always believed graphs are ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>HydraDB คือ graph-native database ตัวใหม่ ผสม in-memory, NVMe, และ object storage ไว้ใน layer เดียว เพื่อส่ง context ให้ AI agent เร็วและถูกกว่า graph solution ที่มีอยู่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่สร้าง multi-agent pipeline ต้องการ context retrieval ที่เร็ว ถูก และตรวจสอบ agent decision ได้ HydraDB ออกแบบมาตรงจุดนี้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Benchmark HydraDB เทียบกับ context/memory store ที่ใช้อยู่ใน agent workflow ก่อนตัดสินใจไปทาง vector DB</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/contextkingceo/status/2061452631298752790" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@pontusab</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1269 · 💬 56</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/pontusab/status/2061410279922282556">View @pontusab on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing Caltext, open-source calorie tracking in iMessage. Built with: • Bun + Turborepo • Hono on Nitro (Vercel) • Chat SDK + Sendblue • AI SDK + GPT-4.1 vision • Upstash Redis • Vercel Workflows”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โปรเจกต์ open-source ติดตามแคลอรีผ่าน iMessage เปิด stack จริง: Bun, Turborepo, Hono บน Nitro, GPT-4.1 vision, Upstash Redis, Vercel Workflows ให้ดูครบใน repo เดียว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เห็น pattern จริงของ Vercel Workflows + Upstash Redis + AI vision ใน async pipeline — studio นำไปใช้กับ web หรือ e-learning project ได้เลย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Clone repo แล้วดึง pattern Vercel Workflows + Upstash Redis มาทำ starter template สำหรับ async AI feature ใน web stack ของ studio</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/pontusab/status/2061410279922282556" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@delvieero</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 833 · 💬 793</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/delvieero/status/2061576021405503791">View @delvieero on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Honeycomb uncapping 👏🏻 🍯 🐝 ❤️ https://t.co/9x3NdAz0rf”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Honeycomb (observability platform) ประกาศเอา cap บางอย่างออก — โพสต์แนบวิดีโอแต่ไม่มีรายละเอียดว่า limit ไหน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้า Honeycomb เอา limit ออกจาก tier ล่าง ทีมเล็กได้ observability เพิ่มในราคาเดิม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เช็ค blog หรือ changelog ของ Honeycomb โดยตรงก่อนตัดสินใจขยายการใช้งานใน observability stack</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/delvieero/status/2061576021405503791" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ni5arga</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 738 · 💬 27</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ni5arga/status/2061764653559271577">View @ni5arga on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@cbseindia29 &amp;gt; ddos just cloudflare it dude”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer บน X แซวว่า CBSE India โดน DDoS ก็แค่ใช้ Cloudflare แก้ซะ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ni5arga/status/2061764653559271577" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NVIDIAGeForce</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 653 · 💬 36</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NVIDIAGeForce/status/2061485433314250932">View @NVIDIAGeForce on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“DLSS 4.5 is powering today's hits &amp;amp; tomorrow's releases including: 🟢 Phantom Blade Zero 🟢 CINDER CITY 🟢 Squad 🟢 Marvel Rivals 🟢 Gothic 1 Remake 🟢 NARAKA: Bladepoint 🟢 Honeycomb: The World Beyond 🟢”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>NVIDIA GeForce โพสต์รายชื่อเกมที่ใช้ DLSS 4.5 เพื่อโปรโมต ไม่มี SDK ใหม่หรือ developer tool ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NVIDIAGeForce/status/2061485433314250932" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 614 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061877813053907083">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“It’s been great working with Omar to get observability and verifiable workspaces into OpenClaw.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete โพสต์ขอบคุณ Omar ที่ช่วยเพิ่ม observability และ verifiable workspaces ใน OpenClaw แต่ไม่มีรายละเอียดทางเทคนิค ลิงก์ หรือ release ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061877813053907083" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 561 · 💬 30</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2061415178298937365">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Beautiful example of a full-stack agent on @vercel. Great learning material!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@rauchg CEO ของ Vercel ชื่นชม full-stack agent ตัวอย่างบน Vercel ว่าน่าเรียนรู้ โดยไม่ได้ระบุ link, stack หรือรายละเอียดใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2061415178298937365" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
