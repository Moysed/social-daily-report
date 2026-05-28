---
type: social-topic-report
date: '2026-05-28'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-05-28T05:01:01+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- reddit
- x
regions:
- global
post_count: 69
salience: 0.78
sentiment: positive
confidence: 0.72
tags:
- gaussian-splatting
- blender
- ai-previz
- shaders
- unity
- photogrammetry
thumbnail: https://external-preview.redd.it/eXg3OTk3Mjh4cDNoMd9Qn7y5N5D268ReIaIXhfcTYlZHHdFBk-z0Qh3Se9gx.png?format=pjpg&auto=webp&s=509255971f64b4b19eaf38102568c3a85d2aff15
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-05-28

## TL;DR
- Sketch-to-drone-POV video ผ่าน Google Omni/Flow กำลังไวรัล [2][14][43][54] — วิธีใหม่ที่เร็วมากสำหรับการ previsualize การเคลื่อนกล้องโดยไม่ต้องทำ 3D blockout
- Gaussian Splatting เข้าสู่เชิงพาณิชย์: Niantic×Spexi ทำ city-scale drone splats [41], XGRIDS PortalCam จับภาพ [36], และ KIRI ผสม real splats กับ AI gen [59]
- TriSplat ส่งออก triangle meshes ที่พร้อมใช้ใน simulation จาก sparse images — ข้ามขั้นตอน Gaussian + mesh extraction ใช้งานได้ใน engine โดยตรง [56]
- Godot WebGPU รองรับ GPU-driven Nanite-style rendering [31]; เผยแพร่สูตร painterly Blender→Unity URP postFX shader [30]
- Claude Code ควบคุม Blender อัตโนมัติ 1 ชั่วโมง — ทำ procedural GeoNodes, retargeting [51]; บทเรียนเตือนใจเรื่องการไม่จ่ายค่าฟรีแลนซ์ [6]

## What happened
วันนี้มีสองกระแสหลักที่โดดเด่น กระแสแรกคือ AI-driven previz: thread ของ Bilawal Sidhu ที่แสดงการวาด camera paths บน map screenshots แล้วส่งให้ Google Omni/Flow สร้างฟุตเทจ drone-POV ระเบิดกระแส [2][14][43][54][60] และ Keety ก็ทำซ้ำได้ด้วย Seedance [14] กระแสที่สองคือ splatting/3D-reconstruction stack ที่พัฒนาต่อเนื่อง — Niantic Spatial จับมือ Spexi สำหรับงาน commissioned city-scale drone Gaussian captures [41], XGRIDS PortalCam splats ขึ้น PlayCanvas [36], KIRI demo การ compositing real splats กับ AI characters [59], และ TriSplat เปิดตัว feed-forward sparse-image → real triangle meshes ที่พร้อมสำหรับ physics [56] โดยมีผู้วิจารณ์รายหนึ่งชี้ถูกต้องว่า GS ยังต้องการ dense viewpoints [52]

ฝั่ง tooling นักพัฒนาคนหนึ่ง port Blender painterly shader ไป Unity URP ผ่าน fullscreen post passes [30], Godot WebGPU ได้ GPU-driven Nanite-style rendering [31], มีการ document Guilty Gear-style toon pipeline (model/shade/lineart/rig) สำหรับ Blender [27], และ Claude Code ควบคุม Blender อัตโนมัตินาน 1 ชั่วโมงจนได้ GeoNodes systems และ retargeting [51] งาน Blender community ยังแข็งแกร่ง — vintage cartoon shaders [1], Kung Fu Panda Rigify rig [4], glass render-settings comparison [11] — พร้อมคำเตือนเรื่องฟรีแลนซ์ไม่ได้รับเงิน $2,800 [6]

## Why it matters (reasoning)
Sketch-to-video previz [2][14][43][54] ลดต้นทุน storyboard/animatic สำหรับ marketing reels และ XR concept pitches — studio สามารถ prototype flythrough ประสบการณ์ VR ได้ก่อนเริ่ม model ใดๆ สาเหตุ: video diffusion models รับ structured camera priors ได้แล้ว ไม่ใช่แค่ text ผลลัพธ์ระดับที่สอง: ลูกค้าจะคาดหวัง cinematic previs ภายในไม่กี่วัน ไม่ใช่สัปดาห์; DOP/animator in-house เสียอำนาจต่อรองในขั้นตอน bid

