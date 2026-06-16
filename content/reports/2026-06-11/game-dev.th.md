---
type: social-topic-report
date: '2026-06-11'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-11T03:26:22+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 179
salience: 0.58
sentiment: mixed
confidence: 0.6
tags:
- unreal-engine-5
- unity
- ai-pipeline
- art-direction
- tooling
- indie
thumbnail: https://pbs.twimg.com/media/HKZjLqlW0AAtsgC.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-11

## TL;DR
- The Wolf Among Us 2 ยืนยันแล้วว่าย้ายออกจาก Telltale Engine มาใช้ Unreal Engine 5 วางจำหน่ายเป็นเกมเต็มครั้งเดียว ~8–12 ชม. (ไม่แบ่ง episode) เหตุการณ์เกิด 6 เดือนหลังภาคแรก ยังคง comic-book look [1][3][7][18][20].
- กระแส 'UE5 slop' แรง: นักวิจารณ์บอก Ocarina of Time remake [2][9], Fable [10], และ Halo CE remake [47] หน้าตาเหมือนกันหมด/แบบ Metahuman; มีคนพูดซ้ำบ่อยว่า 'อะไรที่ไม่ใช่ cel-shaded ก็โดนเรียก Unreal' [6][14].
- กิจกรรม AI ใน pipeline: Claude Code ขับเคลื่อน UE5 prototype ภายใน editor [53], Claude 'Fable' model ถูกใช้สร้าง 'spawn 5.0' (1,687 prompts, 102 sessions) [19], ความพยายามสร้าง GTA6 clone บน Claude Max 20x [17], รวมถึง AI tileset [34] และ single-image-to-3D world generators [41].
- เปิดตัว Unity tool: Lattice Modifier ของ Harry Heath เพิ่ม lattice deformation ให้ static + skinned meshes พร้อม compute shaders, keyframing, และ scripting [5].
- Unreal Fest จัดวันที่ 16–18 มิ.ย.; State of Unreal สตรีมวันที่ 17 มิ.ย. 9AM CT เน้น optimization ของ Epic tools และ 'what's next' สำหรับ Unreal Engine [44][49].

## What happened
cluster engagement ใหญ่สุดของวันคือ Telltale ยืนยัน The Wolf Among Us 2 ทิ้ง proprietary Telltale Engine หันมาใช้ Unreal Engine 5 โดย preview ระบุว่าเป็น release เดียว 8–12 ชม. เหตุการณ์อยู่ 6 เดือนหลังภาคแรก ยังคง comic art style [1][3][7][18][20] กระทู้ขนานกันวิจารณ์ visual homogenization ของ UE5 ใน remake ต่าง ๆ — Ocarina of Time [2][9], Fable [10], และ Halo CE [46][47][54] — หลายโพสต์โต้ว่าเกมที่ไม่ใช่ cel-shaded ถูกตีตรา 'Unreal slop' โดยอัตโนมัติ [6][14][16][33].

## Why it matters (reasoning)
สองเทรนด์เสริมกัน ประการแรก UE5 กำลังกลายเป็น default สำหรับ AA/AAA remake และ revival; studio ที่มี bespoke tech อย่าง Telltale ยังเลือกทิ้งมาใช้ Unreal [1] สะท้อนว่าการรักษา proprietary engine ไว้ยากจะคุ้มค่าเมื่อเทียบกับ tooling และ talent pool ของ UE5 ผลระดับสองคือ homogenization ที่มองเห็นได้ [2][10] — เมื่อหลาย team ใช้ default rendering และ Metahuman-style assets เหมือนกัน output จึงหลอมรวม และ art direction (ไม่ใช่ engine) กลายเป็นตัวแยกแยะ ประการสอง AI กำลังเข้าสู่ production loop จริง ไม่ใช่แค่ concept art: Claude Code เชื่อมต่อกับ UE5 project จริงพร้อม context ของ asset/editor ครบ [53] และ builder รายหนึ่งรายงานว่างานเปลี่ยนจาก 'architecture ไปสู่การตัดสิน taste' [19] ยังไม่ได้ verify เป็นแค่ claim ของผู้เขียนรายเดียว แต่ทิศทางสอดคล้องกัน — code/asset generation กำลังเชื่อมตรงเข้า engine คำวิจารณ์ของ Aaltonen ว่า mixed asset-store packs ไม่ fit กัน [51] เป็นตัวถ่วงดุล: ปริมาณ generation มากขึ้นโดยไม่ควบคุม coherence ทำให้คุณภาพตก

