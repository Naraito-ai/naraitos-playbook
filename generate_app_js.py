# Python generator script for Naraito's Playbook UI Overhaul and New Sections
import os

app_js_code = r'''/**
 * Naraito's Playbook: Mastering US Remote Engineering Jobs (0 Experience Edition)
 * Comprehensive Interactive Dashboard & Career Execution Portal Engine
 */

// ==========================================
// STATE MANAGEMENT & LOCALSTORAGE KEYS
// ==========================================
const STORAGE_KEYS = {
  ROADMAP: 'us_remote_roadmap_v1',
  ROADMAP_90: 'us_remote_90day_roadmap_v1',
  AUDIT: 'us_remote_audit_v1',
  KANBAN: 'us_remote_kanban_v1',
  DAILY: 'us_remote_daily_v1',
  AUDIO: 'us_remote_audio_v1',
  LI_CHECKLIST: 'us_remote_li_checklist_v2',
  LI_LAUNCH30: 'us_remote_li_launch30_v2',
  FINAL_CHECKLIST: 'us_remote_final_checklist_v1'
};

// Default Initial Roadmap Tasks (24 Actionable Milestones across 4 Phases)
const DEFAULT_ROADMAP = {
  phase1: [
    { id: 'p1-1', title: 'Audit Target US Startup JDs', desc: 'Select 5 high-growth Seed/Series A tech startups and analyze their required backend/ML/full-stack architecture.', completed: false },
    { id: 'p1-2', title: 'Choose 2 Production Blueprints', desc: 'Select 2 real-world projects from the Blueprint Vault (e.g. Hybrid Cost-Optimized Classifier + Anomaly Pipeline).', completed: false },
    { id: 'p1-3', title: 'Implement Tiered Routing Architecture', desc: 'Build the core logic: Rule filters (at $0) -> Small local/fast model -> LLM fallback only when necessary.', completed: false },
    { id: 'p1-4', title: 'Instrument Prometheus & Latency Profiling', desc: 'Add latency percentiles (p50, p95, p99), token cost counters, and drift detection (KL divergence).', completed: false },
    { id: 'p1-5', title: 'Containerize & Deploy on Cloud', desc: 'Deploy with Docker & FastAPI on AWS / GCP / Fly.io / Render with live public health-check & Swagger API docs.', completed: false },
    { id: 'p1-6', title: 'Write Production-Grade GitHub README', desc: 'Include architecture diagrams, cost-per-inference comparisons, benchmark tables, and failure post-mortems.', completed: false }
  ],
  phase2: [
    { id: 'p2-1', title: 'Map Founder Hiring Friction Risks', desc: 'Identify the 5 core concerns US founders have: Execution risk, timezone overlap, communication lag, legal, and ramp-up speed.', completed: false },
    { id: 'p2-2', title: 'Create 1-Page Risk Reversal Proposal', desc: 'Draft your paid 1-week scoped trial offer with zero-risk terms and concrete milestone deliverables.', completed: false },
    { id: 'p2-3', title: 'Record 2-Minute Architecture Loom', desc: 'Record a crisp, 120-second screen share walking through your system design, cost metrics, and code structure.', completed: false },
    { id: 'p2-4', title: 'Establish 4-Hour Timezone Overlap Block', desc: 'Define your dedicated US team communication window (e.g. 7 AM – 11 AM EST / 5:30 PM – 9:30 PM IST).', completed: false },
    { id: 'p2-5', title: 'Setup International Contractor Invoicing', desc: 'Register Deel / Wise / Stripe Express account for seamless friction-free cross-border wire transfers.', completed: false },
    { id: 'p2-6', title: 'Pre-Interview Product Audit / Teardown', desc: 'Identify a UX or API latency bottleneck on target startup and prepare a 3-bullet constructive improvement proposal.', completed: false }
  ],
  phase3: [
    { id: 'p3-1', title: 'Execute Profile Hygiene Audit', desc: 'Professional headshot, solid neutral background, custom banner with architecture diagram, remove OpenToWork ring.', completed: false },
    { id: 'p3-2', title: 'Write Outcome-Driven Headline', desc: 'Implement one of the 16 headline formulas (e.g., "I build cost-efficient ML systems for B2B SaaS | Reduced inference costs 70%").', completed: false },
    { id: 'p3-3', title: 'Craft 5-Block Value Proposition About Section', desc: 'Write 150–250 words following: Hook -> Proof -> Method -> Stack -> Low-friction CTA.', completed: false },
    { id: 'p3-4', title: 'Curate 3-Slot Featured Centerpiece', desc: 'Slot 1: Best case study repo; Slot 2: Highest engagement post; Slot 3: Architecture / cost breakdown PDF.', completed: false },
    { id: 'p3-5', title: 'Turn On Creator Mode & Claim Clean URL', desc: 'Set custom URL (linkedin.com/in/yourname) and pin top 3 relevant technical skills with peer endorsements.', completed: false },
    { id: 'p3-6', title: 'Launch 3x/Week Build-in-Public Schedule', desc: 'Publish 1 confusion/bug post, 1 trade-off math analysis, and 1 failure post-mortem each week.', completed: false }
  ],
  phase4: [
    { id: 'p4-1', title: 'Build Target Decision-Maker Lead List', desc: 'Source 100+ founders and engineering leads from Y Combinator, Product Hunt, and Canadian funded tech dataset.', completed: false },
    { id: 'p4-2', title: 'Execute Daily 20–25 Outreach Routine', desc: 'Send personalized value-first messages daily (~800/month target) using our 3-phase DM templates.', completed: false },
    { id: 'p4-3', title: 'Post 10 Substantive Comments Daily', desc: 'Engage on target founders\' posts with architectural insights, questions, and trade-off math (no "Great post!").', completed: false },
    { id: 'p4-4', title: 'Track Pipeline in Outbound Kanban', desc: 'Log contact dates, personalized hooks, and schedule follow-ups every 3–5 days with fresh value-add updates.', completed: false },
    { id: 'p4-5', title: 'Ace the Introductory Screening Call', desc: 'Lead with eye-level 1080p video, clear audio, BLUF communication, and propose a 1-week paid trial task.', completed: false },
    { id: 'p4-6', title: 'Negotiate $60K–$120K Remote Contractor Agreement', desc: 'Finalize scope, weekly rate ($1,200–$2,500/week), milestone deliverables, and execute contract via Deel/contract.', completed: false }
  ]
};

// Default 90-Day Roadmap Outputs
const DEFAULT_90DAY_ROADMAP = {
  phase1: [
    { id: 'nr-1', text: 'One Python API project', completed: false },
    { id: 'nr-2', text: 'One data analysis project', completed: false },
    { id: 'nr-3', text: 'Updated GitHub profile', completed: false }
  ],
  phase2: [
    { id: 'nr-4', text: 'One deployed machine learning project', completed: false },
    { id: 'nr-5', text: 'One basic RAG application', completed: false },
    { id: 'nr-6', text: 'First version of your resume', completed: false }
  ],
  phase3: [
    { id: 'nr-7', text: 'One production-style AI project', completed: false },
    { id: 'nr-8', text: 'Three pinned GitHub repositories', completed: false },
    { id: 'nr-9', text: 'Updated LinkedIn profile', completed: false },
    { id: 'nr-10', text: 'Live portfolio', completed: false },
    { id: 'nr-11', text: 'Application tracker', completed: false },
    { id: 'nr-12', text: 'Consistent weekly applications', completed: false }
  ]
};

// Default Initial Kanban CRM Leads
const DEFAULT_KANBAN = [
  {
    id: 'lead-init-1',
    name: 'Rocket Doctor AI',
    founder: 'William Cherniak',
    stage: 'conversation',
    linkedin: 'https://www.linkedin.com/company/rocketdoctorai',
    website: 'https://www.rocketdoctor.ai',
    notes: 'Virtual care AI. Pitched hybrid triage classifier to reduce GPT-4 API costs. Call scheduled for Thursday.',
    followUp: '2026-09-18'
  },
  {
    id: 'lead-init-2',
    name: 'QSE Group / Scope Tech',
    founder: 'Sean Prescott',
    stage: 'sent',
    linkedin: 'https://www.linkedin.com/company/scope-technologies-corp/',
    website: 'https://www.qse.group',
    notes: 'Quantum security & SaaS platform. Sent Phase 2 Trade-off DM regarding latency bottlenecks.',
    followUp: '2026-09-19'
  },
  {
    id: 'lead-init-3',
    name: 'Universal Digital',
    founder: 'Crypto Lead',
    stage: 'target',
    linkedin: 'https://www.linkedin.com/company/universaldigital/',
    website: 'https://www.universaldigital.io/',
    notes: 'Analytics SaaS. Analyzing their public tech stack before sending Phase 1 Curiosity DM.',
    followUp: '2026-09-20'
  },
  {
    id: 'lead-init-4',
    name: 'VentureScale AI',
    founder: 'David K. (YC W24)',
    stage: 'interview',
    linkedin: 'https://www.linkedin.com',
    website: 'https://venturescale.io',
    notes: 'Completed 1-week paid trial task ($1,500). Reviewing pull request and final contractor terms.',
    followUp: '2026-09-21'
  }
];

// 5 Diagnostic Audit Questions & Answers
const AUDIT_QUESTIONS = [
  {
    id: 1,
    title: "1. Autonomous Ownership & Ambiguity",
    scenario: "A US founder assigns you a vague task on Slack: 'Our dashboard search is feeling slow. Can you fix it?' What is your immediate action?",
    options: [
      { text: "Ask the founder for a detailed specification document, acceptance criteria, and exact database queries before touching code.", points: 0, feedback: "Traditional ticket-taking behavior. Signals high management overhead." },
      { text: "Tell them you'll write some code to make it faster without profiling first.", points: 2, feedback: "Unstructured action. Founders fear blind code changes that cause regressions." },
      { text: "Profile latency percentiles (p50, p95, p99), isolate query bottlenecks, build a local semantic cache, and send a 2-min Loom with 2 proposed solutions and latency/cost trade-offs.", points: 20, feedback: "Exceptional! High-agency autonomous ownership." },
      { text: "Wait for the next weekly sprint planning meeting to bring it up as a blocker.", points: 0, feedback: "Passive. Remote startups move at daily velocity." }
    ]
  },
  {
    id: 2,
    title: "2. Professional Pushback & Business Consciousness",
    scenario: "The founder excitedly suggests: 'Let's call GPT-4 on all 100,000 daily user requests to classify spam comments.' You know this will cost $6,000/month. What do you do?",
    options: [
      { text: "Say 'Yes sir' and deploy it immediately because the founder requested it.", points: 0, feedback: "Authority deference trap. Costs the startup thousands and wastes runway." },
      { text: "Say 'That won't work' and refuse without proposing an alternative.", points: 2, feedback: "Negative blocker. Frustrates founders." },
      { text: "Present the math: 'GPT-4 will cost $6k/mo. A 3-tier system (Regex rules @ $0 + Small FastText model @ $15/mo + Claude Haiku for 5% edge cases) achieves 99% accuracy for $45/mo. Here is the benchmark.'", points: 20, feedback: "Master-level! Solves the problem while saving runway." },
      { text: "Ignore the message and hope they forget about it.", points: 0, feedback: "Unprofessional and dangerous in remote roles." }
    ]
  },
  {
    id: 3,
    title: "3. Direct Asynchronous Communication (BLUF)",
    scenario: "You discover a critical bug in production on Friday at 3:00 PM EST that will take 4 hours to fix. How do you notify the team?",
    options: [
      { text: "Write a 5-paragraph academic essay explaining the history of the codebase and why previous developers caused it.", points: 0, feedback: "Buried the lead and avoids ownership." },
      { text: "Stay silent, work over the weekend in secret, and tell them on Monday.", points: 2, feedback: "High communication risk. Founders panic when surprises occur." },
      { text: "Post a BLUF Slack update: [BUG] Search API failing for 8% users. [ROOT CAUSE] Null pointer on unindexed tags. [FIX] Hotfix PR #42 open, tests passing. [ETA] Deployed by 4:30 PM EST. [MONITORING] Rollback ready.", points: 20, feedback: "Gold standard! Crisp, transparent, and actionable." },
      { text: "Post 'Hey we have a problem' and wait for someone to ask what it is.", points: 0, feedback: "Low-effort communication that causes anxiety." }
    ]
  },
  {
    id: 4,
    title: "4. Audio/Video Hygiene & Executive Presence",
    scenario: "You have a 30-minute introductory interview call with a US venture-backed founder. How do you prepare your setup?",
    options: [
      { text: "Sit on your bed with laptop on your lap, camera pointing at ceiling fan, ambient room noise, slouched posture.", points: 0, feedback: "Disqualified in 15 seconds. Signals amateurism." },
      { text: "Use blurry fake zoom background, built-in echoey laptop mic, dark lighting with window behind you.", points: 3, feedback: "Silhouette effect and muffled voice distract from your competence." },
      { text: "1080p webcam at eye level, soft front lighting, dedicated noise-canceling mic (or Krisp), neutral background, straight posture, looking directly into camera lens.", points: 20, feedback: "World-class presence! Radiates authority and reliability." },
      { text: "Turn camera off and tell the founder you don't like video calls.", points: 0, feedback: "Instant rejection for remote US roles." }
    ]
  },
  {
    id: 5,
    title: "5. Public Proof of Work & Visibility",
    scenario: "You spent 2 weeks building a machine learning system and encountered a nasty data leakage bug that ruined your initial accuracy. What do you do?",
    options: [
      { text: "Hide the mistake, delete the git history, and only post that you achieved 99% accuracy.", points: 0, feedback: "Fails the credibility test. Experienced founders spot fake metrics immediately." },
      { text: "Keep the project private on your local machine because you feel it's not perfect yet.", points: 2, feedback: "Zero proof of work. Private code doesn't generate inbound job leads." },
      { text: "Publish a detailed GitHub README & LinkedIn post: 'How I diagnosed data leakage in my production model: The audit checklist and 100x speedup lessons.'", points: 20, feedback: "Phenomenal! Demonstrates deep judgment, transparency, and technical depth." },
      { text: "Add 'Machine Learning Expert' to your LinkedIn headline without linking any projects.", points: 0, feedback: "Buzzword soup. Ignored by hiring managers." }
    ]
  }
];

// 6 Production Blueprints Data
const PRODUCTION_BLUEPRINTS = [
  {
    id: 'bp-1',
    title: 'Hybrid Cost-Optimized Classifier',
    tagline: '100K req/day for $23/month using Tiered Routing',
    tech: 'Python, FastAPI, Redis, FastText, Claude 3.5 Haiku, Docker',
    problem: 'Startups burning $3,000–$10,000/mo sending every customer request to GPT-4.',
    architecture: 'Tier 1 (Regex/Cache) -> Tier 2 (Lightweight Local Model) -> Tier 3 (LLM Fallback for 10% edge cases).',
    metrics: '99.4% accuracy, $23/mo infrastructure cost (vs $2,800/mo all-LLM), p95 latency: 28ms.',
    antiResumeProof: 'Includes cost modeling spreadsheet, Locust load-test scripts, and automated fallback tests.',
    readmeSample: '## Hybrid Classifier Architecture\n- Tier 1: Regex & Redis cache catches 60% queries ($0)\n- Tier 2: DistilBERT/FastText catches 30% queries ($5/mo)\n- Tier 3: LLM API invoked for 10% complex queries ($18/mo)\n- **Monthly Cost Savings:** 92.4% reduction.'
  },
  {
    id: 'bp-2',
    title: 'Streaming Anomaly & Fraud Detection Engine',
    tagline: 'High-throughput real-time event pipeline serving 15M events/day',
    tech: 'Kafka / Redpanda, Python, DuckDB, Prometheus, Grafana, Docker',
    problem: 'Fintech startups needing sub-50ms fraud screening without paying enterprise Datadog bills.',
    architecture: 'Kafka event ingestion -> Sliding window feature aggregation -> LightGBM inference -> Alert webhook & Grafana dashboard.',
    metrics: '15M events/day, <18ms p99 latency, zero event loss under backpressure testing.',
    antiResumeProof: 'Includes chaos-engineering test suite (simulated Kafka broker downtime & packet loss).',
    readmeSample: '## Real-time Fraud Engine\n- Processes 180 req/sec at $0.0002 per evaluation\n- Chaos tested: Survives worker node kills with zero message drop\n- Live Grafana dashboard: CPU, Memory, Latency Percentiles.'
  },
  {
    id: 'bp-3',
    title: 'E-Commerce Personalization Engine ($0.001/req)',
    tagline: 'Two-stage retrieval & ranking pipeline generating measurable revenue lift',
    tech: 'Python, Qdrant / FAISS, FastAPI, PyTorch, Redis',
    problem: 'E-commerce brands losing 40% cart conversions due to slow, unpersonalized search.',
    architecture: 'Two-stage pipeline: Fast vector ANN candidate generation (top 500 in 8ms) -> Cross-encoder re-ranking (top 10 in 15ms) -> Redis cache.',
    metrics: '23ms end-to-end latency, 1M catalog items, 100% cache hit for top 20% frequent queries.',
    antiResumeProof: 'Includes offline NDCG@10 evaluation vs naive keyword search & A/B testing framework.',
    readmeSample: '## 2-Stage Recommender\n- Vector retrieval via Qdrant with HNSW indexing\n- Cache warm-up script for top trending SKUs\n- Production Docker compose with 1-click startup.'
  },
  {
    id: 'bp-4',
    title: 'Multi-Tenant RAG Engine with Caching & Cost Caps',
    tagline: 'Enterprise document search with per-workspace budget limits and vector eviction',
    tech: 'FastAPI, LangChain/LlamaIndex, Qdrant, PostgreSQL (pgvector), Docker',
    problem: 'B2B SaaS companies needing RAG without tenant data leakage or runaway API billing.',
    architecture: 'Tenant metadata filtering -> Semantic query deduplication cache -> Hybrid BM25 + Vector search -> Per-tenant token quota governor.',
    metrics: 'Multi-tenant data isolation, 70% cache hit rate on repeated queries, strict $50/mo tenant spending caps.',
    antiResumeProof: 'Includes multi-tenant security test suite proving zero data leakage between customer IDs.',
    readmeSample: '## Multi-Tenant RAG Engine\n- Row-level security on PostgreSQL vector embeddings\n- Rate limiting & cost circuit breaker on OpenAI API calls\n- Evaluation suite using RAGAS for faithfulness and context recall.'
  },
  {
    id: 'bp-5',
    title: 'Drift-Aware Production MLOps Pipeline',
    tagline: 'Automated retraining trigger using KL Divergence and Data Quality Gateways',
    tech: 'Python, Evidently AI, MLflow, Great Expectations, FastAPI, Docker',
    problem: 'Deployed models silently degrading in accuracy after 3 weeks in production without anyone noticing.',
    architecture: 'Incoming feature logging -> Daily distribution drift calculation (KL divergence / KS test) -> Automated retraining pipeline on GitHub Actions -> Canary deployment.',
    metrics: 'Detects data distribution shift in <60 seconds, automated rollback if validation accuracy drops >2%.',
    antiResumeProof: 'Includes synthetic drift generator to simulate sudden customer demographic changes.',
    readmeSample: '## Drift-Aware MLOps\n- Automated statistical testing on incoming payloads\n- Slack webhook alerts when feature drift exceeds threshold\n- Automated rollback to last stable model checkpoint.'
  },
  {
    id: 'bp-6',
    title: 'High-Throughput Async Data Ingestion Pipeline',
    tagline: 'Extracts, parses, and vectors 10,000 PDFs/hr with zero memory leaks',
    tech: 'Python, Celery / ARQ, Redis, Unstructured, Docker, AWS S3',
    problem: 'Document processing worker nodes crashing due to RAM spikes on large PDF batches.',
    architecture: 'Async task queue with backpressure -> Chunked stream processing -> Worker pool auto-scaling -> S3 vector persistence.',
    metrics: '10,000 PDFs/hr processed, constant memory footprint (<512MB per worker), automatic retry with exponential backoff.',
    antiResumeProof: 'Memory profiling flamegraphs (using memory_profiler and tracemalloc) included in repo.',
    readmeSample: '## Async Ingestion Engine\n- Streamed chunking avoids loading 500MB files into RAM\n- Exponential backoff on OCR rate limits\n- Memory profiling proofs attached in docs/.'
  }
];

// 16 LinkedIn Headline Formulas
const HEADLINE_FORMULAS = [
  { id: 1, title: 'Outcome + Proof', formula: 'I [verb] [specific outcome] for [target audience] | [proof metric]', example: 'I build cost-efficient ML systems for B2B SaaS | Reduced inference costs 70% through hybrid architecture' },
  { id: 2, title: 'Problem You Solve', formula: "[Audience]'s [problem] → solved with [your approach]", example: "Helping e-commerce companies turn unused data into revenue | Built recommendation system generating $50K/mo" },
  { id: 3, title: 'Contrarian Identity', formula: '[Your identity] who [unexpected differentiator]', example: 'ML Engineer who thinks like a CFO | I build systems that ship AND save money' },
  { id: 4, title: 'System-Level Proof', formula: '[Role] | [System you own] → [measurable outcome]', example: 'ML Infra Engineer | Own fraud detection pipeline serving 10M txns/day at $0.0002/prediction' },
  { id: 5, title: 'Outcome without Pain', formula: 'I [verb] [outcome] for [audience] without [pain]', example: 'I deploy production ML models for startups without blowing their AWS budget' },
  { id: 6, title: 'Outcome in Time + Proof', formula: '[Outcome] in [time] | [Proof metric]', example: 'Production-ready ML in 60 days | 3 systems deployed, $0 downtime, 99.4% uptime' },
  { id: 7, title: 'State A to State B', formula: 'From [state A] to [state B] using [method]', example: 'From raw messy data to revenue using hybrid ML + rules-based architecture' },
  { id: 8, title: 'Target + Unexpected Combo', formula: '[Target industry] + [unexpected skill combo]', example: 'Healthcare ML Engineer + Regulatory Compliance | HIPAA-ready streaming pipelines' },
  { id: 9, title: 'Quantity + Currently Building', formula: '[Number] [deliverable] for [audience] | Currently [building what]', example: '4 production ML systems for fintech | Currently building real-time fraud detection engine' },
  { id: 10, title: 'Cost / Speed Multiplier', formula: 'I make [expensive thing] [cheaper/faster/better]', example: 'I make LLM inference 10x cheaper with tiered routing, local models, and semantic caching' },
  { id: 11, title: 'Niche Specialist', formula: '[Role] specializing in [niche] | [Anti-resume proof]', example: 'Backend & ML Engineer specializing in cost optimization | $1,200/mo AWS savings documented' },
  { id: 12, title: 'Building at Scale', formula: 'Building [specific system] | [Scale & Uptime metric]', example: 'Building real-time recommendation engine | 50K requests/day, 99.2% uptime, 24ms p95' },
  { id: 13, title: 'Pain Trigger Magnet', formula: '[Audience] hire me when [pain trigger]', example: 'Startups hire me when their LLM costs hit $10K/mo and they need them under $1K' },
  { id: 14, title: 'Replaced Expensive Setup', formula: 'I replaced [expensive thing] with [cheaper thing] | [Result]', example: 'I replaced a $40K/mo all-GPT-4 pipeline with hybrid routing | Same quality, $3K/mo' },
  { id: 15, title: 'Zero to Outcome', formula: 'Zero to [outcome] in [time] | Documenting the journey', example: 'Zero to production ML pipeline in 8 weeks | Documenting every architectural failure publicly' },
  { id: 16, title: 'Domain + System + Metric', formula: '[Domain] | [Specific system] | [Cost/Scale metric]', example: 'E-commerce ML | Personalization engine | 1M users, $0.001/recommendation' }
];

// About Section Templates
const ABOUT_TEMPLATES = {
  A: `Everyone's building with LLMs. Almost nobody's checking the bill.

I built a hybrid customer support classifier that handles 100K requests/day for $23/month. The industry average for the same workload runs $2,500+/month. The difference? Hybrid routing: rules catch 60% of queries at $0, a lightweight local model handles 30% for fractions of a cent, and LLMs only touch the 10% that actually need complex language reasoning.

My first question on any engineering project isn't "which hyped model?" It's "do we even need an LLM here?" That single question saves startups thousands monthly.

Stack: Python, FastAPI, PyTorch, Redis, Docker, monitoring with Prometheus & Grafana.

If your infrastructure or AI costs are higher than they should be, I'd love to compare notes and share my open-source architecture.`,

  B: `Models don't fail because of math. They fail because reality changes and nobody was thinking at the system level.

I've built and owned ML systems that serve real traffic—meaning I've been the person debugging at 2 AM when latency doubles, explaining cost spikes to stakeholders, and designing fallbacks when third-party APIs go down. That's where my judgment was built: not in courses, but in production.

Recent work: Designed end-to-end streaming anomaly detection with drift monitoring (KL divergence), automated retraining, and tiered inference routing. System handles 15M events/day at 99.9% uptime.

What I bring: production deployment, cost optimization, monitoring-first architecture, and the ability to explain technical trade-offs clearly to non-technical founders.

Building something in production and want to talk architecture? Let's connect.`,

  C: `I spent 3 years in analytical problem solving learning something most engineers take a decade to grasp: how businesses actually make decisions and burn capital.

Now I build software and ML systems where every technical choice is filtered through a business lens: Does this reduce burn? Does this ship faster? Does this actually solve the customer's bottleneck, or just look impressive?

Over the past 6 months, I've built 3 production-grade systems from scratch, documented every failure and architecture decision publicly, and learned to think in trade-offs—not just syntax.

My latest project: Hybrid RAG engine with strict tenant cost quotas and semantic caching ($0.001/req).

Currently exploring remote backend and ML roles at US startups. If you value execution velocity and business judgment, let's chat.`
};

// Content Archetype Templates
const CONTENT_TEMPLATES = {
  confusion: `Week 2 of learning vector search indexing:

I kept using brute-force cosine distance across 500,000 embeddings and wondered why my API response time was 4.2 seconds.

Then I implemented HNSW (Hierarchical Navigable Small World) indexing with Qdrant.

Before vs After:
• Brute-force: 4,200ms latency, high CPU spike
• HNSW: 14ms latency, 99% recall accuracy

The mental shift from linear search to approximate graph traversal was the real breakthrough.

When building AI systems, 80% of performance is choosing the right data structure—not a bigger GPU.`,

  mistake: `I deployed my first recommendation model with 94% test accuracy.

24 hours later, it started recommending winter coats to users browsing summer swimwear.

Root cause: Data leakage in my training split. A feature indirectly contained the post-purchase timestamp.

Here is the 3-step feature audit checklist I now run before touching any production database:
1. Timestamp verification (ensure train features strictly precede test events)
2. Permutation feature importance tests
3. Cold-start fallback simulation

Failures in production are painful, but they build the judgment that no certificate can teach.`,

  tradeoff: `Everyone in AI says: "Fine-tuning > Prompt Engineering."

I tested both on 100,000 customer support tickets. Here are the actual numbers:

Approach A (Prompting Claude 3.5 Haiku + Caching):
• Development time: 3 days
• Cost: $0.0008 / request
• Accuracy: 93.5%

Approach B (Fine-tuned Llama 3 8B on AWS GPU):
• Development time: 3 weeks
• Fixed GPU Cost: $650 / month
• Accuracy: 95.8%

For a startup with <200K requests/month, prompting with smart routing won by a landslide. The break-even point for fine-tuning only starts at 600K requests/mo.

Always calculate your cost break-even before renting GPUs.`,

  cost: `How I cut our LLM API bill from $2,400/mo to $185/mo for the exact same workload:

The secret is 3-Tier Hybrid Routing:

1. Tier 1 (Regex + Exact Cache): Catches 55% of queries at $0.00
2. Tier 2 (Local FastText / Embeddings): Handles 35% of intent classification at $0.00001
3. Tier 3 (Claude Haiku / GPT-4o): Only invoked for the 10% ambiguous edge cases

90% of user queries never need a $20/million token model.

Architecture diagram and open-source benchmark repo linked in comments.`,

  build: `Week 4 of building my Multi-Tenant RAG engine in public:

Just implemented token quota circuit breakers.

Here's why: If a single tenant uploads a 500-page document and spams the search endpoint, they could burn your entire OpenAI monthly credit in 20 minutes.

My solution:
• Token bucket rate-limiter per workspace ID
• Hard spending cap ($25/mo per tenant) with automatic fallback to keyword BM25
• Automated Slack webhook when tenant hits 80% quota

Building for multi-tenancy forces you to design for abuse from Day 1.`,

  failure: `Post-Mortem: Why our Kafka consumer group lagged 45,000 messages during Friday's traffic spike.

System: Real-time fraud detection pipeline processing 200 events/sec.

What went wrong:
1. Synchronous database writes blocked the message polling thread.
2. Default heartbeat timeout expired, triggering repeated partition rebalances.
3. Message lag cascaded from 50ms to 8 minutes.

The Fix:
• Decoupled polling from DB persistence using an async memory buffer and bulk inserts.
• Tuned max.poll.interval.ms and increased session.timeout.ms.
• Added Prometheus alert for consumer lag >1,000 messages.

Production isn't what works in Jupyter notebooks. Production is surviving edge-case failures gracefully.`
};

// 3 Cold Outreach DM Templates
const OUTREACH_TEMPLATES = {
  1: `Hi [Founder Name],

Saw your recent launch of [Feature Name] on Product Hunt — love the direction.

I noticed [Company Name] is handling high-volume [data/search/requests]. I recently built an open-source hybrid caching & routing architecture that handles 100k requests/day for under $25/mo (92% cheaper than standard LLM calls) with sub-30ms p95 latency.

Documented the full architecture, Locust load benchmarks, and cost analysis here: [GitHub/Loom Link].

Would love to share the teardown if relevant to your current infrastructure roadmap!

Best,
[Your Name]`,

  2: `Hi [Founder / Eng Lead Name],

Quick question on [Company Name]'s search latency — noticed the new semantic filter takes ~3.2s on complex queries.

I recently benchmarked two-stage vector retrieval (HNSW indexing in Qdrant + cross-encoder reranking) vs naive similarity search, dropping p95 latency from 3.5s to 24ms while preserving 99% NDCG accuracy.

Put together a 2-min Loom screen walkthrough comparing the trade-offs: [Loom Link].

Happy to send over the Docker compose config if helpful!

Cheers,
[Your Name]`,

  3: `Hi [Founder Name],

Saw you're scaling [Company Name] and looking for engineers who can ship autonomously without handholding.

To de-risk hiring, I built a working prototype of [Specific Solution, e.g., Multi-Tenant RAG with $50/mo budget guardrails] specifically tailored to your stack.

• Live Demo: [URL]
• Architecture & Test Suite: [GitHub URL]
• 2-Min Loom Breakdown: [Loom URL]

I'm available for a 1-week scoped paid trial task ($1,250) with guaranteed 4-hr US timezone overlap and daily async Loom updates.

Looking forward to connecting!

Best,
[Your Name]`
};

// Initial App State
let appState = {
  roadmap: loadFromStorage(STORAGE_KEYS.ROADMAP, DEFAULT_ROADMAP),
  audit: loadFromStorage(STORAGE_KEYS.AUDIT, { answers: {}, score: null }),
  kanban: loadFromStorage(STORAGE_KEYS.KANBAN, DEFAULT_KANBAN),
  daily: loadFromStorage(STORAGE_KEYS.DAILY, { count: 0, date: new Date().toISOString().slice(0, 10) }),
  sound: loadFromStorage(STORAGE_KEYS.AUDIO, true)
};

// Web Audio FX Engine
const AudioFX = {
  ctx: null,
  init() {
    if (!this.ctx && typeof AudioContext !== 'undefined') {
      this.ctx = new (window.AudioContext || window.webkitAudioContext)();
    }
  },
  playClick() {
    if (!appState.sound) return;
    try {
      this.init();
      if (!this.ctx) return;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(800, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(400, this.ctx.currentTime + 0.04);
      gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.04);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.04);
    } catch (e) {}
  },
  playSuccess() {
    if (!appState.sound) return;
    try {
      this.init();
      if (!this.ctx) return;
      const now = this.ctx.currentTime;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(523.25, now); // C5
      osc.frequency.setValueAtTime(659.25, now + 0.08); // E5
      osc.frequency.setValueAtTime(783.99, now + 0.16); // G5
      gain.gain.setValueAtTime(0.12, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(now + 0.35);
    } catch (e) {}
  }
};

// On DOM Loaded
document.addEventListener('DOMContentLoaded', () => {
  // Check daily date reset
  const todayStr = new Date().toISOString().slice(0, 10);
  if (appState.daily.date !== todayStr) {
    appState.daily.count = 0;
    appState.daily.date = todayStr;
    saveToStorage(STORAGE_KEYS.DAILY, appState.daily);
  }

  // Render all components
  render90DayRoadmap();
  renderAuditQuestions();
  renderRoadmap();
  renderBlueprints();
  renderHeadlineFormulas();
  renderProfileChecklist();
  renderLaunch30Plan();
  renderFinalChecklist();
  renderKanban();
  renderPreloadedLeadsTable();
  updateRoadmapProgress();
  updateDailyDisplay();
  updateAudioIcon();
  
  // Set initial textareas
  const aboutTextarea = document.getElementById('about-textarea');
  if (aboutTextarea) {
    aboutTextarea.value = ABOUT_TEMPLATES.A;
    updateAboutWordCount();
  }
  loadContentPrompt('confusion');
  loadOutreachTemplate(1);
  updateTodaysFocus();

  // Initialize Lucide icons
  if (window.lucide) {
    lucide.createIcons();
  }

  // Scroll spy for nav pill active state
  const navPills = document.querySelectorAll('.nav-pill');
  const sections = document.querySelectorAll('section[id]');
  if ('IntersectionObserver' in window && sections.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          navPills.forEach(pill => {
            pill.classList.remove('active');
            if (pill.getAttribute('href') === '#' + entry.target.id) {
              pill.classList.add('active');
            }
          });
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    sections.forEach(s => observer.observe(s));
  }
});

// ==========================================
// STORAGE UTILS
// ==========================================
function loadFromStorage(key, fallback) {
  try {
    const item = localStorage.getItem(key);
    return item ? JSON.parse(item) : fallback;
  } catch (e) {
    return fallback;
  }
}

function saveToStorage(key, value) {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch (e) {}
}

// Toast Notifications
function showToast(message, type = 'success') {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = `p-3.5 rounded-xl text-xs font-semibold shadow-2xl flex items-center gap-2.5 transition-all duration-300 transform translate-y-4 opacity-0 pointer-events-auto ${
    type === 'success' 
      ? 'bg-[#13131A] border border-[#00D4AA]/50 text-white' 
      : 'bg-[#13131A] border border-[#2A2A3A] text-slate-200'
  }`;

  const iconName = type === 'success' ? 'check-circle-2' : 'info';
  toast.innerHTML = `
    <i data-lucide="${iconName}" class="w-4 h-4 text-[#00D4AA]"></i>
    <span>${message}</span>
  `;

  container.appendChild(toast);
  if (window.lucide) lucide.createIcons({ root: toast });

  setTimeout(() => {
    toast.classList.remove('translate-y-4', 'opacity-0');
  }, 10);

  setTimeout(() => {
    toast.classList.add('opacity-0', 'translate-y-2');
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// ==========================================
// SECTION 1: ARBITRAGE CALCULATOR
// ==========================================
function updateArbitrageCalculator(val) {
  const salary = parseInt(val, 10);
  const inrRate = 86.5;
  const inrTotal = Math.round(salary * inrRate);
  const sfCost = 300000;
  const savings = sfCost - salary;
  const multiplier = (inrTotal / 800000).toFixed(1);
  const monthlyUsd = Math.round(salary / 12);

  const salDisp = document.getElementById('calc-salary-display');
  const fSav = document.getElementById('calc-founder-savings');
  const inrAnn = document.getElementById('calc-inr-annual');
  const mult = document.getElementById('calc-multiplier');
  const mUsd = document.getElementById('calc-usd-monthly');

  if (salDisp) salDisp.textContent = `$${salary.toLocaleString()} / year`;
  if (fSav) fSav.textContent = `$${savings.toLocaleString()} / yr`;
  if (inrAnn) inrAnn.textContent = `₹${inrTotal.toLocaleString('en-IN')}`;
  if (mult) mult.textContent = `${multiplier}x`;
  if (mUsd) mUsd.textContent = `$${monthlyUsd.toLocaleString()} / mo`;
}

function openArbitrageModal() {
  AudioFX.playClick();
  const el = document.getElementById('hero-section');
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}

// ==========================================
// SECTION 2: 90-DAY ROADMAP (NEW)
// ==========================================
let roadmap90State = loadFromStorage(STORAGE_KEYS.ROADMAP_90, DEFAULT_90DAY_ROADMAP);

function render90DayRoadmap() {
  ['phase1', 'phase2', 'phase3'].forEach((pKey, idx) => {
    const container = document.getElementById(`roadmap-90-p${idx+1}-outputs`);
    if (!container) return;
    const items = roadmap90State[pKey] || [];
    container.innerHTML = items.map(item => `
      <label class="flex items-start gap-2.5 p-2 rounded-lg bg-[#13131A] border ${item.completed ? 'border-[#00D4AA]/40 bg-[#13131A]/90' : 'border-[#2A2A3A]'} cursor-pointer hover:border-[#6C63FF]/50 transition text-xs">
        <input 
          type="checkbox" 
          ${item.completed ? 'checked' : ''} 
          onchange="toggle90DayItem('${pKey}', '${item.id}')"
          class="mt-0.5 w-3.5 h-3.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-[#6C63FF] focus:ring-[#6C63FF] cursor-pointer"
        />
        <span class="${item.completed ? 'line-through text-[#8888A8]' : 'text-slate-200'}">${item.text}</span>
      </label>
    `).join('');
  });
  update90DayProgress();
}

function toggle90DayItem(phaseKey, itemId) {
  AudioFX.playClick();
  const item = roadmap90State[phaseKey]?.find(i => i.id === itemId);
  if (item) {
    item.completed = !item.completed;
    saveToStorage(STORAGE_KEYS.ROADMAP_90, roadmap90State);
    render90DayRoadmap();
    if (item.completed) {
      AudioFX.playSuccess();
      showToast(`Output completed: ${item.text}`);
    }
    updateRoadmapProgress();
  }
}

function update90DayProgress() {
  let total = 0;
  let done = 0;
  Object.values(roadmap90State).forEach(list => {
    total += list.length;
    done += list.filter(i => i.completed).length;
  });
  const pct = Math.round((done / total) * 100);
  const badge = document.getElementById('roadmap-90-progress-badge');
  if (badge) badge.textContent = `${done}/${total} Outputs (${pct}%)`;
}

// ==========================================
// SECTION 3: THE 5 FILTERS DIAGNOSTIC AUDIT
// ==========================================
function renderAuditQuestions() {
  const container = document.getElementById('audit-questions-container');
  if (!container) return;

  container.innerHTML = AUDIT_QUESTIONS.map((q, qIdx) => {
    const selected = appState.audit.answers[q.id];
    return `
      <div class="p-5 rounded-xl bg-[#13131A] border border-[#2A2A3A] space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold font-heading text-slate-100">${q.title}</span>
          <span class="text-[11px] font-mono text-[#8888A8]">20 Points</span>
        </div>
        <p class="text-xs text-slate-300 font-medium">${q.scenario}</p>
        
        <div class="grid grid-cols-1 gap-2.5 pt-1">
          ${q.options.map((opt, optIdx) => {
            const isChecked = selected === optIdx;
            return `
              <label onclick="selectAuditAnswer(${q.id}, ${optIdx})" class="p-3 rounded-xl border text-xs cursor-pointer transition flex items-start gap-3 ${
                isChecked 
                  ? 'bg-[#1C1C27] border-[#00D4AA] text-white' 
                  : 'bg-[#0A0A0F] border-[#2A2A3A] text-slate-300 hover:border-[#6C63FF]/50'
              }">
                <input type="radio" name="audit_q_${q.id}" ${isChecked ? 'checked' : ''} class="mt-0.5 text-[#6C63FF] focus:ring-[#6C63FF]" />
                <div class="flex-1">
                  <span>${opt.text}</span>
                  ${isChecked ? `<p class="mt-1.5 text-[11px] font-mono ${opt.points === 20 ? 'text-[#00D4AA]' : 'text-amber-400'}">💡 ${opt.feedback}</p>` : ''}
                </div>
              </label>
            `;
          }).join('')}
        </div>
      </div>
    `;
  }).join('');

  checkAuditCompletion();
}

function selectAuditAnswer(qId, optIdx) {
  AudioFX.playClick();
  appState.audit.answers[qId] = optIdx;
  saveToStorage(STORAGE_KEYS.AUDIT, appState.audit);
  renderAuditQuestions();
}

function checkAuditCompletion() {
  const answeredCount = Object.keys(appState.audit.answers).length;
  if (answeredCount === AUDIT_QUESTIONS.length) {
    let totalScore = 0;
    AUDIT_QUESTIONS.forEach(q => {
      const chosenIdx = appState.audit.answers[q.id];
      if (chosenIdx !== undefined) {
        totalScore += q.options[chosenIdx].points;
      }
    });

    appState.audit.score = totalScore;
    saveToStorage(STORAGE_KEYS.AUDIT, appState.audit);

    const badge = document.getElementById('audit-score-circle');
    const label = document.getElementById('audit-readiness-label');
    const resultCard = document.getElementById('audit-result-card');
    const largeScore = document.getElementById('audit-result-score-large');
    const title = document.getElementById('audit-result-title');
    const desc = document.getElementById('audit-result-desc');
    const recs = document.getElementById('audit-result-recommendations');

    if (badge) badge.textContent = `${totalScore}%`;
    if (largeScore) largeScore.textContent = `${totalScore}%`;
    if (resultCard) resultCard.classList.remove('hidden');

    let tierTitle = '';
    let tierDesc = '';
    let recsHtml = '';

    if (totalScore >= 80) {
      tierTitle = 'High-Leverage US Remote Operator (Top 5%)';
      tierDesc = 'You possess strong autonomous ownership, direct communication, and business judgment. You are ready for live founder outreach.';
      recsHtml = '<div class="text-[#00D4AA] font-bold mb-1">Recommended Next Step:</div> Jump directly to <strong>Phase 3 (LinkedIn Branding)</strong> and <strong>Phase 4 (Cold Outreach Engine)</strong>. Your non-technical maturity will stand out immediately.';
      if (label) {
        label.textContent = 'Top 5% Ready';
        label.className = 'text-xs font-bold text-[#00D4AA]';
      }
    } else if (totalScore >= 50) {
      tierTitle = 'Transitioning Builder (Needs Polish)';
      tierDesc = 'You have good engineering fundamentals but still show some traditional deferential traits or lack direct asynchronous communication habits.';
      recsHtml = '<div class="text-amber-400 font-bold mb-1">Recommended Next Step:</div> Focus on <strong>Module 1 Filters 1, 2, and 3</strong>. Practice writing 5-sentence BLUF updates and calculating cost trade-offs for your projects.';
      if (label) {
        label.textContent = 'Needs Polish (50-79%)';
        label.className = 'text-xs font-bold text-amber-400';
      }
    } else {
      tierTitle = 'Junior Ticket-Taker (High Risk)';
      tierDesc = 'Your responses reflect heavy dependence on management, Leetcode-style thinking, or reluctance to challenge flawed technical ideas.';
      recsHtml = '<div class="text-rose-400 font-bold mb-1">Critical Action Required:</div> Study <strong>Module 2 (Evaluation Matrix)</strong> and build <strong>Blueprint #1</strong> with documented cost-saving metrics before reaching out to founders.';
      if (label) {
        label.textContent = 'Needs Training (<50%)';
        label.className = 'text-xs font-bold text-rose-400';
      }
    }

    if (title) title.textContent = tierTitle;
    if (desc) desc.textContent = tierDesc;
    if (recs) recs.innerHTML = recsHtml;

    if (totalScore === 100 && window.confetti) {
      confetti({ particleCount: 60, spread: 70, origin: { y: 0.6 } });
      AudioFX.playSuccess();
    }
  }
}

function resetAudit() {
  AudioFX.playClick();
  appState.audit = { answers: {}, score: null };
  saveToStorage(STORAGE_KEYS.AUDIT, appState.audit);
  const badge = document.getElementById('audit-score-circle');
  const label = document.getElementById('audit-readiness-label');
  const card = document.getElementById('audit-result-card');
  if (badge) badge.textContent = '?%';
  if (label) label.textContent = 'Audit Not Completed';
  if (card) card.classList.add('hidden');
  renderAuditQuestions();
  showToast('Audit reset. Choose your genuine responses.');
}

// Camera & Mic Diagnostic (WebRTC)
let mediaStream = null;

async function startCameraTest() {
  AudioFX.playClick();
  try {
    const video = document.getElementById('webcam-preview');
    const placeholder = document.getElementById('webcam-placeholder');
    const overlay = document.getElementById('camera-overlay');
    const startBtn = document.getElementById('start-av-btn');
    const stopBtn = document.getElementById('stop-av-btn');

    mediaStream = await navigator.mediaDevices.getUserMedia({
      video: { width: { ideal: 1280 }, height: { ideal: 720 } },
      audio: true
    });

    video.srcObject = mediaStream;
    video.classList.remove('hidden');
    placeholder.classList.add('hidden');
    overlay.classList.remove('hidden');
    startBtn.classList.add('hidden');
    stopBtn.classList.remove('hidden');
    showToast('Camera & Microphone connected! Verify eye-level line.');
  } catch (err) {
    showToast('Unable to access webcam. Please check browser camera permissions.', 'error');
  }
}

function stopCameraTest() {
  AudioFX.playClick();
  if (mediaStream) {
    mediaStream.getTracks().forEach(track => track.stop());
    mediaStream = null;
  }
  const video = document.getElementById('webcam-preview');
  const placeholder = document.getElementById('webcam-placeholder');
  const overlay = document.getElementById('camera-overlay');
  const startBtn = document.getElementById('start-av-btn');
  const stopBtn = document.getElementById('stop-av-btn');

  if (video) video.classList.add('hidden');
  if (placeholder) placeholder.classList.remove('hidden');
  if (overlay) overlay.classList.add('hidden');
  if (startBtn) startBtn.classList.remove('hidden');
  if (stopBtn) stopBtn.classList.add('hidden');
}

// ==========================================
// SECTION 4: SCENARIO SIMULATOR
// ==========================================
function handleScenarioAnswer(scenarioId, option) {
  AudioFX.playClick();
  const feedback = document.getElementById('scenario-feedback-box');
  if (!feedback) return;
  feedback.classList.remove('hidden');

  if (option === 'C') {
    feedback.className = 'p-4 rounded-xl text-xs space-y-1.5 bg-[#13131A] border border-[#00D4AA] text-[#00D4AA]';
    feedback.innerHTML = `
      <div class="font-bold flex items-center gap-1.5 font-heading">
        <i data-lucide="check-circle" class="w-4 h-4 text-[#00D4AA]"></i> High-Agency US Remote Response (A+)
      </div>
      <p class="text-slate-200">You validated the business goal, presented exact cost economics, offered a hybrid 3-tier architecture, and prepared a fast prototype. US founders love engineers who protect their budget while shipping at high velocity.</p>
    `;
    if (window.confetti) confetti({ particleCount: 35, spread: 60 });
    AudioFX.playSuccess();
  } else {
    feedback.className = 'p-4 rounded-xl text-xs space-y-1.5 bg-[#13131A] border border-rose-800 text-rose-300';
    feedback.innerHTML = `
      <div class="font-bold flex items-center gap-1.5 font-heading text-rose-400">
        <i data-lucide="alert-triangle" class="w-4 h-4"></i> Sub-Optimal Traditional Response
      </div>
      <p class="text-slate-300">${option === 'A' ? 'Blind agreement causes severe AWS/API billing spikes and hallucinations. Founders will blame you for the burn.' : 'Outright refusal without a constructive alternative makes you a blocker.'} Read Option C to see the high-agency standard.</p>
    `;
  }
  if (window.lucide) lucide.createIcons({ root: feedback });
}

// ==========================================
// SECTION 5: EXECUTION ROADMAP
// ==========================================
function switchRoadmapPhase(phaseNum) {
  AudioFX.playClick();
  for (let i = 1; i <= 4; i++) {
    const tab = document.getElementById(`phase-tab-${i}`);
    const content = document.getElementById(`phase-content-${i}`);
    if (tab && content) {
      if (i === phaseNum) {
        tab.classList.add('active', 'bg-[#6C63FF]', 'text-white');
        tab.classList.remove('text-[#8888A8]');
        content.classList.remove('hidden');
      } else {
        tab.classList.remove('active', 'bg-[#6C63FF]', 'text-white');
        tab.classList.add('text-[#8888A8]');
        content.classList.add('hidden');
      }
    }
  }
}

function renderRoadmap() {
  for (let p = 1; p <= 4; p++) {
    const container = document.getElementById(`phase-${p}-checklist`);
    if (!container) continue;

    const phaseKey = `phase${p}`;
    const tasks = appState.roadmap[phaseKey] || [];

    container.innerHTML = tasks.map(t => `
      <div class="p-4 rounded-xl border transition flex items-start justify-between gap-4 ${
        t.completed 
          ? 'bg-[#13131A] border-[#00D4AA]/40' 
          : 'bg-[#1C1C27] border-[#2A2A3A] hover:border-[#6C63FF]/50'
      }">
        <div class="flex items-start gap-3.5 flex-1">
          <input 
            type="checkbox" 
            ${t.completed ? 'checked' : ''} 
            onchange="toggleTask('${phaseKey}', '${t.id}')" 
            class="mt-1 w-4 h-4 rounded bg-[#0A0A0F] border-[#2A2A3A] text-[#6C63FF] focus:ring-[#6C63FF] cursor-pointer"
          />
          <div class="space-y-1">
            <h4 class="text-xs font-bold text-white font-heading ${t.completed ? 'line-through text-[#8888A8]' : ''}">${t.title}</h4>
            <p class="text-[11px] text-[#8888A8] leading-relaxed">${t.desc}</p>
          </div>
        </div>
        <span class="text-[10px] font-mono px-2 py-0.5 rounded shrink-0 ${
          t.completed 
            ? 'bg-[#00D4AA]/10 text-[#00D4AA] border border-[#00D4AA]/30' 
            : 'bg-[#13131A] text-[#8888A8] border border-[#2A2A3A]'
        }">
          ${t.completed ? 'Done ✓' : 'To Do'}
        </span>
      </div>
    `).join('');
  }
}

function toggleTask(phaseKey, taskId) {
  AudioFX.playClick();
  const task = appState.roadmap[phaseKey]?.find(t => t.id === taskId);
  if (task) {
    task.completed = !task.completed;
    saveToStorage(STORAGE_KEYS.ROADMAP, appState.roadmap);
    renderRoadmap();
    updateRoadmapProgress();
    updateTodaysFocus();
    if (task.completed) {
      AudioFX.playSuccess();
      showToast(`Milestone completed: ${task.title}`);
    }
  }
}

function updateRoadmapProgress() {
  let totalTasks = 0;
  let completedTasks = 0;

  // 24 Execution Roadmap tasks
  for (let p = 1; p <= 4; p++) {
    const tasks = appState.roadmap[`phase${p}`] || [];
    totalTasks += tasks.length;
    completedTasks += tasks.filter(t => t.completed).length;
  }

  const pct = Math.round((completedTasks / totalTasks) * 100);

  const bar = document.getElementById('header-progress-bar');
  const txt = document.getElementById('header-progress-text');
  const totPct = document.getElementById('roadmap-total-percentage');
  const badge = document.getElementById('roadmap-counter-badge');

  if (bar) bar.style.width = `${pct}%`;
  if (txt) txt.textContent = `${pct}% (${completedTasks}/${totalTasks} tasks)`;
  if (totPct) totPct.textContent = `${pct}%`;
  if (badge) badge.textContent = `${completedTasks}/${totalTasks}`;

  if (pct === 100 && window.confetti) {
    confetti({ particleCount: 100, spread: 80, origin: { y: 0.5 } });
  }
}

// ==========================================
// SECTION 6: PROJECT BLUEPRINTS
// ==========================================
function renderBlueprints() {
  const container = document.getElementById('blueprints-container');
  if (!container) return;

  container.innerHTML = PRODUCTION_BLUEPRINTS.map(bp => `
    <div class="rounded-xl p-6 space-y-4 bg-[#1C1C27] border border-[#2A2A3A] flex flex-col justify-between hover:border-[#6C63FF]/50 transition">
      <div class="space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-[10px] font-mono uppercase bg-[#6C63FF]/10 text-[#6C63FF] px-2 py-0.5 rounded border border-[#6C63FF]/20 font-semibold">Production Blueprint</span>
          <span class="text-xs font-mono text-[#8888A8]">Zero Toy Projects</span>
        </div>
        <h3 class="text-base font-bold text-white font-heading">${bp.title}</h3>
        <p class="text-xs text-[#00D4AA] font-mono font-semibold">${bp.tagline}</p>
        
        <div class="p-3.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] space-y-1.5 text-xs text-slate-300">
          <div><strong class="text-[#8888A8]">Problem Solved:</strong> ${bp.problem}</div>
          <div><strong class="text-[#8888A8]">Architecture:</strong> ${bp.architecture}</div>
          <div><strong class="text-[#8888A8]">Production Metrics:</strong> <span class="text-[#00D4AA] font-mono">${bp.metrics}</span></div>
          <div><strong class="text-[#8888A8]">Stack:</strong> <span class="text-indigo-300 font-mono">${bp.tech}</span></div>
        </div>

        <div class="p-3 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-xs space-y-1">
          <div class="text-[11px] font-mono text-amber-400 font-semibold">Anti-Resume Proof Layer:</div>
          <p class="text-[#8888A8] text-[11px]">${bp.antiResumeProof}</p>
        </div>
      </div>

      <div class="pt-3 border-t border-[#2A2A3A] flex justify-between items-center">
        <button onclick="copyBlueprintReadme('${bp.id}')" class="px-3.5 py-1.5 rounded-lg bg-[#13131A] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-slate-200 text-xs font-semibold flex items-center gap-1.5 transition">
          <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy README Template
        </button>
        <span class="text-[11px] text-[#8888A8] font-mono">Ready to map to JD</span>
      </div>
    </div>
  `).join('');

  if (window.lucide) lucide.createIcons({ root: container });
}

function copyBlueprintReadme(bpId) {
  AudioFX.playClick();
  const bp = PRODUCTION_BLUEPRINTS.find(b => b.id === bpId);
  if (bp) {
    navigator.clipboard.writeText(bp.readmeSample + '\n\n---\nTarget Stack: ' + bp.tech);
    showToast(`Copied ${bp.title} README template!`);
  }
}

function loadSampleJD() {
  AudioFX.playClick();
  const sample = `Company: NovaScale AI (Seed funded, SF / Remote)
Role: Backend / AI Systems Engineer ($75k - $110k/yr)
About Us: We help e-commerce stores automate customer inquiries and search ranking.
Requirements:
- Strong experience with Python, FastAPI, and PostgreSQL
- Experience optimizing LLM API costs and handling 50k+ daily requests
- Ability to write clean, modular async pipelines and instrument latency monitoring
- Comfortable working autonomously under ambiguity with daily asynchronous updates`;

  const el = document.getElementById('jd-input-text');
  if (el) el.value = sample;
  showToast('Sample US remote JD loaded!');
}

function analyzeJDAndGenerateBlueprint() {
  AudioFX.playClick();
  const el = document.getElementById('jd-input-text');
  const text = el ? el.value.trim() : '';
  if (!text) {
    showToast('Please paste a job description first.', 'error');
    return;
  }

  const outputContent = `
    <div class="space-y-3 font-mono text-xs">
      <div class="p-3 rounded-lg bg-[#13131A] border border-pink-900/60 text-pink-200">
        <strong class="text-pink-400">1. Core Founder Risk Identified:</strong><br/>
        Founder is terrified of runaway LLM API costs ($5k+/mo) and high p95 latency on incoming requests.
      </div>

      <div class="p-3 rounded-lg bg-[#13131A] border border-[#2A2A3A] space-y-2">
        <strong class="text-white">2. Recommended Tailored MVP Architecture:</strong>
        <p class="text-slate-300">
          Build a <strong>3-Tier Hybrid Ingestion & Caching Gateway</strong>:
          <br/>• Tier 1: Redis hash-based exact query cache (0ms latency, $0 cost).
          <br/>• Tier 2: Qdrant vector semantic similarity (catch 35% related questions).
          <br/>• Tier 3: Asynchronous Celery / FastAPI worker calling Claude 3.5 Haiku.
        </p>
      </div>

      <div class="p-3 rounded-lg bg-[#13131A] border border-[#2A2A3A] space-y-1">
        <strong class="text-[#00D4AA]">3. Anti-Resume Proof Points to Include in README:</strong>
        <p class="text-slate-300">
          • Locust load-test benchmark graph showing 250 requests/sec under 40ms latency.<br/>
          • Cost comparison table: $3,200/mo (naive approach) vs $85/mo (your hybrid approach).
        </p>
      </div>
    </div>
  `;

  const outBox = document.getElementById('jd-output-content');
  if (outBox) outBox.innerHTML = outputContent;
  showToast('Tailored Project Blueprint generated!');
  AudioFX.playSuccess();
}

function copyJDOutput() {
  AudioFX.playClick();
  const el = document.getElementById('jd-output-content');
  if (el) {
    navigator.clipboard.writeText(el.innerText);
    showToast('Copied tailored plan to clipboard!');
  }
}

// ==========================================
// SECTION 7: OFFER FRAMEWORK PROPOSAL
// ==========================================
function openProposalGeneratorModal() {
  AudioFX.playClick();
  const modal = document.getElementById('proposal-modal');
  if (modal) modal.classList.remove('hidden');
  generateProposalPreview();
}

function generateProposalPreview() {
  const comp = document.getElementById('prop-company-name')?.value || 'Acme AI';
  const founder = document.getElementById('prop-founder-name')?.value || 'Alex';
  const pain = document.getElementById('prop-pain-point')?.value || 'high API costs & latency';
  const sol = document.getElementById('prop-solution')?.value || 'hybrid 3-tier routing architecture';

  const proposal = `Subject: 1-Week Trial Proposal to solve ${pain} for ${comp}

Hi ${founder},

I noticed ${comp} is scaling rapidly and facing challenges around ${pain}.

To completely de-risk hiring me, I'd like to propose a 1-Week Paid Scoped Trial Task ($1,250):

• Deliverable: Deploy a working prototype of ${sol} on a staging branch.
• Guarantee: Measurable 50%+ reduction in latency / API bills with automated tests.
• Timezone Overlap: Guaranteed 4 hours daily overlap (7 AM – 11 AM EST).
• Daily Communication: 2-minute daily Loom walkthrough + 3-bullet Slack update.
• No Long-term Obligation: If you aren't thrilled with the code velocity, we part ways with zero friction.

I've attached my architecture diagram and Locust benchmark metrics here: [Loom / GitHub Link].

Looking forward to hearing your thoughts.

Best regards,
[Your Name]
Remote Software Engineer`;

  const out = document.getElementById('proposal-output-text');
  if (out) out.value = proposal;
}

function copyProposalOutput() {
  AudioFX.playClick();
  const text = document.getElementById('proposal-output-text')?.value || '';
  navigator.clipboard.writeText(text);
  showToast('Proposal copied to clipboard!');
}

// ==========================================
// SECTION 8: LINKEDIN STUDIO
// ==========================================
function switchLinkedInTab(tabKey) {
  AudioFX.playClick();
  const tabs = ['headlines', 'about', 'checklist', 'featured', 'content', 'launch30'];
  tabs.forEach(t => {
    const btn = document.getElementById(`li-tab-${t}`);
    const content = document.getElementById(`li-content-${t}`);
    if (btn && content) {
      if (t === tabKey) {
        btn.classList.add('bg-[#6C63FF]', 'text-white', 'font-semibold');
        btn.classList.remove('text-[#8888A8]', 'hover:text-white');
        content.classList.remove('hidden');
      } else {
        btn.classList.remove('bg-[#6C63FF]', 'text-white', 'font-semibold');
        btn.classList.add('text-[#8888A8]', 'hover:text-white');
        content.classList.add('hidden');
      }
    }
  });

  if (tabKey === 'checklist') renderProfileChecklist();
  if (tabKey === 'launch30') renderLaunch30Plan();
}

function renderHeadlineFormulas() {
  const container = document.getElementById('headline-formulas-grid');
  if (!container) return;

  container.innerHTML = HEADLINE_FORMULAS.map(hf => `
    <div class="p-4 rounded-xl bg-[#13131A] border border-[#2A2A3A] hover:border-[#6C63FF]/50 space-y-2.5 transition">
      <div class="flex items-center justify-between">
        <span class="text-xs font-bold text-white font-mono">Formula ${hf.id}: ${hf.title}</span>
        <button onclick="copyFormulaExample('${hf.example.replace(/'/g, "\\'")}')" class="text-[11px] font-mono text-[#00D4AA] hover:underline flex items-center gap-1">
          <i data-lucide="copy" class="w-3 h-3"></i> Copy
        </button>
      </div>
      <div class="text-[11px] font-mono text-[#8888A8] bg-[#0A0A0F] p-2 rounded border border-[#2A2A3A]">${hf.formula}</div>
      <div class="text-xs text-[#00D4AA] font-medium"><em>“${hf.example}”</em></div>
    </div>
  `).join('');

  if (window.lucide) lucide.createIcons({ root: container });
}

function copyFormulaExample(example) {
  AudioFX.playClick();
  navigator.clipboard.writeText(example);
  showToast('Copied headline to clipboard!');
}

function loadAboutTemplate(key) {
  AudioFX.playClick();
  const el = document.getElementById('about-textarea');
  if (el) el.value = ABOUT_TEMPLATES[key];
  updateAboutWordCount();
  showToast(`Loaded Template ${key}`);
}

function updateAboutWordCount() {
  const text = document.getElementById('about-textarea')?.value.trim() || '';
  const words = text ? text.split(/\s+/).length : 0;
  const label = document.getElementById('about-word-count');
  if (label) {
    label.textContent = `Word Count: ${words} words (Target: 150-250)`;
    if (words >= 150 && words <= 250) {
      label.className = 'text-xs font-mono text-[#00D4AA] font-bold';
    } else {
      label.className = 'text-xs font-mono text-[#8888A8]';
    }
  }
}

function copyAboutText() {
  AudioFX.playClick();
  const text = document.getElementById('about-textarea')?.value || '';
  navigator.clipboard.writeText(text);
  showToast('Copied About pitch to clipboard!');
}

function loadContentPrompt(archetype) {
  AudioFX.playClick();
  const prompt = CONTENT_TEMPLATES[archetype] || '';
  const el = document.getElementById('post-draft-textarea');
  if (el) el.value = prompt;
}

function copyPostDraft() {
  AudioFX.playClick();
  const text = document.getElementById('post-draft-textarea')?.value || '';
  navigator.clipboard.writeText(text);
  showToast('Copied post draft to clipboard!');
}

// TAB 1: 30-Day Launch Plan
const DEFAULT_LAUNCH_30_PLAN = [
  { id: 'l30-1', day: 'Day 1', title: 'Profile Setup', desc: 'Photo, banner, headline (Formula 1–4), About (5-Block Framework), custom URL, Creator Mode ON', completed: false },
  { id: 'l30-2', day: 'Day 2', title: 'Featured Section', desc: "Add your best project link (even if it's a learning project with metrics). Placeholder for Slots 2–3.", completed: false },
  { id: 'l30-3', day: 'Day 3–7', title: 'Daily Outreach Begins', desc: 'Connect with 25 people/day (hiring managers, ML leads, founders). Comment on 10 posts. Join 5 conversations.', completed: false },
  { id: 'l30-4', day: 'Day 7', title: 'First Post', desc: "Write your first \"confusion post\": what you're learning, what confused you, how you figured it out.", completed: false },
  { id: 'l30-5', day: 'Day 8–14', title: 'Outreach + Content', desc: 'Continue daily outreach. Post second piece (a mistake you made while learning). Track stats.', completed: false },
  { id: 'l30-6', day: 'Day 14', title: 'Audit', desc: 'Check connection acceptance rate (target: 40%+). Check post engagement. Refine headline if needed.', completed: false },
  { id: 'l30-7', day: 'Day 15–21', title: 'Deepen Content', desc: 'Post tradeoff analysis or cost breakdown from your learning. Engage 50+ posts/week.', completed: false },
  { id: 'l30-8', day: 'Day 21', title: 'Case Study Draft', desc: 'Start documenting your learning journey as a structured case study for Featured Slot 1.', completed: false },
  { id: 'l30-9', day: 'Day 22–28', title: 'Scale Outreach', desc: 'Personalize messages using Phase 1 template. Start tracking in CRM spreadsheet.', completed: false },
  { id: 'l30-10', day: 'Day 30', title: 'Full Audit', desc: "Re-run checklist from Section 3. Update Featured section. Refine About section based on what you've learned about your audience.", completed: false }
];

let launch30PlanState = loadFromStorage(STORAGE_KEYS.LI_LAUNCH30, DEFAULT_LAUNCH_30_PLAN);

function renderLaunch30Plan() {
  const tbody = document.getElementById('launch-30-tbody');
  const progressBadge = document.getElementById('launch-30-progress-badge');
  const progressBar = document.getElementById('launch-30-progress-bar');
  if (!tbody) return;

  const total = launch30PlanState.length;
  const completed = launch30PlanState.filter(item => item.completed).length;
  const pct = Math.round((completed / total) * 100);

  if (progressBadge) progressBadge.textContent = `${completed}/${total} completed (${pct}%)`;
  if (progressBar) progressBar.style.width = `${pct}%`;

  tbody.innerHTML = launch30PlanState.map(item => `
    <tr class="hover:bg-[#13131A] transition border-b border-[#2A2A3A] ${item.completed ? 'bg-[#13131A]/50' : ''}">
      <td class="py-3.5 px-4 w-12 text-center">
        <input 
          type="checkbox" 
          ${item.completed ? 'checked' : ''} 
          onchange="toggleLaunch30Item('${item.id}')" 
          class="w-4 h-4 rounded bg-[#0A0A0F] border-[#2A2A3A] text-[#6C63FF] focus:ring-[#6C63FF] cursor-pointer" 
        />
      </td>
      <td class="py-3.5 px-4 font-mono text-xs font-bold text-[#00D4AA] whitespace-nowrap">
        ${item.day}
      </td>
      <td class="py-3.5 px-4">
        <div class="font-bold text-xs text-white font-heading ${item.completed ? 'line-through text-[#8888A8]' : ''}">${item.title}</div>
        <p class="text-[11px] text-[#8888A8] mt-0.5 leading-relaxed">${item.desc}</p>
      </td>
      <td class="py-3.5 px-4 text-right whitespace-nowrap">
        <span class="text-[10px] font-mono px-2 py-0.5 rounded ${
          item.completed 
            ? 'bg-[#00D4AA]/10 text-[#00D4AA] border border-[#00D4AA]/30' 
            : 'bg-[#13131A] text-[#8888A8] border border-[#2A2A3A]'
        }">
          ${item.completed ? 'Completed ✓' : 'Pending'}
        </span>
      </td>
    </tr>
  `).join('');
}

function toggleLaunch30Item(itemId) {
  AudioFX.playClick();
  const item = launch30PlanState.find(i => i.id === itemId);
  if (item) {
    item.completed = !item.completed;
    saveToStorage(STORAGE_KEYS.LI_LAUNCH30, launch30PlanState);
    renderLaunch30Plan();
    if (item.completed) {
      AudioFX.playSuccess();
      showToast(`Completed: ${item.day} — ${item.title}`);
      const allDone = launch30PlanState.every(i => i.completed);
      if (allDone && window.confetti) {
        confetti({ particleCount: 80, spread: 70, origin: { y: 0.6 } });
      }
    }
  }
}

function resetLaunch30Plan() {
  AudioFX.playClick();
  launch30PlanState = DEFAULT_LAUNCH_30_PLAN.map(i => ({ ...i, completed: false }));
  saveToStorage(STORAGE_KEYS.LI_LAUNCH30, launch30PlanState);
  renderLaunch30Plan();
  showToast('30-Day Launch Plan reset.');
}

// TAB 2: Profile Checklist
const DEFAULT_PROFILE_CHECKLIST = [
  {
    category: 'PROFILE PHOTO & BANNER',
    icon: 'camera',
    items: [
      { id: 'pc-1', title: 'Profile Photo', desc: 'Professional headshot, clear face, neutral/solid background. No group photos, no filters, no sunglasses. Slight smile. Shoulders visible.', completed: false },
      { id: 'pc-2', title: 'Banner Image', desc: 'Custom banner showing either: (a) your tech stack / architecture diagram, (b) a headline-reinforcing tagline, or (c) your personal brand colors with your value proposition text overlay.', completed: false },
      { id: 'pc-3', title: 'Photo Ring', desc: 'Turn OFF "Open to Work" green ring. It signals desperation to hiring managers. Instead, signal availability through your content and outreach.', completed: false }
    ]
  },
  {
    category: 'CORE PROFILE SECTIONS',
    icon: 'user-check',
    items: [
      { id: 'pc-4', title: 'Headline', desc: 'Use one of the 16 headline formulas from Section 1. Must contain: outcome + audience + proof metric. No buzzwords.', completed: false },
      { id: 'pc-5', title: 'About Section', desc: 'Follow the 5-Block Framework from Section 2. Must include: contrarian hook, specific proof, method/thinking, stack, CTA. 150–250 words max.', completed: false },
      { id: 'pc-6', title: 'Location', desc: 'Set to your target job market, not your current city (if different). Recruiters filter by location.', completed: false },
      { id: 'pc-7', title: 'Industry', desc: "Set to the industry you're targeting, not \"Computer Software\" generically.", completed: false },
      { id: 'pc-8', title: 'Custom URL', desc: 'Claim linkedin.com/in/yourname. Remove random numbers. This appears in search results and email signatures.', completed: false }
    ]
  },
  {
    category: 'EXPERIENCE SECTION',
    icon: 'briefcase',
    items: [
      { id: 'pc-9', title: 'Titles', desc: 'Use industry-standard titles even for side projects. "ML Engineer (Independent)" > "Freelancer." "Founder, [Project Name]" > "Self-employed."', completed: false },
      { id: 'pc-10', title: 'Descriptions', desc: 'Every role must answer: What system did you own? What was the scale? What was the business outcome? What decisions did you make and why?', completed: false },
      { id: 'pc-11', title: 'Metrics', desc: 'Include at least 2 quantifiable results per role: cost saved, latency reduced, requests served, uptime achieved, accuracy improved.', completed: false },
      { id: 'pc-12', title: 'Side Projects', desc: "List production deployments as experience entries with proper descriptions, not just in a \"Projects\" section. If it serves traffic, it's real work.", completed: false }
    ]
  },
  {
    category: 'FEATURED SECTION',
    icon: 'sparkles',
    items: [
      { id: 'pc-13', title: 'Slot 1', desc: 'Your best case study or portfolio piece with metrics. Link to deployed system, GitHub repo, or detailed write-up.', completed: false },
      { id: 'pc-14', title: 'Slot 2', desc: 'Your highest-engagement LinkedIn post (proves you can communicate and that others find your thinking valuable).', completed: false },
      { id: 'pc-15', title: 'Slot 3', desc: 'An architecture diagram or cost analysis (visual proof of system-level thinking). Could be a blog post or a PDF.', completed: false },
      { id: 'pc-16', title: 'Ordering', desc: 'Most impressive item first. Hiring managers typically only click the first 1–2 items. Make them count.', completed: false }
    ]
  },
  {
    category: 'SKILLS, ENDORSEMENTS & RECOMMENDATIONS',
    icon: 'award',
    items: [
      { id: 'pc-17', title: 'Top 3 Skills', desc: 'Pin the 3 skills most relevant to your target role. These appear first and signal your positioning.', completed: false },
      { id: 'pc-18', title: 'Endorsements', desc: 'Ask 5–10 colleagues/peers to endorse your pinned skills. Quantity matters for search ranking.', completed: false },
      { id: 'pc-19', title: 'Recommendations', desc: 'Request 2–3 recommendations from people who can speak to your production work, problem-solving, or technical leadership. Provide them talking points so they mention specific outcomes.', completed: false }
    ]
  },
  {
    category: 'ACTIVITY & CONTENT SETTINGS',
    icon: 'activity',
    items: [
      { id: 'pc-20', title: 'Creator Mode', desc: 'Turn ON. Unlocks Featured section, Follow button, and LinkedIn Live. Shows your content prominently.', completed: false },
      { id: 'pc-21', title: 'Post Frequency', desc: 'Minimum 2x/week. Content should demonstrate thinking, not just activity.', completed: false },
      { id: 'pc-22', title: 'Engagement', desc: 'Comment on 10+ posts daily. Add value, not "Great post!". Ask questions, share related experiences, offer contrarian viewpoints.', completed: false },
      { id: 'pc-23', title: 'Hashtags', desc: 'Follow and use 3–5 niche hashtags your target audience follows. Not #AI or #MachineLearning (too broad). Try #MLOps, #MLEngineering, #AIArchitecture.', completed: false }
    ]
  }
];

let profileChecklistState = loadFromStorage(STORAGE_KEYS.LI_CHECKLIST, DEFAULT_PROFILE_CHECKLIST);

function renderProfileChecklist() {
  const container = document.getElementById('profile-checklist-container');
  const badge = document.getElementById('profile-checklist-progress-badge');
  const bar = document.getElementById('profile-checklist-progress-bar');
  if (!container) return;

  let totalItems = 0;
  let completedItems = 0;

  profileChecklistState.forEach(cat => {
    totalItems += cat.items.length;
    completedItems += cat.items.filter(i => i.completed).length;
  });

  const pct = Math.round((completedItems / totalItems) * 100);
  if (badge) badge.textContent = `${completedItems}/${totalItems} completed (${pct}%)`;
  if (bar) bar.style.width = `${pct}%`;

  container.innerHTML = profileChecklistState.map(cat => {
    const catTotal = cat.items.length;
    const catCompleted = cat.items.filter(i => i.completed).length;
    const catDone = catTotal === catCompleted;

    return `
      <div class="p-5 rounded-xl bg-[#13131A] border ${catDone ? 'border-[#00D4AA]/40' : 'border-[#2A2A3A]'} space-y-3.5">
        <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
          <div class="flex items-center gap-2">
            <i data-lucide="${cat.icon || 'check-circle'}" class="w-4 h-4 text-[#6C63FF]"></i>
            <h4 class="text-xs font-bold font-mono uppercase tracking-wider text-white font-heading">${cat.category}</h4>
          </div>
          <span class="text-[11px] font-mono px-2 py-0.5 rounded ${
            catDone ? 'bg-[#00D4AA]/20 text-[#00D4AA] font-bold' : 'bg-[#0A0A0F] text-[#8888A8] border border-[#2A2A3A]'
          }">
            ${catCompleted}/${catTotal}
          </span>
        </div>

        <div class="space-y-2">
          ${cat.items.map(item => `
            <label class="flex items-start gap-2.5 p-2.5 rounded-lg border cursor-pointer transition ${
              item.completed 
                ? 'bg-[#1C1C27] border-[#00D4AA]/30' 
                : 'bg-[#0A0A0F] border-[#2A2A3A] hover:border-[#6C63FF]/50'
            }">
              <input 
                type="checkbox" 
                ${item.completed ? 'checked' : ''} 
                onchange="toggleProfileChecklistItem('${item.id}')" 
                class="mt-0.5 w-3.5 h-3.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-[#6C63FF] focus:ring-[#6C63FF] cursor-pointer" 
              />
              <div class="flex-1">
                <div class="text-xs font-bold text-white font-heading ${item.completed ? 'line-through text-[#8888A8]' : ''}">${item.title}:</div>
                <p class="text-[11px] text-[#8888A8] mt-0.5 leading-relaxed">${item.desc}</p>
              </div>
            </label>
          `).join('')}
        </div>
      </div>
    `;
  }).join('');

  if (window.lucide) lucide.createIcons({ root: container });
}

function toggleProfileChecklistItem(itemId) {
  AudioFX.playClick();
  for (const cat of profileChecklistState) {
    const item = cat.items.find(i => i.id === itemId);
    if (item) {
      item.completed = !item.completed;
      break;
    }
  }
  saveToStorage(STORAGE_KEYS.LI_CHECKLIST, profileChecklistState);
  renderProfileChecklist();

  let totalItems = 0;
  let completedItems = 0;
  profileChecklistState.forEach(cat => {
    totalItems += cat.items.length;
    completedItems += cat.items.filter(i => i.completed).length;
  });

  if (completedItems === totalItems && window.confetti) {
    confetti({ particleCount: 100, spread: 80, origin: { y: 0.6 } });
    AudioFX.playSuccess();
    showToast('🏆 Full Profile Optimization Checklist Completed!');
  } else {
    AudioFX.playSuccess();
  }
}

function resetProfileChecklist() {
  AudioFX.playClick();
  profileChecklistState = DEFAULT_PROFILE_CHECKLIST.map(cat => ({
    ...cat,
    items: cat.items.map(item => ({ ...item, completed: false }))
  }));
  saveToStorage(STORAGE_KEYS.LI_CHECKLIST, profileChecklistState);
  renderProfileChecklist();
  showToast('Profile Checklist reset.');
}

// ==========================================
// SECTION 9: OUTREACH CRM & KANBAN
// ==========================================
function loadOutreachTemplate(phaseNum) {
  AudioFX.playClick();
  for (let i = 1; i <= 3; i++) {
    const btn = document.getElementById(`outreach-btn-${i}`);
    if (btn) {
      if (i === phaseNum) {
        btn.classList.add('border-[#00D4AA]', 'bg-[#1C1C27]');
        btn.classList.remove('border-[#2A2A3A]');
      } else {
        btn.classList.remove('border-[#00D4AA]', 'bg-[#1C1C27]');
        btn.classList.add('border-[#2A2A3A]');
      }
    }
  }
  const el = document.getElementById('outreach-template-text');
  if (el) el.value = OUTREACH_TEMPLATES[phaseNum];
}

function copyOutreachTemplate() {
  AudioFX.playClick();
  const text = document.getElementById('outreach-template-text')?.value || '';
  navigator.clipboard.writeText(text);
  showToast('Copied cold message template!');
}

function renderKanban() {
  const stages = ['target', 'sent', 'conversation', 'interview', 'offer'];
  
  stages.forEach(stage => {
    const container = document.getElementById(`col-${stage}-container`);
    const countBadge = document.getElementById(`col-count-${stage}`);
    if (!container) return;

    const leads = appState.kanban.filter(l => l.stage === stage);
    if (countBadge) countBadge.textContent = leads.length;

    container.innerHTML = leads.map(lead => `
      <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] hover:border-[#6C63FF]/40 space-y-2.5 transition">
        <div class="flex items-start justify-between gap-2">
          <div>
            <h5 class="text-xs font-bold text-white font-heading">${lead.name}</h5>
            <p class="text-[11px] text-[#8888A8]">${lead.founder || 'Decision Maker'}</p>
          </div>
          <button onclick="deleteLead('${lead.id}')" title="Delete" class="text-[#8888A8] hover:text-rose-400 transition">
            <i data-lucide="trash" class="w-3.5 h-3.5"></i>
          </button>
        </div>

        ${lead.notes ? `<p class="text-[11px] text-slate-300 line-clamp-2 bg-[#13131A] p-2 rounded border border-[#2A2A3A]">${lead.notes}</p>` : ''}

        <div class="flex items-center justify-between pt-1 border-t border-[#2A2A3A] text-[10px]">
          <div class="flex gap-2">
            ${lead.linkedin ? `<a href="${lead.linkedin}" target="_blank" class="text-blue-400 hover:underline"><i data-lucide="linkedin" class="w-3.5 h-3.5 inline"></i></a>` : ''}
            ${lead.website ? `<a href="${lead.website}" target="_blank" class="text-[#8888A8] hover:text-white"><i data-lucide="globe" class="w-3.5 h-3.5 inline"></i></a>` : ''}
          </div>
          <select onchange="moveLeadStage('${lead.id}', this.value)" class="bg-[#13131A] border border-[#2A2A3A] text-slate-300 rounded px-1.5 py-0.5 text-[10px] focus:outline-none">
            <option value="target" ${lead.stage === 'target' ? 'selected' : ''}>1. Target</option>
            <option value="sent" ${lead.stage === 'sent' ? 'selected' : ''}>2. Sent</option>
            <option value="conversation" ${lead.stage === 'conversation' ? 'selected' : ''}>3. In Talk</option>
            <option value="interview" ${lead.stage === 'interview' ? 'selected' : ''}>4. Trial</option>
            <option value="offer" ${lead.stage === 'offer' ? 'selected' : ''}>5. Offer 🏆</option>
          </select>
        </div>
      </div>
    `).join('');
  });

  if (window.lucide) lucide.createIcons({ root: document.getElementById('kanban-board') });
}

function moveLeadStage(leadId, newStage) {
  AudioFX.playClick();
  const lead = appState.kanban.find(l => l.id === leadId);
  if (lead) {
    lead.stage = newStage;
    saveToStorage(STORAGE_KEYS.KANBAN, appState.kanban);
    renderKanban();
    showToast(`Moved ${lead.name} to ${newStage.toUpperCase()}`);
    if (newStage === 'offer' && window.confetti) {
      confetti({ particleCount: 80, spread: 70 });
      AudioFX.playSuccess();
    }
  }
}

function deleteLead(leadId) {
  AudioFX.playClick();
  appState.kanban = appState.kanban.filter(l => l.id !== leadId);
  saveToStorage(STORAGE_KEYS.KANBAN, appState.kanban);
  renderKanban();
  showToast('Lead deleted from CRM.');
}

function openAddLeadModal() {
  AudioFX.playClick();
  document.getElementById('add-lead-modal')?.classList.remove('hidden');
}

function saveNewLead() {
  const name = document.getElementById('lead-name-input')?.value.trim();
  if (!name) {
    showToast('Please enter a company name.', 'error');
    return;
  }

  const founder = document.getElementById('lead-founder-input')?.value.trim() || '';
  const stage = document.getElementById('lead-stage-input')?.value || 'target';
  const linkedin = document.getElementById('lead-linkedin-input')?.value.trim() || '';
  const website = document.getElementById('lead-website-input')?.value.trim() || '';
  const notes = document.getElementById('lead-notes-input')?.value.trim() || '';

  const newLead = {
    id: `lead-user-${Date.now()}`,
    name,
    founder,
    stage,
    linkedin,
    website,
    notes,
    followUp: new Date().toISOString().slice(0, 10)
  };

  appState.kanban.unshift(newLead);
  saveToStorage(STORAGE_KEYS.KANBAN, appState.kanban);
  renderKanban();
  closeModal('add-lead-modal');
  showToast(`Added ${name} to CRM pipeline!`);
  AudioFX.playSuccess();

  // Reset inputs
  document.getElementById('lead-name-input').value = '';
  document.getElementById('lead-founder-input').value = '';
  document.getElementById('lead-linkedin-input').value = '';
  document.getElementById('lead-website-input').value = '';
  document.getElementById('lead-notes-input').value = '';
}

// 300+ Preloaded Leads Database Modal
function openLeadDatabaseModal() {
  AudioFX.playClick();
  document.getElementById('lead-database-modal')?.classList.remove('hidden');
  renderPreloadedLeadsTable();
}

function renderPreloadedLeadsTable(query = '') {
  const tbody = document.getElementById('preloaded-leads-tbody');
  const countBadge = document.getElementById('leads-count-filtered');
  if (!tbody || typeof PRELOADED_LEADS === 'undefined') return;

  const q = query.toLowerCase().trim();
  const filtered = PRELOADED_LEADS.filter(lead => {
    if (!q) return true;
    const text = (lead.name + ' ' + lead.description + ' ' + lead.location + ' ' + lead.categories.join(' ')).toLowerCase();
    return text.includes(q);
  });

  if (countBadge) countBadge.textContent = filtered.length;

  tbody.innerHTML = filtered.slice(0, 50).map(lead => `
    <tr class="hover:bg-[#13131A] transition border-b border-[#2A2A3A]">
      <td class="py-3 px-4">
        <div class="font-bold text-white font-heading">${lead.name}</div>
        <div class="text-[11px] text-[#8888A8] line-clamp-1 max-w-xs">${lead.description}</div>
      </td>
      <td class="py-3 px-4">
        <div class="flex flex-wrap gap-1">
          ${lead.categories.map(c => `<span class="px-1.5 py-0.2 rounded bg-[#0A0A0F] text-[10px] text-slate-300 border border-[#2A2A3A]">${c}</span>`).join('')}
        </div>
      </td>
      <td class="py-3 px-4 text-[11px] text-[#8888A8]">${lead.location}</td>
      <td class="py-3 px-4 font-mono text-[11px] text-[#00D4AA] font-semibold">${lead.funding}</td>
      <td class="py-3 px-4 text-right">
        <button onclick="importLeadToCRM('${lead.id}')" class="px-2.5 py-1 rounded-lg bg-[#6C63FF] hover:bg-indigo-500 text-white font-bold text-[11px] flex items-center gap-1 ml-auto transition">
          <i data-lucide="plus" class="w-3 h-3"></i> Add
        </button>
      </td>
    </tr>
  `).join('');

  if (window.lucide) lucide.createIcons({ root: tbody });
}

function filterPreloadedLeads(query) {
  renderPreloadedLeadsTable(query);
}

function importLeadToCRM(leadId) {
  AudioFX.playClick();
  const lead = PRELOADED_LEADS.find(l => l.id === leadId);
  if (!lead) return;

  const exists = appState.kanban.some(k => k.name.toLowerCase() === lead.name.toLowerCase());
  if (exists) {
    showToast(`${lead.name} is already in your CRM!`, 'info');
    return;
  }

  const newKanbanLead = {
    id: `kanban-${Date.now()}`,
    name: lead.name,
    founder: lead.founders || 'Founder / CTO',
    stage: 'target',
    linkedin: lead.linkedin || '',
    website: lead.website || '',
    notes: `${lead.description} • Categories: ${lead.categories.join(', ')}`,
    followUp: new Date().toISOString().slice(0, 10)
  };

  appState.kanban.unshift(newKanbanLead);
  saveToStorage(STORAGE_KEYS.KANBAN, appState.kanban);
  renderKanban();
  showToast(`Imported ${lead.name} into Target Startup stage!`);
  AudioFX.playSuccess();
}

function adjustDailyCount(delta) {
  AudioFX.playClick();
  appState.daily.count = Math.max(0, appState.daily.count + delta);
  saveToStorage(STORAGE_KEYS.DAILY, appState.daily);
  updateDailyDisplay();

  if (appState.daily.count === 25 && window.confetti) {
    confetti({ particleCount: 75, spread: 70 });
    AudioFX.playSuccess();
    showToast("🎉 Daily Goal of 25 Outreach DMs Achieved!");
  }
}

function updateDailyDisplay() {
  const count = appState.daily.count;
  const pct = Math.min(100, Math.round((count / 25) * 100));
  const disp = document.getElementById('daily-count-display');
  const bar = document.getElementById('daily-goal-bar');
  const badge = document.getElementById('daily-streak-badge');
  if (disp) disp.textContent = count;
  if (bar) bar.style.width = `${pct}%`;
  if (badge) badge.textContent = `${count} / 25 Today`;
}

function filterBySector(sector) {
  AudioFX.playClick();
  const searchInput = document.getElementById('lead-search-input');
  if (searchInput) {
    searchInput.value = sector;
    filterPreloadedLeads(sector);
  }

  const pills = document.querySelectorAll('.sector-pill');
  pills.forEach(p => {
    p.classList.remove('bg-[#6C63FF]', 'text-white', 'font-bold');
    p.classList.add('bg-[#13131A]', 'text-[#8888A8]');
  });

  const activeId = sector === '' ? 'sec-pill-all' : 
                   sector === 'AI' ? 'sec-pill-ai' :
                   sector === 'Software' ? 'sec-pill-saas' :
                   sector === 'Health' ? 'sec-pill-health' :
                   sector === 'Financial' ? 'sec-pill-fintech' :
                   sector === 'Vancouver' ? 'sec-pill-van' :
                   sector === 'Toronto' ? 'sec-pill-tor' : 'sec-pill-mtl';
                   
  const activePill = document.getElementById(activeId);
  if (activePill) {
    activePill.classList.remove('bg-[#13131A]', 'text-[#8888A8]');
    activePill.classList.add('bg-[#6C63FF]', 'text-white', 'font-bold');
  }
}

// ==========================================
// SECTION 10: JOB SEARCH ENGINE TABS & UTILS
// ==========================================
function switchPlatformTab(tabId) {
  AudioFX.playClick();
  const tabs = ['startups', 'remote', 'freelance', 'india'];
  tabs.forEach(t => {
    const btn = document.getElementById(`platform-tab-${t}`);
    const content = document.getElementById(`platform-content-${t}`);
    if (btn && content) {
      if (t === tabId) {
        btn.classList.add('bg-[#6C63FF]', 'text-white', 'font-semibold');
        btn.classList.remove('text-[#8888A8]', 'hover:text-white');
        content.classList.remove('hidden');
      } else {
        btn.classList.remove('bg-[#6C63FF]', 'text-white', 'font-semibold');
        btn.classList.add('text-[#8888A8]', 'hover:text-white');
        content.classList.add('hidden');
      }
    }
  });
}

function switchInterviewTab(tabId) {
  AudioFX.playClick();
  const tabs = ['python', 'sql', 'ml', 'llm', 'agents'];
  tabs.forEach(t => {
    const btn = document.getElementById(`interview-tab-${t}`);
    const content = document.getElementById(`interview-content-${t}`);
    if (btn && content) {
      if (t === tabId) {
        btn.classList.add('bg-[#6C63FF]', 'text-white', 'font-semibold');
        btn.classList.remove('text-[#8888A8]', 'hover:text-white');
        content.classList.remove('hidden');
      } else {
        btn.classList.remove('bg-[#6C63FF]', 'text-white', 'font-semibold');
        btn.classList.add('text-[#8888A8]', 'hover:text-white');
        content.classList.add('hidden');
      }
    }
  });
}

function copySearchString(text) {
  AudioFX.playClick();
  navigator.clipboard.writeText(text);
  showToast('Copied search string to clipboard!');
}

function copyTemplateMessage(templateId) {
  AudioFX.playClick();
  const el = document.getElementById(templateId);
  if (el) {
    navigator.clipboard.writeText(el.innerText || el.value);
    showToast('Template copied to clipboard!');
  }
}

// ==========================================
// SECTION 13: FINAL CHECKLIST (NEW)
// ==========================================
const DEFAULT_FINAL_CHECKLIST = [
  { id: 'fc-1', text: 'One-page resume', completed: false },
  { id: 'fc-2', text: 'Updated LinkedIn profile', completed: false },
  { id: 'fc-3', text: 'Three strong GitHub projects', completed: false },
  { id: 'fc-4', text: 'At least one live AI application', completed: false },
  { id: 'fc-5', text: 'Architecture diagrams', completed: false },
  { id: 'fc-6', text: 'Evaluation results', completed: false },
  { id: 'fc-7', text: 'Project walkthrough videos', completed: false },
  { id: 'fc-8', text: 'Five target job titles', completed: false },
  { id: 'fc-9', text: 'Five to eight selected job portals', completed: false },
  { id: 'fc-10', text: 'Application tracker', completed: false },
  { id: 'fc-11', text: 'Prepared outreach message', completed: false },
  { id: 'fc-12', text: 'Interview revision plan', completed: false }
];

let finalChecklistState = loadFromStorage(STORAGE_KEYS.FINAL_CHECKLIST, DEFAULT_FINAL_CHECKLIST);

function renderFinalChecklist() {
  const container = document.getElementById('final-checklist-items-container');
  const badge = document.getElementById('final-checklist-progress-badge');
  const bar = document.getElementById('final-checklist-progress-bar');
  if (!container) return;

  const total = finalChecklistState.length;
  const done = finalChecklistState.filter(i => i.completed).length;
  const pct = Math.round((done / total) * 100);

  if (badge) badge.textContent = `${done}/${total} complete (${pct}%)`;
  if (bar) bar.style.width = `${pct}%`;

  container.innerHTML = finalChecklistState.map(item => `
    <label class="flex items-start gap-3 p-3.5 rounded-xl bg-[#13131A] border ${item.completed ? 'border-[#00D4AA]/40 bg-[#1C1C27]' : 'border-[#2A2A3A]'} cursor-pointer hover:border-[#6C63FF]/50 transition">
      <input 
        type="checkbox" 
        ${item.completed ? 'checked' : ''} 
        onchange="toggleFinalChecklistItem('${item.id}')"
        class="mt-0.5 w-4 h-4 rounded bg-[#0A0A0F] border-[#2A2A3A] text-[#6C63FF] focus:ring-[#6C63FF] cursor-pointer"
      />
      <span class="text-xs font-medium font-heading ${item.completed ? 'line-through text-[#8888A8]' : 'text-slate-200'}">${item.text}</span>
    </label>
  `).join('');
}

function toggleFinalChecklistItem(itemId) {
  AudioFX.playClick();
  const item = finalChecklistState.find(i => i.id === itemId);
  if (item) {
    item.completed = !item.completed;
    saveToStorage(STORAGE_KEYS.FINAL_CHECKLIST, finalChecklistState);
    renderFinalChecklist();
    if (item.completed) {
      AudioFX.playSuccess();
      showToast(`Checked: ${item.text}`);
      const allDone = finalChecklistState.every(i => i.completed);
      if (allDone && window.confetti) {
        confetti({ particleCount: 100, spread: 80, origin: { y: 0.6 } });
        showToast('🏆 100% Job Ready! Congratulations!');
      }
    }
  }
}

function resetFinalChecklist() {
  AudioFX.playClick();
  finalChecklistState = DEFAULT_FINAL_CHECKLIST.map(i => ({ ...i, completed: false }));
  saveToStorage(STORAGE_KEYS.FINAL_CHECKLIST, finalChecklistState);
  renderFinalChecklist();
  showToast('Final Checklist reset.');
}

// Global Audio & Backup Handlers
function toggleAudio() {
  appState.sound = !appState.sound;
  saveToStorage(STORAGE_KEYS.AUDIO, appState.sound);
  updateAudioIcon();
  if (appState.sound) {
    AudioFX.playClick();
    showToast('Sound effects enabled');
  } else {
    showToast('Sound effects muted');
  }
}

function updateAudioIcon() {
  const icon = document.getElementById('audio-icon');
  if (icon) {
    icon.setAttribute('data-lucide', appState.sound ? 'volume-2' : 'volume-x');
    if (window.lucide) lucide.createIcons({ root: document.getElementById('audio-toggle-btn') });
  }
}

function openBackupModal() {
  AudioFX.playClick();
  document.getElementById('backup-modal')?.classList.remove('hidden');
}

function exportUserDataJSON() {
  AudioFX.playClick();
  const data = {
    exportedAt: new Date().toISOString(),
    roadmap: appState.roadmap,
    roadmap90: roadmap90State,
    audit: appState.audit,
    kanban: appState.kanban,
    daily: appState.daily,
    liChecklist: profileChecklistState,
    liLaunch30: launch30PlanState,
    finalChecklist: finalChecklistState
  };
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `naraitos_playbook_backup_${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  URL.revokeObjectURL(url);
  showToast('Backup JSON exported successfully!');
}

function importUserDataJSON(event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = (e) => {
    try {
      const data = JSON.parse(e.target.result);
      if (data.roadmap) appState.roadmap = data.roadmap;
      if (data.roadmap90) roadmap90State = data.roadmap90;
      if (data.audit) appState.audit = data.audit;
      if (data.kanban) appState.kanban = data.kanban;
      if (data.daily) appState.daily = data.daily;
      if (data.liChecklist) profileChecklistState = data.liChecklist;
      if (data.liLaunch30) launch30PlanState = data.liLaunch30;
      if (data.finalChecklist) finalChecklistState = data.finalChecklist;

      saveToStorage(STORAGE_KEYS.ROADMAP, appState.roadmap);
      saveToStorage(STORAGE_KEYS.ROADMAP_90, roadmap90State);
      saveToStorage(STORAGE_KEYS.AUDIT, appState.audit);
      saveToStorage(STORAGE_KEYS.KANBAN, appState.kanban);
      saveToStorage(STORAGE_KEYS.DAILY, appState.daily);
      saveToStorage(STORAGE_KEYS.LI_CHECKLIST, profileChecklistState);
      saveToStorage(STORAGE_KEYS.LI_LAUNCH30, launch30PlanState);
      saveToStorage(STORAGE_KEYS.FINAL_CHECKLIST, finalChecklistState);

      render90DayRoadmap();
      renderAuditQuestions();
      renderRoadmap();
      renderProfileChecklist();
      renderLaunch30Plan();
      renderFinalChecklist();
      renderKanban();
      updateRoadmapProgress();
      updateDailyDisplay();
      closeModal('backup-modal');
      showToast('Data imported successfully!');
      AudioFX.playSuccess();
    } catch (err) {
      showToast('Invalid backup JSON format.', 'error');
    }
  };
  reader.readAsText(file);
}

function resetAllData() {
  if (confirm("Are you sure you want to reset all checklist progress and CRM data to default?")) {
    localStorage.clear();
    location.reload();
  }
}

function closeModal(modalId) {
  AudioFX.playClick();
  document.getElementById(modalId)?.classList.add('hidden');
}

function updateTodaysFocus() {
  const focusEl = document.getElementById('todays-focus-task');
  if (!focusEl) return;
  // Find first incomplete task across all 4 phases of the execution roadmap
  let found = null;
  for (let p = 1; p <= 4; p++) {
    const tasks = appState.roadmap['phase' + p] || [];
    found = tasks.find(t => !t.completed);
    if (found) break;
  }
  if (found) {
    focusEl.textContent = 'Phase task: ' + found.title;
  } else {
    // Check 90-day roadmap
    let foundNR = null;
    for (const pKey of ['phase1', 'phase2', 'phase3']) {
      const items = roadmap90State[pKey] || [];
      foundNR = items.find(i => !i.completed);
      if (foundNR) break;
    }
    if (foundNR) {
      focusEl.textContent = '90-Day milestone: ' + foundNR.text;
    } else {
      focusEl.textContent = '🏆 All milestones completed! You are job-ready.';
    }
  }
}

function scrollToSection(sectionId) {
  AudioFX.playClick();
  const sec = document.getElementById(sectionId);
  if (sec) sec.scrollIntoView({ behavior: 'smooth' });
}

document.getElementById('mobile-menu-btn')?.addEventListener('click', () => {
  const nav = document.getElementById('mobile-pill-nav');
  if (nav) nav.classList.toggle('hidden');
});
'''

with open(r'D:\us-remote-engineering-playbook\app.js', 'w', encoding='utf-8') as f:
    f.write(app_js_code)

print("Generated updated app.js successfully!")
