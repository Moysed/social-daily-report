---
type: social-topic-report
date: '2026-05-25'
topic: ai-research
lang: en
pair: ai-research.th.md
generated_at: '2026-05-25T08:37:26+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- reddit
- rss
- x
regions:
- global
post_count: 33
salience: 0.45
sentiment: mixed
confidence: 0.55
tags:
- ai-research
- arxiv
- rag
- agents
- evaluation
- text-to-sql
thumbnail: https://preview.redd.it/uogbt0fjw23h1.png?width=2928&format=png&auto=webp&s=8b81e48af69b8935ddeb569d882d866b3e9ba216
---

# AI Research — 2026-05-25

## TL;DR
- PapersWithCode revival under HuggingFace gains traction [1] — useful for tracking SOTA before model picks.
- arXiv flood is mostly agentic systems, formal math, and eval/accountability papers [4][6][9][11][15][17]; few studio-actionable.
- Practical RAG/SQL/Cypher improvements appear [21][22][24] — directly relevant to NDF DEV's Supabase + Next.js stack.
- Hype around $SUPERGEMMA [3] looks like crypto-token marketing, not a real model release — ignore.
- Energy-per-goal accounting [8] and FIM memorization study [30] hint at cost/risk tooling that matters for production agents.

## What happened
PapersWithCode is back under HuggingFace with weekly feature rollouts [1], the only community-validated signal today. The arXiv batch (May 25) is dominated by agentic frameworks (RMA [6], EVE-Agent [11], Foundation Protocol [17], AutoResearch AI [16]), formal-math/verified-code stacks (ImProver 2 [9], Inductive Deductive Synthesis [14], DeepMind formal proof search [2]), and accountability/eval theory ([12][15][19][23]). Direct studio-relevant findings are narrower: query-adaptive semantic chunking for RAG [21], knowledge-distilled open-source Text-to-SQL [22], reflection-augmented Cypher generation [24], FIM memorization dynamics for code models [30], and goal-level energy accounting [8].

## Why it matters (reasoning)
The center of gravity has shifted from base-model papers to agentic orchestration and evaluation infrastructure — meaning adoption decisions now hinge on eval suites and accountability tooling, not raw benchmarks. Second-order effects: (a) RAG/SQL/graph-query papers [21][22][24] keep pushing small open models into 'good enough' territory for retrieval workloads, which lowers Supabase+pgvector integration cost; (b) energy-per-goal [8] reframes 'cheap model' from per-token to per-completed-task — important once agents loop; (c) the $SUPERGEMMA post [3] is a token shill ('people on Base'), not a research signal — a reminder to gate model-card claims by source.

## Possibility
Likely (~70%): PapersWithCode becomes the default model/benchmark index again, replacing scattered HF leaderboards within ~6 months. Likely (~60%): goal-level energy metrics [8] get adopted by at least one major eval harness this year. Possible (~40%): formal-proof + verified-code lines [2][9][14] start producing usable Lean/Coq copilots for non-experts in 12-18 months. Unlikely (<10%): $SUPERGEMMA [3] is a legitimate model worth evaluating.

## Org applicability — NDF DEV
Worth it: (1) Track PapersWithCode [1] as the primary SOTA scan source — low effort, high signal. (2) Pilot query-adaptive semantic chunking [21] in the next Supabase RAG feature (edutech content retrieval) — drop-in over current fixed-window chunking. (3) Watch open-source Text-to-SQL distillation [22] for the HR/Employee page natural-language query feature — could replace LLM API calls with a local small model. (4) Bookmark energy-per-goal [8] when agent loops enter production. Skip: agentic-society/accountability theory papers [15][17][12]; formal-math stack [2][6][9][14] — interesting but off-mission for game/XR/edutech. Explicitly ignore $SUPERGEMMA [3].

