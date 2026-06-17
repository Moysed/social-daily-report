---
type: social-topic-report
date: '2026-06-17'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-06-17T15:10:08+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 242
salience: 0.5
sentiment: mixed
confidence: 0.5
tags:
- open-weights
- glm-5.2
- model-access
- devtools
- ai-policy
- model-portability
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2067212364966141952/img/B2iaJKQdjOI4kZVb.jpg
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-06-17

## TL;DR
- GLM-5.2 (Z.ai/Zhipu) เปิดตัวเป็น open-weights และขึ้นอันดับ 1 ของ open model / ~อันดับ 4 โดยรวมบน Artificial Analysis Intelligence Index (คะแนน 51) รายงานว่าเทรนบนชิป Huawei Ascend (ไม่ใช่ Nvidia) ด้วยงบ ~$25m และถูกกว่าคู่แข่ง ~90% [41][43][59][60]
- OpenAI's Codex App, CLI และ SDK รองรับ open-source model ใดก็ได้ ไม่จำกัดเฉพาะ model ของ OpenAI — สำคัญสำหรับ agent tooling แบบไม่ผูกกับ vendor เดียว [2]
- มีรายงานซ้ำ (ยังไม่ยืนยัน) บน social ว่า US กดดันการเข้าถึง Claude: Macron กดดัน G7 หาทางเลี่ยง, CEO ของ frontier lab (Amodei, Altman) นัดหารือเรื่อง model access [23][31][40][42]
- Wipro เปิด Anthropic Claude AI center ที่ Bengaluru และวางแผนเทรนพนักงาน 10,000 คนบน Claude [11][34][36]
- รายงาน WP VIP 'Future of the Web 2026': ผู้บริโภค US 60% บอกว่าคำว่า 'AI' ในสาร brand ทำให้รู้สึกแย่ [37] หมายเหตุ: item ที่ engagement สูงวันนี้ส่วนใหญ่เป็น noise — fandom นักแสดงไทยชื่อ 'Gemini' และ crypto spam — ไม่ใช่เรื่อง AI

## สิ่งที่เกิดขึ้น
Signal density ต่ำ item ที่ engagement สูงส่วนใหญ่ไม่เกี่ยว: fandom celebrity/BL ไทยรอบนักแสดงชื่อ 'Gemini' [1][3][5][6][7][8][9][10][12][14][15][19][20][22][24][26][28][38][48][53] และ crypto/get-rich spam [44][52][55][56] ใน AI item ที่แท้จริง สิ่งที่ชัดที่สุดคือ GLM-5.2 ซึ่งเป็น open-weights model จาก Z.ai ที่ครอง top open model และขึ้นอันดับ ~4 โดยรวมบน Artificial Analysis (คะแนน 51) พร้อมอ้างว่าเทรนบนชิป Huawei Ascend ด้วยงบ ~$25m และถูกกว่า ~90% [41][43][59][60] OpenAI ระบุว่า Codex (App/CLI/SDK) ใช้กับ open-source model ใดก็ได้ [2] item ฝั่ง Anthropic โดดเด่นในแนว policy: Claude center ของ Wipro ที่ Bengaluru และแผนเทรน 10,000 คน [11][34][36] รวมถึงโพสต์เก็งเรื่อง US จำกัดการเข้าถึง Claude และการหารือระดับ CEO/G7 [23][31][40][42]

## ทำไมถึงสำคัญ (เหตุผล)
มี 2 thread ที่สำคัญสำหรับ studio ที่ build AI เข้าสู่ edutech และ app — **หนึ่ง** คุณภาพ open-weights ดีขึ้นต่อเนื่องพร้อมต้นทุนที่ลด: GLM-5.2 ที่รายงานว่าเทรนด้วยงบ $25m บน stack จีนล้วน (Huawei Ascend) ถูกกว่า ~90% [59] บวกกับ ranking บน AA [41][60] หมายความว่ามีตัวเลือกที่ถูกกว่าสำหรับ backend inference ใน e-learning/app feature เทียบกับ closed Claude/GPT — Codex ที่รองรับ open model ทุกตัว [2] ยิ่งตอกย้ำว่า agent tooling กำลังแยกออกจาก vendor รายเดียว **สอง** โพสต์เรื่อง Claude access [23][31][40][42] — แม้จะเป็นแค่ tweet/prediction-market คาดเดา — ชี้ถึงความเสี่ยงด้าน provider/geopolitical; studio นอก US ที่ Chiang Mai ซึ่งพึ่ง US model เพียงตัวเดียวอาจเจอปัญหาการเข้าถึงหรือ pricing ดังนั้น provider-agnostic abstraction จึงควรมี แยกจากนี้ ข้อมูล 60%-AI-turnoff [37] เป็น input โดยตรงสำหรับวิธีที่จะ (ไม่) label feature AI ในการตลาด edutech

