# Delegation Suitability Matrix — HR Onboarding Coordination (Aldridge & Sykes)

> **Deliverable #2** | Scenario 1 (enriched) | Practice run

---

## Assumption Log

| # | Type | Assumption | Confidence | Test |
|---|------|-----------|------------|------|
| A1 | AGENT | ServiceNow API supports ticket creation, priority modification, and status query without IT team involvement | Medium | Ask Priya: "Can your team create and modify ServiceNow tickets via API, or does IT gate that?" |
| A2 | AGENT | Workday REST API can read hire type, role code, country, and employment history sufficient for routing decisions | Medium | Confirm API scope with IT: "Which Workday fields are exposed via API?" |
| A3 | AGENT | The Master Tracker could be replaced or supplemented by a system with proper API access (e.g. moving from Excel to a structured database) | Low | Ask Priya: "Would you be open to the tracker being replaced by something that updates in real-time, or is the Excel format load-bearing for you?" |
| A4 | AGENT | Saba LMS has no workaround (no CSV import, no browser automation tolerance) — all assignments are truly manual | Medium | Ask Priya/IT: "Is there any bulk assignment mechanism in Saba? Has anyone tried RPA or browser automation against it?" |

---

## Suitability Gate (Pre-filter)

Before scoring, each task cluster is checked against the 4 suitability gate criteria:

| Task cluster | Can be solved with rules/RPA alone? | Requires pure tacit judgment with no structure? | Critical data/system blocked? | Extreme compliance risk with no HITL path? | Gate result |
|---|---|---|---|---|---|
| Classify hire type (standard) | ✓ (rule-based) | No | No | No | **Route to RPA/rules — not an agent** |
| Classify hire type (non-standard) | No — judgment required | No — patterns exist | No | No | **Pass** |
| Create Workday record | ✓ (data entry) | No | No | No | **Route to automation — not an agent** |
| Raise ServiceNow tickets | ✓ (form fill) | No | No | No | **Route to automation — not an agent** |
| Determine equipment spec | No — tacit + changing | No — patterns exist | Partial (no system holds spec mapping) | No | **Conditional — needs spec repository** |
| Override ServiceNow routing | No — requires detecting failure | No | No | No | **Pass** |
| Calibrate escalation priority | No — judgment + politics | Borderline — very context-dependent | No (data exists in tracker) | No | **Pass (agent-support candidate)** |
| Monitor ticket status | ✓ (status check) | No | No | No | **Route to automation** |
| Apply compliance routing (standard) | ✓ (if rules are digitised) | No | Blocked on Saba (no API for assignment) | No | **Conditional — Saba constraint** |
| Apply compliance routing (edge cases) | No — stale rules + judgment | No — patterns exist | Blocked on Saba | No | **Conditional — Saba constraint** |
| Check prior certifications | No — manual reconciliation | No — but no equivalency rules exist | Blocked on Saba (manual lookup) | No | **Conditional — Saba + rule gap** |
| Chase overdue training | Partially (template emails) | No | No | No | **Pass** |
| Escalate to manager | No — judgment on timing/tone | No | No | No | **Pass** |

---

## Delegation Suitability Scoring

### Work Stream 1: New-Hire System & Access Setup

