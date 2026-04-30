# Agent Purpose Document — Onboarding Provisioning Coordinator

> **Deliverable #4** | Scenario 1 (enriched) | Practice run

---

## Assumption Log

| # | Type | Assumption | Confidence | Test |
|---|------|-----------|------------|------|
| A1 | AGENT | Average time Priya spends on monitoring/escalation per active onboarding is ~1.5 hrs of the 3 hrs/case total | Low | Ask Priya: "Of the 3 hours per onboarding, roughly how much is monitoring and chasing vs initial setup?" |
| A2 | AGENT | Aldridge & Sykes fully loaded HR Ops cost is ~£45/hr (UK professional services firm, Manchester-based) | Low | Confirm with finance or Priya: "What's your team's cost centre rate?" |
| A3 | AGENT | ServiceNow ticket priority reset does not require IT approval — HR Ops can modify priority directly | Medium | Ask Priya: "When you reset Tom's ticket priority, did you need IT to approve that, or could you just do it?" |
| A4 | AGENT | Equipment spec mapping can be maintained in a structured document/database updated quarterly by division heads | Low | Ask Priya: "Who decides when laptop specs change? How was the consulting spec change communicated — or wasn't it?" |
| A5 | AGENT | The agent would have read access to the Master Tracker (or its replacement) — specifically the hidden columns containing stakeholder context and risk flags | Medium | Ask Priya: "Would you be comfortable with an automated system reading your tracker, including the notes and risk flags?" |
| A6 | AGENT | Target HITL rate of 15–20% reflects the ~15% non-standard hire rate plus some margin for edge cases in standard hires | Medium | Validate against actual case logs if available |

---

## Agent Identity

```
Agent Name:        Onboarding Provisioning Coordinator (OPC)
Job to be Done:    Ensure every new hire at Aldridge & Sykes has correct IT equipment, 
                   system access, building access, and badge provisioned before or on 
                   their start date — detecting provisioning failures early and 
                   escalating with appropriate context before stakeholders complain.

Business context:  HR Ops team (3 people), supporting ~190 system & access setups/year 
                   across audit, tax, consulting, and Dublin office. The consulting 
                   division is the primary source of escalation pressure due to senior 
                   hires and visible onboarding standards.
```

---

## Primary Objectives

1. **Eliminate silent provisioning failures** — detect equipment spec mismatches and auto-routing failures at ticket-creation time, not days later when the hire or their manager complains. [Artefact 1.1 — 5-day failure]

2. **Reduce escalation cycle time** — surface SLA breaches and provide escalation context (stakeholder sensitivity, hire profile) proactively so Priya can act before the CFO gets involved. [Artefact 1.1 — Day 5: "The director has emailed the CFO"]

3. **Free Priya from routine monitoring** — shift the daily status-check and tracker-update workload from human to agent, reserving human attention for judgment calls and stakeholder relationships

---

## KPIs

| KPI | Target | Acceptable floor/ceiling | Measurement |
|---|---|---|---|
| **Accuracy** (correct provisioning spec detected at ticket time) | 95% | Floor: 90% (below this, spec repository is unreliable) | % of tickets raised with correct spec vs tickets requiring later correction |
| **Coverage** (cases handled without human escalation for routine steps) | 80% of standard FTE onboardings | Floor: 70% | % of standard onboardings where agent handles monitoring, flagging, and sync autonomously |
| **Throughput** | All active onboardings monitored daily | — | Monitoring cadence (no onboarding goes >24 hrs without status check) |
| **Cost per case** | ≤ £5/case (agent operational cost) | Ceiling: £10/case | Token + tool call + infrastructure per onboarding lifecycle `[ASSUMED — A2]` |
| **HITL rate** | 15–20% of cases requiring human decision | Ceiling: 30% (above this, autonomy matrix is too conservative) | % of cases where agent escalates to human for decision `[ASSUMED — A6]` |

---

## Failure Modes

### FM-1: Stale spec repository → wrong equipment ordered

**What bad output looks like:** Agent raises a ServiceNow ticket with an outdated laptop spec because the spec repository wasn't updated after a quarterly change.

