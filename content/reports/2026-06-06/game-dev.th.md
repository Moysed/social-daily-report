---
type: social-topic-report
date: '2026-06-06'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-06T15:30:31+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 150
salience: 0.55
sentiment: mixed
confidence: 0.5
tags:
- unreal-engine
- ue6
- art-direction
- tech-art
- ai-pipeline
- indie
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2062662459861643264/img/zgxv0oBQaVjf9Nge.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-06

## TL;DR
- กระแสหลักวันนี้คือการต่อต้านภาพลักษณ์ Unreal Engine ที่เริ่มดูเหมือนกันหมด — วิจารณ์ซ้ำว่า 'UE5 slop' ชี้ไปที่ default particles, motion blur, และความซ้ำซากของเกมต่างๆ [1][2][4][10][15][18]
- Unreal Engine 6 เริ่มปรากฏในผลิตภัณฑ์ที่ shipping แล้ว: Rocket League ประกาศย้ายไป UE6 [5] และ Fortnite trailer ถูกอ้างว่ารันบน UE6 [14]
- RE Engine ของ Capcom ถูกยกขึ้นมาซ้ำหลายครั้งว่ามีเอกลักษณ์ต่างจาก UE/Unity สอดคล้องกับการเปิดตัว RE Code Veronica ใน Summer Game Fest [23][25][27]
- สัญญาณด้าน tooling/tech-art ที่น่าสนใจ: Unity ShaderGraph dissolve effect [17], เทคนิค glass+inverted-normals สำหรับของเหลว [3], SplatBox 'Smart Splat Decimator' (~50% splat reduction, ~5x ขนาดเล็กลง) [31], และ rollback netcode milestone [60]
- กิจกรรม AI-in-pipeline: workflow สร้าง 3D character แบบ modular (head/torso/ฯลฯ) รันใน Unreal [46] พร้อม Nano Banana Pro / Gemini image generation [44]

## What happened
Feed ส่วนใหญ่เป็นความเห็นและ indie self-promotion มากกว่าข่าวจริง กลุ่มใหญ่สุดคือกระแสต้าน default look ของ Unreal Engine ที่ถูกเรียกว่า 'slop' — บ่นซ้ำๆ เรื่อง motion blur, default particles, และภาพที่ออกมาเหมือนกันหมด [1][2][4][9][10][15][18] รวมถึง reaction ต่อ Guild Wars 3 UE5 reveal [29][43][54][57] ตรงข้ามกัน หลายโพสต์ยก RE Engine ของ Capcom ว่ามีเอกลักษณ์ชัดเจน เชื่อมกับ RE Code Veronica ใน Summer Game Fest [23][25][27] ข่าว engine version มีสองชิ้น: Rocket League ประกาศย้ายไป Unreal Engine 6 [5] และ Fortnite trailer ถูกระบุว่ารันบน UE6 [14] ส่วน Virtua Fighter Crossworlds ยืนยันว่าใช้ UE5 จาก editor UI ที่เห็นในงาน showcase [30]

## Why it matters (reasoning)
คำบ่นซ้ำว่า 'looks like every other UE5 game' [4][10][15][18] เป็นสัญญาณว่าคนดูเริ่มมองว่า engine-default rendering คือแบรนด์เชิงลบ ขณะที่ art pipeline ที่โดดเด่น (RE Engine [27], pixel art ที่ตั้งใจ [4]) กลับอ่านเป็นสัญลักษณ์ของคุณภาพ สาเหตุมาจากการ converge ของ tooling — default post-processing ที่ง่ายเกินไป (TAA, motion blur, Lumen-style lighting) ทำให้เกิด house style ที่จดจำได้; ผลลัพธ์ระดับที่สองคือ art direction กลายเป็นตัวแบ่งแยก ไม่ใช่ความละเอียดของภาพ การที่ UE6 โผล่ใน Rocket League และ Fortnite [5][14] แสดงว่า Epic กำลัง push version ถัดไปเข้าสู่ live title ที่มี traffic สูง ซึ่งจะกลายเป็น baseline ที่ studio อื่นถูกเปรียบเทียบด้วย รายการ tech-art และ AI [17][31][46][60] คือ signal ที่มีประโยชน์จริงใต้เสียงรบกวน: splat decimation [31] แก้ปัญหา asset budget โดยตรงสำหรับ mobile/XR