Gaussian Splatting ที่เคลื่อนจาก research ไปสู่ commissioned drone capture [41] และ consumer hardware [36] หมายความว่า location-based XR (มรดกทางวัฒนธรรม, การท่องเที่ยว, real estate walkthroughs) กลายเป็นบริการที่จัดซื้อได้แล้ว ไม่ใช่ R&D project อีกต่อไป TriSplat [56] คือ technical signal ที่สำคัญกว่า — หาก feed-forward triangle meshes จาก sparse images เชื่อถือได้จริง pipeline photogrammetry ทั้งหมด (COLMAP→mesh cleanup→retopo) จะย่อเหลือแค่ไม่กี่นาที ป้อน Unity/Unreal ได้โดยตรง Painterly URP postFX [30] และ Godot Nanite [31] แสดงให้เห็นว่าช่องว่างของ indie engine เทียบ Unreal กำลังแคบลงสำหรับ stylized + high-density rendering ซึ่งเกี่ยวข้องกับ Unity stack ของ studio

## Possibility
น่าจะเกิด (70%): ภายใน 12 เดือน sketch-camera-path previz กลายเป็นขั้นตอนมาตรฐานใน agency pitch decks; Google Flow / Runway / Seedance แข่งกันด้าน camera-control fidelity น่าจะเกิด (60%): TriSplat-class feed-forward mesh reconstruction เข้าสู่ Unity/Unreal plugin ภายในสิ้นปี 2026 ตัดราคา RealityCapture/Polycam สำหรับการสแกน prop เป็นไปได้ (40%): commissioned city-scale splats กลายเป็น B2B SKU ที่มาพร้อม location-based VR/AR experiences — Niantic+Spexi [41] คือต้นแบบ โอกาสน้อย (25%): Claude-Code-drives-Blender [51] ถึงระดับ production ที่เชื่อถือได้ในปีนี้ — geometry nodes ผ่าน LLM ยังอยู่แค่ demo ความเสี่ยง: GS hype เกินกว่าความเป็นจริงของการ capture [52] และลูกค้าสับสนระหว่าง 'AI video' กับ '3D scene จริง'

## Org applicability — NDF DEV
คุ้มค่าสูง ต้นทุนต่ำ: นำ sketch-to-video previz [2][14] มาใช้ทันทีสำหรับ client pitches โปรเจกต์ VR/XR และ Unity game cinematic mockups — ต้นทุน <$50/pitch เทียบกับงาน blockout หลายวัน คุ้มทำ ปานกลาง: ทดลอง Gaussian Splatting สำหรับ heritage/temple XR demo สักแห่งในเชียงใหม่ โดยใช้ hardware ระดับ PortalCam หรือ KIRI [36][59] — สอดคล้องกับ edutech (e-learning มรดกวัฒนธรรม) และ tourism pitches คุ้มค่า R&D spike 1 สัปดาห์ ปานกลาง: port painterly URP shader recipe [30] เข้า Unity stylized-game pipeline — ประหยัดแรงงานด้านศิลปะสำหรับงาน hand-painted looks ลำดับต่ำ: TriSplat [56], Godot Nanite [31], Claude→Blender [51] — ติดตามไว้ก่อน ยังไม่ต้องสร้างพื้นฐานบนสิ่งเหล่านี้ เชิงปฏิบัติการ: ทบทวนบทเรียนเรื่องฟรีแลนซ์ไม่ได้รับเงิน [6] — บังคับใช้ milestone invoicing และ signed SOW กับ 3D contractor ภายนอกทุกราย