## ความเป็นไปได้
**มีโอกาสสูง:** open-weights model จะยังปิดช่องว่างและถูกลงเรื่อยๆ เห็นได้จากทิศทาง GLM-5.2 และ benchmark จากบุคคลที่สามที่น่าเชื่อถือ [41][59][60] **เป็นไปได้:** มีแรงเสียดทานด้านการเข้าถึง Claude บ้าง เห็นจากรายงานซ้ำเรื่องแรงกดดันทางการเมืองและการประชุม CEO [40][23][31] — แต่เป็นโพสต์ social ที่ยังไม่ยืนยัน จึงควรจับตาในฐานะความเสี่ยง ไม่ใช่ข้อเท็จจริง **ไม่น่าเชื่อถือถ้าไม่ verify:** ข้อกล่าวอ้างว่า Anthropic open-source 'the entire Wall Street workflow' (DCF/LBO/KYC) ฟรี [45] — มีแหล่งเดียวที่ hype เกินจริง ยืนยันก่อนใช้ ไม่มีแหล่งใดให้ตัวเลข probability ยกเว้นตัวเลข 60% ของ [37]

## การประยุกต์ใช้สำหรับ NDF DEV
1) รัน eval GLM-5.2 (open-weights) สำหรับ inference งานที่ไม่ critical ใน edutech/app feature และ internal tooling เพื่อเปรียบ cost/quality กับ Claude/GPT ที่ใช้อยู่ — effort medium [41][43][59] 2) เก็บ AI integration ไว้หลัง provider-agnostic interface เพื่อสลับ model ได้ถ้า Claude access หรือ pricing เปลี่ยน — effort medium ได้รับการยืนยันจาก access-risk posts [23][40] 3) ถ้ามีใครใช้ Codex CLI ทดสอบชี้ไปที่ open/self-hosted model — effort low [2] 4) นำ 60%-turnoff finding ไปใช้กับ marketing ของ app/edutech: อธิบาย feature ผ่าน outcome แทนการเน้น label 'AI' — effort low [37] 5) ทดลอง Google's free chat-based AI video editor สำหรับ game trailer/marketing clip — effort low แต่ verify ก่อนว่ามีจริง/เข้าถึงได้ [54] ข้าม: Anthropic finance-workflow artifact [45] (ไม่เกี่ยวกับ games/XR และยังไม่ verified), เทคนิค 'threaten the model' prompt [51] (ไม่มีหลักฐาน น่าสงสัย) และ item ทั้งหมดฝั่ง fandom/crypto

## Signals ที่ต้องจับตา
- Open-weights leadership และ cost: ดูว่า claim ของ GLM-5.2 ที่เทรนบน Ascend ถูกกว่า ~90% จะยืนได้ใน independent testing หรือไม่ [41][59]
- Claude access/geopolitics: ยืนยันว่า US restrictions หรือ G7 'workarounds' จะเดินหน้าเกินกว่าแค่ social rumor [23][40]
- Tooling gap: ยังไม่มี cross-tool (Claude Code/Codex/Cursor) thread search ที่ดี — shadcn flagged ไว้; แก้เองภายในอาจช่วยทีมได้ [46]
- Google's chat-driven video editor ในฐานะ CapCut alternative สำหรับ marketing content — verify launch และ access [54]

