# Checklist Review — All 7 Deliverables (Scenario 1, Run 001)

> Generated: 29.04.2026 | Reviewed against all 7 checklist files in `Week2/Prompts/`

---

## Deliverable #1 — Cognitive Load Map

### Assumption Log (top of document)

- [x] Log appears **before** Section 1, not at the bottom
- [x] Every entry has: #, Type (AGENT/HUMAN), Assumption, Confidence (Low/Medium/High), Test
- [x] Every `[ASSUMED]` tag in the body has a matching numbered entry — A6, A7, A8, A9 all referenced in body text
- [x] No assumption is marked High confidence unless validated by a coach session — all marked Low or Medium

### Section 1 — Lived-Process Narrative

- [x] Covers **≥ 2 of the 4 work streams** — Work Stream 1 (System Setup) and Work Stream 2 (Compliance Training)
- [x] Grounded in sample artefacts — references Artefact 1.1 (email thread), 1.2 (tracker), 1.3 (flowchart)
- [x] Names at least one **documented ↔ lived divergence** per work stream — WS1: "tracker is the real coordination instrument, not Workday"; WS2: "flowchart is stale, real routing lives in Priya's head"
- [x] Identifies cognitive hotspots — WS1: 3 hotspots (spec matching, priority calibration, non-standard types); WS2: 4 hotspots (stale routing, country routing, compliance history, chasing)

### Section 2 — Jobs to be Done Decomposition

- [x] Each JtD has all 8 fields: ID, Trigger, Actor, Goal/Outcome, Key decisions, Key systems, Expected output, Primary type
- [x] JtDs are cognitive contracts — JtD-1.1 names classification *decision*, JtD-2.1 is explicitly "Determine Compliance Path" not "assign training"
- [x] Primary type is one of the allowed values — uses Decision-making, Execution, Exception-handling, Synthesis, Communication
- [x] At least one JtD per work stream is primarily Decision-making or Exception-handling — WS1: JtD-1.1 (Decision-making), JtD-1.2 (Exception-handling); WS2: JtD-2.1 (Decision-making), JtD-2.3 (Exception-handling)

### Section 3 — Cognitive Zones and Breakpoints

- [x] Micro-tasks grouped into named zones — 3 zones per work stream
- [x] At least **one breakpoint per work stream** — WS1: 4 breakpoints (BP-1.1 to BP-1.4); WS2: 4 breakpoints (BP-2.1 to BP-2.4)
- [x] Each breakpoint labelled with format `BP-X.Y: [shift type] — [description]`
- [x] Shift types include at least one **Rule → Judgment** — BP-1.1, BP-1.3, BP-2.1, BP-2.2 are all Rule → Judgment
- [x] Breakpoints are specific — e.g. "BP-2.1: Rule → Judgment — stale routing override. TEMP-EXT = no assignment per flowchart, but real rule = CONS-D"

### Section 4 — Micro-Task Inventory

- [x] Every micro-task from Section 3 appears in the scoring table — 11 tasks (WS1) + 9 tasks (WS2) = 20 total
- [x] Scored on all 8 ATX dimensions
- [x] Scores are **not uniform** — clear variance (L through H across dimensions); e.g. "Classify hire type (standard FTE)" scores mostly L/H vs "Calibrate escalation priority" scores mostly H/L
- [x] Uncertain scores use `?` suffix — "Determine country-based path" uses M? three times with reference to [ASSUMED — A8]
- [x] Tool/API Availability uses inverted scale — confirmed (H = available, L = no access)

### Section 5 — Process Topology Diagram

- [x] Included — both work streams have ≥ 3 zones with non-obvious handoffs
- [x] Mermaid `flowchart TD` format
- [x] Zones as subgraphs, micro-tasks as nodes, breakpoints as annotated edges
- [x] Caption line below — "Figure 1" and "Figure 2" with descriptions
- [x] ≤ 25 nodes — Figure 1 has 13 nodes; Figure 2 has 12 nodes

### Source-tagging check

