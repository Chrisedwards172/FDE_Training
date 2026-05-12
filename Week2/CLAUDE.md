# CLAUDE.md — Week 2: Cognitive Work Assessment & Agent Design

> **Inherits:** [`../CLAUDE.md`](../CLAUDE.md) (root project constitution). Load both files when executing any prompt from `Week2/Prompts/`.

## Week 2 Context

Week 2 takes the specification skill from Week 1 and turns it outward: **given a real business process with people doing messy, inconsistent, partially-documented work, can you figure out what the agents should actually do?**

Week 2 introduces **ATX — Agentic Transformation** — the methodology for decomposing cognitive work, scoring delegation suitability, and designing agents that fit real business reality. There is no lecture on ATX — you read the reference pack, apply the methodology under time pressure, and use AI to accelerate every phase.

- **FDE Level targeted:** Level 1 → Level 2 transition (single capability → multi-capability thinking)
- **Key methodology:** ATX (Agentic Transformation) — cognitive load mapping, delegation suitability scoring, agent purpose documents
- **Gate 2:** 3-hour timed exercise on a previously unseen scenario, followed by a ~10-minute live clarification round where a coach plays the Main Stakeholder

## Week 2 Directory Structure

```
Week2/
├── CLAUDE.md                          ← this file
├── SupportingDocs/                    ← Week 2 reference material
│   ├── README-Participants-Week2.md   ← week guide, calendar, deliverables, evaluation
│   ├── discovery-questioning-patterns.md  ← discovery questioning methodology
│   ├── enriched_scenarios.md          ← practice scenarios for the week
│   ├── spec-ambiguity-vs-builder-mistakes.md  ← build-loop diagnostic taxonomy (carried forward)
│   └── references/                    ← ATX framework reference documents
│       ├── atx-concepts.md            ← three production factors, lived vs documented work
│       ├── atx-assessment.md          ← four-phase ATX assessment methodology
│       ├── atx-agent-mapping.md       ← mapping cognitive work to agent designs
│       ├── atx-scoring.md             ← volume × value, delegation suitability scoring
│       └── atx-economics.md           ← economics of digital labour (used more in Week 4)
```

> Note: `Week2/Prompts/` and `Week2/Output/` folders will appear as the participant begins producing artefacts. `Week2/Gate2/` will be populated during the gate exercise.

## Standing Sources

When executing any prompt from `Week2/Prompts/` (or `Week2/Gate2/Prompts/` if created), load **all** of the following in addition to the root `../CLAUDE.md`:

| # | Source | Path (relative to `Week2/`) | Purpose |
|---|---|---|---|
| 1 | Thinking Discipline Primer | `../Week1/SupportingDocs/Week1-Thinking-Discipline-Primer.md` | Reasoning-discipline constitution. **Not a Week-1-only artefact** — applies every week. Frame claims as Assumption → Hypothesis → Test → Confidence. |
| 2 | Participant README (Week 2) | `./SupportingDocs/README-Participants-Week2.md` | Week 2 deliverables, calendar, evaluation criteria, what coaches are looking for |
| 3 | ATX Concepts | `./SupportingDocs/references/atx-concepts.md` | Three production factors, lived vs documented work, compounding thesis |
| 4 | ATX Assessment | `./SupportingDocs/references/atx-assessment.md` | Four-phase ATX assessment methodology |
| 5 | ATX Agent Mapping | `./SupportingDocs/references/atx-agent-mapping.md` | Mapping cognitive work to agent designs |
| 6 | ATX Scoring | `./SupportingDocs/references/atx-scoring.md` | Volume × value analysis, delegation suitability scoring |
| 7 | ATX Economics | `./SupportingDocs/references/atx-economics.md` | Economics of digital labour |
| 8 | Discovery Questioning Patterns | `./SupportingDocs/discovery-questioning-patterns.md` | Discovery questioning methodology for live clarification rounds |
| 9 | Build-Loop Diagnostic Taxonomy | `./SupportingDocs/spec-ambiguity-vs-builder-mistakes.md` | Carried forward from Week 1 — still applies to build loops |
| 10 | FDE Role Definition | `../Week1/SupportingDocs/the-fde.md` | Role framing and level definitions. **Canonical; never modified.** |
| 11 | Production Spec Checklist | `../Week1/SupportingDocs/production-spec-checklist.md` | Buildability bar — still applies to agent purpose documents |
| 12 | Scenario file | `./SupportingDocs/enriched_scenarios.md` (practice) or gate scenario (released at gate start) | Scenario text and participant HUMAN assumptions |

## Active Scenario (Gate 2)

**Scenario file:** `./Gate2/Gate2-Participant-Pack.md` — Apex Distribution Ltd, Customer Operations transformation.

**Sample artefacts:** `./Gate2/Artefacts/` — 7 CSV batch exports from the Aurum Billing legacy system plus a README describing schema and cadence.

