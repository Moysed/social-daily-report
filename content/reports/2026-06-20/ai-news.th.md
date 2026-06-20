---
type: social-topic-report
date: '2026-06-20'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-06-20T03:10:14+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 234
salience: 0.45
sentiment: mixed
confidence: 0.5
tags:
- ai-news
- claude-code
- devtools
- agents
- anthropic
- talent-moves
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2068048584067432448/img/8t3rTJcvfET74VJA.jpg
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-06-20

## TL;DR
- บุคลากรระดับสูงกำลังย้ายค่าย: John Jumper เจ้าของรางวัล Nobel (AlphaFold) กำลังออกจาก Google DeepMind มาร่วม Anthropic [2][6][17] สัปดาห์เดียวกับที่ Noam Shazeer (transformer/MoE) ย้ายไป OpenAI [3][17]; การ recruit ล่าสุดของ Anthropic ยังรวมถึง Mike Krieger, Peter Bailis และ Bryan McCann [47]
- artifact ที่ใช้งานได้จริงวันนี้มีน้อย — ที่โดดเด่นคือ Claude Code 'loops' (ผู้สร้างบอกว่า 30% ของโค้ดตัวเองเขียนด้วย loops แล้ว) [58], OpenAI รวม ChatGPT Library เข้า Codex [28] และ Claude Design อัปเดตใหม่ [57]
- Claude Code ถูกนำไปทดลองถอดรหัส Linear A อักษรโบราณของ Crete อายุ ~3,500 ปี [7] — ผู้เขียนระบุชัดว่ายังรอ peer review ไม่ใช่ผลิตภัณฑ์ที่ ship แล้ว
- Trump ถอยจากท่าทีที่เคยจัด Anthropic/Dario Amodei ว่าเป็นภัยความมั่นคงแห่งชาติ หันมาบอกว่าพวกเขา 'ประพฤติตัวอย่างรับผิดชอบมาก' [8][13][42]; Andrew Ng ชี้ว่าทั้งรัฐบาลสหรัฐฯ และ Anthropic ต่างดำเนินการจำกัดการเข้าถึง frontier model [25]
- ข่าว 'SpaceX ซื้อ Cursor ราคา $60B' กำลังแพร่ [9][16] แต่มาจากแหล่งที่น่าเชื่อถือต่ำและยังไม่ยืนยัน — อย่าถือเป็นข้อเท็จจริง

## What happened
รายการที่ได้รับ engagement สูงวันนี้ถูกครอบงำด้วยเรื่องคนและการเมือง ไม่ใช่ artifact John Jumper รายงานว่าออกจาก DeepMind มา Anthropic [2][3][6][11][17] ต่อจาก Noam Shazeer ที่ย้ายไป OpenAI [3][17] ทำให้เกิด narrative เรื่อง DeepMind สูญเสียคนระดับนำ [11] และ Anthropic กำลังเสริมทีม [47] ขณะเดียวกัน Trump ลดน้ำเสียงจากที่เคยใช้คำว่า 'ภัยความมั่นคงแห่งชาติ' กับ Anthropic โดยบอกว่าจะไม่ปิด และพวกเขาตอบสนองอย่างรับผิดชอบ [8][13][35][40][42] ซึ่ง Andrew Ng ตีความว่าทั้งรัฐบาลและ lab กำลังจำกัดการเข้าถึง frontier model พร้อมกัน [25]

## Why it matters (reasoning)
สำหรับ studio สัญญาณที่ใช้งานได้จริงมีน้อย: 'loops' ในฐานะก้าวถัดจาก agent [58], Codex รวม ChatGPT Library [28] และ Claude Design ปรับปรุง [57] เป็นการรวม devtool แบบค่อยเป็นค่อยไป ไม่ใช่ capability ใหม่ที่ต้องรีบนำมาใช้ตอนนี้ การย้ายคนระดับสูง [2][17][47] มีผลทางอ้อมเท่านั้น — อาจเปลี่ยน roadmap ของ model ในช่วงหลายเดือน แต่ไม่กระทบ toolchain วันนี้ การเมืองที่ไปมา [8][13][25][42] เตือนว่าการเข้าถึง model ระดับสูงสุดอาจเผชิญข้อจำกัดด้านนโยบาย ซึ่งเป็น supply risk สำหรับคนที่ผูกแน่นกับ provider เจ้าเดียว การทดลอง Linear A [7] น่าสนใจในฐานะหลักฐานของ long-context structured reasoning แต่ยังไม่ verified และไม่ใช่ product

