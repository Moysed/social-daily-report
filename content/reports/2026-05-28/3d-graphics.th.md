---
type: social-topic-report
date: '2026-05-28'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-05-28T03:32:04+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- reddit
- x
regions:
- global
post_count: 64
salience: 0.62
sentiment: mixed
confidence: 0.68
tags:
- gaussian-splatting
- blender
- ai-video
- shaders
- unity
- previs
thumbnail: https://external-preview.redd.it/eXg3OTk3Mjh4cDNoMd9Qn7y5N5D268ReIaIXhfcTYlZHHdFBk-z0Qh3Se9gx.png?format=pjpg&auto=webp&s=509255971f64b4b19eaf38102568c3a85d2aff15
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-05-28

## TL;DR
- เส้นทางกล้องที่ขับเคลื่อนด้วย AI (Google Omni/Flow) แปลงเส้นร่างเป็นฟุตเทจมุมมองโดรน — previsualization รวดเร็ว ไม่ต้องใช้อุปกรณ์จริง [2][14][42][54][59]
- Gaussian Splatting เข้าสู่การใช้งานจริง: พาร์ทเนอร์ชิปการแคปเจอร์เมืองระดับโดรน และ use case ด้านการท่องเที่ยว/มรดกทางวัฒนธรรม [40][36][41]
- TriSplat เสนอ triangle mesh แบบ feed-forward ที่พร้อมใช้กับ physics จากภาพ sparse — ข้ามขั้นตอน Gaussian/mesh-extraction [56]
- Toon/painterly shader ข้ามจาก Blender ไป Unity URP ผ่าน fullscreen post pass; เผยแพร่การวิเคราะห์สไตล์ Guilty Gear เช่นกัน [29][1][28]
- Godot WebGPU ได้รับ GPU-driven rendering แบบ Nanite-style — การเปลี่ยนแปลงระดับ engine ไม่ใช่แค่ shader trick [32]

## What happened
สัญญาณสำคัญแบ่งออกเป็นสามกลุ่ม การผสาน AI/3D ครองกระแสหลัก: เส้นทางที่ร่างด้วยมือของ Bilawal Sidhu ที่แปลงเป็นฟุตเทจโดรนผ่าน Google Omni/Flow แพร่กระจายอย่างรวดเร็วและก่อให้เกิดกระแสเลียนแบบบน Seedance [2][14][42][54][59]; KIRI แสดง environment ที่แคปเจอร์ด้วย splat ประกอบกับตัวละครที่สร้างด้วย AI [58]; Claude Code ควบคุม Blender อัตโนมัติเป็นเวลาหนึ่งชั่วโมงเพื่อสร้างระบบ Geometry Nodes และ retargeting [51] ด้านการแคปเจอร์/reconstruction: Niantic + Spexi เป็นพาร์ทเนอร์กันถ่าย Gaussian splat ระดับเมืองด้วยโดรน [40], อัปโหลด splat ของ Ferstel Passage ผ่าน XGRIDS PortalCam [36], และ paper TriSplat อ้างว่าสร้าง triangle พร้อมใช้งานใน simulation โดยตรงจากภาพ sparse ที่ไม่มี pose [56] ด้าน tooling/shader: การวิเคราะห์ vintage cartoon shader ติดอันดับต้นของ r/blender [1], การ recreate painterly post-process จาก Blender ไป Unity URP เวียนในวงการ [29], เผยแพร่ writeup เทคนิค Guilty Gear [28], Godot WebGPU ได้รับ GPU-driven rendering แบบ Nanite-style [32], และ grass shader ใน Unity ผ่าน vertex-color wind ที่ทำโดย solo dev ถูก ship ออกมา [50] สัญญาณพื้นหลัง: โพสต์ portfolio บน Blender จำนวนมาก [4][6][7][9][13][15], บทเรียนเตือนใจเรื่องลูกค้าไม่จ่ายค่าจ้าง freelance [5], และการถกเถียงเรื่อง graphics API เกี่ยวกับ descriptor/binding [22]

