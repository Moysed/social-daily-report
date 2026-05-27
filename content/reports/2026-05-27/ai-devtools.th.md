---
type: social-topic-report
date: '2026-05-27'
topic: ai-devtools
lang: th
pair: ai-devtools.en.md
generated_at: '2026-05-27T04:18:30+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- hackernews
- lobsters
- reddit
- x
regions:
- global
post_count: 101
salience: 0.78
sentiment: positive
confidence: 0.72
tags:
- agent-skills
- mcp
- coding-agents
- skillopt
- local-llm
- devtools
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2059014023979708416/img/piQWt-tsvd5ADLIz.jpg
translated_by: claude-sonnet-4-6
---

# AI Devtools — 2026-05-27

## TL;DR
- แนวโน้ม SkillOpt/SkillX: agent skills ในฐานะ trainable text-space parameters — งานวิจัยของ Microsoft อ้างว่าได้ผลดีที่สุดหรือเทียบเท่าดีที่สุดใน 52/52 settings [4][25][31][53][60]
- Karpathy เผยแพร่คอร์สฝึก training stack เต็มรูปแบบฟรีบน YouTube — คุ้มค่าสูงสำหรับการพัฒนาทักษะของทีม [1]
- 'Better code more slowly' สร้างแรงสั่นสะเทือน (420 comments): โค้ดที่ใช้ AI ช่วยต้องการการไตร่ตรองจากมนุษย์มากขึ้น ไม่ใช่น้อยลง [2]
- Agent Skills กำลังกลายเป็นมาตรฐานใน IDE: VS/Copilot SKILL.md, Expo MCP สำหรับนักพัฒนา RN/mobile [10][27][45]
- benchmark สำหรับ coding-agent แบบ long-horizon ชุดใหม่ปรากฏขึ้น — ทำงานกับ repo จริง แก้ไขหลายไฟล์ และมี debug loops [8]

## What happened
มีสัญญาณที่ชัดเจนสองอย่างครองบทสนทนาเกี่ยวกับ AI devtools ในวันนี้ อย่างแรกคือ 'Agent Skills' ในฐานะ abstraction ระดับเฟิร์สคลาส: งานวิจัย SkillOpt ของ Microsoft [25][31][53] มองไฟล์ markdown SKILL.md เป็น trainable parameters ที่ optimize ในพื้นที่ text (ไม่มีการ finetuning weights) ซึ่งรายงานว่าให้ผลดีที่สุดหรือเทียบเท่าดีที่สุดใน 52/52 settings; SkillX [60] ขยายแนวคิดนี้ไปสู่การสร้าง skill knowledge bases อัตโนมัติจากประสบการณ์ของ agent; Visual Studio ส่ง Copilot Agent Skills พร้อม SKILL.md แบบ drop-in [45] และ Expo เปิดตัว MCP server สำหรับ AI coding assistants [10][27] อย่างที่สองคือการตั้งคำถามอย่างมีสติต่อความเร็วของ AI coding: บทความ 'write better code more slowly' ของ Nolan Lawson [2] ได้รับ 420 HN comments — แก่นของบทความคือ AI ยกระดับเพดานได้ แต่ต่อเมื่อมนุษย์ชะลอลงเพื่อตรวจสอบเท่านั้น ที่เกี่ยวข้องกัน: คอร์สฝึกแบบ full-stack ฟรีของ Karpathy [1], coding-agent benchmark แบบ long-horizon ชุดใหม่ [8] และบทความว่าด้วยเศรษฐศาสตร์ 'outsourcing + local AI vs frontier labs' [17]

## Why it matters (reasoning)
Skills-as-parameters คือ layer ที่ขาดหายไประหว่าง prompt engineering กับ finetuning — ถูก พกพาได้ ควบคุม version ได้ และไม่ผูกกับ model ใด สำหรับ studio ขนาดเล็ก นี่คือระดับที่เหมาะสม: บันทึกความรู้เฉพาะของ studio (Unity patterns, Supabase conventions, XR pipelines) ไว้ใน markdown ที่ agent ทุกตัว (Claude Code, Copilot, Cursor) โหลดได้ ในระดับ second-order: MCP + Skills รวมกันทำให้ 'agent ที่รู้จัก stack ของคุณ' กลายเป็นสินค้าทั่วไป — Expo MCP [10] คือต้นแบบที่ทุก framework จะตามมาภายในไม่กี่เดือน บทความของ Lawson [2] เป็นตัวถ่วงดุลกับกระแส vibe-coding: studio ที่วัดจาก 'PRs merged' จะ ship bugs; ส่วนที่วัดจาก 'defects caught in review' จะเติบโตแบบทบต้น แนวโน้ม local-model (Qwen3.5 [7][19][51], MiniCPM5-1B [40], Bonsai 1-bit diffusion [6]) ยืนยันการแบ่ง 'frontier สำหรับงานยาก, local สำหรับ hot loops' ต่อไป [17]

