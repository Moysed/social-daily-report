---
type: social-topic-report
date: '2026-05-23'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-05-23T06:47:06+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- reddit
- rss
- x
regions:
- global
post_count: 86
salience: 0.5
sentiment: neutral
confidence: 0.0
tags:
- gamedev
- engines
- tools
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-05-23

## TL;DR
- ขัดเกลา water rendering มาสักพักแล้ว และในที่สุดก็ได้มาถึงจุดนี้ คิดเห็นอย่างไรบ้าง? คิดว่าในที่สุดมันก็ st
- คนแรกที่รัน Godot ใน Minecraft? นี่คือ waylandcraft : [https://github.com/EVV1E/waylandcraft](https://github.com/EVV1
- shield effect ที่ปรับแต่งได้ นี่คือ effect จาก Battle FX ของฉัน: [https://binbun3d.itch.io/battle-fx](https://binbun3d

## What happened
Output ของ model ไม่ใช่ JSON ที่ถูกต้อง กลับไปใช้ stub แทน

{"tldr":["Godot ครองสัญญาณของวันนี้: water shaders [1], shield FX [3], vehicle camera plugin [10], การจำลอง zombie horde 5K ตัว [21] — engine กำลัง ship งานระดับ production","Unity discourse เอียงไปทาง tooling pain: ความมองเห็นใน asset-store [9], scene-diff tooling [37], ตัวจัดระเบียบ texture/material [31], painterly fog [26]","โพสต์จาก veteran เรื่อง metrics-driven design และการหลุดออกของผู้เล่น [8] ได้รับการตอบรับดี; รูปแบบ marketing-first-then-flop ถูกตั้งข้อสังเกต [20]","Workflow และ production craft (atmosphere ตลอด 4 ปี [13], ความพยายามใน cutscene [11], isometric retargeting [18]) มีน้ำหนักเหนือกว่าข่าว AI-in-pipeline ในวันนี้","ที่น่าสังเกต: แทบไม่มี content เกี่ยวกับ AI-in-pipeline เลยในชุดนี้ — ชุมชนโฟกัสไปที่ tech และ shaders ที่ทำด้วยมือ"],"what_happened":"Godot 4 ยังคงพัฒนาต่อเนื่องในฐานะ engine ระดับเชิงพาณิชย์ โดยนักพัฒนาแสดงผลงาน water rendering ที่ขัดเกลาแล้ว [1], shield/battle FX แบบ modular [3], vehicle camera plugin ที่ปรับแต่งสำหรับ arcade feel [10], และการจำลอง zombie horde 5,000 agent ที่ทำได้ 80+ FPS บน RTX 2080 โดยใช้ OpenVAT + fl

## Why it matters (reasoning)
ตั้งค่า ANTHROPIC_API_KEY เพื่อเปิดใช้งาน Opus reasoning

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | Faislx | ^732 c33 | [ขัดเกลา water rendering มาสักพักแล้ว และในที่สุดก็ได้มาถึงจุดนี้ ](https://www.reddit.com/r/godot/comments/1tkspzb/ive_been_polishing_this_water_rendering_for_a/) |
| reddit | Opposite-Fix6783 | ^534 c39 | [คนแรกที่รัน Godot ใน Minecraft? นี่คือ waylandcraft : [https://github.com/EVV](https://www.reddit.com/r/godot/comments/1tkq7qa/frist_to_run_godot_in_minecraft/) |
| reddit | binbun3 | ^359 c6 | [shield effect ที่ปรับแต่งได้ นี่คือ effect จาก Battle FX ของฉัน: [https://binb](https://www.reddit.com/r/godot/comments/1tkfayb/customizable_shield_effect/) |
| reddit | kevdev3d | ^313 c19 | [Solo dev นี่แหละ ทำ 3D weapon generator (ไม่ใช้ AI) แก้ไขรูปทรงและ textures ของอาวุธ](https://www.reddit.com/r/Unity3D/comments/1tkh1hj/solo_dev_here_made_a_3d_weapon_generator_no_ai/) |
| reddit | Bin_H | ^271 c29 | [เพิ่ม online character recognition ลงใน note-taking app แล้ว ดูได้ที่: [h](https://www.reddit.com/r/godot/comments/1tkhev9/i_added_online_character_recognition_to_my/) |
| reddit | 9joao6 | ^257 c8 | [ให้ผู้เล่นจัดเฟอร์นิเจอร์ในบ้านตัวเองตามใจชอบ กำลังทำ [S](https://www.reddit.com/r/godot/comments/1tksg35/letting_players_arrange_their_own_homes_furniture/) |
| reddit | ViremorfeStudios | ^216 c48 | [คุณใช้ tools อะไรทำเกม Godot และเพราะอะไร? ตอนนี้กำลังทำ 3D](https://www.reddit.com/r/godot/comments/1tkzdn6/what_tools_do_you_use_to_make_your_godot_game_and/) |
| reddit | Monkeh77 | ^203 c56 | [สิ่งที่เรียนรู้หลังเป็น dev มากกว่า 10 ปี 1.ฟังเกมของตัวเอง ](https://www.reddit.com/r/gamedev/comments/1tkl92n/some_things_ive_learned_after_being_a_dev_for_10/) |
| reddit | LastCallDevs | ^194 c49 | [อะไรที่ช่วยให้ Unity Asset Store asset มองเห็นได้จริงๆ? ทำตัวแรกแล้ว](https://www.reddit.com/r/Unity3D/comments/1tkociu/what_actually_helps_a_unity_asset_store_asset/) |
| reddit | No_Zookeepergame9004 | ^174 c17 | [สร้าง plugin "Pro Vehicle Camera" สำหรับ Godot 4 เน้น elastic physics และ a](https://www.reddit.com/r/godot/comments/1tkggp2/i_created_pro_vehicle_camera_plugin_for_godot_4/) |
| reddit | Dariks | ^170 c15 | [ใช้เวลา 14 ชั่วโมงต่อเนื่องทำ cutscene นี้สำหรับเกม Godot ของฉัน](https://www.reddit.com/r/godot/comments/1tklyn7/i_spent_14_hours_straight_making_this_cutscene/) |
| bluesky | majormcdoom.bsky.social | ^157 c12 | [ไม่เคยคิดคณิตศาสตร์ถูกในครั้งแรกอีกต่อไปแล้ว และไม่รู้ว่าควร ](https://bsky.app/profile/majormcdoom.bsky.social/post/3mmi4nwg52c24) |
| reddit | NoReasonForHysteria | ^141 c25 | [การทำให้ atmosphere ลงตัวใน unity-game ของเราใช้เวลา 4 ปี เต็มไปด้วยความเจ็บปวด ](https://www.reddit.com/r/Unity3D/comments/1tkg2md/getting_the_atmosphere_just_right_in_our/) |
| reddit | RiescArts | ^134 c10 | [กำลังทำ Stylized Mining node system โดยใช้ gradients อยู่ คิดเห็นอย่างไร ](https://www.reddit.com/r/Unity3D/comments/1tkjr03/ive_been_working_on_a_stylized_mining_node_system/) |
| reddit | deohvii | ^102 c20 | [ได้ยิน indie dev ชาวปาเลสไตน์อธิบายว่าแม้แต่ "choose your country" ก็ยังไม่](https://www.reddit.com/r/gamedev/comments/1tkw2m7/hearing_a_palestinian_indie_dev_explain_how_not/) |
| reddit | chem-farmer | ^100 c6 | [รู้มาตลอดว่าการบันทึกเสียงผายลมของตัวเองจะมีประโยชน์สักวัน](https://www.reddit.com/r/godot/comments/1tkcod1/i_always_knew_recording_my_farts_would_prove_to/) |
| reddit | Glass-Ad672 | ^97 c6 | [อะไรบางอย่าง มันตลกกว่านี้ในหัว](https://www.reddit.com/r/Unity3D/comments/1tl0t85/something_something_it_was_funnier_in_my_head/) |
| reddit | ImmaBun | ^90 c28 | [จะปรับ line ให้ดูแบนบน isometric board ได้อย่างไร? กำลังเปลี่ยน](https://www.reddit.com/r/godot/comments/1tkjd0l/how_do_i_tweak_the_line_to_make_it_look_flat_on/) |
| reddit | framedworld | ^86 c9 | [แน่ใจว่าเพิ่งทำ anim tree พัง... พยายามทำให้ crouching มีเงื่อนไข และ](https://www.reddit.com/r/godot/comments/1tl1xe5/pretty_sure_i_just_broke_my_anim_tree/) |
| reddit | wassup_son | ^74 c52 | [เคยติดตามการพัฒนาเกมแล้วดูมันล้มเหลวตอน launch ไหม? (YT shor](https://www.reddit.com/r/gamedev/comments/1tkfpxa/did_you_ever_follow_a_games_development_only_to/) |
| reddit | ywadi85 | ^64 c4 | [สร้าง zombie horde sim 5K+ / 80+FPS ใน Godot 4 บน RTX2080 ด้วย OpenVAT-animated z](https://www.reddit.com/r/godot/comments/1tkkr33/built_a_5k_80fps_zombie_horde_sim_in_godot_4_on_a/) |
| reddit | RDStoat | ^62 c0 | [UPDATE: ศัตรู 3D "ปลอม" ที่ทำจาก 2D sprites](https://www.reddit.com/r/Unity3D/comments/1tkpud0/update_fake_3d_enemies_made_with_2d_sprites/) |
| reddit | EliasWick | ^56 c15 | [ข้อความถึงทุกคนที่กำลังเรียนรู้และโพสต์ที่นี่เกี่ยวกับ Unreal Engine project ของคุณ](https://www.reddit.com/r/unrealengine/comments/1tkwag5/a_message_to_everyone_learning_and_posting_here/) |
| reddit | InfectedTribe | ^55 c6 | [เกม Tennis แบบ Pong ง่ายๆ หนึ่งในโปรเจกต์แรกๆ ที่ทิ้งไว้หลายปีแล้ว](https://www.reddit.com/r/godot/comments/1tkx0uy/simple_pong_like_tennis_game/) |
| reddit | SPOOKJUMP | ^47 c4 | [นี่คือภาพแรกๆ ของเกม PvP magic แบบ spell-drawing ของฉัน กำลังทำมาแล้ว ](https://www.reddit.com/r/Unity3D/comments/1tkw86o/heres_an_early_look_into_my_spelldrawing_pvp/) |
| reddit | Feld_Four | ^46 c5 | [Unity สร้าง fog แบบ stylized "painterly" ได้ไหม? มีคำถามมากมายเกี่ยวกับวิธี](https://www.reddit.com/r/Unity3D/comments/1tl44n2/is_stylized_painterly_fog_possible_in_unity/) |
| reddit | 8BitBeard | ^43 c5 | [ใช้งาน Cleaning Shift แล้ว!⚓ ตอนนี้มี state machine และ navigati ที่เสถียรแล้ว](https://www.reddit.com/r/godot/comments/1tkhz2j/cleaning_shift_implemented/) |
| reddit | iam_ibrahem | ^35 c130 | [Voice Acting ภาษาอาหรับล้วนสำหรับ Dungeon Crawler ที่ได้แรงบันดาลใจจากอาหรับ จะส่งผล](https://www.reddit.com/r/gamedev/comments/1tkuj8w/arabiconly_voice_acting_for_an_arabicinspired/) |
| reddit | Bramblefort | ^18 c2 | [รอดจากการเผชิญหน้าในหนองน้ำสไตล์ศตวรรษที่ 19](https://www.reddit.com/r/Unity3D/comments/1tkriug/surviving_a_19thcentury_marsh_encounter/) |
| bluesky | morbidember.bsky.social | ^15 c1 | [งาน visdev หยาบและเป็นบล็อกมาก ส่วนใหญ่สำรวจ themes และกำหนด colo](https://bsky.app/profile/morbidember.bsky.social/post/3mmhrofm7sc2m) |