## Repos & Tools ที่ควรลอง
| repo | source | url |
|---|---|---|
| **rxi/microui** — MicroUI – A tiny, portable, immediate-mode UI library written in ANSI C | radar | <https://github.com/rxi/microui> |
| **freeCodeCamp/freeCodeCamp** — freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer scienc | rss | <https://github.com/freeCodeCamp/freeCodeCamp> |
| **swc-project/swc** — Rust-based platform for the Web Make the web (development) faster. SWC (stands for Speedy Web Compil | rss | <https://github.com/swc-project/swc> |
| **teslamate-org/teslamate** — A self-hosted data logger for your Tesla 🚘 [main maintainer=@JakobLichterfeld]TeslaMate A powerful,  | rss | <https://github.com/teslamate-org/teslamate> |
| **iptv-org/iptv** — Collection of publicly available IPTV channels from all over the worldIPTV Collection of publicly av | rss | <https://github.com/iptv-org/iptv> |
| **puppeteer/puppeteer** — JavaScript API for Chrome and FirefoxPuppeteer Puppeteer is a JavaScript library which provides a hi | rss | <https://github.com/puppeteer/puppeteer> |
| **meshery/meshery** — Meshery, the cloud native manager If you like Meshery, please ★ this repository to show your support | rss | <https://github.com/meshery/meshery> |
| **cypress-io/cypress** — Fast, easy and reliable testing for anything that runs in a browser. Documentation / Changelog / Roa | rss | <https://github.com/cypress-io/cypress> |
| **music-assistant/server** — Music Assistant is a free, opensource Media library manager that connects to your streaming services | rss | <https://github.com/music-assistant/server> |
| **Universal-Debloater-Alliance/universal-android-debloater-next-generation** — Cross-platform GUI written in Rust using ADB to debloat non-rooted Android devices. Improve your pri | rss | <https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation> |
| **OpenBMB/VoxCPM** — VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-L | rss | <https://github.com/OpenBMB/VoxCPM> |
| **alibaba/zvec** — A lightweight, lightning-fast, in-process vector database English / 中文 🚀 Quickstart / 🏠 Home / 📚 Doc | rss | <https://github.com/alibaba/zvec> |

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | RRinda6 | ^4121 c2 | [(1/3) 🐻: Good evening everyone, so glad to meet y'all. Earlier, I phoned to Gemi](https://x.com/RRinda6/status/2067212506096103440) |
| x | thsottiaux | ^3466 c278 | [Reminder that you can use the Codex App, CLI and SDK with any open source model,](https://x.com/thsottiaux/status/2067181377028538431) |
| x | aydellch | ^3280 c1 | [Fotfot turn is to say the line with 'angry voice', he hesitated to choose Gemini](https://x.com/aydellch/status/2067215427672101008) |
| x | ergoquerencia | ^2652 c4 | [https://t.co/q0coJOoFxR they were talking about "size diff" but gf + ppw didn't ](https://x.com/ergoquerencia/status/2067222787756900729) |
| x | MarziaRahman55 | ^2526 c2 | [~ #WilliamEst #williamjkp ~ PondPhuwin & Gemini appreciating William's hardwork🥹](https://x.com/MarziaRahman55/status/2067161006519042076) |
| x | nongsiii | ^1756 c2 | [choose someone to be angry at 4️⃣: need to be angry, right? 4️⃣: *looked at gem*](https://x.com/nongsiii/status/2067218521432678701) |
| x | softforg4 | ^1530 c0 | [oh the teams being "nani, fourth, phuwin" and "sky, gemini, pond"... this puppyk](https://x.com/softforg4/status/2067218214573256973) |
| x | nongsiii | ^1367 c1 | [FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเปิดบ้านGrabFood #GeminiFourth #เจมีไนน](https://x.com/nongsiii/status/2067219972145959150) |
| x | aydellch | ^1246 c0 | [Even Gemini as cake is cute in Fourth's eyes 😭🤏🏻🤏🏻 FRIENDS OF GRAB OPEN HOUSE #F](https://x.com/aydellch/status/2067230709681619025) |
| x | nongsiii | ^1231 c2 | [Birthday blessing for Gemini 4️⃣: I wish Gemini to have strong health, to have h](https://x.com/nongsiii/status/2067232431074365919) |
| x | IndianTechGuide | ^962 c46 | [🚨 Wipro has opened an applied AI center in Bengaluru focused on Anthropic's Clau](https://x.com/IndianTechGuide/status/2067238388910965016) |
| x | ttfotgem | ^955 c0 | ["are they still making out till now?" he is crazy for saying that look at fourth](https://x.com/ttfotgem/status/2067187143726743807) |
| radar | Cider9986 | ^909 c476 | [GrapheneOS has been ported to Android 17](https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon) |
| x | centralparkBKK | ^900 c7 | [Happy birthday to Phuwin Gemini Sky🎂🤍 FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเ](https://x.com/centralparkBKK/status/2067230762437583194) |
| x | jjforgf | ^891 c0 | [They looked nonchalant after doing that right but look at Fourth 😆😆 he's shy and](https://x.com/jjforgf/status/2067225889289740344) |
| x | ttfotgem | ^868 c0 | [gemini after the bathroom scene. bro was zoning out https://t.co/3ES5yMQViF](https://x.com/ttfotgem/status/2067183699246895565) |
| x | kapsology | ^836 c27 | [WTF is training on Anthropic models? 😂😂😂](https://x.com/kapsology/status/2067135468467277973) |
| x | WilliamsRuto | ^831 c153 | [On the margins of the G7 Leaders' Summit, I held discussions with OpenAI Chief E](https://x.com/WilliamsRuto/status/2067208801049051286) |
| x | naranest08 | ^761 c0 | [Word Guessing Game / Team: Sky, Gemini, Pond Q:​Right now, what are you to GrabF](https://x.com/naranest08/status/2067218402813653223) |
| x | geminiscity | ^752 c0 | [FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเปิดบ้านGrabFood ♊️: Sawadeekrub, I'm G](https://x.com/geminiscity/status/2067208368687878623) |
| x | ThePrimeagen | ^741 c48 | [Sacrebleu! This new model is insane https://t.co/z1nuDnW55v](https://x.com/ThePrimeagen/status/2067127546676953322) |
| x | aydellch | ^722 c0 | [Fourth's wish for Gemini 🤍 FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเปิดบ้านGrab](https://x.com/aydellch/status/2067232899380994218) |
| x | Polymarket | ^704 c82 | [NEW: Macron is reportedly pressing G7 leaders &amp; tech CEOs for a workaround t](https://x.com/Polymarket/status/2067232291395661848) |
| x | BRNarawins | ^701 c1 | [Gemini is Pond's loved one… alright 😌👀 FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrab](https://x.com/BRNarawins/status/2067216991862018331) |
| x | shoguncheang | ^622 c0 | [Phuwin said he ask Progress about his ages and Pond said he is 8 years younger t](https://x.com/shoguncheang/status/2067156759102566413) |
| x | misswinmetawin | ^611 c0 | [gemini is so narawins coded im cryingggsgdgdg 😭 FRIENDS OF GRAB OPEN HOUSE #Frie](https://x.com/misswinmetawin/status/2067217866525651146) |
| x | Kenyans | ^558 c43 | [President Ruto and OpenAI CEO Sam Altman hold talks on establishing OpenAI Acade](https://x.com/Kenyans/status/2067220274525647186) |
| x | geminiscity | ^554 c0 | [Fourth is playing with the nose of mini Gemini on the cake 🥹🤏🏻 FRIENDS OF GRAB O](https://x.com/geminiscity/status/2067230945443565979) |
| x | etherXwave | ^542 c9 | [Things have never been better, actually. "We have Claude, we have phones, we hav](https://x.com/etherXwave/status/2067119380400415030) |
| x | BritIndianVoice | ^532 c13 | [China's online war against India — documented facts: 🤖 23,750+ fake accounts rem](https://x.com/BritIndianVoice/status/2067169865358549247) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RRinda6</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4121 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RRinda6/status/2067212506096103440">View @RRinda6 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“(1/3) 🐻: Good evening everyone, so glad to meet y’all. Earlier, I phoned to Gemini &amp;amp; said I’d buy Grab…it’s not what you assume, I didn’t want to buy something on Grab ♊️: Then what? 🐻: I want the”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>คนดังโพสต์มุกตลกว่าอยากซื้อบริษัท Grab ทั้งบริษัท โดยเป็นส่วนหนึ่งของงาน Grab Food Open House</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RRinda6/status/2067212506096103440" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@thsottiaux</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3466 · 💬 278</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/thsottiaux/status/2067181377028538431">View @thsottiaux on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Reminder that you can use the Codex App, CLI and SDK with any open source model, not just with OpenAI models. https://t.co/spPifB4ck3”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Codex App, CLI, และ SDK ของ OpenAI ใช้ open-source model ใดก็ได้เป็น backend ไม่จำกัดแค่ model ของ OpenAI เอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมเอา Codex CLI/SDK ต่อกับ open-source model ที่ host เองได้ ลดค่า API และไม่ผูกกับ vendor เดียวสำหรับ code-gen</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง Codex CLI กับ open-source model local (เช่น Qwen-Coder หรือ Llama) แล้ว benchmark quality vs. cost เทียบกับ workflow ปัจจุบัน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/thsottiaux/status/2067181377028538431" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aydellch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3280 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aydellch/status/2067215427672101008">View @aydellch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Fotfot turn is to say the line with 'angry voice', he hesitated to choose Gemini as the partner bcs he doesn't want to be mad at him 😭 FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเปิดบ้านGrabFood #Gemini”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนอีเวนต์ดาราไทย พูดถึงนักแสดงชื่อ Fourth ลังเลพูดบทโกรธเพราะ AI partner ชื่อ Gemini — เนื้อหาบันเทิงล้วนๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aydellch/status/2067215427672101008" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ergoquerencia</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2652 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ergoquerencia/status/2067222787756900729">View @ergoquerencia on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/q0coJOoFxR they were talking about &quot;size diff&quot; but gf + ppw didn't understand so p'godji made sknn stand together in the middle 😭 p'godji: ah sky stand in the middle, nani stand in the mi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนคลับโพสต์คลิปงาน fan event ที่มีการเล่นคำระหว่าง 'ไส้ดิบ' กับ 'size diff' ในงาน Friends of Grab Open House</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ergoquerencia/status/2067222787756900729" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MarziaRahman55</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2526 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MarziaRahman55/status/2067161006519042076">View @MarziaRahman55 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“~ #WilliamEst #williamjkp ~ PondPhuwin &amp; Gemini appreciating William's hardwork🥹🙏🏻 Phu: Wait, did WilliamEst stay overnight, na? Pond: WilliamEst went back earlier.. Gem: They're heading to Frankfurt ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับไทยพูดถึงตารางงานของ William นักแสดง/ศิลปิน และการซื้อ Aston Martin ไม่มีเนื้อหาด้านเทคโนโลยีใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MarziaRahman55/status/2067161006519042076" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nongsiii</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1756 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nongsiii/status/2067218521432678701">View @nongsiii on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“choose someone to be angry at 4️⃣: need to be angry, right? 4️⃣: *looked at gem* i also dont want to be mad at you (🤭) ♊️: try it once (🫪) 4️⃣: then i choose Gemini FRIENDS OF GRAB OPEN HOUSE #Friends”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับดาราไทย GeminiFourth งาน Grab Food Open House ไม่มีเนื้อหาด้านเทคโนโลยี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nongsiii/status/2067218521432678701" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@softforg4</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1530 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/softforg4/status/2067218214573256973">View @softforg4 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“oh the teams being &quot;nani, fourth, phuwin&quot; and &quot;sky, gemini, pond&quot;... this puppykitty division !! FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเปิดบ้านGrabFood https://t.co/4Y0HJmfUsA”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับแสดงความตื่นเต้นกับการจับคู่ดาราไทยในงานโปรโมท GrabFood ชื่อ Friends of Grab Open House</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/softforg4/status/2067218214573256973" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nongsiii</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1367 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nongsiii/status/2067219972145959150">View @nongsiii on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“FRIENDS OF GRAB OPEN HOUSE #FriendsOfGrabเปิดบ้านGrabFood #GeminiFourth #เจมีไนน์โฟร์ท should be angy 😹🤏🏻 4️⃣: i’m hungry!! order grab for me! are you going to order it or not? 😼 ♊️: i’m not ordering!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับจากงาน GrabFood open house ที่มีศิลปินไทย ไม่มีเนื้อหาด้านเทคโนโลยี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nongsiii/status/2067219972145959150" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