## Possibility
มีโอกาสสูง (~70%): ภายใน 2-3 เดือน SKILL.md จะกลายเป็น convention โดยพฤตินัยใน Claude Code, Copilot, Cursor, Codex — studio ต่างๆ จะดูแล /skills folder เหมือนกับ /tests ปานกลาง (~45%): การ auto-optimization ของ skills แบบ SkillOpt จะลงสู่ OSS tooling ให้ทีมพัฒนา skills จาก telemetry ได้ ต่ำกว่า (~25%): coding-agent benchmark อย่าง [8] จะกลายเป็น reference อ้างอิงใหม่แทน SWE-bench ปรับรูป vendor claims ความเสี่ยง: skill-sprawl และ prompt-injection ผ่าน shared skill marketplaces; คาดว่าจะมี incident ระดับ CVE ภายใน 6-12 เดือน ข้อจำกัดการเดินทางต่างประเทศของนักวิจัย AI ของจีน [22] อาจชะลอความถี่ของ open-weights จาก Qwen/DeepSeek ในช่วง H2

## Org applicability — NDF DEV
ความเกี่ยวข้องสูง ต้นทุนต่ำ แนวทางที่เป็นรูปธรรมสำหรับ NDF DEV: (1) เริ่มสร้าง /skills folder ในแต่ละ repo (V/VRoom Unity, N NDF HR, W Dej carving, G TM Gym, E Employee) — SKILL.md แยกตาม domain (Unity input system, Supabase RLS patterns, Next.js app-router conventions, XR locomotion) (2) ตั้ง MCP server ภายในองค์กรแบบ Expo สำหรับ docs/components ของเรา — ให้ Claude Code + Cursor ดึงใช้ [10] (3) นำวินัยของ Lawson [2] มาใช้: PR template บังคับให้ระบุ 'สิ่งที่ verify ด้วยตนเอง' ก่อน merge (4) แชร์คอร์สของ Karpathy [1] ให้ทีม — 1 episode/สัปดาห์ พร้อม standup discussion 30 นาที ข้ามไป: SkillOpt auto-optimization (เร็วเกินไป ยังเป็นแค่งานวิจัย), crypto/MCP agent-skills hype [16][35][37][46][48][49] (ไม่เกี่ยวข้อง) ROI: skills + MCP น่าจะช่วยประหยัดได้ 3-5 ชั่วโมง/dev/สัปดาห์ภายในหนึ่งเดือน