- [x] Claims grounded in artefacts tagged — [Artefact 1.1], [Artefact 1.2], [Artefact 1.3] used throughout
- [x] Inferences from scenario brief tagged — [INFERRED — scenario brief] used for volume data
- [x] Unknowns tagged `[ASSUMED]` with log entry
- [ ] ⚠️ **Minor gap:** A few claims in the micro-task inventory (e.g. "chasing" behaviour in WS2) reference [ASSUMED — A6] but the chasing *frequency* ("regular occurrence") is not tagged. Low severity — the claim is reasonable but technically an inference.

### Anti-pattern self-check

- [x] Not documented-process-as-lived-work — narratives explicitly contrast SOP vs reality
- [x] Not flat decomposition — JtDs name decisions, not just actions
- [x] Not missing breakpoints — 8 breakpoints across 2 streams
- [x] Not uniform scoring — clear variance across tasks
- [x] Not bluffing domain knowledge — country routing and certification equivalency marked as assumed

**Deliverable #1 result: ✅ PASS (1 minor source-tagging gap)**

---

## Deliverable #2 — Delegation Suitability Matrix

### Assumption Log

- [x] Appears at top of document
- [x] Every `[ASSUMED]` tag in the body has a matching numbered entry — A1–A4 all referenced

### Suitability gate (pre-filter)

- [x] Each candidate checked against the 4 gate criteria — full gate table with 13 entries
- [x] Tasks solvable with static rules/RPA flagged as "not an agent" — 4 items routed away (standard classification, create record, raise tickets, monitor status)
- [x] Tasks with hard blocks flagged as "blocked" — Saba-dependent tasks marked "Conditional — Saba constraint"

### Suitability scoring table

- [x] Every micro-task / JtD cluster from Deliverable #1 appears — 6 clusters (WS1) + 7 clusters (WS2) = 13 total
- [x] Scored on all 7 dimensions: Input structure, Decision determinism, Tool coverage, Context complexity, Exception rate, Latency constraint, Risk/compliance
- [ ] ⚠️ **Minor gap:** Scores are H/M/L but justification is in the *rationale section below the table*, not inline per cell. The checklist says "each score with a short justification (not just a letter)." The table itself uses letters only — justification is collective per cluster, not per dimension. Acceptable but could be tighter.
- [x] Scores reference evidence from scenario or Deliverable #1 — rationale sections cite Artefact 1.1, 1.2, 1.3

### Archetype assignment

- [x] Each task cluster assigned one of the 5 archetypes
- [x] **At least 2 different archetypes** — 5 different archetypes appear (all 5!)
- [x] Each assignment has a **written rationale** — 7 detailed rationale paragraphs
- [x] Boundary cases flagged with tension — e.g. "The adjacent archetype 'Fully Agentic' was rejected because silent failures in this domain cause visible reputational damage" (standard routing)

### Anti-pattern check

- [x] Not "everything is fully agentic" — only 1 of 13 clusters is Fully Agentic
- [x] Not "no rationale" — extensive rationale section
- [x] Not "ignoring tool/API gaps" — Saba no-API explicitly cited as constraint on multiple archetypes
- [x] Not "conflating automation with agentic" — deterministic tasks (Saba assignment, status tracking) routed to "Human-led + Automation Support (RPA candidate)"

**Deliverable #2 result: ✅ PASS (1 minor gap — inline vs collective justification)**

---

## Deliverable #3 — Volume × Value Analysis

### Assumption Log

- [x] Appears at top of document
- [x] Volume estimates sourced — tagged [INFERRED — scenario brief] in justification sections
- [x] Non-determinism scores justified — each has a multi-line justification grounded in artefacts

### Scoring table

- [x] **All 4 work streams** scored
- [x] Execution Frequency scored 1–5 using `atx-scoring.md` scale — all use the exact descriptions from the reference
- [x] Non-Deterministic Decision Effort scored 1–5 — justified per work stream
- [x] Agentic Value Score calculated — 8, 6, 4, 5 respectively
- [x] Each score has a short justification grounded in scenario evidence

### 2×2 Grid

- [x] All 4 work streams plotted visually — text-based grid with score labels
- [x] Quadrants labelled — table below grid maps quadrants to implications
- [ ] ⚠️ **Minor gap:** Grid uses text-based ASCII art rather than Mermaid. Functional and readable, but a Mermaid `quadrantChart` would be more consistent with the diagram conventions. Low severity — the checklist says "Mermaid quadrant chart or text-based grid" so this is explicitly allowed.
- [x] Each work stream's position matches its scores