## Possibility
TWAU2 จะ ship บน UE5 ตามที่บรรยายไว้มีแนวโน้มสูง เพราะมี official studio statement และ preview หลายแหล่งยืนยัน [7][18][20] UE5 ครอง remake ต่อไปมีแนวโน้มสูง [1][2][10] โดยกระแสต้าน art-direction น่าจะผลักบาง studio ไปทาง stylized/cel-shaded เพื่อหลีก label 'generic Unreal' [6][9] AI engine integration ที่พัฒนาจนเป็น production tool ที่เชื่อถือได้เป็นไปได้แต่ยังไม่มีหลักฐานพิสูจน์ — หลักฐานปัจจุบันเป็นแค่ demo และ claim รายบุคคล [17][19][53] ไม่ใช่ title ที่ ship แล้ว; ปัญหาด้าน quality และ asset-coherence [51] ทำให้การพึ่งพาใน production ระยะสั้นยังไม่น่าเกิดขึ้น State of Unreal วันที่ 17 มิ.ย. น่าจะมี optimization tooling ที่จับต้องได้ตามวาระที่ประกาศไว้ [49].

## Org applicability — NDF DEV
NDF DEV เน้น Unity เป็นหลัก ควรชั่งน้ำหนักตามนั้น (1) ทดลอง Claude Code + Unity MCP สำหรับ in-editor prototyping — studio มี UnityMCP tooling อยู่แล้ว; UE5 analog [53] และ workflow 'taste over architecture' [19] แสดงว่า pattern นี้ใช้ได้แล้ว effort med [53][19]. (2) ประเมิน Lattice Modifier ของ Harry Heath สำหรับ character/prop mesh deformation ใน Unity projects — เพิ่ม toolchain ต้นทุนต่ำ [5] effort low [5]. (3) ติดตาม State of Unreal วันที่ 17 มิ.ย. หา optimization techniques ที่นำมาใช้กับ rendering/production ทั่วไปได้ แม้จะยังอยู่บน Unity [44][49] effort low [49]. (4) ใช้ art-direction coherence เป็นตัวแยกแยะโดยเจตนาใน XR/edutech — กระแสต้าน homogenization [2][10] บ่งชี้ว่า stylized look ที่โดดเด่นดูดีกว่า realism แบบ default effort med [2][10]. (5) บังคับใช้ asset coherence: เลือก asset ชุดเล็กที่สอดคล้องกันหรือสั่งทำเองแทนการผสม store packs [51] effort low [51]. ข้ามไปก่อน: การวางเดิมพัน production กับ AI platform ระดับ 'studio-grade' อย่าง DAOverse [23] หรือ single-image world generators [41] — เป็นแค่ marketing ที่ยังไม่มีหลักฐาน ship จริง