**Consequence:** Same failure as today (Artefact 1.1) but now attributed to the agent — trust erosion. Hire gets wrong equipment; delay compounds.

**Recovery path:** Agent flags "spec last confirmed: [date]" on every ticket. If >90 days since confirmation and division = consulting, escalate to human for spec verification before raising ticket. Build quarterly spec refresh into governance.

### FM-2: False-positive SLA alerts → alert fatigue

**What bad output looks like:** Agent flags tickets as "at risk" when they're actually on track (e.g. misreading ServiceNow status transitions), causing Priya to waste time checking non-issues.

**Consequence:** Alert fatigue — Priya starts ignoring agent alerts, defeating purpose.

**Recovery path:** Tune SLA thresholds based on actual fulfilment data. Require 2 consecutive missed checkpoints before flagging. Provide confidence score with each alert.

### FM-3: Escalation without sufficient context → unhelpful alerts

**What bad output looks like:** Agent escalates a stuck ticket but doesn't surface the relevant context (who the hire is, stakeholder sensitivity, history of the issue), forcing Priya to investigate from scratch.

**Consequence:** Adds work instead of saving it — Priya must context-switch from her current work to investigate.

**Recovery path:** Every escalation must include: hire profile, stakeholder context, ticket timeline, what the agent already tried (priority reset, etc.), and a recommended next action. Delivered as a formatted email to the division coordinator (or Priya for Red/CFO cases). Template sections:
1. **Hire Profile** — name, type, division, office, start date, sensitivity level
2. **Issue Summary** — 1–2 sentences describing the problem
3. **Ticket Timeline** — created date → current status → SLA status (days remaining or days overdue)
4. **Actions Taken** — what the agent already did (e.g. "one-level priority reset on Day 4")
5. **Recommended Next Step** — what the agent proposes the human do next

### FM-4: Agent acts beyond delegation boundary — resets priority when human judgment needed

**What bad output looks like:** Agent automatically escalates a ticket priority for a routine hire when the SLA breach is due to a valid reason (e.g. hire's start date was pushed back but ServiceNow wasn't updated).

**Consequence:** Unnecessary IT disruption; IT loses trust in HR ticket urgency signals.

**Recovery path:** Priority resets above a threshold (e.g. from P3→P1) require Priya's approval. Agent can propose but not execute high-priority escalations.

---

## Delegation Archetype

**Agent-led + Human Oversight**

**Rationale:** The majority of the OPC's work (status monitoring, spec matching for standard cases, SLA breach detection, tracker updates, Workday sync) is deterministic and well-suited to autonomous execution within defined bounds. However:
- Escalation priority calibration requires human judgment (Context Complexity = High, Decision Determinism = Low) — scored in Deliverable #2
- Non-standard hire classification requires human decision — the agent surfaces options but doesn't decide
- Equipment spec confidence degrades over time — human must confirm when specs may be stale

The agent leads on execution but human oversight governs escalation decisions and edge-case routing. The adjacent archetype "Fully Agentic" was rejected because silent failures in this domain [Artefact 1.1] cause visible reputational damage that warrants human-in-the-loop for non-routine decisions. **This is also validated by prior experience:** a Power Automate flow attempted 3 years ago auto-created tickets for all hire types including contractors, generated incorrect tickets, and required a week of cleanup. The lesson: non-standard hire types must not be fully automated. `[CONFIRMED — Priya, Q8]`

---

## Escalation Triggers

| # | Condition | Target role | Urgency |
|---|---|---|---|
| ET-1 | Non-standard hire type detected (conversion, rehire, secondment) requiring classification decision | Division coordinator: **Dev** (consulting/Dublin), **Sarah** (audit/tax), or **Priya** (edge cases) | Within 4 hours of hire record creation |
| ET-2 | Equipment spec or location-code confidence < 80% | Priya | Before raising ServiceNow ticket |
| ET-3 | SLA breach detected AND hire is flagged as high-sensitivity | Priya | Immediate — with full context package |
| ET-4 | ServiceNow auto-routing produced unexpected result (ticket category ≠ expected based on role/division/location) | Division coordinator: **Dev** or **Sarah** per assignment | Within 2 hours of ticket creation |
| ET-5 | Proposed priority escalation from P3→P1 or P4→P1 (high-jump) | Priya | Before execution |
| ET-6 | Agent confidence below threshold on any decision (< 70% — e.g. ambiguous role code, division not in spec repository) | Division coordinator per assignment | Before acting |