## Signals to Watch
- การ adopt convention SKILL.md ใน Cursor/Codex/Gemini CLI — จับตาดูการ converge ของ spec
- OSS implementations ของ SkillOpt บน GitHub — เมื่อ training loop ออกมา ให้ประเมินสำหรับ skills folder ของเรา
- รูปแบบการใช้งาน Expo MCP [10] — template สำหรับ MCP server ภายในองค์กรของเรา
- leaderboard ของ long-horizon coding benchmark [8] — ตรวจสอบ vendor agent claims

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **redraw/rapel** — Show HN: Rapel – chunked resumable downloads in unstable networks | hackernews | <https://github.com/redraw/rapel> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Aicoder786 | ^1455 c17 | [ANDREJ KARPATHY COULD HAVE CHARGED $2,000 FOR THIS COURSE. He put it on YouTube.](https://x.com/Aicoder786/status/2059250699087884506) |
| hackernews | signa11 | ^1154 c420 | [Using AI to write better code more slowly](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/) |
| hackernews | thm | ^818 c375 | [Spain blocks prediction markets Polymarket, Kalshi over lack of gambling licence](https://www.reuters.com/business/spain-blocks-prediction-markets-polymarket-kalshi-over-lack-gambling-licences-2026-05-26/) |
| x | Yif_Yang | ^798 c48 | [🚀 Introducing SkillOpt — an optimizer for agent skills. Instead of finetuning mo](https://x.com/Yif_Yang/status/2058918317918998795) |
| hackernews | vrganj | ^537 c211 | [Netherlands blocks US takeover of vital digital supplier](https://www.politico.eu/article/netherlands-blocks-us-takeover-vital-digital-supplier/) |
| reddit | xenovatech | ^402 c47 | [PrismML just released Binary and Ternary Bonsai Image 4B: 1-bit/ternary text-to-](https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/) |
| reddit | LLMFan46 | ^399 c75 | [Qwen3.5 35B A3B uncensored heretic Native MTP Preserved is Out Now With the Full](https://www.reddit.com/r/LocalLLaMA/comments/1tnzalm/qwen35_35b_a3b_uncensored_heretic_native_mtp/) |
| x | Chrisgpt | ^390 c23 | [wait a minute 💀 they made a benchmark to test whether coding agents can handle r](https://x.com/Chrisgpt/status/2059371392823402804) |
| hackernews | cdrnsf | ^369 c209 | [Big tech's anti-labor playbook has come for Wikipedia](https://medium.com/@jakeorlowitz/wikipedia-is-doing-the-capitalist-thing-56a393232943) |
| x | expo | ^325 c12 | [The Expo MCP Server is now available to everyone. Anyone with an Expo account ca](https://x.com/expo/status/2059351778714583068) |
| hackernews | ggcr | ^322 c682 | [The real cost of owning a home](https://ericturner.dev/posts/cost-of-home-ownership/) |
| hackernews | aghuang | ^314 c341 | [Dropbox CEO Drew Houston to step down <a href="https:&#x2F;&#x2F;blog.dropbox.co](https://www.cnbc.com/2026/05/26/dropbox-ceo-drew-houston-ashraf-alkarmi.html) |
| hackernews | zdw | ^288 c61 | [A few interesting modern pixel fonts](https://unsung.aresluna.org/a-few-interesting-modern-pixel-fonts/) |
| hackernews | croes | ^282 c247 | [The user is visibly frustrated](https://pscanf.com/s/354/) |
| hackernews | nooks | ^276 c106 | [Chemistry behind the Garden Grove chemical tank](https://www.science.org/content/blog-post/methyl-methacrylate-tank) |
| x | AerodromeFi | ^272 c16 | [The next stage of the agentic onchain economy is here. Agent skills for Aerodrom](https://x.com/AerodromeFi/status/2059315557003075922) |
| hackernews | GodelNumbering | ^262 c285 | [Outsourcing plus local AI will soon become more economical vs. frontier labs](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/) |
| x | CryptoCoffee369 | ^250 c18 | [I Found New PulseChain Tool - Use to Your Advantage (Imagine The Use Cases) - Cr](https://x.com/CryptoCoffee369/status/2059049400098275773) |
| reddit | Porespellar | ^247 c68 | [A rare look inside Qwen 3.7's open source model release approval process: For re](https://www.reddit.com/r/LocalLLaMA/comments/1toi50p/a_rare_look_inside_qwen_37s_open_source_model/) |
| x | FellMentKE | ^208 c19 | [The landscape of autonomous AI agents is shifting. SkyClaw-v1.0 has arrived, spe](https://x.com/FellMentKE/status/2058936933204791502) |
| reddit | Forward_Jackfruit813 | ^194 c127 | [Okay 27B made me a believer I previously hated on this model, but I have just be](https://www.reddit.com/r/LocalLLaMA/comments/1to73op/okay_27b_made_me_a_believer/) |
| reddit | kaggleqrdl | ^180 c135 | [China Clamps Down on Overseas Travel for AI Talent at Alibaba, DeepSeek Big, if ](https://www.reddit.com/r/LocalLLaMA/comments/1to5fj5/china_clamps_down_on_overseas_travel_for_ai/) |
| hackernews | gingerlime | ^170 c104 | [Stripe is friendly to "friendly fraud"](https://www.gingerlime.com/2026/stripe-seem-friendly-to-friendly-fraud/) |
| hackernews | cratermoon | ^162 c158 | [Erin Brockovich made a map to track data centers around the country](https://www.niemanlab.org/2026/05/erin-brockovich-made-a-map-to-track-data-centers-around-the-country/) |
| x | HuggingPapers | ^152 c1 | [Microsoft just released SkillOpt Train agent skills like neural networks — in te](https://x.com/HuggingPapers/status/2058899653098086647) |
| reddit | ivari | ^133 c57 | [One letter to appease them all](https://www.reddit.com/r/LocalLLaMA/comments/1tnx5rn/one_letter_to_appease_them_all/) |
| x | betomoedano | ^120 c12 | [Every week another AI image app hits the top charts. The window is open, but not](https://x.com/betomoedano/status/2059263984541253836) |
| x | BeyonderTR | ^119 c146 | [Closed AI systems share the same problem: No matter how much you use them, the p](https://x.com/BeyonderTR/status/2058796863646560297) |
| hackernews | tjek | ^118 c55 | [Cloudflare Flagship](https://developers.cloudflare.com/flagship/) |
| lobsters | pyfisch | ^113 c53 | [Encyclical Letter of His Holiness Leo XIV Magnifica Humanitas](http://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Aicoder786</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1455 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Aicoder786/status/2059250699087884506">View @Aicoder786 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“ANDREJ KARPATHY COULD HAVE CHARGED $2,000 FOR THIS COURSE. He put it on YouTube. The full training stack. Tokenization. Neural network internals. Hallucinations. Tool use. Reinforcement learning. RLHF”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Andrej Karpathy ปล่อยคอร์ส LLM ฟรี 3 ชั่วโมงบน YouTube ครอบคลุม tokenization, neural network internals, hallucinations, tool use, RLHF, DeepSeek และ AlphaGo</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Dev ที่เข้าใจ LLM internals สร้างของที่คนแค่ prompt ไม่มีทางคิดได้ — ได้เปรียบจริงสำหรับทีมเล็กที่ ship AI features ข้าม Unity, XR, และ web</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Dev ในทีมที่สร้าง AI features สำหรับ e-learning หรือ XR ควร block 3 ชั่วโมงดูคอร์สนี้ — เข้าใจว่า LLM hallucinate เพราะอะไรและ RLHF ทำงานยังไง ช่วย improve prompt design และ agent architecture ได้ตรงๆ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Aicoder786/status/2059250699087884506" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Yif_Yang</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 798 · 💬 48</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Yif_Yang/status/2058918317918998795">View @Yif_Yang on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚀 Introducing SkillOpt — an optimizer for agent skills. Instead of finetuning model weights, we treat a natural-language skill as a trainable external parameter. Think of it as deep learning for the f”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>SkillOpt ปรับ skill ของ AI agent โดยใช้ natural-language skill description เป็น trainable parameter แทนการ finetune model weights ใช้แนวคิด deep learning (LR, momentum, epoch) ใน text-space ได้ผลดีที่สุดใน 52/52 benchmark settings</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมเล็กปรับ performance ของ agent ได้โดย iterate บน skill prompt แทนการจ่ายค่า finetune — optimizer เรียนรู้ 'gradient direction' จาก execution log ของ agent loop จริงอย่าง Claude Code</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">studio รัน feedback loop แบบ SkillOpt บน skill prompt ของ agent ที่มีอยู่ได้ — เก็บ execution trace จาก automation pipeline สรุป failure pattern เป็น 'gradient text' แล้ว edit prompt แบบ bounded ทุก cycle ไม่ต้องใช้ GPU</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Yif_Yang/status/2058918317918998795" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@xenovatech</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 402 · 💬 47</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/MjJtcWdvbnAyajNoMRUAidRtSeHG3AHsqjmYv2JB7OCCSSOBELAe-XVtLJ1l.png?format=pjpg&amp;auto=webp&amp;s=426a3e068ac859239a76b1ce25919ca9acf01a35" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“PrismML just released Binary and Ternary Bonsai Image 4B: 1-bit/ternary text-to-image diffusion transformers that can even run 100% locally in your browser on WebGPU. The PrismML team really cooked wi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>PrismML ปล่อย Bonsai Image 4B โมเดล text-to-image แบบ 1-bit/ternary (~3GB) รันได้ใน browser ผ่าน WebGPU, license Apache-2.0</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>โมเดล image-gen 3GB รัน client-side บน WebGPU 100% ตัดต้นทุน server และ backend ออกได้เลย — สำคัญมากสำหรับทีมเล็กที่ทำ web creative tools</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">โปรเจกต์ Next.js ของ studio ฝัง image generation ใน browser ได้โดยไม่มีค่า inference; ทีม XR/VR ทดสอบ asset generation pipeline แบบ offline on-device ได้เลยโดยไม่ต้องมี GPU server</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@LLMFan46</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 399 · 💬 75</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1tnzalm/qwen35_35b_a3b_uncensored_heretic_native_mtp/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/NuJoeV0pDXdCss6LQMmTsZirXhAB7Ep19_9Taoo-y1o.png?auto=webp&amp;s=efeccef16cb40de293ae56d988bd1995ebf78b3f" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Qwen3.5 35B A3B uncensored heretic Native MTP Preserved is Out Now With the Full 785 MTPs Preserved and Retained, Available in Safetensors, GGUFs. NVFP4, NVFP4 GGUFs and GPTQ-Int4 Formats Safetensors,”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Community fine-tune ของ Qwen3.5 35B A3B แบบ uncensored พร้อม MTP heads ครบ 785 ตัว วางให้โหลดใน format GGUF, NVFP4, GPTQ-Int4 บน Hugging Face</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การคง MTP heads ครบ 785 ตัวทำให้ speculative decoding ยังเร็วเต็มที่บน local hardware — ของพวก uncensored release ส่วนใหญ่ตัดออกหมด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีมรัน GGUF variant บน local ได้เลยสำหรับงาน code-gen หรือเขียน narrative ใน e-learning และเกม โดยไม่ติด rate limit หรือ content filter ของ API</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1tnzalm/qwen35_35b_a3b_uncensored_heretic_native_mtp/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Chrisgpt</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 390 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Chrisgpt/status/2059371392823402804">View @Chrisgpt on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“wait a minute 💀 they made a benchmark to test whether coding agents can handle real long horizon engineering work - repo understanding, multi file edits, tool use, debugging loops, test feedback, and ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>benchmark ใหม่ทดสอบ coding agent งาน engineering ระยะยาว — multi-file edits, debugging loops, test feedback, system coherence — GPT-5.5 ทำได้ 70% แล้ว และ OpenAI ยังมี model ภายในที่แรงกว่านี้อีก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ได้ 70% ในงาน coding หลาย file หลาย step จริงๆ หมายความว่า AI agent รับงาน feature เล็กๆ แทน junior dev ได้แล้ว — gap กำลังปิดเร็วมาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีมควรทดลองให้ agent อย่าง Claude Code หรือ Cursor จัดการ bug-fix Unity หรือ feature Next.js แล้ววัด pass rate เทียบ benchmark นี้ — จะได้รู้ว่าตรงไหนยังต้องคน ตรงไหน agent ship ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Chrisgpt/status/2059371392823402804" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@expo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 325 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/expo/status/2059351778714583068">View @expo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Expo MCP Server is now available to everyone. Anyone with an Expo account can connect an AI coding assistant to Expo docs and tools. We see devs using it for a lot of stuff, but here are a couple ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Expo ปล่อย MCP Server สาธารณะ เชื่อม AI coding assistant เข้ากับ docs, build logs, workflow runs, TestFlight crashes และ local simulator ได้เลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>MCP เปลี่ยน AI editor ให้กลายเป็น Expo control panel สด — ไม่ต้องสลับ tab ดู build หรือหา docs ระหว่าง code</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR ใช้ไม่ได้โดยตรง แต่ถ้า project ไหนใช้ React Native หรือ Expo เชื่อม MCP นี้เข้า Cursor หรือ VS Code ได้เลย — ดู build status และ docs ได้โดยไม่ออกจาก editor</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/expo/status/2059351778714583068" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AerodromeFi</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 272 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AerodromeFi/status/2059315557003075922">View @AerodromeFi on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The next stage of the agentic onchain economy is here. Agent skills for Aerodrome are live. Get started at https://t.co/TCAVmmEUY2 https://t.co/b09pqlUXgb”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Aerodrome Finance (DEX บน Base chain) เปิดตัว agent skills ให้ AI agent เชื่อมต่อและใช้งาน liquidity protocol บน chain ได้โดยตรง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>DeFi protocol เริ่ม ship agent interface แบบ native ชี้ว่า 'agent skills' กำลังกลายเป็น integration layer หลัก ไม่ใช่แค่ API เสริม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Not directly applicable. stack ของ studio เป็น Unity/XR/Next.js+Supabase ไม่มี onchain component แต่ pattern 'skills as agent interface' น่าติดตามถ้าทีมจะทำ AI agent ให้ web app ของตัวเอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AerodromeFi/status/2059315557003075922" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CryptoCoffee369</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 250 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CryptoCoffee369/status/2059049400098275773">View @CryptoCoffee369 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I Found New PulseChain Tool - Use to Your Advantage (Imagine The Use Cases) - Crypto HEX Bitcoin https://t.co/sXg3WFt99C”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โปรโมท tool ใหม่บน PulseChain blockchain แบบ hype คลุมเครือ ไม่ระบุ use case จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เป็นแค่ crypto promotion ไม่มี technical content จริง ไม่เกี่ยวกับ dev tooling</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่เกี่ยวกับ studio</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CryptoCoffee369/status/2059049400098275773" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