## Possibility
การ adopt UE6 ต่อเนื่องเป็นไปได้สูงเมื่อ title ใหญ่สองตัว commit ไปแล้ว [5][14] กระแสต่อต้านด้านวิชวลไม่น่าจะเขย่า market position ของ Unreal ได้ แต่เป็นไปได้ว่ามันจะดัน indie บางส่วนไปทาง stylization หรือ engine อื่นอย่าง Godot [21][4] AI asset pipeline ที่กำลัง mature ไปสู่ modular in-engine output เป็นไปได้แต่ยังไม่พิสูจน์ใน production quality — workflow ที่อ้างถึงเป็นแค่ demo ยังไม่ใช่ shipped result [46] RE Engine ที่ยังคงเป็น closed competitive advantage ของ Capcom เป็นไปได้สูง เพราะไม่มี external license [27]

## Org applicability — NDF DEV
สำหรับงาน Unity/XR/edutech ของ NDF DEV: (1) นำ ShaderGraph dissolve/edge-glow pattern ไปทำ enemy death/teleport VFX — ใช้ได้เลย [17] (low) (2) ประเมิน SplatBox-style Gaussian-splat decimation สำหรับ XR/mobile asset budget ที่ใช้ splat capture [31] (med) (3) ถ้า title ไหนต้องการ real-time multiplayer ให้ศึกษา rollback-netcode ตั้งแต่ตอนนี้แทนที่จะ retrofit ทีหลัง [60] (med) (4) ใช้กระแสต่อต้าน UE sameness เป็น brief สำหรับ edutech/XR: ลงทุนกับ art direction ที่โดดเด่น detail ต่ำ แทนการไล่ตาม photoreal fidelity [4][15][27] (low) (5) ทดสอบ AI modular 3D character generation แบบ prototype เท่านั้น อย่าใส่ใน delivery path [46] (med) ข้ามไปได้: flame war UE5/UE6, Guild Wars 3 hype [43][57], การคาดเดา wafer/silicon ของ Carmack [11], และ indie wishlist/screenshot promo [34][39][40] — ไม่มีเนื้อหา actionable