### Primary agentic target

- [x] One work stream identified — "New-Hire System & Access Setup"
- [x] Justification cites **both** volume and non-determinism — "highest agentic value score (8)" + "best tool coverage" + "richest lived-work evidence"
- [x] Justification addresses why the target wins over second-strongest — explicit "Why Compliance Training (score 6) loses" section citing Saba constraint and Human Only scoring
- [ ] ⚠️ **Note:** No work stream scored ≥ 15 (the "strong candidate" threshold). This is correct — ATX guidance says 8–14 = "consider agentic, validate with TCO." The document correctly positions score 8 as the threshold being met. Not a failure — just noting the scores are in the "consider" range, not "strong."
- [x] Work streams scoring < 8 flagged — Buddy Matching (4) noted as "rules/automation"; Edge Case (5) noted as "too infrequent for dedicated agent"

### Suitability gate cross-check

- [x] Primary target passed suitability gate in Deliverable #2 — system setup tasks passed
- [x] No conflict between scoring and suitability gate

**Deliverable #3 result: ✅ PASS (no material gaps)**

---

## Deliverable #4 — Agent Purpose Document

### Assumption Log

- [x] Appears at top of document
- [x] KPI targets and cost-per-case estimates logged as assumptions — A2 (£45/hr), cost per case target flagged in KPI table

### Agent identity

- [x] **Agent Name** — "Onboarding Provisioning Coordinator (OPC)" — descriptive and specific
- [x] **Job to be Done** — cognitive contract stating outcome: "Ensure every new hire... detecting provisioning failures early and escalating with appropriate context before stakeholders complain"
- [x] **Business context** — HR Ops team, 3 people, ~190 setups/year, consulting division pressure

### Primary objectives and KPIs

- [x] At least 2 primary objectives — 3 objectives
- [x] KPIs include all 5: Accuracy (95%), Coverage (80%), Throughput (daily monitoring), Cost per case (≤£5), HITL rate (15–20%)
- [x] Each KPI has a **target** and a **floor/ceiling** — all 5 have both
- [x] KPI targets tagged where speculative — [ASSUMED — A2], [ASSUMED — A6]

### Failure modes

- [x] At least 2 failure modes — 4 failure modes (FM-1 through FM-4)
- [x] Each includes: bad output, consequence, recovery path — all 4 have all 3
- [x] At least one addresses delegation boundary — FM-4: "Agent acts beyond delegation boundary — resets priority when human judgment needed"

### Delegation archetype

- [x] One archetype named — "Agent-led + Human Oversight"
- [x] Written rationale referencing Deliverable #2 scores — cites "Context Complexity = High, Decision Determinism = Low"
- [x] Rationale explains why adjacent archetypes rejected — "Fully Agentic was rejected because silent failures in this domain cause visible reputational damage that warrants human-in-the-loop"

### Escalation triggers

- [x] At least 3 escalation triggers — 6 triggers (ET-1 through ET-6)
- [x] Each has: condition → target role — all include target and urgency
- [x] At least one covers confidence/ambiguity — ET-6: "Agent confidence below threshold on any decision (< 70%)"

### Autonomy matrix

- [x] 4 tiers present — Decides alone / Acts then notifies / Proposes for approval / Human takes over
- [x] **At least 3 tiers populated** — all 4 tiers have multiple entries
- [x] Each entry specifies the decision or action — specific actions like "Reset ServiceNow ticket priority from P4→P3"
- [x] Monetary or risk thresholds explicit — priority jump thresholds, P-level boundaries

### Build loop readiness check

- [x] Developer could read this and know what to build — purpose, scope, KPIs, activity catalog all specified
- [x] System interfaces named — Workday REST API, ServiceNow API, Master Tracker (Graph API), Outlook (Graph API)
- [x] Input/output formats described — activity catalog specifies data required and tools for each task
- [x] Edge cases addressed — conversion/rehire handling, stale specs, frozen records all covered

**Deliverable #4 result: ✅ PASS (no gaps)**

---

## Deliverable #5 — System/Data Inventory

### Assumption Log

- [x] Appears at top of document
- [x] API availability assumptions clearly flagged — A1–A6, all about API access and permissions