**In-pack artefacts (§4 of the participant pack):**
1. Driver voicemail (delivery exception — refused delivery, damaged pallet)
2. Email thread (billing dispute — fuel surcharge on damaged consignment, 9-day resolution)
3. SMS exchange (ETA inquiry — lookup + dispatch check)
4. SOP fragment (exception handling v2.3 — stale, references retired DispatchHub)
5. Aurum Billing batch export catalogue + sample CSVs

**The 4 work streams:**
1. Delivery exceptions (~180/day, 12 min/case) — dispatcher judgment-driven
2. ETA inquiries (~400/day, 4 min/case) — mostly lookup, edge cases need driver call
3. Dispatch adjustments (~90/day, 18 min/case) — tight time pressure
4. Billing disputes (~60/day, 28 min/case) — crosses legacy billing system

**Main stakeholder:** Sarah Whitmore, COO. Sceptical of chatbots and consultants; burned by 2 prior automation failures. Open to something that works.

**Key constraints:**
- Aurum Billing: batch-file-only exports (daily CSV, T-1/T-2 lag), no real-time API, 48h turnaround for invoice modifications, schema changes quarterly without notice
- Dispatch console: Java/Citrix, limited API surface
- SOP is stale (references retired DispatchHub, last revised Oct 2023)
- Sandra applied a £170 goodwill credit via manual override with no audit log entry

## Output Placement

| Artefact type | Path |
|---|---|
| Practice artefacts | `Week2/Output/` — filename encodes deliverable + 3-digit run suffix |
| Gate intermediate artefacts | `Week2/Gate2/Output/` |
| Gate final deliverables | `Week2/Gate2/Final/` |

## Week 2 Deliverables (7)

Gate 2 requires **7 deliverables** (up from 5 in Week 1):

| # | Deliverable | What it tests |
|---|---|---|
| 1 | Cognitive Load Map | Decompose ≥ 2 of 4 work streams into JTBDs, micro-tasks, cognitive dimensions; map zones and breakpoints |
| 2 | Delegation Suitability Matrix | Score each task cluster on delegation dimensions; assign archetypes with rationale |
| 3 | Volume × Value Analysis | Plot 4 work streams; identify the primary agentic target and justify why it wins |
| 4 | Agent Purpose Document | Purpose, scope, KPIs, autonomy matrix, escalation triggers, failure modes |
| 5 | System/Data Inventory | What the agent needs to access, what's available, what's missing, what's risky |
| 6 | Discovery Questions for the Main Stakeholder | Questions whose answers would *actually change your design* — not generic discovery |
| 7 | `CLAUDE.md` for the project | Demonstrates workflow discipline |

## Week 2 Key Concepts (ATX)

- **Jobs to be Done (JTBD)** — the unit of cognitive work decomposition
- **Cognitive Zones** — where in the cognitive load spectrum a task falls
- **Breakpoints** — where cognitive load shifts abruptly (zone transitions)
- **Delegation Archetypes:** fully agentic / agent-led with human oversight / human-led with agent support / human-only
- **Delegation Suitability Dimensions** — the scoring axes for whether a task should be delegated
- **Volume × Value** — the prioritisation lens for which work stream to automate first
- **Agent Purpose Document** — the Week 2 equivalent of Week 1's capability spec

## Deliverable Output Rules

When producing any of the 7 deliverables, apply these structural rules automatically — do not wait for a prompt file to specify them.

### All deliverables

- **Assumption Log (split between D4 and D5)**:
  - **Deliverable #4 (Agent Purpose Document)** holds assumptions about the scenario, stakeholder behaviour, design decisions, KPI targets, and delegation boundaries — things you inferred from the brief or decided during design.
  - **Deliverable #5 (System/Data Inventory)** holds assumptions about systems, data, artefacts, and tooling — things you inferred from the sample artefacts or assumed about systems the brief did not detail (per participant pack: "If you need more than what is here, that is an assumption — name it as one in Deliverable 5").
  - All other deliverables reference assumptions by ID (e.g. `[ASSUMED — A3]`) pointing back to the relevant log in D4 or D5. Do not duplicate logs in every file.