## Signals to Watch
- PapersWithCode weekly changelogs — feature velocity tells if the revival sticks [1]
- Adoption of energy-per-goal [8] in HELM/lm-eval-harness
- Open-source Text-to-SQL benchmarks crossing usable threshold for production [22]
- Reproducible RAG chunking ablations citing [21]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | NielsRogge | ^107 c7 | [PapersWithCode new features - week 1 [P] Hi, Niels here from the open-source tea](https://www.reddit.com/r/MachineLearning/comments/1tmawv5/paperswithcode_new_features_week_1_p/) |
| x | WesRoth | ^34 c10 | [This is one of the more interesting AI math results I’ve seen recently. DeepMind](https://x.com/WesRoth/status/2058699572180886015) |
| x | ordiboysxwg | ^33 c3 | [How are people on Base not talking about $SUPERGEMMA ? The model card claims imp](https://x.com/ordiboysxwg/status/2058303640667033837) |
| rss | Joss Armstrong | ^0 c0 | [BOHM: Zero-Cost Hierarchical Attribution for Compound AI Systems arXiv:2605.2286](https://arxiv.org/abs/2605.22866) |
| rss | Paapa Kwesi Quansah, Ernest Bonnah | ^0 c0 | [NeuroNL2LTL: A Neurosymbolic Framework for Natural Language Translation of Linea](https://arxiv.org/abs/2605.22874) |
| rss | Zelin Zhao, Bo Yuan, Jaemoo Choi, Yongxin Chen | ^0 c0 | [RMA: an Agentic System for Research-Level Mathematical Problems arXiv:2605.22875](https://arxiv.org/abs/2605.22875) |
| rss | Shuofei Qiao, Yunxiang Wei, Jiazheng Fan, Bin Wu, Busheng Zhang, Mengru Wang, Yuqi Zhu, Ningyu Zhang, Keyan Ding, Qiang Zhang, Huajun Chen | ^0 c0 | [SciAtlas: A Large-Scale Knowledge Graph for Automated Scientific Research arXiv:](https://arxiv.org/abs/2605.22878) |
| rss | Deepak Panigrahy, Aakash Tyagi | ^0 c0 | [Energy per Successful Goal: Goal-Level Energy Accounting for Agentic AI Systems ](https://arxiv.org/abs/2605.22883) |
| rss | Riyaz Ahuja, Tate Rowney, Jeremy Avigad, Sean Welleck | ^0 c0 | [ImProver 2: Iteratively Self-Improving LMs for Neurosymbolic Proof Optimization ](https://arxiv.org/abs/2605.22885) |
| rss | Oscar Montiel Ross | ^0 c0 | [Mediative Fuzzy Logic: From Type-1 Foundations to Type-2, Type-3 and Quantum Ext](https://arxiv.org/abs/2605.22900) |
| rss | Yamato Arai, Yuma Ichikawa | ^0 c0 | [EVE-Agent: Evidence-Verifiable Self-Evolving Agents arXiv:2605.22905v1 Announce ](https://arxiv.org/abs/2605.22905) |
| rss | Dongxin Guo | ^0 c0 | [The Deterministic Horizon: Impossibility Results as Design Specifications for Tr](https://arxiv.org/abs/2605.23024) |
| rss | Lingyu Jiang, Zirui Li, Shuo Xing, Peiran Li, Tsubasa Takahashi, Dengzhe Hou, Zhengzhong Tu, Kazunori Yamada, Fangzhou Lin | ^0 c0 | [PathCal: State-Aware Reflection-Marker Calibration for Efficient Reasoning arXiv](https://arxiv.org/abs/2605.23074) |
| rss | Shubham Agarwal, Alexander Krentsel, Shu Liu, Mert Cemri, Audrey Cheng, Rui Meng, Tomas Pfister, Chun-Liang Li, Sylvia Ratnasamy, Aditya Parameswaran, Matei Zaharia, Ion Stoica, Mohsen Lesani | ^0 c0 | [Inductive Deductive Synthesis: Enabling AI to Generate Formally Verified Systems](https://arxiv.org/abs/2605.23109) |
| rss | Muhammad Zia Hydari, Farooq Muzaffar | ^0 c0 | [Redrawing the AI Map: A Theory of Accountability Boundaries in Agentic Ecosystem](https://arxiv.org/abs/2605.23179) |
| rss | Guiyao Tie, Jiawen Shi, Dingjie Song, Yixiao Huang, Ziji Sheng, Xueyang Zhou, Daizong Liu, Pan Zhou, Yongchao Chen, Ran Xu, Lifang He, Qingsong Wen, Manling Li, Cong Lu, Shuai Li, Pengtao Xie, Yixuan Yuan, Rui Meng, Lei Xing, Lichao Sun, Caiming Xiong, Philip S. Yu, Jianfeng Gao | ^0 c0 | [AutoResearch AI: Towards AI-Powered Research Automation for Scientific Discovery](https://arxiv.org/abs/2605.23204) |
| rss | Bang Liu, Yongfeng Gu, Jiayi Zhang, Zhaoyang Yu, Sirui Hong, Maojia Song, Xiaoqiang Wang, Mingyi Deng, Zijie Zhuang, Ronghao Wang, Mingzhe Cao, Yutong Zhu, Xingjian Li, Yifan Wu, Jianhao Ruan, Yiran Peng, Shuangrui Chen, Jinlin Wang, Yizhang Lin, Dongjie Zhang, Dekun Wu, Chen Ma, Lizi Liao, Han Yu, Jian Pei, Heng Ji, Qiang Yang, Yuyu Luo, Chenglin Wu | ^0 c0 | [Foundation Protocol: A Coordination Layer for Agentic Society arXiv:2605.23218v1](https://arxiv.org/abs/2605.23218) |
| rss | Vartan Shadarevian, Kia Ghods, Alex Kenich, Anany Kotawala | ^0 c0 | [GENSTRAT: Toward a Science of Strategic Reasoning in Large Language Models arXiv](https://arxiv.org/abs/2605.23238) |
| rss | Niklas Bauer | ^0 c0 | [Evaluating Large Language Models in a Complex Hidden Role Game arXiv:2605.22826v](https://arxiv.org/abs/2605.22826) |
| rss | Mahounan Pericles Adjovi, Victor Olufemi, Roald Eiselen, Prasenjit Mitra | ^0 c0 | [A Survey of Text and Speech Resources for Hausa and Fongbe: Availability, Qualit](https://arxiv.org/abs/2605.22828) |
| rss | Mudit Rastogi | ^0 c0 | [Query-Adaptive Semantic Chunking for Retrieval-Augmented Generation: A Dynamic S](https://arxiv.org/abs/2605.22834) |
| rss | Tianhao Qiu, Xiaojun Chen | ^0 c0 | [Knowledge Distillation for Low-Resource Open-source Text-to-SQL Model arXiv:2605](https://arxiv.org/abs/2605.22843) |
| rss | Daniel C. Ruiz, Anna Serbina, Ashwin Rao, Emilio Ferrara, Luca Luceri | ^0 c0 | [How Far Will They Go? Red-Teaming Online Influence with Large Language Models ar](https://arxiv.org/abs/2605.22880) |
| rss | Minseok Jung, Abhas Ricky, Muhammad Rameez Chatni | ^0 c0 | [RAS: Reflection-Augmented Scaling with In-Context Learning for Executable Cypher](https://arxiv.org/abs/2605.22937) |
| rss | Shubham Parashar, Atharv Chagi, Jacob Helwig, Lakshmi Jotsna, Sushil Vemuri, James Caverlee, Dileep Kalathil, Shuiwang Ji | ^0 c0 | [Learnability-Informed Fine-Tuning of Diffusion Language Models arXiv:2605.22939v](https://arxiv.org/abs/2605.22939) |
| rss | Paul Landes, Pranav Herur, Adam Cross, Jimeng Sun | ^0 c0 | [Graph Alignment Topology as an Inductive Bias for Grounding Detection arXiv:2605](https://arxiv.org/abs/2605.22963) |
| rss | Ko Watanabe, Shoya Ishimaru | ^0 c0 | [Can AI Guess What You Know? Performance Comparison of Large Language Models for ](https://arxiv.org/abs/2605.22971) |
| rss | Brett Israelsen, Sheryl Carty, Josh Coates, Nancy Fulda, Julie Park, Pete Whiting | ^0 c0 | [When AI Takes Sides on Questions of Faith: Persistent Asymmetries in AI-Mediated](https://arxiv.org/abs/2605.22975) |
| rss | George Mikros, Fotios Fitsilis | ^0 c0 | [A Reproducible Universal Dependencies-Style Pipeline for Katharevousa Greek Parl](https://arxiv.org/abs/2605.22978) |
| rss | Tobias von Arx, Tanguy Dieudonn\'e | ^0 c0 | [Memorization Dynamics of Fill-in-the-Middle Pretraining arXiv:2605.22981v1 Annou](https://arxiv.org/abs/2605.22981) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@NielsRogge</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 107 · 💬 7</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/MachineLearning/comments/1tmawv5/paperswithcode_new_features_week_1_p/" target="_blank" rel="noopener"><img src="https://preview.redd.it/uogbt0fjw23h1.png?width=2928&amp;format=png&amp;auto=webp&amp;s=8b81e48af69b8935ddeb569d882d866b3e9ba216" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“PapersWithCode new features - week 1 [P] Hi, Niels here from the open-source team at Hugging Face. It's been one week since I [launched](https://www.reddit.com/r/MachineLearning/comments/1tgmwqr/reviv”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Hugging Face revived PapersWithCode at paperswithcode.co and added multi-metric leaderboard support in its first week, letting benchmarks show e.g. both WER and RTFx for ASR, or mAP and FPS for object detection.</dd>
      <dt>Why interesting</dt>
      <dd>A single hub now tracks SOTA across agents, computer vision, and time-series with richer benchmark comparisons — directly useful for vetting which model to integrate before committing dev time.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can use paperswithcode.co as the first stop when evaluating AI models for XR/e-learning features, comparing speed (FPS/RTF) alongside accuracy so Unity integration trade-offs are data-backed from day one.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/MachineLearning/comments/1tmawv5/paperswithcode_new_features_week_1_p/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@WesRoth</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 34 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/WesRoth/status/2058699572180886015">View @WesRoth on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is one of the more interesting AI math results I’ve seen recently. DeepMind researchers published a new paper showing AI-driven formal proof search can solve real open mathematics problems. The s”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>DeepMind's AI system used LLM agents with Lean formal verification to autonomously solve 9 open Erdős problems and 44 OEIS conjectures, at a cost of a few hundred dollars per problem.</dd>
      <dt>Why interesting</dt>
      <dd>Formal verification via Lean eliminates hallucinated proofs — the LLM generates candidates, Lean certifies correctness, giving a reliable human-reviewable output loop small teams can trust.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can apply the same generate-then-verify loop to e-learning assessment logic or XR simulation rules: LLM drafts the logic, a formal checker (or unit test suite) gates correctness before shipping.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/WesRoth/status/2058699572180886015" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ordiboysxwg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 33 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ordiboysxwg/status/2058303640667033837">View @ordiboysxwg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“How are people on Base not talking about $SUPERGEMMA ? The model card claims improved speed, better benchmark scores, and stronger performance across code, logic, Korean and browser tasks. SuperGemma ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Author promotes $SUPERGEMMA on Base blockchain, citing its model card's claims of faster speed, higher benchmarks, and better code/logic/Korean/browser task performance, plus compatibility with Openclaw and Hermes Agent for local terminal AI workflows.</dd>
      <dt>Why interesting</dt>
      <dd>Openclaw + Hermes Agent as a terminal-first local AI stack is a concrete pairing worth benchmarking — independent of the $SUPERGEMMA token hype.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can evaluate Openclaw + Hermes Agent as a local AI workflow layer for dev tooling, independent of the crypto token angle — test against current local LLM setup.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ordiboysxwg/status/2058303640667033837" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