## Signals to Watch
- State of Unreal วันที่ 17 มิ.ย. (9AM CT) หา optimization tooling ที่จับต้องได้ [49].
- ว่า Claude Code → engine integrations จะข้ามพ้น demo ไปสู่ feature ที่ ship ได้จริงหรือไม่ [53][17][19].
- AI asset/world generators (tilesets [34], single-image 3D [41]) และ output coherence เทียบกับคำวิจารณ์เรื่อง asset-fragmentation [51].
- ปฏิกิริยาตลาดต่อกระแสต้าน UE5 art-direction ที่กำหนดความคาดหวัง remake [2][10].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | DomTheBomb | ^1798 c16 | [Telltale Games has officially moved on from the Telltale Engine and The Wolf Amo](https://x.com/DomTheBomb/status/2064777114919022662) |
| x | AussieGamr | ^1572 c134 | [People slamming the new Ocarina of Time remake's art direction are repeating the](https://x.com/AussieGamr/status/2064603671216931256) |
| x | shinobi602 | ^1539 c24 | [The Wolf Among Us 2 / New Details and Previews ▪️"Looks fantastic", "looking to ](https://x.com/shinobi602/status/2064776133564870847) |
| x | ID_AA_Carmack | ^1277 c45 | [Trista had never played tabletop Dungeons & Dragons before, so I recently dusted](https://x.com/ID_AA_Carmack/status/2064720302005748031) |
| x | GameZoneHQ | ^1203 c6 | [This is a really smart Unity tool release 🔥 Harry Heath's Lattice Modifier bring](https://x.com/GameZoneHQ/status/2064322319124738285) |
| x | KirboP73024 | ^1103 c5 | [This is Twitter everything that is not cel shaded its automatically unreal engin](https://x.com/KirboP73024/status/2064743046428729674) |
| x | telltalegames | ^1031 c25 | ["Yes, I've seen it. It's real, and it's now running on Unreal Engine 5…what matt](https://x.com/telltalegames/status/2064774858483888228) |
| x | cherry_pic9129 | ^929 c7 | [New idle animation for Orca! ✨ #indieDev #Devlog #D1ALogue https://t.co/9vDUBLO3](https://x.com/cherry_pic9129/status/2064716717134328083) |
| x | moripoyo_art | ^696 c46 | [I'm sorry to say it but Ocarina of Time remake looks more like Hyrule Warriors t](https://x.com/moripoyo_art/status/2064610374389805165) |
| x | Grummz | ^659 c39 | [What happened to Fable art direction? It used to look like this. Now it feels li](https://x.com/Grummz/status/2064805770106184147) |
| x | JJWong34755181 | ^538 c7 | [Steam Page is available. Game's name: &lt;Not Only One Brain&gt; A survival horr](https://x.com/JJWong34755181/status/2064663593183056146) |
| x | BorgesDev | ^496 c8 | [Better graphics Settings #Godot https://t.co/AHp0VK53Ur](https://x.com/BorgesDev/status/2064736784915820949) |
| x | HedProtag | ^469 c8 | [None of THIS will stop me. Here is some awesome sick footage of the work-in prog](https://x.com/HedProtag/status/2064891582847819908) |
| x | starsuper64 | ^449 c3 | [@JoshuaTookes They really took Schaffrillas and gave him the Unreal Engine treat](https://x.com/starsuper64/status/2064775662246727785) |
| x | ParanoiaCy81004 | ^344 c5 | [Come meet this cute therapy robot. You can do Whatever you WANT with him❤️ #Cybe](https://x.com/ParanoiaCy81004/status/2064624631345209818) |
| x | KaizokuBalls | ^334 c6 | [&gt;the best game of all time is getting a remake, why are you complaining say t](https://x.com/KaizokuBalls/status/2064596377242415358) |
| x | ziwenxu_ | ^329 c53 | [Day 1 of building GTA 6. Still feels fake typing that out. Upgraded to Claude Ma](https://x.com/ziwenxu_/status/2064821269380362386) |
| x | HazzadorGamin | ^313 c2 | [The Wolf Among US 2 Preview • 8-12 hrs long • Launches as one full game • Set 6 ](https://x.com/HazzadorGamin/status/2064778117827453256) |
| x | jsnnsa | ^250 c22 | [claude fable 5 is live. spawn 5.0 was built with it: 1,687 prompts, 102 sessions](https://x.com/jsnnsa/status/2064420561078693941) |
| x | TWAUWiki | ^213 c3 | [The Wolf Among Us 2 details so far: — Unreal Engine 5 while keeping the comic bo](https://x.com/TWAUWiki/status/2064786698840490128) |
| x | ID_AA_Carmack | ^187 c2 | [A novel thing for me happened during character creation: one of the players had ](https://x.com/ID_AA_Carmack/status/2064720305868640532) |
| x | the_MegaByte | ^184 c4 | [Broke something? Use Reversal Powder! This will restore destroyed objects. Your ](https://x.com/the_MegaByte/status/2064724273390883198) |
| x | daoverse_games | ^183 c28 | [Studio-quality games have always needed a studio. A big team, a publisher, and a](https://x.com/daoverse_games/status/2064765814037700833) |
| x | Inomi133 | ^180 c5 | [There's a huge centipede in the basement 👻 #gamedev #indiegame #indiedev https:/](https://x.com/Inomi133/status/2064797063187959819) |
| x | ID_AA_Carmack | ^179 c12 | [I always add a few low-level player friendly rule tweaks, but my favorite house ](https://x.com/ID_AA_Carmack/status/2064720308490092844) |
| x | StormcoreDev | ^169 c0 | [WIP for water spell "Hydro-Megia." We captured water particles from Blender in c](https://x.com/StormcoreDev/status/2064627351145865449) |
| x | drattzy | ^165 c4 | [Alterium Shift carries the spirit of the JRPGs we grew up with. Inspired by clas](https://x.com/drattzy/status/2064724755064770585) |
| x | OzgursAssets | ^162 c2 | [Traffic Racer (2013) - VW Beetle 1300 #trafficracer #gamedev #indiedev #ue5 #Uni](https://x.com/OzgursAssets/status/2064283966144651317) |
| x | JiltedValkyrie | ^162 c15 | [Guys, I think I just noclipped into some unending place with infinite rooms with](https://x.com/JiltedValkyrie/status/2064766455267102723) |
| x | ID_AA_Carmack | ^156 c5 | [@evildojo666 Trista is my partner, not my daughter 😃. You can see my original 4'](https://x.com/ID_AA_Carmack/status/2064755973336482288) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DomTheBomb</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1798 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DomTheBomb/status/2064777114919022662">View @DomTheBomb on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Telltale Games has officially moved on from the Telltale Engine and The Wolf Among Us 2 will be on Unreal Engine 5 🔥🎮 https://t.co/9egQcnpfi1”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Telltale Games ยืนยันย้าย The Wolf Among Us 2 จาก Telltale Engine เดิมมาใช้ Unreal Engine 5</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Studio ที่เน้น narrative เลือก UE5 แทน engine เดิม — ยืนยันว่า UE5 ใช้ได้จริงกับเกมแนว cinematic/dialogue-heavy</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ใช้เคสนี้อ้างอิงได้เวลา pitch งาน cinematic หรือ story-driven ที่อาจพิจารณา UE5</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DomTheBomb/status/2064777114919022662" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AussieGamr</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1572 · 💬 134</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AussieGamr/status/2064603671216931256">View @AussieGamr on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“People slamming the new Ocarina of Time remake’s art direction are repeating the same mistake. The trailer hit and the complaints started straight away. Too realistic. Looks like some generic Unreal E”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิจารณ์บน Twitter ชี้ว่ากระแสต่อต้าน art style ของ Ocarina of Time remake ซ้ำรอย Wind Waker และ Nintendo มักพิสูจน์ว่าตัวเองถูกในระยะยาว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AussieGamr/status/2064603671216931256" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@shinobi602</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1539 · 💬 24</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/shinobi602/status/2064776133564870847">View @shinobi602 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Wolf Among Us 2 | New Details and Previews ▪️&quot;Looks fantastic&quot;, &quot;looking to be a worthy sequel&quot; ▪️Now running on UE5, still retains the same comic book style look but running on modern tech ▪️Arou”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>The Wolf Among Us 2 รันบน UE5 แต่รักษา art style แบบ comic book ไว้ได้ ออกเป็นเกมเต็มไม่แบ่ง episode ยาว 8-12 ชั่วโมง มี full mocap และกล้อง 360°</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>UE5 รักษา stylized comic-book look ได้โดยไม่ต้องรีเซ็ต art direction — เป็น precedent ที่ดีสำหรับโปรเจกต์ stylized บน engine ใหม่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ใช้ TWAU2 เป็น reference ตอน scope งาน stylized บน UE5 เพื่อแสดงให้ client เห็นว่า 2D-adjacent aesthetic รอดได้บน engine ใหม่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/shinobi602/status/2064776133564870847" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ID_AA_Carmack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1277 · 💬 45</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ID_AA_Carmack/status/2064720302005748031">View @ID_AA_Carmack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Trista had never played tabletop Dungeons &amp; Dragons before, so I recently dusted off some old skills and ran a little four player game for her. I never learned modern 5e rules, and I wanted to keep it”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>John Carmack จัด session D&amp;D แบบ tabletop ให้แฟนสาว โดยใช้กฎ Rules Cyclopedia และ miniature ที่ผู้เล่นทุกคนระบายสีเอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ID_AA_Carmack/status/2064720302005748031" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GameZoneHQ</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1203 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GameZoneHQ/status/2064322319124738285">View @GameZoneHQ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is a really smart Unity tool release 🔥 Harry Heath’s Lattice Modifier brings lattice-based deformation to static + skinned meshes, supports keyframing and scripting, and uses compute shaders for ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Harry Heath ปล่อย Lattice Modifier สำหรับ Unity — deform mesh ทั้ง static และ skinned ผ่าน lattice, รองรับ keyframing และ scripting, ใช้ compute shader ได้ performance เทียบเท่า GPU skinning</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Unity ไม่มี lattice deformer built-in — tool นี้เติมช่องโหว่สำหรับ squash-stretch, prop animation, และ runtime mesh FX โดยไม่ต้องเขียน custom vertex shader เอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลองใช้กับ character หรือ environment asset ใน project ปัจจุบัน ดูว่าแทน custom deformation code เดิมได้หรือเปล่า</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GameZoneHQ/status/2064322319124738285" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KirboP73024</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1103 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KirboP73024/status/2064743046428729674">View @KirboP73024 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is Twitter everything that is not cel shaded its automatically unreal engine slop”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ Twitter ระบุว่าเกมที่ไม่ใช่ cel-shaded ทุกเกมคือ Unreal Engine slop โดยไม่มีหลักฐานหรือบริบทเชิงเทคนิครองรับ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KirboP73024/status/2064743046428729674" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@telltalegames</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1031 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/telltalegames/status/2064774858483888228">View @telltalegames on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">““Yes, I've seen it. It's real, and it's now running on Unreal Engine 5…what matters is that somehow, The Wolf Among Us 2 is still alive, and I couldn't be happier about it.” https://t.co/1lEphpHDN8 ht”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Telltale Games ยืนยัน The Wolf Among Us 2 ยังอยู่ในการพัฒนา และย้ายมาทำบน Unreal Engine 5 หลังจากหายไปนานหลังสตูดิโอปิดตัวปี 2018</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/telltalegames/status/2064774858483888228" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cherry_pic9129</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 929 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cherry_pic9129/status/2064716717134328083">View @cherry_pic9129 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“New idle animation for Orca! ✨ #indieDev #Devlog #D1ALogue https://t.co/9vDUBLO30x”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev โพสต์ idle animation ใหม่ของตัวละคร Orca ในเกม D1ALogue</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cherry_pic9129/status/2064716717134328083" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