**ET-1 classification rule:** A hire is considered **non-standard** if any of the following are true:
- `hire_type ∉ {FTE}` (contractor, secondment)
- `rehire_flag = true` (returning employee)
- `conversion_flag = true` (contractor-to-FTE or secondment-to-FTE)
- Workday record has a pre-existing employee ID with a different status (potential frozen record)
- `office = Dublin` AND rehire (Dublin entity is separate in Workday — always requires new record regardless of gap) `[CONFIRMED — Priya, Q4]`

All other hires are **standard** → agent proceeds without ET-1 escalation.

**ET-1 rehire sub-classification (agent proposes, human confirms):**
- Rehire gap < 1 year → propose "reactivate existing record" `[CONFIRMED — Priya's heuristic, Q4]`
- Rehire gap ≥ 1 year → propose "create new record, link old in notes"
- Dublin rehires → always propose "create new record" (entity constraint)
- Note: IT's response to reactivation requests is inconsistent — agent proposes but human must confirm with IT `[CONFIRMED — Priya, Q4]`

**ET-3 high-sensitivity determination:** A hire is flagged as high-sensitivity if:
1. Tracker "Risk flag" column has been manually set to Amber or Red by Priya (manual flag takes precedence), OR
2. Auto-inferred: `division = Consulting AND job_level ≥ Manager` → Amber baseline `[CONFIRMED — Priya, Q3: "Consulting hires above manager level are almost always sensitive"]`
3. Auto-inferred: `office = Dublin` → elevated sensitivity (treat as consulting-level) `[CONFIRMED — Priya, Q3: "Dublin Country Manager has a short fuse"]`
4. Auto-inferred: `partner_sponsored = true` OR hire's notes column contains keywords ("director's hire", "CFO", "partner", "poach", "competitor") → Red from day one `[CONFIRMED — Priya, Q3/Q7]`
5. Auto-inferred: `client_facing = true` AND start_date is imminent (≤ 3 days) → elevated `[CONFIRMED — Priya, Q7: "client notices if no laptop on day one"]`
6. **Reactive signal:** inbound email from a stakeholder (hiring manager, PA, director) about a specific hire → auto-elevate to Amber if currently Green `[CONFIRMED — Priya, Q7: "sometimes I don't know until the PA calls"]`

Manual flag overrides auto-inference. If no flag is set and no auto-inference conditions are met, the hire is standard-sensitivity.

**Field source notes:**
- `partner_sponsored`: no structured Workday field exists. Determined by keyword detection in tracker notes column only. Keywords: "director's hire", "CFO", "partner", "poach", "competitor", "board". If a structured field becomes available in Workday, prefer it over keyword matching.
- `client_facing`: check Workday field `job_profile.client_facing_flag` if exposed by API. If field not available, infer from role_code: codes starting with `CONS-` in the consulting division are assumed client-facing. `[ASSUMED — confirm Workday field availability with Raj in IT]`

---

## Operating Triggers

### Case initiation
The agent polls Workday daily (06:00 UTC) for hire records with `start_date ≤ today + 14 calendar days` that do not yet have a corresponding row in the Master Tracker. For each new record found, the agent:
1. Creates a new tracker row (status = "Initiated", risk = Green)
2. Reads hire attributes (type, role code, division, country, job level)
3. Applies the ET-1 classification rule — if non-standard, escalates immediately; if standard, proceeds to provisioning orchestration