## Possibility
น่าจะเกิด: devtool รวมกันต่อเนื่อง — feature saved-prompt/library ย้ายเข้า coding agent อย่าง Codex [28] — เพราะเป็น retention play ต้นทุนต่ำ น่าจะเกิดได้: pattern 'loops' [58] กลายเป็น abstraction ที่มีชื่อและนำกลับมาใช้ใหม่ได้ใน agent tooling แต่วันนี้มีหลักฐานแค่ anecdote จาก practitioner คนเดียว ควรให้น้ำหนักเบาๆ น่าจะเกิดได้: DeepMind สูญเสียคนระดับ senior เพิ่มขึ้น เพราะมีสองรายในสัปดาห์เดียว [3][11][17] ไม่น่าจะเกิดตามที่อ้าง: การซื้อกิจการ SpaceX/Cursor $60B [9][16] — แหล่งที่มาอ่อนและขัดแย้งกันเอง รอการยืนยันจาก primary source ก่อนตัดสิน ไม่มีแหล่งไหนให้ตัวเลขความน่าจะเป็น จึงไม่ระบุไว้

## Org applicability — NDF DEV
1) ทำ spike เล็กกับ Claude Code 'loops' สำหรับงานซ้ำๆ ที่จำกัดขอบเขต เช่น asset/config generation หรือ test scaffolding แล้ววัดว่าดีกว่า agent setup ปัจจุบันไหม [58] — effort: low/med 2) ถ้าทีมใช้ Codex อยู่ ดู Library/saved-prompt consolidation ใหม่ เพื่อ standardize reusable prompt สำหรับงาน web/mobile [28] — effort: low 3) ประเมิน Claude Design updates ในฐานะ design-to-code path สำหรับ prototype UI web/mobile [57] — effort: low 4) จดไว้ว่าการถอดรหัส Linear A เป็น reference สำหรับ long-context structured analysis หากสร้าง feature วิเคราะห์เนื้อหา edutech [7] — effort: low (investigation เท่านั้น) ข้ามได้: รายการ talent-move และการเมือง Trump/Anthropic ทั้งหมด [1][2][3][8][13][17][42][47] (ไม่มี action), ข่าวลือ SpaceX/Cursor [9][16] (ยังไม่ verified) และ speculation อย่าง 'recursive self-improvement' [4] และการเข้าถึง 'Claude Mythos' [55] (ไม่มีหลักฐาน)