## Why it matters (reasoning)
การเปลี่ยนแปลงเชิงโครงสร้างสองประเด็นที่สำคัญต่อ studio ประเด็นแรก เครื่องมือ AI camera-path ลดต้นทุน previs ลงอย่างมาก: เส้นทางที่ร่างบนแผนที่กลายเป็นฟุตเทจ flyover ภายในไม่กี่นาที [2][14][42] — การนำเสนอ XR หรือ game cinematics ไม่จำเป็นต้องตั้งกล้องใน Unity หรือ Unreal Sequencer สำหรับการดูภาพแรก ประเด็นที่สอง Gaussian Splatting กำลังเคลื่อนจาก research demo ไปสู่ commercial pipeline (Niantic/Spexi ว่าจ้างบินสำรวจ [40], KIRI ประกอบ real splat กับตัวละคร AI [58], ระบุการท่องเที่ยว/มรดกทางวัฒนธรรมเป็นเป้าหมายการ disrupt อย่างชัดเจน [36]) สำหรับ XR มรดกทางวัฒนธรรมไทยหรือ location-based edutech นี่ช่วยลดต้นทุนการแคปเจอร์ลงอย่างมีนัยสำคัญ TriSplat [56] คือตัวแปรที่คาดเดาได้ยาก — หากการแปลง feed-forward ไปเป็น triangle mesh ทำได้จริง มันจะข้ามปัญหาการแปลง splat-to-mesh ที่ปัจจุบันเป็นอุปสรรคต่อการใช้ splat กับ Unity physics/lighting ด้าน painterly/toon shader ที่ port ข้าม engine [29][28][1] ยืนยันว่า stylized non-realistic look ยังคงเป็น visual differentiator ที่ปกป้องได้ดีที่สุดเมื่อเทียบกับ content photoreal ที่สร้างด้วย AI

## Possibility
3–6 เดือนข้างหน้า: (a) โอกาส ~70% ที่ AI camera-path → video จะกลายเป็นขั้นตอน previs มาตรฐานใน indie pipeline; คุณภาพยังไม่สม่ำเสมอสำหรับ hero shot แต่ใช้ได้ดีสำหรับการนำเสนองาน (b) โอกาส ~60% ที่ Gaussian Splatting capture-as-a-service จะเข้าถึง Southeast Asia ผ่าน XGRIDS หรือผู้ให้บริการโดรนท้องถิ่นภายในหนึ่งปี (c) โอกาส ~40% ที่ TriSplat หรือเทคนิค feed-forward-to-mesh ที่คล้ายกันจะ viable ในระดับ production ในปี 2026 — ยังอยู่ในขั้น paper ยังไม่มีเครื่องมือที่ ship จริง (d) โอกาส ~80% ที่ stylized/toon shader workflow จะยังคงมีประสิทธิภาพเหนือกว่า AI photoreal ในด้าน brand identity สำหรับเกม ความเสี่ยงทวนกระแส: เครื่องมือ AI video (Omni, Seedance, Luma) กดดันความต้องการ traditional 3D motion design — ดูข้อพิพาท freelance ใน [5] เป็นสัญญาณความเครียดในระยะต้น

## Org applicability — NDF DEV
ทดลองได้เลย ต้นทุนต่ำ: (1) ทดสอบ Google Flow/Omni sketched-path previs สำหรับ pitch ลูกค้าด้าน XR location experience และ game cinematics — spike 1 วัน ไม่ต้องเปลี่ยน pipeline [2][59] (2) แคปเจอร์วัดในเชียงใหม่หรือ interior ของ studio ด้วยเครื่องมือ Gaussian Splat บนโทรศัพท์ (KIRI Engine, Polycam) แล้วลอง import เข้า Unity ผ่าน splat plugin ที่มีอยู่ — มีประโยชน์สำหรับ pitch XR มรดกทางวัฒนธรรม [36][58] (3) จับตา TriSplat [56] แต่ยังไม่ต้องสร้างบนนั้นจนกว่า code จะ release (4) สำหรับ Unity edutech, URP painterly post-process [29] และ grass shader [50] สามารถนำไปใช้ใน Next.js-embedded WebGL หรือ Unity WebGL build ได้โดยตรง ข้ามไปได้เลย: Claude-Code-drives-Blender [51] เป็นแค่ novelty ยังไม่ production-ready; Godot Nanite [32] น่าสนใจแต่ studio ใช้ Unity เป็นหลัก

