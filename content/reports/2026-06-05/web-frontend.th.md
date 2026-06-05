---
type: social-topic-report
date: '2026-06-05'
topic: web-frontend
lang: th
pair: web-frontend.en.md
generated_at: '2026-06-05T03:20:47+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- hackernews
- lobsters
- x
regions:
- global
post_count: 229
salience: 0.55
sentiment: mixed
confidence: 0.6
tags:
- build-tooling
- vite
- voidzero-cloudflare
- vercel
- sveltekit
- react-native
thumbnail: https://pbs.twimg.com/media/HJ811JQW4AAdids.jpg
translated_by: claude-sonnet-4-6
---

# Web & Frontend — 2026-06-05

## TL;DR
- Cloudflare กำลังซื้อกิจการ VoidZero บริษัทที่อยู่เบื้องหลัง Vite, Rolldown, Vitest และ oxc [16]; กระทู้บน Hacker News ได้รับ 585 points และ 259 comments [16].
- Vercel ตอบโต้ด้วยการยืนยันจุดยืน 'open platform for the web' โดยชี้ให้เห็นถึงการลงทุนใน nitrojsdev (Nitro), open runtimes และการรองรับ Vite-based frameworks อย่าง Nuxt และ Svelte [12].
- SvelteKit รองรับการลบ svelte.config.js ทิ้งได้แล้ว และย้าย config ทั้งหมดไปไว้ใน Vite plugin โดย VS Code, svelte-check และ SvelteKit อ่าน config จากแหล่งเดียวกัน [55].
- NitroWebSockets prewarm React Native WebSocket ตั้งแต่ตอน app เปิด ตัด delay ~1s ของการเชื่อมต่อออก ทำให้ socket พร้อมใช้ก่อน screen แรก render [52].
- รายการส่วนใหญ่ที่กล่าวถึง 'react', 'astro', 'svelte' เป็นการชนคำโดยบังเอิญ (คลิปยิม, โหราศาสตร์, ฮอกกี้, การ์ตูน) และไม่มี frontend signal ใดทั้งสิ้น [2][7][9][28][29].

## What happened
signal จริงของวันนี้ในแง่ web platform วนอยู่ที่เรื่องการโอนกรรมสิทธิ์ build tooling Cloudflare ประกาศซื้อกิจการ VoidZero บริษัทที่ดูแล Vite, Rolldown, Vitest และ toolchain อย่าง oxc [16][44]. Vercel ออกมายืนยันจุดยืน 'open platform for the web' อย่างเป็นทางการ โดยชี้ให้เห็นการลงทุนใน nitrojsdev (Nitro), open runtimes และการรองรับ Vite-based frameworks อย่าง Nuxt และ Svelte พร้อมแสดงความยินดีกับทีม Void [12]. ชุมชนมองว่านี่คือการควบรวมต่อเนื่อง ('First Astro, then Vite') [44]. ในอีกทาง SvelteKit เลิกพึ่ง svelte.config.js แบบ standalone โดยย้าย configuration เข้าไปใน Vite plugin เพื่อให้ tooling (VS Code, svelte-check) อ่านจากแหล่งเดียว [55]. ในฝั่ง mobile web/native มีการสาธิต NitroWebSockets ที่ prewarm React Native socket ตั้งแต่ launch เพื่อกำจัด cold-connect delay ~1s [52] และมีการพูดถึง ChatGPT 'Codex Sites' ว่าช่วยให้ app ที่ build แล้วอัปเดตตัวเองได้อัตโนมัติ [25]. อีกราว 50 รายการที่เหลือเป็น keyword match ที่ไม่เกี่ยวกับ frontend [2][3][7][8][9][28][29][34].

## Why it matters (reasoning)
Vite อยู่ใต้ stack สมัยใหม่แทบทุกอย่างที่ NDF DEV ต้องแตะ ไม่ว่าจะเป็น Astro, Svelte, Vue, Nuxt และ React setup ส่วนใหญ่ต่างพึ่ง Vite ทั้งสิ้น การที่ core toolchain (Vite/Rolldown/Vitest) ถูกโอนไปอยู่ภายใต้ Cloudflare ทำให้การควบคุม shared dependency กระจุกอยู่ใน cloud vendor รายเดียว [16] ขณะที่ Vercel ออกมาส่งสาร 'open platform' ทันที [12] ชี้ว่าสองแพลตฟอร์ม edge/hosting ที่ใหญ่ที่สุดกำลังแข่งขันกันผ่านชั้น build ไม่ใช่แค่ hosting อีกต่อไป ผลกระทบระดับที่สอง: การผสาน tooling เข้ากับ runtime ของ vendor รายใดรายหนึ่งอาจเร่งการพัฒนา feature แต่ก็ตั้งคำถามถึง neutral governance และว่า optimization จะเอียงเข้าหา deploy target เฉพาะของใครหรือไม่ สำหรับทีมงาน นี่ยังเป็นแค่ช่วง watch-and-wait เพราะ license และ package ยังเป็น open source อยู่ ผลกระทบจริงจึงอยู่ที่การวางตำแหน่งเชิงกลยุทธ์มากกว่าการเปลี่ยนแปลงโค้ดในทันที [12][16]. รายการ SvelteKit [55] และ NitroWebSockets [52] เป็น quality-of-life และ performance wins ขนาดเล็กที่เป็นอิสระจากเรื่องการเปลี่ยนกรรมสิทธิ์ทั้งหมด.