- **Source tagging**: every non-trivial claim is tagged `[Artefact N]` (grounded in scenario sample artefacts), `[INFERRED — scenario brief]` (derived from scenario text), or `[ASSUMED — AN]` (referencing the numbered entry in D4 or D5's Assumption Log). No untagged factual claims about how work happens.
- **Lived work over documented process**: if the scenario provides sample artefacts (emails, tracker excerpts, flowchart annotations, call transcripts), ground claims in those — not in SOPs or flowcharts. Name any documented ↔ lived divergences explicitly.

### Deliverable #1 — Cognitive Load Map

Produce in this order:

1. **Lived-Process Narrative** (≥ 2 of 4 work streams) — how work actually happens, cognitive hotspots, documented ↔ lived gaps
2. **Jobs to be Done Decomposition** — each JtD has: ID, Trigger, Actor, Goal/Outcome, Key decisions, Key systems, Expected output, Primary type (Decision-making / Execution / Synthesis / Communication / Exception-handling). JtDs are cognitive contracts, not task lists.
3. **Cognitive Zones and Breakpoints** — micro-tasks grouped into named zones; breakpoints labelled `BP-X.Y: [shift type] — [description]`. Every work stream must have at least one Rule → Judgment breakpoint.
4. **Micro-Task Inventory** — score each micro-task on the 8 ATX dimensions (Cognitive Load, Input Structure, Decision Determinism, Exception Frequency, Turn-Taking Degree, Latency Constraint, Compliance/Risk Sensitivity, Tool/API Availability) as H/M/L. Tool/API Availability is inverted (H = available). Use `?` suffix for uncertain scores with matching assumption.
5. **Process Topology Diagram** (optional — include only if ≥ 3 zones with non-obvious handoffs). Mermaid `flowchart TD`, zones as subgraphs, breakpoints as annotated edges.

Feed-forward: the micro-task inventory is the direct input to Deliverable #2.

### Deliverable #2 — Delegation Suitability Matrix

Takes micro-tasks from Deliverable #1. Score each on the 7 delegation suitability dimensions (Input structure, Decision determinism, Tool coverage, Context complexity, Exception rate, Latency constraint, Risk/compliance). Assign delegation archetype with rationale. Must include at least 2 different archetypes — if everything is "fully agentic", the analysis is incomplete.

### Deliverable #3 — Volume × Value Analysis

Plot all 4 work streams on a 2×2 grid (Y: volume/frequency, X: non-deterministic decision effort). Identify the primary agentic target and justify why it wins over other quadrants.

### Deliverable #4 — Agent Purpose Document

For the highest-value opportunity: Agent Name, Job to be Done, Business context, Primary objectives, KPIs (accuracy, coverage, throughput, cost per case, HITL rate), Failure modes, Delegation archetype + rationale, Escalation triggers, Autonomy matrix (decides alone / acts then notifies / proposes for approval / human takes over).

### Deliverable #5 — System/Data Inventory

Table: System, Data needed, Access type, Availability, Gap/Risk. Address every system named in the scenario. Flag legacy systems, missing APIs, and batch-only exports explicitly — do not hand-wave.

### Deliverable #6 — Discovery Questions

Questions whose answers would *actually change the agent design*. Each question must name the specific design decision it would affect. Generic questions ("tell me about your process") are not acceptable.

### Deliverable #7 — CLAUDE.md for the project

Demonstrates workflow discipline. Encodes scenario context, standing sources, output rules, and agent-specific constraints.

## Week 2 Anti-Patterns

These are the failure modes coaches and peer reviewers watch for:

- **"Everything is fully agentic"** — the dominant Week 2 anti-pattern. If every box in the delegation matrix is agentic, the real thinking hasn't happened. Delegation boundary drift is the #1 signal coaches track.
- **Documented-process-as-lived-work** — mapping the SOP instead of how work actually happens. The cognitive load map must reflect reality, not documentation.
- **Generic discovery questions** — "Walk me through your process" reads as bluffing. Questions must be tied to specific tensions: *"If your standard delivery-exception call takes 4 minutes but your billing dispute takes 25, are those the same job or two jobs?"*
- **Bluffing domain knowledge** — stating client behaviour or system internals as fact when the brief didn't provide it. Marked assumptions with confidence levels are the alternative.
- **Missing the lived-work vs documented-work distinction** — the scenario includes sample artefacts (calls, emails, partial SOPs, system fragments) to ground "lived work" claims. Use them.

## Closed Build Loop (Week 2 variant)

Same principle as Week 1, different artefact — this week you hand the **Agent Purpose Document** to Claude Code:

1. Prompt: *"Begin building the agent described in this document. First, tell me what you can build confidently. Second, what you need to clarify. Third, build the confident parts."*
2. Review: (a) faithful or drifted? (b) questions asked = gaps (c) couldn't build = buildability gaps
3. Diagnose against `spec-ambiguity-vs-builder-mistakes.md` **plus one new Week 2 category: delegation boundary gaps** — where Claude Code can't tell from the document whether a step is fully agentic, agent-led, or human-led
4. Revise — good revisions usually touch the **autonomy matrix** or **escalation triggers**, not just the purpose statement
5. Re-run and verify. **Must be complete by Thursday early afternoon** — the refined artefact feeds the 14:30 peer review session.

## Live Clarification Round (Gate 2)

Unlike Week 1's walkthrough (you present, coach challenges), Week 2's live round is a **simulated stakeholder interview**:

- A coach plays the Main Stakeholder — impatient, sceptical, answers some questions precisely and others vaguely or contradictorily
- You ask focused discovery questions, detect evasion, and adapt
- Generic questions won't land; questions tied to specific tensions in the brief will
- This tests FDE judgment under domain uncertainty — the most direct signal when domain knowledge is shallow