## Signals to Watch
- TriSplat code/weights release และ Unity/Unreal importer plugins
- ราคา Google Flow / Seedance tier เชิงพาณิชย์สำหรับ sketch-path previz
- XGRIDS PortalCam หรือ hardware capture splat เทียบเท่าราคา <$3k ที่หาได้ในไทย
- Blender-MCP / Claude-Code-Blender ที่พัฒนาจนเป็น agent workflow ที่ใช้งานได้จริง [51]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | rahulparihar | ^4922 c53 | [Vintage cartoon shaders in Blender](https://www.reddit.com/r/blender/comments/1tpd4c0/vintage_cartoon_shaders_in_blender/) |
| x | bilawalsidhu | ^3066 c133 | [Gave google omni a sketched camera path and asked it to generate drone POV foota](https://x.com/bilawalsidhu/status/2059419767417487718) |
| reddit | flockaroo | ^854 c27 | [home grown gas giant](https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/) |
| x | 3DxDEV7 | ^721 c4 | [DreamWorks animator Nicolas Prothais showcased a stunning Kung Fu Panda rig in B](https://x.com/3DxDEV7/status/2059497395352748099) |
| reddit | x_otosaka_x | ^537 c20 | [I made a moroccan-themed slot machine inspired by moorish architecture and desig](https://www.reddit.com/r/blender/comments/1tpd00r/i_made_a_moroccanthemed_slot_machine/) |
| reddit | Vegetable-Site-3715 | ^524 c81 | [Client agreed to pay hourly on a recorded call, then denied the whole agreement ](https://www.reddit.com/r/blender/comments/1toxcb6/client_agreed_to_pay_hourly_on_a_recorded_call/) |
| reddit | Wellie_man | ^521 c18 | [First attempts at making a walk cycle! How'd I do?](https://www.reddit.com/r/blender/comments/1tp6fah/first_attempts_at_making_a_walk_cycle_howd_i_do/) |
| x | BrainezVisuals | ^499 c59 | [I just turned 18. Here's my VFX/CG work. #b3d #blender https://t.co/g6RRZSsTZm](https://x.com/BrainezVisuals/status/2059681346449031677) |
| reddit | Legal-Collection2425 | ^317 c31 | [i present the ice cube on plate do you like it](https://www.reddit.com/r/blender/comments/1tp89ev/i_present_the_ice_cube_on_plate/) |
| reddit | LoquatPutrid2894 | ^313 c18 | [Made Saber Artoria Pendragon, used only blender , how is it ?](https://www.reddit.com/r/blender/comments/1toxkbq/made_saber_artoria_pendragon_used_only_blender/) |
| x | HidemyCG | ^313 c0 | [The most optimal renderer settings for a close-up scene with glass and the glass](https://x.com/HidemyCG/status/2059658635236528157) |
| reddit | OzGang | ^275 c9 | [NYC Subway Full CGI (Blender + DaVinci Resolve)](https://www.reddit.com/r/blender/comments/1tpmpvd/nyc_subway_full_cgi_blender_davinci_resolve/) |
| x | austin_rief | ^216 c41 | [I'm hiring a founding engineer for my new company. You'll be a good fit if you: ](https://x.com/austin_rief/status/2059704887118586039) |
| x | bilawalsidhu | ^211 c4 | [Camera path scribbles are turning into an AI video trend. Cool seedance example ](https://x.com/bilawalsidhu/status/2059751008746471791) |
| x | A_fan_of_Sonic | ^199 c2 | [Ripped, fixed, and shaded Goku from Sparking! Zero for Blender! 🐉✨ Free download](https://x.com/A_fan_of_Sonic/status/2059644148907417663) |
| reddit | creationstation99 | ^188 c15 | [Made this low poly character in blender](https://www.reddit.com/r/blender/comments/1tp0hu6/made_this_low_poly_character_in_blender/) |
| reddit | Sufficient-Limit-392 | ^185 c10 | [The stuff I animated](https://www.reddit.com/r/blender/comments/1tpi497/the_stuff_i_animated/) |
| reddit | Working-Winner52 | ^182 c23 | [Please rate my art and also suggest what I should improve](https://www.reddit.com/r/blender/comments/1tpoqad/please_rate_my_art_and_also_suggest_what_i_should/) |
| x | sevenout | ^160 c0 | [@MarkDuplass They're saying the same thing about Curry Barker, that some mystery](https://x.com/sevenout/status/2059398926797537667) |
| reddit | Unhappy_Document_796 | ^155 c5 | [Yet another test anim](https://www.reddit.com/r/blender/comments/1tpfazt/yet_another_test_anim/) |
| x | vikare06 | ^151 c12 | [There is no discernible design in that image. Just asking GPT to generate a monu](https://x.com/vikare06/status/2059580032826101762) |
| reddit | AlarmedBag9653 | ^142 c17 | [Procedural Creature gen and animation Procedural creature generation and animati](https://www.reddit.com/r/proceduralgeneration/comments/1to7rei/procedural_creature_gen_and_animation/) |
| reddit | Content_Economist132 | ^141 c36 | [Why do graphics apis need so many layers of abstractions like buffer, descriptor](https://www.reddit.com/r/GraphicsProgramming/comments/1tow7ic/why_do_graphics_apis_need_so_many_layers_of/) |
| reddit | Affectionate_Fly_457 | ^112 c8 | [Made something new using particles](https://www.reddit.com/r/blender/comments/1tp0qt2/made_something_new_using_particles/) |
| reddit | huleeb | ^109 c5 | [the forgotten pipeline](https://www.reddit.com/r/blender/comments/1tp5ehx/the_forgotten_pipeline/) |
| reddit | islammhran_86 | ^94 c6 | [Warm Luxury Interior in Blender I have also completed a **daylight version** of ](https://www.reddit.com/r/blender/comments/1tpc074/warm_luxury_interior_in_blender/) |
| x | Noggi_3D | ^86 c1 | [I finished setting up a page explaining the techniques Guilty Gear uses to creat](https://x.com/Noggi_3D/status/2059683849521508509) |
| reddit | ExistingMark2998 | ^81 c20 | [first blender ANIMATION!!! rate my work :)) also any idea what should i start ne](https://www.reddit.com/r/blender/comments/1tp3t7w/first_blender_animation/) |
| reddit | Significant-Tree4752 | ^77 c3 | [Maria Calavera: Life and Death scythe (WIP) Maria's weapon did it while practici](https://www.reddit.com/r/blender/comments/1tp2tqk/maria_calavera_life_and_death_scythe_wip/) |
| x | jettelly | ^77 c0 | [Developer tantaneity shared how they recreated a painterly shader from Blender i](https://x.com/jettelly/status/2059243161311187193) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@rahulparihar</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 4922 · 💬 53</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tpd4c0/vintage_cartoon_shaders_in_blender/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/eXg3OTk3Mjh4cDNoMd9Qn7y5N5D268ReIaIXhfcTYlZHHdFBk-z0Qh3Se9gx.png?format=pjpg&amp;auto=webp&amp;s=509255971f64b4b19eaf38102568c3a85d2aff15" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Vintage cartoon shaders in Blender”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ศิลปินแชร์ shader สไตล์การ์ตูนวินเทจใน Blender แสดงการ render แบบ non-photorealistic ที่มีสไตล์โดดเด่น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Engagement สูง (4922 likes) ยืนยันว่า NPR aesthetic แบบ stylized เป็นที่ต้องการมาก — ตรงกับสไตล์ที่ทำให้ indie game และ e-learning โดดเด่นจาก 3D ทั่วไป</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team แปลง shader logic นี้เป็น URP custom shader หรือ Shader Graph ได้ — ให้ game และ XR project มีลุค vintage cartoon โดดเด่นโดยไม่ต้องใช้ต้นทุน art production สูง</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tpd4c0/vintage_cartoon_shaders_in_blender/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3066 · 💬 133</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2059419767417487718">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gave google omni a sketched camera path and asked it to generate drone POV footage. https://t.co/cQZFMtOkEi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Google Omni รับ camera path ที่วาดด้วยมือแล้ว generate วิดีโอมุม drone POV ออกมาได้เลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Sketch-to-video ที่ control camera path ได้ตัดขั้นตอน pre-viz และ location scouting ออกด้วย AI prompt เดียว — ประหยัดเวลาชัดเจนสำหรับทีมเล็ก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ใช้สำหรับทำ cinematic pre-viz และ XR environment fly-through ก่อน build 3D scene จริงได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2059419767417487718" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@flockaroo</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 854 · 💬 27</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/c3g3bHdsdm15aTNoMVQtrb6zyT3nVgsSB9Yrq2NdNhskp9hccODKkoNMp-gx.png?format=pjpg&amp;auto=webp&amp;s=39d0536eb07e798dacd50cf924457269fb83feff" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“home grown gas giant”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Gas giant ที่สร้างด้วย procedural generation น่าจะใช้ custom shader หรือ noise algorithm โพสต์ใน r/proceduralgeneration</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>854 upvotes บอกว่า community หิว procedural space visuals มาก — technique นี้ใช้ใน Unity real-time 3D ได้ตรงๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ศึกษา noise layering กับ shader approach นี้ แล้วทำ procedural skybox หรือ environment asset ที่ reuse ได้ในโปรเจกต์ XR/VR</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 721 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2059497395352748099">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“DreamWorks animator Nicolas Prothais showcased a stunning Kung Fu Panda rig in Blender using Rigify, seriously impressive 🔥🐼 #B3D #Blender3D #Blender #Animation #Rigify #CharacterRigging #3DArt #VFX h”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Animator จาก DreamWorks ชื่อ Nicolas Prothais โชว์ character rig ของ Kung Fu Panda ที่ทำใน Blender ด้วย Rigify addon คุณภาพสูงมาก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Rigify ใน Blender ทำ character rig ระดับ production ได้เทียบเท่า studio pipeline จริง พิสูจน์ว่า free tools ตามทันความต้องการระดับมืออาชีพแล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ศึกษา Rigify workflow นี้เป็น pipeline ต้นทุนต่ำก่อน import เข้า Unity ลดการพึ่ง tool แพงสำหรับ character animation ใน game หรือ XR project ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2059497395352748099" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@x_otosaka_x</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 537 · 💬 20</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tpd00r/i_made_a_moroccanthemed_slot_machine/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/Mm05emZwNGJ3cDNoMZJUmXUucVO8qDsVPdtz19OfQWpAFS9IwdVRzavJoUoJ.png?format=pjpg&amp;auto=webp&amp;s=8bec2a4c4cb152ec786ece2a8ca24e3966e1f14c" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I made a moroccan-themed slot machine inspired by moorish architecture and design”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>คนทำ slot machine 3D ธีมโมร็อกโกใน Blender โดย inspired จาก Moorish architecture และลวดลายประดับ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>สะท้อนว่า architecture จากวัฒนธรรมเฉพาะช่วยสร้าง visual identity ที่แข็งแกร่งให้ 3D asset ได้ — Moorish style ทำให้ชิ้นงานโดดเด่นจนได้ engagement สูง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ใช้แนวทางนี้ได้ — เลือก cultural style เป็น anchor ของ art direction ตั้งแต่ต้น เวลาสร้าง environment หรือ prop สำหรับ XR หรือ game</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tpd00r/i_made_a_moroccanthemed_slot_machine/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Wellie_man</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 521 · 💬 18</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tp6fah/first_attempts_at_making_a_walk_cycle_howd_i_do/" target="_blank" rel="noopener"><img src="https://i.redd.it/x1zm4ycwro3h1.gif" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“First attempts at making a walk cycle! How'd I do?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>User คนนึงใน Blender community โพสต์ walk cycle แรกของตัวเองเพื่อขอ feedback.</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Walk cycle คือพื้นฐาน animation — การขอ feedback สาธารณะแบบนี้แสดงให้เห็นว่า community critique ช่วยให้เรียนรู้ได้เร็วแค่ไหน.</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ใช้ workflow walk cycle จาก Blender เป็น pipeline ตรงสำหรับ character animation ในโปรเจกต์เกมได้เลย — ฝึกใน Blender แล้ว export เข้า Unity ต้นทุนต่ำ.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tp6fah/first_attempts_at_making_a_walk_cycle_howd_i_do/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@BrainezVisuals</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 499 · 💬 59</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/BrainezVisuals/status/2059681346449031677">View @BrainezVisuals on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I just turned 18. Here's my VFX/CG work. #b3d #blender https://t.co/g6RRZSsTZm”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Creator อายุ 18 โชว์ผลงาน VFX และ CG ที่ทำด้วย Blender</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แสดงว่า VFX คุณภาพสูงทำได้คนเดียวด้วย Blender ฟรี ไม่ต้องพึ่ง studio pipeline</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team สามารถ scout ศิลปิน Blender รุ่นใหม่สำหรับงาน VFX และ environment ได้เลย pipeline Blender-to-Unity นิ่งแล้ว ประหยัดกว่าจ้าง senior</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/BrainezVisuals/status/2059681346449031677" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Legal-Collection2425</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 317 · 💬 31</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tp89ev/i_present_the_ice_cube_on_plate/" target="_blank" rel="noopener"><img src="https://i.redd.it/sbudef2e3p3h1.png" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“i present the ice cube on plate do you like it”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist ใน Blender สร้าง render รูปน้ำแข็งบนจาน แล้วโพสต์ถามความเห็นคนในชุมชน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Material น้ำแข็งและกระจกเป็น benchmark ของ PBR shader และ subsurface scattering — 317 likes บอกว่า render นี้คุณภาพดีพอใช้เป็น reference ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู lighting และ material setup จาก scene นี้เป็น reference สำหรับ real-time ice/glass shader ใน XR หรือ game</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tp89ev/i_present_the_ice_cube_on_plate/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
</div>
