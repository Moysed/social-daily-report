---
type: social-topic-report
date: '2026-05-27'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-05-27T16:45:46+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- reddit
- x
regions:
- global
post_count: 58
salience: 0.72
sentiment: positive
confidence: 0.78
tags:
- gaussian-splatting
- blender
- unity
- procedural
- ai-3d
- photogrammetry
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2059419707556438016/img/0fBSltBoNiBhjxOZ.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-05-27

## TL;DR
- Gaussian Splatting พัฒนาเร็วมาก: Niantic+Spexi บินโดรนระดับเมือง [51], ทดสอบ dynamic GS พร้อม production [33], native D3D12 splat renderer [41], และ pipeline 4D GS จากวิดีโอธรรมดา [27]
- TriSplat สร้าง triangle mesh พร้อมใช้งานในซิมูเลเตอร์จากภาพ sparse unposed — ข้ามขั้นตอน GS-to-mesh ใช้ใน Unity/Unreal physics ได้ทันที [53]
- NVIDIA PiD ทำ super-resolution 4x ใน latent space สำหรับ FLUX/Z-Image, upscale pixel ไวสำหรับ texture และ concept ที่สร้างโดย AI [9]
- วาด camera path → วิดีโอมุมโดรนผ่าน Google Omni/Flow [1][44][57] แสดงให้เห็นว่า AI virtual cinematography ถึงระดับใช้งาน previs ได้จริงแล้ว
- ecosystem ของ Blender ยังมี signal volume มากที่สุด: rig ตัวละครด้วย Rigify [5], NPR stylized ใน Eevee [4], procedural ด้วย Geo Nodes, add-on VHS [43], port painterly shader ของ URP [31]

## What happened
มีสองกระแสชัดในฟีด 3D วันนี้ กระแสแรก Gaussian Splatting เดินหน้าจากของเล่นวิจัยสู่ production: Niantic Spatial จับมือ Spexi รับจ้างบินโดรนสร้าง splat ระดับเมือง [51]; pipeline GS สำหรับ dynamic scene ที่ผ่านการทดสอบได้รับการประกาศว่าพร้อม production [33]; ไลบรารี native D3D12 GS rendering แบบ open-source ปรากฏขึ้นสำหรับฝังในแอป Windows [41]; และมีนักพัฒนาเดโม 4D GS reconstruction จากวิดีโอทั่วไป [27] — แม้มีเสียงน่าเชื่อถือค้านว่าการ capture ฉากทั้งหมดจากวิดีโอเดียวคือข้อมูลที่บิดเบือน และยังต้องการ array อยู่ดี [48] ควบคู่กัน TriSplat เสนอ feed-forward จากภาพ sparse → triangle mesh ข้ามขั้นตอน GS และ mesh extraction ทั้งหมด [53]

กระแสที่สอง tooling สร้างคอนเทนต์ด้วย AI: Bilawal Sidhu วาด camera path บน screenshot ของ Google Maps แล้ว Google Omni/Flow สร้างวิดีโอมุมโดรนที่สอดคล้องกัน [1][44][57]; NVIDIA ปล่อย PiD, super-resolution 4x ใน latent space สำหรับ FLUX.1/2 และ Z-Image [9]; Luma ผลัก 'Agents' สำหรับกราฟิก marketplace/LinkedIn/newsletter [47][50][52] Blender ยังเป็นปริมาณหลักของชุมชน — rig Kung Fu Panda ด้วย Rigify [5], ปลา watercolor ใน Eevee ผ่าน Geo Nodes [4], port painterly shader Blender→Unity URP [31], และ add-on VHS [43] งาน procedural ครอบคลุม gas giant [3], เซลล์ที่มี genome [14], และ creature gen ใน Godot [20] dev เดี่ยวส่งเกมบน custom engine [17], และคำเตือนจาก freelancer [7] ชี้ความเสี่ยงจากลูกค้าในงาน 3D contracting จริง