| Task cluster | Input Structure | Decision Determinism | Tool Coverage | Context Complexity | Exception Rate | Latency Constraint | Risk/Compliance | **Archetype** | **Key drivers** |
|---|---|---|---|---|---|---|---|---|---|
| Classify hire type (non-standard: conversions, rehires) | M — structured fields but cross-reference needed | L — judgment on how to represent edge cases | M — Workday API has data; logic is tacit | H — requires institutional knowledge of prior records | M — ~15% of hires | L — batch OK | H — wrong classification cascades | **Human-led + Agent Support** | Context Complexity H + Decision Determinism L |
| Determine equipment spec | M — role/division structured; spec mapping not | M — patterns change quarterly | L — no system holds spec mapping `[ASSUMED — A1]` | M — needs current divisional knowledge | M — changes each quarter | L | L — wrong spec = delay, not compliance issue | **Human-led + Agent Support** | Tool Coverage L (no spec repository exists) |
| Override ServiceNow routing | M — requires detecting the mismatch | M — once detected, fix is deterministic | H — ServiceNow API supports modification | M — must know current spec vs routing rules | M — when specs change | M — each day of delay compounds | L | **Agent-led + Human Oversight** | Tool Coverage H + Detection requires reasoning |
| Calibrate escalation priority | L — unstructured context (stakeholder politics, hidden notes) | L — highly judgment-dependent | L — context lives in tracker hidden columns, not APIs | H — requires relationship context and political sensitivity | M — regular occurrence | M — delay-sensitive | M — reputational risk | **Human-led + Agent Support** | Input L + Determinism L + Context H |
| Monitor ticket status + flag SLA breaches | H — structured ServiceNow status fields | H — deterministic (overdue = flag) | H — ServiceNow API | L — just status checking | L — standard check | L | L | **Fully Agentic** | All dimensions favour delegation |
| Update tracker + sync Workday | H — structured both sides | H — deterministic | M — tracker is Excel (scriptable but not ideal) | L | L | L | M — data integrity | **Agent-led + Human Oversight** | Oversight for data integrity — tracker is source of truth |

**Rationale for archetype assignments (Work Stream 1):**