## Signals to Watch
- จับตาว่า 'loops' จะได้ workflow ที่ documented และทำซ้ำได้จริงหรือยังอยู่แค่ anecdote เดียว [58]
- จับตา Codex Library rollout ว่าเป็นสัญญาณของการรวม prompt reuse เข้า coding agent อย่างไร [28]
- จับตานโยบายการเข้าถึง frontier model (US + นอร์เวย์ที่เกือบแบน AI ในโรงเรียนประถม) สำหรับผลด้าน supply และ compliance ต่อ edutech [25][36]
- จับตาการยืนยันหรือหักล้างจาก primary source ของดีล SpaceX/Cursor ก่อนตัดสินใจ [9][16]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **DeusData/codebase-memory-mcp** — MCP server ด้าน code intelligence ประสิทธิภาพสูง Index codebase ลง knowledge graph แบบถาวร | rss | <https://github.com/DeusData/codebase-memory-mcp> |
| **google-research/timesfm** — TimesFM (Time Series Foundation Model) คือ pretrained foundation model สำหรับ time-series พัฒนาโดย Google | rss | <https://github.com/google-research/timesfm> |
| **palmier-io/palmier-pro** — video editor บน macOS ที่สร้างมาสำหรับ AI Palmier Pro ต้องใช้ macOS 26 (Tahoe) | rss | <https://github.com/palmier-io/palmier-pro> |
| **koala73/worldmonitor** — dashboard intelligence โลกแบบ real-time รวม AI-powered news aggregation และ geopolitical monitoring | rss | <https://github.com/koala73/worldmonitor> |
| **aishwaryanr/awesome-generative-ai-guide** — repo รวม generative AI research updates, interview resources, notebooks และอื่นๆ ครบที่เดียว | rss | <https://github.com/aishwaryanr/awesome-generative-ai-guide> |
| **BuilderIO/agent-native** — framework สำหรับสร้าง agent-native application แบบ open-source | rss | <https://github.com/BuilderIO/agent-native> |
| **chopratejas/headroom** — บีบ tool output, log, file และ RAG chunk ก่อนส่งเข้า LLM ลด token 60-95% | rss | <https://github.com/chopratejas/headroom> |
| **calesthio/OpenMontage** — ระบบ agentic video production แบบ open-source ระบบแรกของโลก 12 pipeline, 52 tool, 500+ agent skill | rss | <https://github.com/calesthio/OpenMontage> |
| **zai-org/GLM-5** — GLM-5: From Vibe Coding to Agentic Engineering รวม GLM-5.2, GLM-5.1 และ GLM-5 | rss | <https://github.com/zai-org/GLM-5> |
| **withastro/flue** — sandbox agent framework — Flue ไม่ใช่แค่ SDK อีกตัว แต่เป็น harness สำหรับ build autonomous agent | rss | <https://github.com/withastro/flue> |
| **n0-computer/iroh** — IP address พัง? dial ด้วย key แทน Modular networking stack ใน Rust | rss | <https://github.com/n0-computer/iroh> |
| **obra/superpowers** — agentic skills framework และ methodology การพัฒนาซอฟต์แวร์ที่ใช้งานได้จริง | rss | <https://github.com/obra/superpowers> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ns123abc | ^4593 c174 | [🚨BREAKING: TRUMP ON ANTHROPIC REPORTER: Do you view Anthropic and to a degree it](https://x.com/ns123abc/status/2068051762708099449) |
| x | ns123abc | ^2198 c50 | ["Sir… John Jumper… the director of DeepMind… the co-creator of AlphaFold… the ma](https://x.com/ns123abc/status/2068023211904602418) |
| x | scaling01 | ^1838 c74 | [Google is in free fall This is the second VP of Engineering that left Google Dee](https://x.com/scaling01/status/2068033319418134965) |
| x | arpitrage | ^1798 c133 | [My best guess is that Anthropic has cracked recursive self improvement, which is](https://x.com/arpitrage/status/2068087090328248474) |
| x | itsgemfourth | ^1562 c6 | [do you guys see what i see. the way fourth ate only half of the cake that's on t](https://x.com/itsgemfourth/status/2068014686436749562) |
| x | Polymarket | ^1191 c88 | [NEW: Nobel Prize-winning AI researcher John Jumper is leaving Google DeepMind fo](https://x.com/Polymarket/status/2068044513931657721) |
| x | bcherny | ^1173 c107 | [Cool way to use Claude Code: deciphering Linear A, a 3500 year old written langu](https://x.com/bcherny/status/2068064304503660962) |
| x | Polymarket | ^1149 c78 | [NEW: Trump says Anthropic was seen as a possible national security threat a week](https://x.com/Polymarket/status/2068054811304476745) |
| x | WallStreetApes | ^1021 c52 | [Elon Musk just made one if the biggest moves in taking over the programming indu](https://x.com/WallStreetApes/status/2068132984004472876) |
| x | DoseofTarot | ^897 c3 | [Mutable Signs Gemini , Pisces , Sagittarius , Virgo Release your ex New doors ar](https://x.com/DoseofTarot/status/2068031747527266592) |
| x | theo | ^821 c80 | [Is DeepMind dying? I've seen multiple high profile departures this week](https://x.com/theo/status/2068077260612276497) |
| x | beffjezos | ^812 c26 | [How it would to feel to be running small local LLMs in a secret container in you](https://x.com/beffjezos/status/2068068034234011694) |
| x | AndrewCurran_ | ^812 c53 | [President Trump on the Axios show this morning 'You know we have a situation wit](https://x.com/AndrewCurran_/status/2068041439481901157) |
| x | levelsio | ^810 c72 | [Any SF startup office we can work from today? SF cafes are absolutely unworkable](https://x.com/levelsio/status/2068033500792717454) |
| x | BoringBiz_ | ^792 c20 | [Asset management associate accidentally sent a Claude prompt that automates his ](https://x.com/BoringBiz_/status/2068044524937425405) |
| x | theallinpod | ^787 c62 | [POD UP! 🚨 Besties are back to discuss: -- SpaceX's record IPO, Cursor deal, and ](https://x.com/theallinpod/status/2068097328154624172) |
| x | mreflow | ^776 c65 | [Google Deepmind losing Noam Shazeer and John Jumper just days apart feels like a](https://x.com/mreflow/status/2068019606435070439) |
| x | levelsio | ^728 c27 | [I respect his game but he's proving that the biggest part of beauty (especially ](https://x.com/levelsio/status/2068069963126943909) |
| x | GreenIrisTarot | ^707 c3 | [❤️‍🔥❤️‍🔥 THIS IS FOR YOU IF… — wearing/using a green object (bag, notebook, clot](https://x.com/GreenIrisTarot/status/2068033261964525866) |
| x | _mohansolo | ^700 c62 | [We've root caused and mitigated the high rates of output text looping in Gemini ](https://x.com/_mohansolo/status/2068054113104069058) |
| radar | ck2 | ^676 c315 | [Hyundai buys Boston Dynamics](https://startupfortune.com/hyundai-takes-full-control-of-boston-dynamics-as-softbank-exits-for-325-million/) |
| x | astroinrealtime | ^646 c11 | [gemini, someone new may surprise you soon. don't close the door too fast.](https://x.com/astroinrealtime/status/2068038858751520848) |
| x | willdepue | ^636 c52 | [there is no question, none at all, that china has full access to all of openai &](https://x.com/willdepue/status/2068118253633737077) |
| x | Katarhein | ^627 c0 | [Night Duty - Claude 🐺 Artist + ai🎛 https://t.co/XPn98fkCNx](https://x.com/Katarhein/status/2068059986060595389) |
| x | AndrewYNg | ^591 c89 | [Over the last two weeks, both the U.S. Government and Anthropic took significant](https://x.com/AndrewYNg/status/2068039709126017356) |
| x | hourIyhoroscope | ^545 c21 | [gemini, you can keep distracting yourself, but the connection between you and le](https://x.com/hourIyhoroscope/status/2068053955377344849) |
| radar | philonoist | ^542 c336 | [Project Valhalla, Explained: How a Decade of Work Arrives in JDK 28](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a) |
| x | testingcatalog | ^533 c29 | [OpenAI is preparing to add Library from ChatGPT into Codex as well. The next pha](https://x.com/testingcatalog/status/2068036927199097272) |
| x | esssdabest | ^512 c1 | [Virgo • Gemini • Sagittarius • Pisces Ooo, love this weekend may take you for a ](https://x.com/esssdabest/status/2068037412622606802) |
| x | alessio_joseph | ^493 c23 | [i miss the old openai, the research lab openai, the area17 design openai https:/](https://x.com/alessio_joseph/status/2068014077453209860) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ns123abc</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4593 · 💬 174</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ns123abc/status/2068051762708099449">View @ns123abc on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨BREAKING: TRUMP ON ANTHROPIC REPORTER: Do you view Anthropic and to a degree its CEO, Dario Amodei, as a threat to national security? TRUMP: &quot;Well, not now, but a week ago, maybe. I was with him yest”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Trump ระบุว่าไม่มองว่า Anthropic หรือ CEO Dario Amodei เป็นภัยต่อความมั่นคงแล้ว หลังจากพบกัน โดยระบุว่ามีคู่แข่งที่เป็นผู้ถือหุ้นบางส่วนเป็นคนรายงาน Anthropic ก่อนหน้า</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ns123abc/status/2068051762708099449" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ns123abc</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2198 · 💬 50</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ns123abc/status/2068023211904602418">View @ns123abc on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">““Sir… John Jumper… the director of DeepMind… the co-creator of AlphaFold… the man who won the Nobel Prize with you… sir… he just announced he’s leaving Google DeepMind and joining Anthropic…” https://”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>John Jumper นักวิทยาศาสตร์ที่ได้รับ Nobel Prize สาขาเคมีปี 2024 และผู้ร่วมสร้าง AlphaFold ประกาศลาออกจาก Google DeepMind เพื่อย้ายไปร่วมงานกับ Anthropic</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Anthropic ดึงนักวิจัยระดับ Nobel จาก DeepMind แสดงถึงทิศทาง deep research ที่ชัดเจนขึ้น — มีนัยต่อ Claude ที่ studio ใช้อยู่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ns123abc/status/2068023211904602418" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@scaling01</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1838 · 💬 74</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/scaling01/status/2068033319418134965">View @scaling01 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Google is in free fall This is the second VP of Engineering that left Google DeepMind this week First, Noam Shazeer, Transformer and MoE pioneer Today, nobel laureate John Jumper who basically built A”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Noam Shazeer (ผู้บุกเบิก Transformer/MoE) และ John Jumper (ผู้สร้าง AlphaFold, รางวัล Nobel) ลาออกจากตำแหน่ง VP ที่ Google DeepMind ในสัปดาห์เดียวกัน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/scaling01/status/2068033319418134965" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@arpitrage</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1798 · 💬 133</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/arpitrage/status/2068087090328248474">View @arpitrage on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“My best guess is that Anthropic has cracked recursive self improvement, which is why the top talent wants to be there”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ Twitter คาดเดาว่า Anthropic ทำ recursive self-improvement ได้แล้ว อ้างเป็นเหตุผลที่ talent ย้ายมา — ไม่มีหลักฐานรองรับ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/arpitrage/status/2068087090328248474" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@itsgemfourth</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1562 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/itsgemfourth/status/2068014686436749562">View @itsgemfourth on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“do you guys see what i see. the way fourth ate only half of the cake that's on the spoon and gemini put the rest in his mouth and ate it. oh my god i cant I CAN FEEL MY INSANITY KICKING IN. #GeminiFou”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนคลับโพสต์เรื่องคู่จิ้น GeminiFourth กินเค้กด้วยกันในคลิป ได้ 1,562 likes จากแฟนๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/itsgemfourth/status/2068014686436749562" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Polymarket</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1191 · 💬 88</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Polymarket/status/2068044513931657721">View @Polymarket on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“NEW: Nobel Prize-winning AI researcher John Jumper is leaving Google DeepMind for Anthropic.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>John Jumper นักวิจัยผู้รับ Nobel เคมี 2024 และผู้นำทีม AlphaFold ที่ Google DeepMind ย้ายมาร่วมงาน Anthropic</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Anthropic ดึง talent ระดับ Nobel จาก DeepMind — สัญญาณว่าจะขยายเกิน LLM ไปสู่ scientific AI จริงจัง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">จับตา research ที่ Anthropic จะออกใน 12 เดือนนี้ — ถ้าเน้น scientific AI อาจมี API/model ใหม่ที่เอาไปใช้ใน project ได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Polymarket/status/2068044513931657721" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bcherny</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1173 · 💬 107</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bcherny/status/2068064304503660962">View @bcherny on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Cool way to use Claude Code: deciphering Linear A, a 3500 year old written language from Crete https://t.co/Aqd4ZG7Cum Hope this holds up in peer review! 🤞”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิจัยใช้ Claude Code วิเคราะห์รูปแบบใน Linear A อักษรมิโนอันอายุ 3,500 ปีที่ยังไม่ถูกถอดรหัส ผลลัพธ์อยู่ระหว่าง peer review</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยืนยันว่า Claude Code ทำ pattern analysis บน unstructured data ที่ไม่ใช่ code ได้จริง — ตรงกับงาน e-learning content pipeline หรือ XR asset classification</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง Claude Code กับ e-learning content ดิบ เพื่อทดสอบการดึงโครงสร้างหรือหา pattern โดยไม่ต้องสร้าง NLP pipeline เอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bcherny/status/2068064304503660962" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Polymarket</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1149 · 💬 78</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Polymarket/status/2068054811304476745">View @Polymarket on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“NEW: Trump says Anthropic was seen as a possible national security threat a week ago, but has since responded “very responsibly.””</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Trump ระบุว่า Anthropic เคยถูกพิจารณาว่าอาจเป็นภัยต่อความมั่นคงแห่งชาติเมื่อสัปดาห์ก่อน แต่ได้รับการยกเว้นหลังตอบสนองอย่างรับผิดชอบ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Polymarket/status/2068054811304476745" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