## Possibility
มีแนวโน้มสูง: Vite, Rolldown และ Vitest ยังคงเป็น open source และใช้งานได้ทั่วไปในระยะใกล้นี้ เพราะทั้งประกาศของ Cloudflare และการตอบสนองของ Vercel ต่างเน้นคำว่า 'open' [12][16]. เป็นไปได้: Cloudflare จะเพิ่ม Workers/runtime integration แบบ first-class เข้าไปใน Vite tooling ขณะที่ Vercel ลึกขึ้นในฝั่ง Nitro/open-runtime เพื่อรักษา Vite-based frameworks ให้เป็นกลางบนแพลตฟอร์มของตัวเอง [12]; ช่องว่างด้าน default developer experience ระหว่างสอง cloud จะยิ่งกว้างขึ้น. เป็นไปได้แต่ยังไม่ยืนยัน: ถ้อยความ 'First Astro, then Vite' [44] บ่งชี้ว่าการควบรวม frontend tooling อิสระเข้าสู่แพลตฟอร์มขนาดใหญ่จะยังดำเนินต่อไป. ไม่น่าเกิดในระยะสั้น: การ fork หรือเปลี่ยน license ที่บังคับให้ migrate เพราะไม่มีรายการใดชี้ไปทางนั้น. ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น.

## Org applicability — NDF DEV
1) ติดตาม governance และเงื่อนไข licensing ของ VoidZero/Cloudflare ก่อนผูก dependency อย่างถาวรในโปรเจกต์ใหม่ (effort ต่ำ) [16]. 2) ถ้าใช้ Svelte ให้ลบ svelte.config.js ทิ้งและรวม config เข้าไปใน Vite plugin ในงาน SvelteKit ใหม่เพื่อลด config surface (effort ต่ำ) [55]. 3) สำหรับ React Native apps ที่เปิด WebSocket บน first screen (chat, live edutech, multiplayer) ให้ประเมิน NitroWebSockets prewarming เพื่อกำจัด cold-connect delay ~1s (effort กลาง, validate ก่อนนำมาใช้จริง) [52]. 4) รักษา web stack ให้ framework-agnostic และ Vite-based เพื่อให้ย้ายแพลตฟอร์มระหว่าง Cloudflare และ Vercel ได้อิสระ แทนที่จะล็อกกับ tooling defaults ของ cloud ใดรายหนึ่ง (effort ต่ำ/กลาง) [12][16]. ข้าม: การนำ ChatGPT Codex 'self-updating apps' มาใช้กับงาน client/edutech ตอนนี้ เพราะ autonomous self-updating ยังพิสูจน์ไม่ได้และมีความเสี่ยงสำหรับ production [25]; ข้ามรายการ keyword-collision ทั้งหมด [2][7][9][28][29].