1. **Non-standard hire classification → Human-led + Agent Support.** The agent can surface relevant prior records, flag potential duplicates, and suggest a classification — but the decision involves institutional knowledge about how Aldridge & Sykes has historically handled conversions and rehires. Decision Determinism is Low and Context Complexity is High. The agent drafts; Priya or a coordinator decides. [Artefact 1.2 — James O'Connor frozen record, Maria Costa conversion]

2. **Equipment spec determination → Human-led + Agent Support.** No system holds the current spec mapping (Tool Coverage is Low), and specs change quarterly. The agent could maintain a structured spec repository and suggest the likely match, but until the repository is built and trusted, a human confirms. This is a *conditional* upgrade path — once the spec repository is reliable, this could move to Agent-led.

3. **Override ServiceNow routing → Agent-led + Human Oversight.** Once a mismatch between the hire's spec and the auto-routing is detected, the fix is deterministic (change ticket parameters). The agent can detect mismatches by comparing hire attributes against known routing rules and make the correction — but a human reviews because routing failures were previously silent. [Artefact 1.1 — silent failure]

4. **Escalation priority calibration → Human-led + Agent Support.** This is the most judgment-intensive task in the work stream. The agent can surface relevant context (who the hire is, their sponsor, previous escalation history) and even suggest a priority level — but the political sensitivity decision stays with Priya. Input Structure is Low (unstructured notes), Decision Determinism is Low, Context Complexity is High.

5. **Status monitoring → Fully Agentic.** All dimensions favour full delegation: structured inputs, deterministic logic, high tool coverage, no judgment required. The agent polls ServiceNow, flags SLA breaches, and reports. No human approval needed.

6. **Tracker/Workday sync → Agent-led + Human Oversight.** Deterministic data movement between structured sources. Human oversight because the tracker is the source of truth (not Workday) and a sync error would propagate incorrect data to the "official" record.

---

### Work Stream 2: Compliance Training Assignment & Tracking

| Task cluster | Input Structure | Decision Determinism | Tool Coverage | Context Complexity | Exception Rate | Latency Constraint | Risk/Compliance | **Archetype** | **Key drivers** |
|---|---|---|---|---|---|---|---|---|---|
| Apply standard routing logic (FTE, known role code) | H — structured fields | H — documented rules (when accurate) | L — Saba has no API for assignment | L — straightforward | L — standard path | L | M — compliance training is regulated | **Agent-led + Human Oversight** (constrained by Saba) | Agent can decide but Tool Coverage L blocks execution |
| Apply routing for edge cases (stale rules, conversions) | M — fields are structured but rules are tacit | L — requires mental override of documented rules | L — Saba no API; routing rules not digitised | H — institutional memory of which rules are stale | M — ~15% non-standard | L | H — wrong assignment = non-compliance | **Human-led + Agent Support** | Determinism L + Context H + Risk H |
| Check prior certifications (conversions/rehires) | L — requires manual cross-reference in Saba | L — no equivalency rules exist | L — Saba no API; two profiles to reconcile | H — requires understanding what "counts" | M — every conversion | L | H — compliance risk if modules skipped | **Human Only** | All key dimensions at L — no viable delegation path |
| Assign modules in Saba UI | H — known module IDs | H — deterministic | L — Saba no API | L | L | L | M | **Human-led + Automation Support** (RPA candidate if Saba permits) | Deterministic but tool-blocked — RPA not agent |
| Track completion (status check) | H — Saba shows pass/fail | H — deterministic check | L — Saba no API (manual login) | L | L | M — deadlines | M | **Human-led + Automation Support** (RPA/screen-scrape candidate) | Same as above — mechanical, tool-blocked |
| Chase overdue (initial email to hire) | M — template but personalised | M — standard process with some judgment on timing | M — Outlook scriptable | L | M — regular | M — deadline-driven | M | **Agent-led + Human Oversight** | Mixed dimensions; agent drafts, human confirms |
| Escalate to manager (persistent non-completion) | L — unstructured judgment | L — timing, tone, firmness decisions | M — Outlook | M — relationship context | L | M | H — compliance escalation | **Human-led + Agent Support** | Determinism L + Risk H — human decides |

**Rationale for archetype assignments (Work Stream 2):**

1. **Standard routing → Agent-led + Human Oversight.** The logic is deterministic *when the rules are current*. The agent can execute the decision — but because (a) the rules change and the system doesn't update, and (b) assignment requires manual Saba interaction, a human confirms the decision before it's executed manually. The archetype would be Fully Agentic if Saba had an API and routing rules were digitised.

2. **Edge-case routing → Human-led + Agent Support.** The agent can surface what the documented rule says and flag where it's known to be stale — but the override decision requires knowing which rules Priya has mentally updated. Decision Determinism is Low, Context Complexity is High. [Artefact 1.3 footnote — TEMP-EXT override]

3. **Prior certification reconciliation → Human Only.** This is the task cluster with the lowest delegation suitability across all dimensions: no documented equivalency rules (Decision Determinism = L), Saba has no API for the lookup (Tool Coverage = L), each case is unique (Exception Rate = M), and making the wrong call is a compliance risk (Risk/Compliance = H). Until equivalency rules are documented and Saba access is solved, this stays with a human. No agent can currently help meaningfully.

4. **Saba module assignment → Human-led + Automation Support.** The task itself is deterministic (assign known modules to known learner), but the constraint is entirely the system interface. This is an RPA candidate (screen automation), not an AI agent candidate. The work is mechanical, not cognitive. [Anti-pattern check: agents are for non-determinism, not for engineering overhead.]

5. **Completion tracking → Human-led + Automation Support.** Same constraint: deterministic check, blocked by Saba's lack of API. RPA or screen-scraping, not an agent.

6. **Initial chase → Agent-led + Human Oversight.** Template-based communication with some personalisation. The agent can draft and send chase emails on a schedule — human reviews before send because tone and timing matter for the working relationship. Relatively low risk per message.

7. **Manager escalation → Human-led + Agent Support.** Higher judgment involved: when to involve the manager, how firmly to phrase it, whether to copy senior leadership. Agent can draft and suggest timing; human decides and sends.

---

## Summary: Archetype Distribution

| Archetype | Count | Task clusters |
|---|---|---|
| **Fully Agentic** | 1 | Status monitoring (ServiceNow) |
| **Agent-led + Human Oversight** | 4 | Override routing, Tracker/Workday sync, Standard compliance routing, Initial chase |
| **Human-led + Agent Support** | 5 | Non-standard classification, Equipment spec, Escalation priority, Edge-case routing, Manager escalation |
| **Human-led + Automation Support** | 2 | Saba module assignment (RPA), Saba completion tracking (RPA) |
| **Human Only** | 1 | Prior certification reconciliation |
| **Not an agent (RPA/rules)** | 4 | Standard hire classification, Create Workday record, Raise ServiceNow tickets, Monitor basic status |

This distribution demonstrates that the HR onboarding process is **not a "fully agentic" opportunity**. The highest-value agentic work is in the middle band — agent-led with oversight and human-led with agent support — where judgment, changing rules, and system constraints interact.

