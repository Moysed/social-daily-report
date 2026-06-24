---
type: social-topic-report
date: '2026-06-24'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-24T15:12:00+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
regions:
- global
post_count: 9
salience: 0.28
sentiment: mixed
confidence: 0.6
tags:
- game-dev
- ai-in-pipelines
- godot
- industry-layoffs
- pricing
- valve
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-24

## TL;DR
- Rockstar ตั้งราคา GTA 6 ที่ $80 พร้อมเปิด pre-order วันพฤหัสฯ — ปิดฝาดีเบต $100 AAA ไว้ต่ำกว่าสามหลัก [1]
- Valve ประกาศราคา Steam Machine เริ่มต้น $1,049 (512GB) และออกคู่มือให้ build เองโดยไม่ต้องมี reservation [5][6]
- Godot maintainers ระบุยอมรับ 'some AI assistance' แต่ auto-reject PR ที่เป็น 'slop' / 'vibe coded' [9]
- Layoff ยังต่อเนื่อง: EA ตัดพนักงานใน Hyderabad และ US (recruitment, support, trust & safety, IT); Ubisoft ปิด 93 ตำแหน่งใน San Francisco ตาม WARN notice [7][8]
- Tencent กำลังพิจารณาถอนตัวจากหลาย Japanese studios เพื่อหันไปโฟกัส UGC [4]

## What happened
ข่าวธุรกิจและอุตสาหกรรมครองพื้นที่หลัก Rockstar ตั้งราคา GTA 6 ที่ $80 โดยเปิด pre-order วันพฤหัสฯ [1] Valve เปิดรายละเอียดราคา Steam Machine เริ่มต้น $1,049 รุ่น 512GB พร้อมทำให้การ build เองทำได้ง่ายขึ้นสำหรับผู้ที่ไม่มี reservation [5][6] ด้าน labor market EA ปลดพนักงานทั้งใน Hyderabad และทีม US (recruitment, customer support, trust & safety, IT) [7] ส่วน Ubisoft ตัด 93 ตำแหน่งใน San Francisco ตาม California WARN notice [8] Tencent รายงานว่าพิจารณาถอนตัวจากหลาย Japanese studios หลังช่วงลงทุนหนัก โดยหันทิศทางมาสู่ UGC [4] Atari และ MobyGames เปิดตัว Moby Professional แพลตฟอร์ม career ในวงการเกม [2]

## Why it matters (reasoning)
ประเด็นที่มีนัยสำคัญต่อการทำงานโดยตรงมีสองข้อ คือ Godot AI policy [9] และราคา GTA 6 [1] การที่ Godot ขีดเส้นชัดเจน — AI assistance ยอมรับได้ แต่ AI PR ที่ไม่ผ่านการกลั่นกรองถูก reject — เป็น reference ที่นำไปใช้ได้ทันทีสำหรับทีมที่กำลังวาง contributor/internal standards สำหรับ AI-generated code [9] การที่ GTA 6 ยึด AAA ไว้ที่ $80 แทน $100 สร้าง ceiling ความคาดหวังด้าน premium pricing ที่ studio เล็กอยู่ต่ำกว่า ไม่ใช่ model ที่ NDF DEV แข่งโดยตรง [1] Layoff ของ EA, Ubisoft และแนวโน้มถอนตัวของ Tencent จาก Japan สะท้อนการหดตัวและการตัดสินใจเลือก portfolio ของ large publishers ต่อเนื่อง [4][7][8] ผลรองคือ talent ที่ว่างมากขึ้นสำหรับงาน contract และ co-dev แต่ client budget ก็มีแนวโน้มตึงขึ้นเช่นกัน Steam Machine ราคา $1,049+ บ่งว่า Valve เจาะกลุ่ม living-room PC tier โดยเฉพาะ — มีความเกี่ยวข้องเฉพาะเมื่อ title ขึ้น Steam/SteamOS [5][6]