## Signals to Watch
- TriSplat code release หรือ Unity/Unreal importer สำหรับ feed-forward mesh
- ความพร้อมและราคาของ XGRIDS PortalCam หรือฮาร์ดแวร์แคปเจอร์ splat ที่เทียบเคียงในไทย
- การเข้าถึง API หรือ pricing tier เชิงพาณิชย์สำหรับ Google Flow/Omni ในงาน previs
- การรองรับ Gaussian Splatting render pipeline อย่างเป็นทางการของ Unity (ปัจจุบันเป็น community plugin เท่านั้น)

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | rahulparihar | ^4479 c46 | [Vintage cartoon shaders in Blender](https://www.reddit.com/r/blender/comments/1tpd4c0/vintage_cartoon_shaders_in_blender/) |
| x | bilawalsidhu | ^2999 c131 | [Gave google omni a sketched camera path and asked it to generate drone POV foota](https://x.com/bilawalsidhu/status/2059419767417487718) |
| reddit | flockaroo | ^838 c27 | [home grown gas giant](https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/) |
| x | 3DxDEV7 | ^700 c3 | [DreamWorks animator Nicolas Prothais showcased a stunning Kung Fu Panda rig in B](https://x.com/3DxDEV7/status/2059497395352748099) |
| reddit | Vegetable-Site-3715 | ^512 c78 | [Client agreed to pay hourly on a recorded call, then denied the whole agreement ](https://www.reddit.com/r/blender/comments/1toxcb6/client_agreed_to_pay_hourly_on_a_recorded_call/) |
| reddit | Wellie_man | ^507 c18 | [First attempts at making a walk cycle! How'd I do?](https://www.reddit.com/r/blender/comments/1tp6fah/first_attempts_at_making_a_walk_cycle_howd_i_do/) |
| x | BrainezVisuals | ^477 c57 | [I just turned 18. Here's my VFX/CG work. #b3d #blender https://t.co/g6RRZSsTZm](https://x.com/BrainezVisuals/status/2059681346449031677) |
| reddit | x_otosaka_x | ^458 c19 | [I made a moroccan-themed slot machine inspired by moorish architecture and desig](https://www.reddit.com/r/blender/comments/1tpd00r/i_made_a_moroccanthemed_slot_machine/) |
| reddit | LoquatPutrid2894 | ^306 c17 | [Made Saber Artoria Pendragon, used only blender , how is it ?](https://www.reddit.com/r/blender/comments/1toxkbq/made_saber_artoria_pendragon_used_only_blender/) |
| reddit | Legal-Collection2425 | ^294 c29 | [i present the ice cube on plate do you like it](https://www.reddit.com/r/blender/comments/1tp89ev/i_present_the_ice_cube_on_plate/) |
| reddit | OzGang | ^228 c8 | [NYC Subway Full CGI (Blender + DaVinci Resolve)](https://www.reddit.com/r/blender/comments/1tpmpvd/nyc_subway_full_cgi_blender_davinci_resolve/) |
| x | austin_rief | ^207 c38 | [I'm hiring a founding engineer for my new company. You'll be a good fit if you: ](https://x.com/austin_rief/status/2059704887118586039) |
| reddit | creationstation99 | ^185 c15 | [Made this low poly character in blender](https://www.reddit.com/r/blender/comments/1tp0hu6/made_this_low_poly_character_in_blender/) |
| x | bilawalsidhu | ^181 c4 | [Camera path scribbles are turning into an AI video trend. Cool seedance example ](https://x.com/bilawalsidhu/status/2059751008746471791) |
| reddit | Sufficient-Limit-392 | ^177 c8 | [The stuff I animated](https://www.reddit.com/r/blender/comments/1tpi497/the_stuff_i_animated/) |
| x | A_fan_of_Sonic | ^162 c2 | [Ripped, fixed, and shaded Goku from Sparking! Zero for Blender! 🐉✨ Free download](https://x.com/A_fan_of_Sonic/status/2059644148907417663) |
| x | sevenout | ^157 c0 | [@MarkDuplass They're saying the same thing about Curry Barker, that some mystery](https://x.com/sevenout/status/2059398926797537667) |
| x | vikare06 | ^150 c12 | [There is no discernible design in that image. Just asking GPT to generate a monu](https://x.com/vikare06/status/2059580032826101762) |
| reddit | Unhappy_Document_796 | ^145 c5 | [Yet another test anim](https://www.reddit.com/r/blender/comments/1tpfazt/yet_another_test_anim/) |
| reddit | AlarmedBag9653 | ^143 c17 | [Procedural Creature gen and animation Procedural creature generation and animati](https://www.reddit.com/r/proceduralgeneration/comments/1to7rei/procedural_creature_gen_and_animation/) |
| reddit | Working-Winner52 | ^142 c23 | [Please rate my art and also suggest what I should improve](https://www.reddit.com/r/blender/comments/1tpoqad/please_rate_my_art_and_also_suggest_what_i_should/) |
| reddit | Content_Economist132 | ^137 c36 | [Why do graphics apis need so many layers of abstractions like buffer, descriptor](https://www.reddit.com/r/GraphicsProgramming/comments/1tow7ic/why_do_graphics_apis_need_so_many_layers_of/) |
| reddit | Affectionate_Fly_457 | ^109 c8 | [Made something new using particles](https://www.reddit.com/r/blender/comments/1tp0qt2/made_something_new_using_particles/) |
| reddit | huleeb | ^108 c5 | [the forgotten pipeline](https://www.reddit.com/r/blender/comments/1tp5ehx/the_forgotten_pipeline/) |
| reddit | islammhran_86 | ^97 c6 | [Warm Luxury Interior in Blender I have also completed a **daylight version** of ](https://www.reddit.com/r/blender/comments/1tpc074/warm_luxury_interior_in_blender/) |
| x | HidemyCG | ^89 c0 | [The most optimal renderer settings for a close-up scene with glass and the glass](https://x.com/HidemyCG/status/2059658635236528157) |
| reddit | ExistingMark2998 | ^79 c20 | [first blender ANIMATION!!! rate my work :)) also any idea what should i start ne](https://www.reddit.com/r/blender/comments/1tp3t7w/first_blender_animation/) |
| x | Noggi_3D | ^77 c1 | [I finished setting up a page explaining the techniques Guilty Gear uses to creat](https://x.com/Noggi_3D/status/2059683849521508509) |
| x | jettelly | ^77 c0 | [Developer tantaneity shared how they recreated a painterly shader from Blender i](https://x.com/jettelly/status/2059243161311187193) |
| reddit | Significant-Tree4752 | ^73 c3 | [Maria Calavera: Life and Death scythe (WIP) Maria's weapon did it while practici](https://www.reddit.com/r/blender/comments/1tp2tqk/maria_calavera_life_and_death_scythe_wip/) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@rahulparihar</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 4479 · 💬 46</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tpd4c0/vintage_cartoon_shaders_in_blender/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/eXg3OTk3Mjh4cDNoMd9Qn7y5N5D268ReIaIXhfcTYlZHHdFBk-z0Qh3Se9gx.png?format=pjpg&amp;auto=webp&amp;s=509255971f64b4b19eaf38102568c3a85d2aff15" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Vintage cartoon shaders in Blender”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist ใน Blender แชร์ shader สไตล์การ์ตูนวินเทจที่จำลองลุค retro hand-drawn ด้วย node editor ของ Blender</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Shader breakdown ที่ได้รับ engagement สูง (4k+ likes) บ่งชี้ว่า NPR stylized rendering กำลังเป็นที่ต้องการสูงในวงการ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team นำ shader logic นี้มา port เป็น custom cartoon pass ใน URP Shader Graph ได้เลย — ตรงกับงาน XR หรือ e-learning ที่ต้องการสไตล์ stylized</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tpd4c0/vintage_cartoon_shaders_in_blender/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2999 · 💬 131</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2059419767417487718">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gave google omni a sketched camera path and asked it to generate drone POV footage. https://t.co/cQZFMtOkEi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Google Omni สร้างวิดีโอ drone POV จาก camera path ที่วาดด้วยมือเปล่าๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Sketch-to-video ตัด pre-vis pipeline ออกได้เลย — ไม่ต้องเช่า drone หรือใช้ software 3D แค่วาด path แล้วได้ footage ทดสอบ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR ใช้ prototype flythrough cinematic และ VR environment reveal ได้ก่อน block จริงใน engine หรือถ่าย reference จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2059419767417487718" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@flockaroo</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 838 · 💬 27</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/c3g3bHdsdm15aTNoMVQtrb6zyT3nVgsSB9Yrq2NdNhskp9hccODKkoNMp-gx.png?format=pjpg&amp;auto=webp&amp;s=39d0536eb07e798dacd50cf924457269fb83feff" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“home grown gas giant”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Gas giant ที่ generate ด้วย procedural technique โพสต์ใน r/proceduralgeneration — ผลลัพธ์ให้ภาพดาวแบบ Jupiter จาก shader หรือ simulation ที่เขียนเอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>838 upvotes บอกว่า procedural planet เป็นที่ต้องการสูงในชุมชน — สัญญาณชัดว่า aesthetic แบบ space/sci-fi มี value ใน indie และ XR ตอนนี้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู technique ของ flockaroo แล้วทำ procedural planet shader แบบ reusable สำหรับ environment แนว space ใน game หรือ XR แทนการใช้ static texture</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 700 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2059497395352748099">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“DreamWorks animator Nicolas Prothais showcased a stunning Kung Fu Panda rig in Blender using Rigify, seriously impressive 🔥🐼 #B3D #Blender3D #Blender #Animation #Rigify #CharacterRigging #3DArt #VFX h”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Animator จาก DreamWorks ชื่อ Nicolas Prothais โชว์ character rig ของ Kung Fu Panda ที่ทำใน Blender โดยใช้ Rigify add-on ระดับโปร</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>rig ระดับ production จาก DreamWorks ถูกสร้างใหม่ด้วย Blender/Rigify ฟรี พิสูจน์ว่า character animation ระดับ studio ทำได้โดยไม่ต้องใช้ซอฟต์แวร์ราคาแพง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ศึกษา Rigify workflow นี้เพื่อสร้าง rig ที่ reuse ได้สำหรับ character ใน XR/game ลด rigging time ในโปรเจกต์ 3D ถัดไป</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2059497395352748099" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Wellie_man</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 507 · 💬 18</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tp6fah/first_attempts_at_making_a_walk_cycle_howd_i_do/" target="_blank" rel="noopener"><img src="https://i.redd.it/x1zm4ycwro3h1.gif" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“First attempts at making a walk cycle! How'd I do?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>User ใน Blender community โพสต์ walk cycle แรกของตัวเองแล้วขอ feedback จากคนอื่น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Walk cycle เป็นพื้นฐาน animation สำคัญ — การ critique จาก community ช่วยพัฒนาได้เร็วกว่าฝึกคนเดียวมาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู thread critique แบบนี้เป็น reference ฟรีสำหรับประเมิน quality ของ character animation ก่อน import เข้า engine</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tp6fah/first_attempts_at_making_a_walk_cycle_howd_i_do/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@BrainezVisuals</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 477 · 💬 57</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/BrainezVisuals/status/2059681346449031677">View @BrainezVisuals on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I just turned 18. Here's my VFX/CG work. #b3d #blender https://t.co/g6RRZSsTZm”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Creator อายุ 18 โชว์ portfolio VFX/CG ที่ทำด้วย Blender แสดงฝีมือ 3D และ visual effects ที่เรียนรู้เอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>งาน VFX คุณภาพสูงจาก artist วัย 18 คนเดียว พิสูจน์ว่า Blender ทำได้ระดับ production จริงโดยไม่ต้องมี studio resources</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity และ XR หา artist สาย Blender แบบนี้มาทำ VFX assets freelance ได้ ระดับฝีมือแบบนี้ใช้เป็น benchmark จ้างงาน junior ด้วย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/BrainezVisuals/status/2059681346449031677" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@x_otosaka_x</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 458 · 💬 19</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tpd00r/i_made_a_moroccanthemed_slot_machine/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/Mm05emZwNGJ3cDNoMZJUmXUucVO8qDsVPdtz19OfQWpAFS9IwdVRzavJoUoJ.png?format=pjpg&amp;auto=webp&amp;s=8bec2a4c4cb152ec786ece2a8ca24e3966e1f14c" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I made a moroccan-themed slot machine inspired by moorish architecture and design”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ศิลปิน Blender สร้าง 3D slot machine ดีเทลสูงในสไตล์สถาปัตยกรรมโมร็อกโก/Moorish พร้อม ornament ละเอียด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ตัวอย่างชัดว่า motif สถาปัตยกรรมจากวัฒนธรรมเฉพาะยก prop ธรรมดาให้ดูโดดเด่น ใช้เป็น reference art direction ใน game environment ธีมวัฒนธรรมได้ดี</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู reference นี้ตอนทำ prop ธีมวัฒนธรรม ศึกษา geometric pattern แบบ Moorish เพื่อเพิ่ม authenticity โดยไม่บวก poly count เกิน</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tpd00r/i_made_a_moroccanthemed_slot_machine/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@LoquatPutrid2894</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 306 · 💬 17</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1toxkbq/made_saber_artoria_pendragon_used_only_blender/" target="_blank" rel="noopener"><img src="https://preview.redd.it/s2j7c7uamm3h1.jpg?width=2048&amp;format=pjpg&amp;auto=webp&amp;s=bf6f5f9af3cd96f147d0893046d5fef9f8a5fbde" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Made Saber Artoria Pendragon, used only blender , how is it ?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Reddit user โชว์ 3D character ของ Saber Artoria Pendragon จาก Fate series ที่ทำใน Blender ทั้งหมด ขอ feedback</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แสดงให้เห็นว่า Blender คือ pipeline เดียวครบสำหรับ anime-style character art โดยไม่ต้องพึ่ง tool อื่น</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู workflow นี้เป็นแนวทางสร้าง character asset ใน Blender ล้วน ลด dependency จาก tool ที่มีค่าใช้จ่ายอย่าง ZBrush หรือ Maya</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1toxkbq/made_saber_artoria_pendragon_used_only_blender/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
</div>