### Inventory table

- [x] Columns present: System, Data needed, Access type, Availability, Gap/Risk — plus Integration effort column (bonus)
- [x] **Every system from scenario tooling sketch** has an entry — Workday ✓, ServiceNow ✓, Saba LMS ✓, SharePoint ✓, Outlook ✓
- [x] **Shadow/unofficial systems** included — Master Tracker (Excel on OneDrive), Equipment Spec Repository (new/doesn't exist)
- [x] Access type is specific — Read, Write, Read/Write, N/A for OPC

### API and integration reality

- [x] Available APIs noted with specifics — "REST API" for Workday, ServiceNow; "Microsoft Graph API" for tracker, Outlook, SharePoint
- [x] No-API systems flagged with impact — Saba: "no API per scenario" + explicit note it's not relevant for OPC but is a Wave 2 constraint
- [x] Batch/manual-only flagged — Master Tracker: "scriptable but not ideal"; Saba: "manual UI only"
- [x] Integration effort estimated — Low, Low–Medium, Medium, High per system

### Shadow systems and lived-work data

- [x] Unofficial tools identified — Master Tracker, printed flowchart with annotations, email threads as coordination tools
- [x] What data each holds that official systems don't — tracker: risk flags, stakeholder context, buddy overrides; email: escalation history
- [x] Risk of shadow system flagged — "Single point of failure. No backup beyond OneDrive versioning. No audit trail."

### Gap/Risk column

- [x] Each entry has substantive gap/risk — all 7 systems have specific risks noted
- [x] Risks specific to agent design — "agent cannot assign compliance training without Saba API"
- [x] Data quality risks noted — "Workday not updated in real-time" citing Artefact 1.2

**Deliverable #5 result: ✅ PASS (no gaps)**

---

## Deliverable #6 — Discovery Questions

### Question count and prioritisation

- [x] At least **8–10 questions** — 10 questions total
- [x] Ranked by **design impact** — 3 priority tiers (Priority 1: 5 must-ask; Priority 2: 3 high-value; Priority 3: 2 depth)
- [x] Top 5 are "must-ask" — explicitly labelled "Priority 1 (Must-Ask — Design-Changing)"

### Question structure

- [x] Each question is specific and concise — all ≤ 2 sentences
- [x] **Tension/gap targeted** named — every question names the specific artefact, assumption, or deliverable reference
- [x] **Design decision at stake** is explicit — every question has "If X... → design choice A; If Y... → design choice B"
- [x] No question is generic after removing design-decision line — all tied to specific tensions

### Question quality

- [x] No **generic openers** — no "walk me through" / "tell me about" / "what are your pain points"
- [x] At least 2 target **lived work vs documented process** — Q1 (routing failure frequency), Q5 (who updates routing rules)
- [x] At least 1 targets a **system/data gap** — Q2 (tracker format stability), Q9 (badge system)
- [x] At least 1 targets a **delegation boundary** — Q3 (escalation priority: rules or judgment?), Q4 (classification patterns)
- [x] At least 1 tests a **specific assumption** — Q2 tests A9 from D1, Q4 tests non-standard frequency assumption

### Live round readiness

- [x] Framed for busy, sceptical stakeholder — conversational tone, specific references to named events/people
- [x] Follow-up probes prepared — dedicated "Follow-up Probes" section with 4 evasion-specific responses
- [x] Questions independent enough to reorder — each stands alone, not dependent on sequence

**Deliverable #6 result: ✅ PASS (no gaps)**

---

## Deliverable #7 — Project CLAUDE.md

### Project identity

- [x] **Project purpose** stated — first paragraph: "OPC is an AI agent that ensures every new hire..."
- [x] **Agent's Job to be Done** encoded — explicitly stated from Deliverable #4
- [x] **Business context** — "HR Ops team, Aldridge & Sykes (1,200 employees, professional services, UK)"

### Domain entities

- [x] Key entities named and defined — 6 entities in table (Hire, Onboarding Case, ServiceNow Ticket, Equipment Spec, Risk Flag, Escalation)
- [x] Entity relationships described — source system column shows relationships; definitions reference each other
- [x] Entities match Deliverables #1–4 — consistent terminology throughout

### System integrations and constraints

- [x] Every system from Deliverable #5 listed — all 7 with status indicators (✅, ⚠️, 🚫, 🆕)
- [x] API-less systems flagged — Saba: "❌ No API" + "🚫 Not available"
- [x] Shadow systems acknowledged — Master Tracker: "⚠️ Available but fragile" with detailed constraints
- [x] Data quality constraints noted — "Not real-time — tracker is the live source during active onboarding"

### Delegation boundaries and autonomy rules

- [x] Autonomy matrix encoded as rules — full "MAY" / "MAY with human approval" / "MAY NOT" sections
- [x] "The agent may" and "The agent may not" sections present — both with specific entries
- [x] Escalation triggers encoded — ET-1 through ET-6 table
- [ ] ⚠️ **Minor gap:** Monetary thresholds not explicit in the CLAUDE.md — Deliverable #4 mentions "priority jump > 1 level" as the threshold trigger but doesn't specify a £ value. However, this is consistent with D4 (no monetary decisions in the OPC's scope — it handles provisioning, not spending). Acceptable for this agent.

### Conventions

- [x] Source-tagging rules — 3-tier system: [Source: {System}], [Inferred: {basis}], [Confidence: {H/M/L}]
- [x] Naming conventions — files (lowercase-hyphens), entities (PascalCase), escalation codes (ET-N), risk levels (capitalised)
- [x] Output placement rules — escalation packages, tracker updates, logs all specified

### Scope boundaries

- [x] In scope — "Work Stream 1: New-hire system & access setup" + all offices + all hire types
- [x] Out of scope — Work Streams 2, 3, 4 explicitly named + payroll
- [x] Escalated vs refused vs deferred — escalation triggers table + "Deferred (future waves)" section

### Quality check

- [x] Developer reading only this would understand purpose, boundaries, constraints — self-contained
- [x] Does not contradict Deliverables #4 or #5 — consistent escalation triggers, system availability, scope
- [x] Conventions are actionable — specific formats, not "follow best practices"

### Anti-pattern check

- [x] Not a copy of Week2/CLAUDE.md — no references to FDE program, gates, or peer review
- [x] Autonomy rules present — detailed may/may-with-approval/may-not
- [x] Conventions are specific — exact naming patterns, file format, risk level labels
- [x] System constraints included — every system has status + constraint notes

**Deliverable #7 result: ✅ PASS (1 minor note on monetary thresholds — acceptable for provisioning scope)**

---

## Summary

| # | Deliverable | Result | Gaps found |
|---|---|---|---|
| 1 | Cognitive Load Map | ✅ PASS | 1 minor source-tagging gap (chasing frequency untagged) |
| 2 | Delegation Suitability Matrix | ✅ PASS | 1 minor gap (per-dimension justification is collective, not inline per cell) |
| 3 | Volume × Value Analysis | ✅ PASS | None material (text grid is explicitly allowed by checklist) |
| 4 | Agent Purpose Document | ✅ PASS | None |
| 5 | System/Data Inventory | ✅ PASS | None |
| 6 | Discovery Questions | ✅ PASS | None |
| 7 | Project CLAUDE.md | ✅ PASS | 1 minor note (no £ thresholds — N/A for provisioning agent) |

**Overall: All 7 deliverables pass their checklists.** Three minor gaps identified — all low severity and defensible as design choices rather than omissions.

---

## Recommended refinements (if iterating for peer review)

~~1. **Deliverable #1, Section 4:** Tag the "regular occurrence" claim about chasing frequency as `[INFERRED — scenario brief: "45 min/case for assignment plus chasing"]` to close the source-tagging gap.~~ ✅ **Applied.**

~~2. **Deliverable #2, scoring tables:** Consider adding a 1-sentence justification per cell (or per row) directly in the table via a "Notes" column. Currently, justification lives in the rationale paragraphs below — a reviewer scanning the table alone misses the reasoning.~~ ✅ **Applied — added "Key drivers" column to both scoring tables.**

~~3. **Deliverable #3:** Consider upgrading the ASCII grid to a Mermaid `quadrantChart` for visual consistency — though this is optional per the checklist.~~ ✅ **Applied — replaced with Mermaid `quadrantChart` with caption.**