## Signals to Watch
- Cloudflare จะรักษา Vite/Rolldown/Vitest ภายใต้ neutral, open governance หรือจะผลักดันไปสู่ Workers-specific defaults [16].
- Vercel ทำตาม follow-through บน Nitro และ open runtimes จริงหรือไม่ในฐานะตัวถ่วงดุลกับการถือครอง tooling ของ Cloudflare [12].
- การ adopt setup SvelteKit แบบไม่มี svelte.config.js และว่าจะกลายเป็น documented default หรือเปล่า [55].
- ตัวเลข latency จริงและความเสถียรของ NitroWebSockets prewarming ใน production RN apps [52].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **anthropics/defending-code-reference-harness** — Anthropic's open-source framework for AI-powered vulnerability discovery | hackernews | <https://github.com/anthropics/defending-code-reference-harness> |
| **huawei-csl/KVarN** — KVarN: Native vLLM backend for KV-cache quantization by Huawei | hackernews | <https://github.com/huawei-csl/KVarN> |
| **alibaba/open-code-review** — Open Code Review – An AI-powered code review CLI tool | hackernews | <https://github.com/alibaba/open-code-review> |
| **connglli/Reify** — Semantic reification: how to generate UB-free code with arbitrary control flow? | hackernews | <https://github.com/connglli/Reify> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | laundryload_ | ^5565 c19 | [astro honey did you even try .? https://t.co/QpL5zdbSdu](https://x.com/laundryload_/status/2062565289687134543) |
| x | TheJoeySwoll | ^3147 c37 | [The ONLY right way to react if someone walks through your video in the gym. It's](https://x.com/TheJoeySwoll/status/2062704420710924630) |
| x | FilmUpdates | ^2828 c27 | [The cast of 'THE ODYSSEY' react to the IMAX Film Camera Popcorn Bucket. https://](https://x.com/FilmUpdates/status/2062620012767232487) |
| x | Ieo018 | ^2117 c19 | [@TrillBroDude Ppl are gonna over react but I bet he was dying when seeing ts and](https://x.com/Ieo018/status/2062631678942609491) |
| x | BujokMr | ^2070 c76 | [The moment is here ladies and gentlemen, the bubble has popped. The lights are f](https://x.com/BujokMr/status/2062356700531654935) |
| x | P_Kallioniemi | ^1181 c41 | [According to Politico, the Trump administration may cancel planned Tomahawk miss](https://x.com/P_Kallioniemi/status/2062646248629518628) |
| x | SaunteringMoon | ^1101 c8 | [ANOTHER kinda updated Astro eye cycle sheet #dandysworld https://t.co/pTj1B5JeJR](https://x.com/SaunteringMoon/status/2062630203109597325) |
| x | aggievaggii | ^915 c10 | [How Goose wants to react to seeing a trans woman kill herself on the big screen ](https://x.com/aggievaggii/status/2062586806160548062) |
| x | VANXIVTA | ^835 c2 | [My mom is convinced Astro is a moth so I doodled mothstro in honor of her https:](https://x.com/VANXIVTA/status/2062429320744976757) |
| x | TheView | ^814 c119 | [TRUMP LAUNCHES PERSONAL ATTACK ON CNN'S KAITLAN COLLINS: 'The View' co-hosts and](https://x.com/TheView/status/2062601834703794230) |
| x | kateesackhoff | ^773 c28 | [I maintain that the blooper reel deserved its own season. 😂 check out our YouTub](https://x.com/kateesackhoff/status/2062636553109647728) |
| x | rauchg | ^765 c31 | [Congrats Void team! We @vercel reaffirm our collaboration on an open platform fo](https://x.com/rauchg/status/2062535454130676193) |
| x | DarioCpx | ^704 c41 | [Next week new US SPR all time low will be official while the full reopening of t](https://x.com/DarioCpx/status/2062344979901776095) |
| x | sage_astr | ^620 c7 | [here's some of my favorite astro pics💫 https://t.co/r4qyikWja7](https://x.com/sage_astr/status/2062373079859237052) |
| x | offcampusseries | ^606 c2 | ["How did you find out about Allie and Dean's story being planted in Season 1, an](https://x.com/offcampusseries/status/2062611771542864327) |
| hackernews | coloneltcb | ^585 c259 | [VoidZero Is Joining Cloudflare <a href="https:&#x2F;&#x2F;voidzero.dev&#x2F;post](https://blog.cloudflare.com/voidzero-joins-cloudflare/) |
| x | offcampusseries | ^583 c3 | ["As shocking as the Allie and Dean reveal was to me as a reader, the Hunter Dave](https://x.com/offcampusseries/status/2062613026528694490) |
| x | mymymarceline | ^563 c14 | [How would you react to seeing this through my dress? 🖤 https://t.co/09wvgMjTKP](https://x.com/mymymarceline/status/2062674509233066043) |
| x | GBNEWS | ^543 c17 | ['I would never of thought that anyone could match Princess Diana'. @PatrickChris](https://x.com/GBNEWS/status/2062674066079936522) |
| hackernews | mooreds | ^522 c199 | [Ian's Secure Shoelace Knot](https://www.fieggen.com/shoelace/secureknot.htm) |
| x | Mike_Ollerton | ^458 c4 | [Astro boy is one of my fav characters! Here's a little animation I'm working on ](https://x.com/Mike_Ollerton/status/2062342564380901840) |
| x | StockSavvyShay | ^446 c29 | [When Anthropic goes public or raises more capital at a $1T valuation, a meaningf](https://x.com/StockSavvyShay/status/2062612044889936291) |
| x | qaldoier | ^439 c1 | [I'll be completely honest, I 100% saw Vegetta react the way he did about qAldo H](https://x.com/qaldoier/status/2062577720463356009) |
| x | jasonjamesbnn | ^387 c67 | [Canadians, I know you're angry. I'm angry too. It feels like the walls are closi](https://x.com/jasonjamesbnn/status/2062586152511836540) |
| x | gregisenberg | ^383 c41 | [EVERYTHING YOU NEED TO KNOW ABOUT CHATGPT'S "LOVABLE KILLER" CODEX SITES (in 25 ](https://x.com/gregisenberg/status/2062603989691044244) |
| x | Ninjago9101 | ^378 c5 | [KRAFTON's new casual 3v3 PvP mobile game Astro Arena is now open for global pre-](https://x.com/Ninjago9101/status/2062464257124642999) |
| x | pillowsfluff | ^376 c7 | [happy pride month heres aroace astro because i am aroace https://t.co/PBJyKq2D61](https://x.com/pillowsfluff/status/2062630571499470899) |
| x | joeyferg | ^376 c43 | [It's really funny that all we've heard since the Leafs won the lottery is Stenbe](https://x.com/joeyferg/status/2062542175070543917) |
| x | Astro_Panditji_ | ^372 c1 | [🌸💞 Astro Placements Linked With a Beautiful & Loyal Partner → Taurus Rising / Ta](https://x.com/Astro_Panditji_/status/2062353645719683407) |
| hackernews | meetpateltech | ^355 c472 | [When AI Builds Itself: Our progress toward recursive self-improvement](https://www.anthropic.com/institute/recursive-self-improvement) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@laundryload_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5565 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/laundryload_/status/2062565289687134543">View @laundryload_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“astro honey did you even try .? https://t.co/QpL5zdbSdu”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ลักษณะ meme เสียดสี Astro framework แบบสั้นๆ ไม่มีข้อมูลเชิงเทคนิคใดๆ และ link ที่แนบมาไม่สามารถเข้าถึงได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/laundryload_/status/2062565289687134543" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheJoeySwoll</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3147 · 💬 37</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheJoeySwoll/status/2062704420710924630">View @TheJoeySwoll on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The ONLY right way to react if someone walks through your video in the gym. It’s that easy! https://t.co/s4Y806XZT6”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์วิดีโอรีแอคชันคนเดินผ่านกล้องในยิม ไม่มีเนื้อหาเทคโนโลยีใด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheJoeySwoll/status/2062704420710924630" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@FilmUpdates</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2828 · 💬 27</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/FilmUpdates/status/2062620012767232487">View @FilmUpdates on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The cast of ‘THE ODYSSEY’ react to the IMAX Film Camera Popcorn Bucket. https://t.co/0qI1FoPTUX”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักแสดงจากหนัง The Odyssey ถ่ายคลิปรีแอคต่อ popcorn bucket ทรง IMAX film camera</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/FilmUpdates/status/2062620012767232487" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Ieo018</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2117 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Ieo018/status/2062631678942609491">View @Ieo018 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@TrillBroDude Ppl are gonna over react but I bet he was dying when seeing ts and showed it to fox”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้คาดเดาว่าคนนึงเห็นอะไรบางอย่างแล้วขำ จนไปแชร์ให้คนที่เรียกว่า 'fox' — ไม่มีหัวข้อด้านเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Ieo018/status/2062631678942609491" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@BujokMr</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2070 · 💬 76</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/BujokMr/status/2062356700531654935">View @BujokMr on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The moment is here ladies and gentlemen, the bubble has popped. The lights are flashing red, as evidenced by the fraudsters crawling out of every last ponzi hole trying to entice retail back in at the”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์คาดการณ์ตลาดหุ้นพัง เพราะความขัดแย้ง Israel/Iran และ SpaceX IPO เป็น exit liquidity — ไม่มีเนื้อหาด้าน tech หรือ dev</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/BujokMr/status/2062356700531654935" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@P_Kallioniemi</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1181 · 💬 41</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/P_Kallioniemi/status/2062646248629518628">View @P_Kallioniemi on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“According to Politico, the Trump administration may cancel planned Tomahawk missile sales to Germany because it fears the move could anger Russia. Europe's largest economy wants to strengthen its defe”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>รายงานจาก Politico ระบุว่า รัฐบาล Trump กำลังพิจารณายกเลิกการขาย Tomahawk missile ให้เยอรมนี เพราะกังวลปฏิกิริยาของรัสเซีย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/P_Kallioniemi/status/2062646248629518628" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SaunteringMoon</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1101 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SaunteringMoon/status/2062630203109597325">View @SaunteringMoon on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“ANOTHER kinda updated Astro eye cycle sheet #dandysworld https://t.co/pTj1B5JeJR”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนเกมโพสต์ reference sheet อัปเดตของตัวละคร Astro จากเกม Roblox ชื่อ Dandys World ไม่เกี่ยวกับ web dev</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SaunteringMoon/status/2062630203109597325" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aggievaggii</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 915 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aggievaggii/status/2062586806160548062">View @aggievaggii on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“How Goose wants to react to seeing a trans woman kill herself on the big screen during pride month. #tadc #theamazingdigitalcircus https://t.co/ztaljaKgxi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนด้อม TADC แสดงความรู้สึกต่อเนื้อหาในซีรีส์ ไม่มีเนื้อหาเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aggievaggii/status/2062586806160548062" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