## Why it matters (reasoning)
สำหรับ studio ที่ทำ Unity + XR สัญญาณที่สำคัญที่สุดคือคลื่น GS + feed-forward mesh splat ที่ capture ระดับเมือง [51] ประกอบกับ runtime renderer แบบ native [41] ทำให้คอนเทนต์ XR แบบ photoreal สำหรับสถานที่จริง (พิพิธภัณฑ์, มรดกวัฒนธรรม, อสังหาริมทรัพย์) เป็นไปได้โดยไม่ต้องสร้าง geometry ด้วยมือ — แต่จนกว่าแนวทางแบบ TriSplat [53] จะ mature, splat ยังยากต่อการจัดแสง, collision, และแก้ไขใน Unity การที่ TriSplat แก้จุดเชื่อมที่หายไปโดยตรง: ถ้าภาพถ่ายจากโทรศัพท์แบบ sparse สามารถสร้าง mesh ที่พร้อมใช้ใน engine ได้, pipeline photogrammetry จะลดลงจากหลายวันเหลือแค่ไม่กี่นาที ความสงสัยใน [48] เป็น brake ที่มีประโยชน์ — คุณภาพการ capture ยังขึ้นกับ coverage ไม่ใช่เวทมนตร์ ผลรองคือ เมื่อ AI virtual cinematography [1] และ AI upscaler [9] ลดต้นทุน concept/previs ลง มูลค่าจะเลื่อนไปที่ integration, interactivity, และ on-device performance — ซึ่งเป็นจุดที่ Unity studio ยังได้เปรียบเหนือ AI shop ล้วน ข้อพิพาทของ freelancer [7] เตือนว่าเมื่อ tool ราคาถูกลง วินัยด้านสัญญาสำคัญกว่าเดิม ไม่ใช่น้อยลง

## Possibility
น่าจะเกิด (≈70%) ภายใน 6–12 เดือน: Gaussian Splatting กลายเป็น asset type ปกติใน pipeline ของ Unity/Unreal พร้อม editor tooling สำหรับแสง, occlusion, และ LOD; feed-forward mesh reconstruction แบบ TriSplat กลายเป็นตัวเลือกทดแทน photogrammetry ที่ใช้งานได้จริงสำหรับวัตถุขนาดเล็ก/กลาง เป็นไปได้ (≈40%): ไลบรารี splat ระดับเมือง (แบบ Niantic/Spexi) ถูก license สำหรับ location-based XR เปิดให้ workflow 'scan เมือง, deploy AR layer' ต่ำกว่า (≈20%): AI text/sketch-to-video (Omni/Flow) ใช้งานได้จริงสำหรับ cinematic ของเกมที่ ship — คุณภาพดีขึ้นแต่ temporal/identity consistency และปัญหา rights/licensing ยังเป็นอุปสรรค จับตาดู: Unity-official GS importer, และเกม AAA เกมแรกที่ ship environment แบบ splat-based

## Org applicability — NDF DEV
การเคลื่อนไหวระยะสั้นที่จับต้องได้สำหรับ NDF DEV: (1) Pilot Gaussian Splatting capture สำหรับฉาก XR/heritage หนึ่งฉาก — โทรศัพท์หรือโดรน render ผ่าน Unity GS plugins ที่มีอยู่; ต้นทุนต่ำ, differentiator สูงสำหรับ pitch ลูกค้า (2) ติดตาม TriSplat [53] และ feed-forward mesh tool ที่คล้ายกันสำหรับ prop/asset pipeline ของ studio — อาจแทน manual modeling สำหรับวัตถุจริงแบบ static ในคอนเทนต์ edutech (3) นำ upscaler แบบ PiD [9] เข้ามาใน pipeline concept/marketing สำหรับ keyart ที่สร้างด้วย FLUX และ screenshot storefront (4) ยืมไอเดีย painterly shader Blender→URP [31] สำหรับลุค stylized ต้นทุนต่ำบน Unity title — portfolio play ที่โดดเด่น (5) ข้ามไปก่อน: AI sketch-to-video [1] (ไม่ถึงระดับ production สำหรับ cinematic ของเกม), Luma carousel agents [47][50][52] (ประโยชน์ด้าน marketing เท่านั้น ไม่ใช่ core) คุ้มค่า: ข้อ 1, 3, 4 effort ต่ำ/signal สูง ข้อ 2 คือ watch-and-prototype ยังไม่ commit