## Possibility
Likely: layoff และการตัด portfolio ของ large publishers ยังดำเนินต่อในระยะใกล้ เมื่อ EA, Ubisoft และ Tencent เดินทิศเดียวกัน [4][7][8] Plausible: engine และ OSS projects รายอื่นจะออก explicit AI-contribution policy ตามแนว Godot [9] Plausible: $80 กลายเป็น de facto AAA ceiling หาก GTA 6 pre-order ยืนราคาได้ [1] Unlikely (ไม่มีหลักฐานรองรับ): ราคา Steam Machine เปลี่ยน decision ว่า studio ใน Chiang Mai จะ ship ที่ไหน เมื่อ entry point อยู่ที่ $1,049 [6]

## Org applicability — NDF DEV
ออก written internal AI-code policy ตามแนว Godot — AI assist ได้ แต่ output ต่ำกว่ามาตรฐาน reject, human review บังคับ — ครอบ Unity/web repos (low effort) [9] ติดตาม contract-talent pool: การตัดพนักงานของ EA/Ubisoft/Tencent อาจปลดปล่อย experienced devs สำหรับงาน co-dev หรือ contract (low effort, monitor only) [4][7][8] หาก title ใดมีแผน Steam/SteamOS ให้จดราคา Steam Machine tier $1,049 ไว้ใช้ตอน set min-spec แต่ยังไม่ต้องดำเนินการใดๆ (low effort) [5][6] ข้ามได้: ราคา GTA 6 [1], Moby Professional [2], บทสัมภาษณ์ Alien Isolation 2 [3] — informational เท่านั้น ไม่มี action สำหรับ NDF DEV

## Signals to Watch
- engine อื่นๆ (Unity, Unreal) จะออก explicit AI-contribution rules ตาม Godot หรือไม่ [9]
- อัตราการ layoff ของ publisher ต่างๆ ในฐานะ indicator ของ talent availability [7][8]
- การตัดสินใจขั้นสุดท้ายของ Tencent เรื่อง Japanese studios และการ pivot สู่ UGC [4]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| rss | Nicole Carpenter | ^0 c0 | [Grand Theft Auto 6's $80 price settles the $100 question Pre-orders for the game](https://www.gamedeveloper.com/console/grand-theft-auto-6-s-80-price-settles-the-100-question) |
| rss | Bryant Francis | ^0 c0 | [Atari and MobyGames launch new career development platform called Moby Professio](https://www.gamedeveloper.com/business/atari-and-mobygames-launch-new-career-development-platform-called-moby-professional) |
| rss | Alessandro Fillari | ^0 c0 | [How a 12 year wait made Alien Isolation 2 a better sequel We sat down with creat](https://www.gamedeveloper.com/design/how-a-12-year-wait-made-alien-isolation-2-a-better-sequel) |
| rss | Chris Kerr | ^0 c0 | [Report: Tencent mulling exits from multiple Japanese studios The company went on](https://www.gamedeveloper.com/business/report-tencent-mulling-exits-from-multiple-japanese-studios) |
| rss | Chris Kerr | ^0 c0 | [Valve is making it easier to build your own Steam Machine No reservation? No pro](https://www.gamedeveloper.com/business/valve-is-making-it-easier-to-build-your-own-steam-machine) |
| rss | Bryant Francis | ^0 c0 | [Steam Machine pricing starts at $1,049 for 512GB model The Steam Machine price t](https://www.gamedeveloper.com/pc/steam-machine-pricing-starts-at-1-049-for-512gb-model) |
| rss | Danielle Riendeau | ^0 c0 | [Report: EA conducts layoffs in Hyderabad, India and the US The latest round of l](https://www.gamedeveloper.com/business/report-ea-conducts-layoffs-in-hyderabad-india-and-the-us) |
| rss | Danielle Riendeau | ^0 c0 | [Ubisoft eliminates 93 roles in San Francisco A California WARN notice shows 93 r](https://www.gamedeveloper.com/business/ubisoft-eliminates-93-roles-in-san-francisco) |
| rss | Chris Kerr | ^0 c0 | [Godot confirms it tolerates 'some AI assistance' but rejects 'vibe coded' tag 'A](https://www.gamedeveloper.com/business/godot-confirms-it-tolerates-some-ai-assistance-but-rejects-vibe-coded-accusations) |