**Provisioning orchestration (standard hires):** All ServiceNow tickets for a given onboarding are created in parallel at case initiation — laptop, software, badge, and building access. No sequencing dependencies between ticket types. Building access follows location-aware rules: Manchester/Leeds via ServiceNow (agent acts); Birmingham/Dublin via email draft (agent proposes, coordinator sends).

### Daily monitoring cadence
At 08:00 UTC daily, the agent checks all active onboarding cases (tracker status ≠ "Closed") for:
- ServiceNow ticket SLA breaches (per § Operating Parameters)
- Auto-routing mismatches — including **location-code validation** (verify ticket routed to correct office's facilities/IT team) `[CONFIRMED — Priya, Q1: Birmingham location codes were once misconfigured]`
- Risk flag changes requiring notification
- **Reactive sensitivity signals:** inbound stakeholder emails about specific hires (elevate risk flag if currently Green)

**Reactive email matching logic:** Scan Outlook inbox (HR Ops shared mailbox) for messages received since last check. For each message: (a) match sender against `hiring_manager_email` or `manager_email` from Workday records for all active onboarding cases; (b) search subject and body for hire's full name. If match found → link to case and evaluate ET-3 reactive sensitivity rule. If no confident match (multiple potential hires, or sender not a known stakeholder) → flag for coordinator review. Prefer false positives over false negatives — a flagged non-issue costs less than a missed escalation email.

### Daily lightweight sync (status + start date)
At 09:00 UTC daily, the agent syncs the following "hard data" fields from tracker → Workday:
- `tracker."Visible status"` → `Workday.onboarding_status`
- `tracker."Start"` → validate matches `Workday.start_date` (flag discrepancy, do not overwrite)

This prevents stale Workday data from affecting downstream systems (payroll runs mid-month). `[CONFIRMED — Priya, Q6: "A selective daily sync for 'hard' data would be fine"]`

### End-of-week full reconciliation
Every Friday at 17:00 UTC, the agent performs a full reconciliation:
- All daily sync fields (above)
- `tracker."Workday status"` → validate matches `Workday.employment_status` (read-only check)
- Flag any tracker rows where data has diverged from Workday beyond the daily sync fields

Notes and risk flags are **never** synced to Workday — they are tracker-only working data. `[CONFIRMED — Priya, Q6: "Some of the notes are messy drafts — I wouldn't want those going into Workday"]`

---

## Operating Parameters

### SLA fulfilment windows (per ticket type)

| Ticket type | Expected fulfilment | SLA breach threshold | Source |
|---|---|---|---|
| Laptop provisioning | 5 business days | Day 6 (first working day after window closes) | `[ASSUMED — confirm with IT]` |
| Software licence assignment | 3 business days | Day 4 | `[ASSUMED]` |
| Building access / badge | 2 business days | Day 3 | `[ASSUMED]` |
| Specialist hardware (e.g. dual monitors, docking station) | 7 business days | Day 8 | `[ASSUMED]` |

SLA clock starts at ticket creation timestamp. Business days = Mon–Fri excluding UK public holidays. If ServiceNow ticket has a custom "expected delivery date" field, use that instead of the default window.

### Equipment spec and location-code confidence scoring

The OPC validates both equipment specs AND location codes when assessing ticket-creation confidence. Location-code mismatches (e.g. Birmingham hire routed to Manchester facilities) are a confirmed failure mode. `[CONFIRMED — Priya, Q1: Birmingham location codes once misconfigured for 2 weeks]`

```
confidence = (match_score × 0.5) + (freshness_score × 0.3) + (location_score × 0.2)

match_score:
  - role_code + division found in spec repository → 100%
  - role_code found but division not matched → 70%
  - role_code not found → 30%

freshness_score:
  - spec last updated ≤ 30 days ago → 100%
  - spec last updated 31–60 days ago → 85%
  - spec last updated 61–90 days ago → 70%
  - spec last updated > 90 days ago → 50% (and decays 1%/day thereafter)

location_score:
  - office location code matches expected ServiceNow routing group → 100%
  - office location code not found in routing map → 50%
  - office location code maps to a different routing group than expected → 20% (likely misconfigured)
```

Gate: if `confidence < 80%` → fire ET-2 (human confirms spec before ticket creation).

`[ASSUMED — scoring weights and decay rates are initial estimates; tune based on actual spec-change frequency after 1 quarter of operation]`

### Priority escalation scoring

When proposing a priority change for a breached ticket:

```
escalation_score = (days_overdue × 2) + (sensitivity_weight × 3) + (stakeholder_escalation_count × 2)

sensitivity_weight:
  - partner-sponsored hire → 4 (Red from day one) [CONFIRMED — Priya, Q3]
  - consulting hire above manager level → 3 [CONFIRMED — Priya, Q3]
  - Dublin office hire → 3 [CONFIRMED — Priya, Q3: "Dublin Country Manager has a short fuse"]
  - client-facing with imminent start → 3 [CONFIRMED — Priya, Q7]
  - standard hire → 1

stakeholder_escalation_count:
  - number of inbound emails/messages from stakeholders about this hire
```

| Score | Proposed action |
|---|---|
| ≥ 7 | Propose P1 (immediate IT attention) — fires ET-5 for human approval |
| 4–6 | Propose P2 — fires ET-5 for human approval |
| 1–3 | One-level reset (agent acts, human notified) |

`[ASSUMED — scoring thresholds need tuning against historical escalation data]`

---

## Autonomy Matrix

### AGENT DECIDES ALONE (no human approval required):

- Monitor ServiceNow ticket status for all active onboardings (daily cadence)
- Detect SLA breaches by comparing ticket age against standard fulfilment windows
- **Validate location codes** on ServiceNow tickets (check ticket routed to correct office's team) `[NEW — from Q1]`
- Update Master Tracker with current status from ServiceNow and Workday
- **Daily lightweight sync** of status + start date from tracker → Workday `[REVISED — from Q6]`
- Raise ServiceNow tickets for standard FTE hires where equipment spec confidence ≥ 80% and auto-routing matches expected category
- Send routine status notifications to **division coordinator** (Dev or Sarah per assignment) `[REVISED — from Q10]`
- Flag onboardings as "Green" when all tickets are on track

### AGENT ACTS, HUMAN NOTIFIED AFTER:

- Reset ServiceNow ticket priority from P4→P3 or P3→P2 (one-level escalation) with notification to **division coordinator**
- Flag onboarding as "Amber" risk in tracker with reason
- **Auto-elevate risk flag** when inbound stakeholder email detected about a currently-Green hire `[NEW — from Q7]`
- Request badge ordering and building access **for Manchester/Leeds** via ServiceNow (low-risk, standard process) `[REVISED — from Q9]`
- Send routine "your ServiceNow ticket is in progress" update to the new hire's stakeholder

### AGENT PROPOSES, HUMAN APPROVES BEFORE ACTION:

- Proposed equipment spec for non-standard roles or roles where spec was last updated >90 days ago
- Priority escalation of >1 level (P4→P2 or P3→P1) — agent drafts justification, human approves
- Raising ServiceNow tickets for non-standard hire types (conversions, rehires)
- **Draft building access email for Birmingham** (to facilities management company) — coordinator reviews and sends `[NEW — from Q9]`
- **Draft building access email for Dublin** (to office manager) — coordinator reviews and sends `[NEW — from Q9]`
- Flagging onboarding as "Red" risk — agent drafts the flag with evidence, Priya confirms
- Sending escalation emails to IT leadership or senior stakeholders
- **Propose rehire sub-classification** (reactivate vs new record) based on gap heuristic `[NEW — from Q4]`

### HUMAN TAKES OVER (agent provides supporting context):

- Classifying non-standard hire types (contractor-to-FTE, rehires with frozen records)
- Calibrating escalation response when stakeholder has directly contacted CFO or senior leadership
- Resolving cases where ServiceNow and Workday data conflict and root cause is unclear
- Any decision involving the hire's start date (delay/advance)
- Disputes with IT team about ticket priority or fulfilment responsibility
- **IT coordination for rehire record reactivation** — IT's response is inconsistent; human must negotiate `[NEW — from Q4]`