## Signals to Watch
- ประกาศ Gaussian Splatting importer แบบ first-party ของ Unity/Unreal
- การปล่อย code/weights ของ TriSplat และคุณภาพบน small-object capture
- โมเดล pricing/licensing ของ Niantic Spatial × Spexi สำหรับ city splat
- การ integrate PiD เข้า ComfyUI/A1111 — สัญญาณการ adopt ในกลุ่ม mainstream

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^2303 c99 | [Gave google omni a sketched camera path and asked it to generate drone POV foota](https://x.com/bilawalsidhu/status/2059419767417487718) |
| reddit | BobThe-Bodybuilder | ^1000 c37 | [Blender is pretty cool. That's about it. I's just crazy that we get this piece o](https://www.reddit.com/r/blender/comments/1toiy1t/blender_is_pretty_cool/) |
| reddit | flockaroo | ^723 c22 | [home grown gas giant](https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/) |
| reddit | Kvendy_ | ^536 c13 | [Just a random fish on your feed!! Everything is rendered in Eevee, tried to make](https://www.reddit.com/r/blender/comments/1toesq0/just_a_random_fish_on_your_feed/) |
| x | 3DxDEV7 | ^461 c2 | [DreamWorks animator Nicolas Prothais showcased a stunning Kung Fu Panda rig in B](https://x.com/3DxDEV7/status/2059497395352748099) |
| reddit | hunter_2one | ^350 c53 | [Made this in blender, How can I still be jobless??? part 2 🤣, So last time, I po](https://www.reddit.com/r/blender/comments/1toporq/made_this_in_blender_how_can_i_still_be_jobless/) |
| reddit | Vegetable-Site-3715 | ^343 c51 | [Client agreed to pay hourly on a recorded call, then denied the whole agreement ](https://www.reddit.com/r/blender/comments/1toxcb6/client_agreed_to_pay_hourly_on_a_recorded_call/) |
| reddit | Educational-Wish7500 | ^324 c13 | [Rate My Work!!](https://www.reddit.com/r/blender/comments/1tomwh0/rate_my_work/) |
| x | multimodalart | ^288 c7 | [NVidia just released PiD: super resolution in pixel space directly from model la](https://x.com/multimodalart/status/2059003125768339649) |
| reddit | Wellie_man | ^286 c13 | [First attempts at making a walk cycle! How'd I do?](https://www.reddit.com/r/blender/comments/1tp6fah/first_attempts_at_making_a_walk_cycle_howd_i_do/) |
| x | delaigrodela | ^258 c6 | [My 12 year old son saw my material generating 4 simple shapes from UV and the co](https://x.com/delaigrodela/status/2058977219188297867) |
| reddit | LoquatPutrid2894 | ^250 c11 | [Made Saber Artoria Pendragon, used only blender , how is it ?](https://www.reddit.com/r/blender/comments/1toxkbq/made_saber_artoria_pendragon_used_only_blender/) |
| reddit | Firm-Dragonfruit-723 | ^247 c27 | [I made this Frutiger Aero video in Blender, what do you think?](https://www.reddit.com/r/blender/comments/1tohe4l/i_made_this_frutiger_aero_video_in_blender_what/) |
| reddit | MaxisGreat | ^177 c19 | [Thousands of procedurally generated cells Each cell has a genome that drives the](https://www.reddit.com/r/proceduralgeneration/comments/1tneul6/thousands_of_procedurally_generated_cells/) |
| reddit | GrimShadow1 | ^166 c7 | [Anime Lips Animation Practice [GP]](https://www.reddit.com/r/blender/comments/1tole1h/anime_lips_animation_practice_gp/) |
| x | bilawalsidhu | ^163 c2 | [This is pretty cool — basically "creative upscaling" for 3d scans https://t.co/S](https://x.com/bilawalsidhu/status/2059029365002744034) |
| reddit | SevenSidedVoxel | ^151 c21 | [Solo dev here, just released my own game, in my own engine I managed to do the i](https://www.reddit.com/r/gameenginedevs/comments/1tnoce5/solo_dev_here_just_released_my_own_game_in_my_own/) |
| reddit | creationstation99 | ^150 c13 | [Made this low poly character in blender](https://www.reddit.com/r/blender/comments/1tp0hu6/made_this_low_poly_character_in_blender/) |
| x | sevenout | ^145 c0 | [@MarkDuplass They're saying the same thing about Curry Barker, that some mystery](https://x.com/sevenout/status/2059398926797537667) |
| reddit | AlarmedBag9653 | ^129 c17 | [Procedural Creature gen and animation Procedural creature generation and animati](https://www.reddit.com/r/proceduralgeneration/comments/1to7rei/procedural_creature_gen_and_animation/) |
| x | ushadersbible | ^96 c0 | [Despite AI, technical artists and VFX artists continue to be some of the most in](https://x.com/ushadersbible/status/2059027261177704656) |
| reddit | Content_Economist132 | ^94 c30 | [Why do graphics apis need so many layers of abstractions like buffer, descriptor](https://www.reddit.com/r/GraphicsProgramming/comments/1tow7ic/why_do_graphics_apis_need_so_many_layers_of/) |
| reddit | IndiProphacy | ^87 c7 | [Test renders for my shortfilm thing :) Not 100% happy with everything yet, but i](https://www.reddit.com/r/blender/comments/1tocwqn/test_renders_for_my_shortfilm_thing/) |
| reddit | Legal-Collection2425 | ^87 c13 | [i present the ice cube on plate do you like it](https://www.reddit.com/r/blender/comments/1tp89ev/i_present_the_ice_cube_on_plate/) |
| x | vikare06 | ^86 c9 | [There is no discernible design in that image. Just asking GPT to generate a monu](https://x.com/vikare06/status/2059580032826101762) |
| reddit | Affectionate_Fly_457 | ^84 c8 | [Made something new using particles](https://www.reddit.com/r/blender/comments/1tp0qt2/made_something_new_using_particles/) |
| x | MarioNawfal | ^79 c18 | [A coder turned everyday video into an explorable 3D environment with AI-driven 4](https://x.com/MarioNawfal/status/2059103478790713398) |
| reddit | Legal-Collection2425 | ^75 c30 | [i present this do you like it?](https://www.reddit.com/r/blender/comments/1top27m/i_present_this/) |
| reddit | ExistingMark2998 | ^72 c17 | [first blender ANIMATION!!! rate my work :)) also any idea what should i start ne](https://www.reddit.com/r/blender/comments/1tp3t7w/first_blender_animation/) |
| reddit | Linirby | ^71 c10 | [Smol VoxelEngine made a smol voxel engine :3 Built HelloVoxel in C++23 using the](https://www.reddit.com/r/GraphicsProgramming/comments/1tnpefa/smol_voxelengine/) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2303 · 💬 99</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2059419767417487718">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gave google omni a sketched camera path and asked it to generate drone POV footage. https://t.co/cQZFMtOkEi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Google Omni รับ input เป็น camera path ที่วาดด้วยมือ แล้ว generate วิดีโอ drone POV ออกมาได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Sketch-to-video ที่ควบคุม camera trajectory ได้ตัด cost การถ่าย drone จริง — ตรงประเด็นสำหรับทีมเล็กที่ผลิต cinematic content</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team นำ sketch-based camera path มาใช้ pre-visualize flythrough หรือ XR walkthrough ก่อน commit assets จริงได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2059419767417487718" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@BobThe-Bodybuilder</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 1000 · 💬 37</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1toiy1t/blender_is_pretty_cool/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/Mjlzc2Q5MXVpajNoMXROZ9b9B3IrLXLUZ8ILg6Hd7As25347xmr95E20RVkv.png?format=pjpg&amp;auto=webp&amp;s=88f68fb575c3f091e9613065599744e5639ed9e6" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Blender is pretty cool. That's about it. I's just crazy that we get this piece of software for free. I want to make something cool with it like a short firebending (from the show Avatar: the last airb”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>User บน Reddit ชื่นชม Blender ว่าเป็น 3D software ฟรีที่ทรงพลัง และอยากทำ animation ไฟแบบ Avatar: The Last Airbender</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Blender ไม่มีค่าใช้จ่าย ทำให้ hobbyist ผลิต 3D asset คุณภาพสูงได้ ยก visual baseline ที่ studio เกมและ XR ต้องแข่งด้วย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity และ XR ใช้ Blender เป็น pipeline หลักฟรีสำหรับ modeling, rigging, และ VFX ได้เลย — fire effect แบบ particle-based แปลงเข้า Unity VFX Graph ได้ตรงๆ ไม่มีค่า license</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1toiy1t/blender_is_pretty_cool/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@flockaroo</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 723 · 💬 22</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/c3g3bHdsdm15aTNoMVQtrb6zyT3nVgsSB9Yrq2NdNhskp9hccODKkoNMp-gx.png?format=pjpg&amp;auto=webp&amp;s=39d0536eb07e798dacd50cf924457269fb83feff" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“home grown gas giant”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Gas giant ที่ generate ด้วย procedural algorithm สร้าง atmospheric band หมุนวนดูสมจริง โพสใน r/proceduralgeneration ได้รับความสนใจสูง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Render ดาวเคราะห์คุณภาพสูงได้โดยไม่ต้องใช้ artist วาด texture — ทีมเล็กสร้าง space environment ได้กว้างขวางโดยใช้ asset น้อย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ทดลอง procedural skybox หรือ space shader โดยใช้ noise layering แบบนี้ — ใช้ได้ตรงกับ XR หรือ game project ที่ต้องการ space background แบบ dynamic</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Kvendy_</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 536 · 💬 13</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1toesq0/just_a_random_fish_on_your_feed/" target="_blank" rel="noopener"><img src="https://preview.redd.it/4ezhkyr6si3h1.png?width=2160&amp;format=png&amp;auto=webp&amp;s=941ebf17c9d261c8b1150b7d1fa9d93ecc8dcd5e" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Just a random fish on your feed!! Everything is rendered in Eevee, tried to make it resample watercolor, hopefully I did a great job. The fish is animated and has a wobbly feel using Geo node, but red”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist ทำปลา animate ใน Blender ด้วย Eevee + Geometry Nodes ให้ look เหมือน watercolor และมีการขยับแบบ wobbly</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ได้ watercolor style จาก Eevee ล้วนๆ ไม่ต้อง bake Cycles พิสูจน์ว่า Eevee ใช้ทำ stylized / non-photorealistic art ได้จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team เอา approach Eevee watercolor + Geo Nodes นี้ไปแปลงเป็น Shader Graph ใน Unity ได้เลย เหมาะกับ asset สาย stylized XR หรือ e-learning</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1toesq0/just_a_random_fish_on_your_feed/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 461 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2059497395352748099">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“DreamWorks animator Nicolas Prothais showcased a stunning Kung Fu Panda rig in Blender using Rigify, seriously impressive 🔥🐼 #B3D #Blender3D #Blender #Animation #Rigify #CharacterRigging #3DArt #VFX h”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Animator จาก DreamWorks ชื่อ Nicolas Prothais โชว์ character rig ของ Kung Fu Panda ที่สร้างใน Blender โดยใช้ Rigify addon</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Rig ระดับ production ของ DreamWorks ที่สร้างด้วย tool ฟรีพิสูจน์ว่า Blender + Rigify ใช้งานจริงในงาน character animation ระดับมืออาชีพได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team เอา Blender + Rigify มาเป็น standard pipeline สำหรับ character rigging แล้ว export ผ่าน FBX/glTF เข้า Unity ได้เลย ลดค่า license และรวม workflow 3D ให้เป็นหนึ่ง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2059497395352748099" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@hunter_2one</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 350 · 💬 53</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1toporq/made_this_in_blender_how_can_i_still_be_jobless/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/ejV0cDdrbW1zazNoMXMC-fj9aGMyp2Y4QAHhio2vfLVLn51_iDTBLr3QOlqq.png?format=pjpg&amp;auto=webp&amp;s=1aae575a8a0df08ec576665598b2ddad9c77359a" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Made this in blender, How can I still be jobless??? part 2 🤣, So last time, I posted a render making a joke.i thought if I say how can I still be jobless, it will be funny and people should give me ad”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ศิลปิน Blender โพสต์ 3D render ใหม่บน Reddit (ภาค 2) แซวตัวเองว่าทำได้ขนาดนี้แต่ยังตกงาน หลังโพสต์แรกโดนด่าหนัก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>พอร์ตโฟลิโอ Blender เก่งอย่างเดียวไม่พอ — การ present งานและการรับ feedback จาก community ก็สำคัญไม่แพ้กัน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team จำไว้ — ตอนแชร์งาน 3D หรือ XR สาธารณะ ต้องระบุ context ให้ชัด เพราะ community reaction กระทบภาพลักษณ์การจ้างงานโดยตรง</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1toporq/made_this_in_blender_how_can_i_still_be_jobless/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Educational-Wish7500</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 324 · 💬 13</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tomwh0/rate_my_work/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/aWpyMWIyZm84azNoMUZlWw3WitR63OQN0bBOmEnczf7ciJir0mmS_SSdzH7u.png?format=pjpg&amp;auto=webp&amp;s=1be4b1f4742769a35f4df877c2c169e20d07de64" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Rate My Work!!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ศิลปิน Blender โพสต์ผลงาน 3D render บน r/blender ขอให้ community ช่วย rate และ critique</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>324 upvotes บอกว่างานโดนใจ community — r/blender เป็น feedback channel ฟรีที่ดีสำหรับ benchmark คุณภาพ 3D</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team โพสต์ WIP environment art หรือ character asset บน r/blender หรือ r/Unity3D รับ feedback ก่อน lock asset เข้า production</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tomwh0/rate_my_work/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@multimodalart</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 288 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/multimodalart/status/2059003125768339649">View @multimodalart on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“NVidia just released PiD: super resolution in pixel space directly from model latents 🔎 4X resolution for any generated image, FAST! 🏎️💨 FLUX.1, 2 and Z-Image (Qwen Image coming) of course, i built a ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Nvidia ปล่อย PiD ระบบ super resolution ที่ upscale รูป 4x จาก model latents โดยตรง รองรับ FLUX.1, FLUX.2, Z-Image มี demo สร้างรูป 4K แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Upscale 4x ตอน generate เลย ไม่ต้องผ่าน post-process แยก ทำให้ใช้ base model เล็กลงแต่ได้ output คุณภาพ print-ready ลด cost pipeline asset</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลอง pipe PiD เข้า workflow สร้าง texture/concept art ได้เลย ได้ 4K asset โดยไม่ต้องซื้อ GPU แรงขึ้น ทดสอบผ่าน Hugging Face demo ก่อนลงทุน infra</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/multimodalart/status/2059003125768339649" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