## Signals to Watch
- UE6 เข้าสู่ live title — ติดตามว่า studio อื่นจะตามหลัง Rocket League และ Fortnite หรือไม่ [5][14]
- AI asset pipeline ที่กำลังพัฒนาไปสู่ modular in-engine generation [46][44]
- Gaussian-splat optimization tooling สำหรับ asset budget ที่ตึงขึ้น [31]
- Rollback netcode ที่ทีมขนาดเล็กเข้าถึงได้มากขึ้น [60]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | MrEatYaAss | ^9345 c34 | [17th Unreal Engine Asian blade game, hang it the fuck up man](https://x.com/MrEatYaAss/status/2063023812082274778) |
| x | mofromyt | ^5008 c9 | [unreal engine be beating these devs ass](https://x.com/mofromyt/status/2062971023276826984) |
| x | Petcson | ^3038 c18 | [Came up with a real simple way to make these flasks look like they have liquid! ](https://x.com/Petcson/status/2062663436618654148) |
| x | Windpress | ^2633 c9 | [Pixel art can be overdone in indie games, BUT when it is done CORRECTLY it is WA](https://x.com/Windpress/status/2063059158010564800) |
| x | gcindisguise | ^1695 c17 | [rocket league in the past 2 months - announced rocket league is moving to unreal](https://x.com/gcindisguise/status/2062942540936978776) |
| x | TheRedBarrels | ^1080 c18 | [Start your day the Murkoff way. ☕ Two new #TheOutlastTrials mugs have arrived at](https://x.com/TheRedBarrels/status/2062944416071926148) |
| x | jasonappleton | ^886 c118 | [I'm personally tired of the bots and trolls crashing out on Charles. The market ](https://x.com/jasonappleton/status/2062592937414853085) |
| x | ABGameDeveloper | ^803 c11 | [Working on a new level where the protagonist becomes tiny… 🦊 #furry #horrorgame ](https://x.com/ABGameDeveloper/status/2063122004434391205) |
| x | RileyTaugor | ^599 c1 | [@naranciagaming Unreal engine ruined everything https://t.co/E0aGoeLLeV](https://x.com/RileyTaugor/status/2063036146876133565) |
| x | Asteristrash | ^584 c10 | [Almost everything at the game awards so far looks ai generated or like its a gam](https://x.com/Asteristrash/status/2063014378681647270) |
| x | ID_AA_Carmack | ^497 c66 | [Current state of the art silicon processes are optimized for maximum performance](https://x.com/ID_AA_Carmack/status/2062965118074233256) |
| x | hongga17 | ^374 c17 | [It's finally here: Lola's Familiars Steam page is now available! The game has be](https://x.com/hongga17/status/2063244518917599566) |
| x | UnrealEngine | ^373 c6 | [Want to create games in Unreal Engine but not sure where to start? Our new begin](https://x.com/UnrealEngine/status/2062589020299985088) |
| x | UltimaShadowX | ^360 c3 | [THIS FORTNITE TRAILER IS RUNNING ON UNREAL ENGINE 6](https://x.com/UltimaShadowX/status/2063011589725315091) |
| x | HedProtag | ^321 c2 | [The biggest disappointment in modern game trailers is when you see a CG cutscene](https://x.com/HedProtag/status/2063018942600298606) |
| x | OzAshborne | ^300 c21 | [Oh my god! A #bug is making Dorothy attack with a Super headbutt! #BugReport #in](https://x.com/OzAshborne/status/2062942225814929682) |
| x | VFX_Therapy | ^285 c1 | [Dissolve Shader = Interactive edge glow + world space control. Perfect for enemy](https://x.com/VFX_Therapy/status/2062607977186738307) |
| x | smlreviewer | ^245 c11 | [people keep saying "it's unique!" to defend that gundam game but idk if id consi](https://x.com/smlreviewer/status/2063082659140538772) |
| x | Ninjago9101 | ^243 c3 | [Swords of Legends Steam page is now live! A single-player action RPG from Aurogo](https://x.com/Ninjago9101/status/2062932190376374434) |
| x | RPGPaperMaker | ^242 c1 | [New feature added in RPG Paper Maker 3.1.18: Fog, screen tone, live preview in m](https://x.com/RPGPaperMaker/status/2062957759537061912) |
| x | Sean_Hinris | ^220 c10 | [The design and behavior aren't final yet, but I'm really happy with the progress](https://x.com/Sean_Hinris/status/2063098039749714232) |
| x | itchio | ^194 c0 | [above eden: she chose levitation. https://t.co/S6PHKje2wv by @seraph_engine http](https://x.com/itchio/status/2062942526961549805) |
| x | thesev_115 | ^193 c5 | [@sbodrojan YEAH!!! For some odd reason I noticed it was RE Engine instantly when](https://x.com/thesev_115/status/2063029779494809836) |
| x | MistySkySky | ^191 c0 | [Sonic Awakened Renders of the alternate skins! I'm using the In-Game Model not t](https://x.com/MistySkySky/status/2062990102171631754) |
| x | horrorvisuals | ^162 c6 | [Summer Game Fest thoughts: - RESIDENT EVIL CODE VERONICA - As soon as I saw the ](https://x.com/horrorvisuals/status/2063045275590250772) |
| x | ReissadStudio | ^161 c16 | [[BODYCAM] - Available only on STEAM 🎮 The countdown is about to begin… The mecha](https://x.com/ReissadStudio/status/2062949478412300516) |
| x | AestheticGamer1 | ^157 c3 | [It is worth mentioning that the RE Engine charm &amp; look does stand out agains](https://x.com/AestheticGamer1/status/2063085532926951642) |
| x | Negen_12 | ^146 c12 | [@Negen_11 The funniest thing about this tweet is I was a professional cg artist ](https://x.com/Negen_12/status/2062938146426552436) |
| x | keyokku | ^140 c3 | [THERE IT IS ITS #GUILDWARS3 FUCKKKKKKK HOLY SHIT IT LOOKS SO GOOD OMGGGG UNREAL ](https://x.com/keyokku/status/2063015318683820267) |
| x | koenjideck | ^134 c5 | [For people who weren't sure that Virtua Fighter Crossworlds was on the Dragon En](https://x.com/koenjideck/status/2063057559775264914) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MrEatYaAss</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 9345 · 💬 34</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MrEatYaAss/status/2063023812082274778">View @MrEatYaAss on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“17th Unreal Engine Asian blade game, hang it the fuck up man”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ X แซวว่า Asian blade game บน Unreal Engine มีออกมามากเกินไปแล้ว และ subgenre นี้หมดความแปลกใหม่แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MrEatYaAss/status/2063023812082274778" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@mofromyt</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5008 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/mofromyt/status/2062971023276826984">View @mofromyt on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“unreal engine be beating these devs ass”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ล้อเลียน dev ที่สู้ Unreal Engine ไม่ไหว ได้ 5k likes แสดงว่าคนในวงการ game dev รู้สึกเหมือนกันเยอะ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/mofromyt/status/2062971023276826984" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Petcson</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3038 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Petcson/status/2062663436618654148">View @Petcson on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Came up with a real simple way to make these flasks look like they have liquid! 💦 1. Model glass &amp;amp; invert the normals 2. Model the liquid 3. Rig the liquid with a bone facing up 4. in engine apply”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer @Petcson แชร์เทคนิค 4 ขั้น: invert normals ของ glass mesh, rig liquid ด้วย bone เดียว, แล้วใช้ jiggle physics + negative gravity ใน engine จำลอง liquid ที่ขยับได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่ต้องใช้ shader หรือ fluid sim — bone เดียว + physics constraint ได้ liquid ที่ดูดีพอ เหมาะกับ stylized game ที่ต้องการ draw call ต่ำ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity นำ pattern นี้ไปใช้กับ prop ขวด/ยา ใน project stylized game ได้เลย ไม่เพิ่ม shader overhead</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Petcson/status/2062663436618654148" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Windpress</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2633 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Windpress/status/2063059158010564800">View @Windpress on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Pixel art can be overdone in indie games, BUT when it is done CORRECTLY it is WAY better than Unreal Engine SLOP. Having less detail actually makes it FEEL more REAL and CHARMING. Something Triple A D”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev @Windpress มองว่า pixel art ที่ทำดีๆ ให้ความรู้สึกดีกว่างาน Unreal Engine ที่ detail ล้น เพราะ detail น้อยสร้าง emotional impact ได้แรงกว่า realism</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Windpress/status/2063059158010564800" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gcindisguise</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1695 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gcindisguise/status/2062942540936978776">View @gcindisguise on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“rocket league in the past 2 months - announced rocket league is moving to unreal engine 6 - are doing a fifa world cup themed season 23 - are adding all the quality of life features from bakkesmod - a”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Rocket League ยืนยันย้ายไป Unreal Engine 6 พร้อม ship feature QoL แนว BakkesMod, Easy Anti-Cheat สำหรับ ranked และ update จากชุมชนอีกหลายอย่างใน 2 เดือน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เกม live-service ใหญ่ที่ migrate ไป UE6 จริงในตอนนี้เป็น signal แรกๆ ของ production-scale ว่า engine transition นี้ต้องการอะไรและให้อะไรกลับมา</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตาม UE6 migration ของ Rocket League ใช้เป็น case study ถ้า studio ประเมิน Unreal Engine 6 สำหรับโปรเจกต์เกมในอนาคต</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gcindisguise/status/2062942540936978776" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheRedBarrels</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1080 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheRedBarrels/status/2062944416071926148">View @TheRedBarrels on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Start your day the Murkoff way. ☕ Two new #TheOutlastTrials mugs have arrived at the Red Barrels Store! Plus, several items are now back in stock! Which one are you adding to your collection? 👁️ Avail”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Red Barrels เปิดขาย mug ใหม่ 2 แบบธีม The Outlast Trials ในร้านค้าออนไลน์ พร้อมสินค้าเก่าที่นำกลับมาขายอีกครั้ง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheRedBarrels/status/2062944416071926148" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jasonappleton</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 886 · 💬 118</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jasonappleton/status/2062592937414853085">View @jasonappleton on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm personally tired of the bots and trolls crashing out on Charles. The market has been getting manipulated down for the past year. &quot;They&quot; want a reset before Clarity. It's the banks, institutions an”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักลงทุน Cardano โต้ว่าราคา ADA ที่ตกเป็นผลจากการ manipulate ตลาดโดย institution ก่อน regulatory framework 'Clarity' ไม่ใช่ความล้มเหลวของโปรเจกต์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jasonappleton/status/2062592937414853085" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ABGameDeveloper</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 803 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ABGameDeveloper/status/2063122004434391205">View @ABGameDeveloper on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Working on a new level where the protagonist becomes tiny… 🦊 #furry #horrorgame #indiedev #gamedev https://t.co/VHpBZeQS0Y”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev โพสต์ภาพ WIP ด่านใหม่ในเกม horror ที่ตัวละครหลักเป็นสุนัขจิ้งจอกขนาดเล็ก ไม่มีรายละเอียด technical เพิ่มเติม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ABGameDeveloper/status/2063122004434391205" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
