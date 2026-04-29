# Closed Build Loop — Onboarding Provisioning Coordinator (OPC)

> **Agent Purpose Document:** `agent-purpose-document-scenario-1-001.md`  
> **Build Loop Run:** 001  
> **Diagnostic taxonomy:** `spec-ambiguity-vs-builder-mistakes.md` + Week 2 delegation boundary gaps

---

## Step 1: Builder Response (simulated)

### What I can build confidently (no clarification needed):

1. **ServiceNow ticket status monitoring** — poll ServiceNow API on a daily cadence, compare ticket age against SLA windows, flag breaches. Clear inputs, clear outputs, deterministic logic.

2. **Tracker status updates** — read ServiceNow ticket state via API, write current status to the Master Tracker via Graph API. Straightforward read/write.

3. **SLA breach detection logic** — compare `ticket.created_date + expected_fulfilment_window` against current date. Flag if overdue. Agent decides alone per autonomy matrix.

4. **Risk flag assignment (Green)** — if all tickets for an onboarding case are on-track, mark Green. Deterministic.

5. **Routine status notifications** — templated email to coordinators: "Here are today's onboarding statuses." Low-risk, informational.

6. **Tracker → Workday sync (end-of-week)** — read tracker, write standard fields to Workday via REST API. Batch job, deterministic mapping.

### What I need to clarify before building:

**Q1: What are the "standard fulfilment windows" for SLA detection?**
The spec says "comparing ticket age against standard fulfilment windows" but doesn't define what the windows are. Is it:
- 3 days for laptops, 1 day for building access, 5 days for software licences?
- A single window for all ticket types (e.g. 5 business days)?
- Different per division (consulting faster than audit)?

**Q2: How does the agent determine "equipment spec confidence ≥ 80%"?**
The autonomy matrix gates ticket creation on spec confidence. But what produces this confidence score? Is it:
- Date-based (last update < 90 days = 100%, > 90 days = declining)?
- Match-based (role+division found in spec repository = high, not found = low)?
- Both?

**Q3: What is the schema of the Equipment Spec Repository?**
The spec mentions it needs to be created (new system). What fields does it contain? Minimum:
- Division, Role code, Laptop model, Software bundle, Accessories?
- Or is it more granular (per office, per seniority level)?
- Who has write access? How does quarterly refresh work?

**Q4: How does the agent read "hidden columns" from the Master Tracker?**
The spec says the agent needs stakeholder context and risk flags from hidden columns. But:
- If accessed via Microsoft Graph API, are hidden columns still readable? (They're hidden in the UI, not necessarily in the API.)
- What are the exact column headers? ("Notes", "Risk flag", "Buddy override"?)
- Does the tracker have a header row the agent can parse, or are positions fixed?

**Q5: What does the "full context package" for ET-3 escalations contain?**
FM-3 says "every escalation must include: hire profile, stakeholder context, ticket timeline, what the agent already tried, recommended next action." What's the format? Is it:
- A structured JSON payload?
- A formatted email draft?
- A Markdown summary posted somewhere?
- Where is it delivered — tracker comment, email to Priya, Teams message?

**Q6: How does the agent know which hires are "high-sensitivity"?**
ET-3 fires when "hire is flagged as high-sensitivity (consulting director hire, senior leader, etc.)." Where does this flag come from?
- Is it in the tracker's "Risk flag" column?
- Is it inferred from hire attributes (division = consulting AND level = senior)?
- Does Priya set it manually, and the agent just reads it?

**Q7: What "standard fields" sync from tracker to Workday?**
The spec says sync "standard fields" end-of-week. Which fields specifically? The tracker has columns the spec didn't enumerate. If I sync the wrong fields or miss one, Workday data integrity is at risk.

**Q8: What happens when a new hire record appears in Workday?**
The spec says the agent monitors "all active onboardings" — but how does a new onboarding case start? Does the agent:
- Poll Workday for new hire records daily and auto-initiate a case?
- Wait for a tracker row to appear (Priya creates it first)?
- Get triggered by an event/webhook from Workday?

### What I said I couldn't build:

**C1: "Classify hire as standard/non-standard"** — The spec says human approves for non-standard, but doesn't define the classification logic. What makes a hire "non-standard"? The spec mentions conversions, rehires, secondments — but are there other categories? Without a decision tree or at least an enumeration of hire types that qualify as non-standard, I can't build the trigger that determines when to escalate (ET-1).

**C2: "Validate auto-routing match"** — The spec says the agent checks whether "ticket category ≠ expected based on role/division." But what IS expected? There's no mapping table of role/division → expected ServiceNow category. Without this, I can't detect a mismatch.

**C3: "Calculate escalation priority" and "Propose priority escalation"** — The spec says the agent proposes priority levels for high-jump escalations, factoring in "SLA status, hire profile, stakeholder context." But the priority calculation logic isn't defined. When does P4→P2 become P4→P1? What weight does "high-sensitivity" carry vs "days overdue"? I'd need a scoring rubric or decision tree.

---

## Step 2: Gap Diagnosis

| # | Gap | Builder question/inability | Category | Fix target |
|---|-----|---------------------------|----------|-----------|
| G1 | SLA fulfilment windows undefined | Q1: "What are the standard windows?" | **Spec Ambiguity** — the spec says to compare against windows but never defines them | Add SLA window table to Agent Purpose Document § Activity Catalog or a new § Operating Parameters |
| G2 | Spec confidence scoring undefined | Q2: "How is confidence calculated?" | **Spec Ambiguity** — spec uses "≥ 80%" as a gate but doesn't define how the score is produced | Add confidence calculation logic: date-based decay + match-based lookup |
| G3 | Equipment Spec Repository schema missing | Q3: "What fields? Who writes?" | **Spec Ambiguity** — spec acknowledges the repo doesn't exist yet but doesn't define its structure | Add schema definition to System/Data Inventory (D5) or as an appendix to the APD |
| G4 | Tracker column schema undefined | Q4: "What are the column headers?" | **Spec Ambiguity** — spec references "hidden columns" generically but not by name | Add tracker schema table (column name, data type, hidden?, read/write for agent) |
| G5 | Escalation context package format undefined | Q5: "What format? Where delivered?" | **Spec Ambiguity** — FM-3 lists required content but not the format or delivery channel | Add escalation output template/format specification |
| G6 | High-sensitivity flag source ambiguous | Q6: "Where does the flag live?" | **Delegation boundary gap** — the builder can't tell whether to read a human-set flag, infer from attributes, or both | Specify: the agent reads from tracker "Risk flag" column (human-set) OR infer from rules (division=consulting AND level≥senior) — which? If both, what's the precedence? |
| G7 | "Standard fields" for Workday sync undefined | Q7: "Which fields exactly?" | **Spec Ambiguity** — a builder syncing the wrong fields causes data corruption | Add field mapping table: tracker column → Workday field |
| G8 | Case initiation trigger undefined | Q8: "How does a new case start?" | **Spec Ambiguity** — the spec describes what the agent does once a case exists but not how it begins | Add trigger definition: poll Workday daily for new hires with start date within N days, OR read new tracker rows |
| G9 | Non-standard hire classification logic missing | C1: "Can't build the classifier" | **Delegation boundary gap** — spec says human decides but the agent needs to know WHEN to escalate (what makes it non-standard?) | Add hire type enumeration: standard = `type=FTE AND NOT rehire AND NOT conversion`; everything else = non-standard → ET-1 |
| G10 | Expected ServiceNow routing map missing | C2: "Can't validate routing without expected values" | **Spec Ambiguity** — agent is told to detect mismatches but has no reference mapping | Add routing expectation table: role_code × division → expected_category |
| G11 | Priority escalation scoring logic missing | C3: "Can't calculate priority" | **Spec Ambiguity** — spec defines *when* human approves (high-jump) but not how the agent *proposes* the level | Add priority scoring rubric (e.g. days_overdue × sensitivity_weight = proposed priority) |

---

## Step 3: Diagnosis Summary

### By category:

| Category | Count | Gaps |
|----------|-------|------|
| **Spec Ambiguity** (FDE fix — rewrite the spec) | 9 | G1, G2, G3, G4, G5, G7, G8, G10, G11 |
| **Delegation Boundary Gap** (Week 2 specific — agent can't tell who decides) | 2 | G6, G9 |
| **Builder Misread** | 0 | — |
| **Overconstrained Spec** | 0 | — |

### Pattern analysis:

The dominant failure mode is **missing operational parameters**. The Agent Purpose Document clearly defines *what* the agent does, *who approves*, and *when to escalate* — but it lacks:

1. **Reference data schemas** — the agent is told to look things up (specs, routing, SLA windows) but the lookup tables don't exist in the spec
2. **Scoring/calculation logic** — the agent is told thresholds (≥ 80% confidence, P3→P1 = high-jump) but not the formulas that produce those numbers
3. **Trigger mechanisms** — how does the agent know when to start working on a new case?

These are not conceptual gaps — the *thinking* is sound. They're **implementation-level gaps** where the spec assumes the builder will "figure it out" but a faithful builder will ask rather than infer.

### The 2 delegation boundary gaps:

- **G6 (high-sensitivity source):** The builder can't tell whether the agent *reads a flag a human set* or *infers sensitivity from attributes*. These are fundamentally different architectures — one is passive (agent reads), the other is active (agent reasons). The autonomy matrix doesn't clarify this.
- **G9 (non-standard classification):** The agent is told "human classifies non-standard" but it needs logic to detect *that a hire IS non-standard* in order to trigger ET-1. Without this, the agent either (a) escalates every hire for classification (useless) or (b) never escalates because it assumes everything is standard (dangerous).

---

## Step 4: Recommended Revisions

### Priority 1 (must fix for buildability):

| Gap | Revision | Where to add |
|-----|----------|------|
| G8 | Add case initiation trigger: "Poll Workday daily for hire records with start_date ≤ 14 days from today. For each new record not already in tracker, initiate new onboarding case." | New § in APD: "Operating Triggers" |
| G9 | Add classification rule: `IF type ∈ {FTE} AND rehire_flag = false AND conversion_flag = false → standard; ELSE → non-standard → fire ET-1` | Autonomy matrix, under "Agent decides alone" with a note |
| G6 | Specify: "High-sensitivity is determined by (a) tracker Risk Flag column IF manually set by Priya, OR (b) auto-inferred IF division=consulting AND job_level ≥ Senior. Manual flag overrides auto-inference." | Escalation triggers, ET-3 elaboration |

### Priority 2 (needed for reliable build):

| Gap | Revision | Where to add |
|-----|----------|------|
| G1 | Add SLA window table: Laptop = 5 business days, Badge = 2 business days, Software = 3 business days, Building access = 2 business days. [ASSUMED — confirm with IT] | New § "Operating Parameters" |
| G2 | Define confidence: `confidence = (match_score × 0.6) + (freshness_score × 0.4)` where match=100% if role+division found in repo, freshness=100% if updated <30 days, decays 1%/day | Below Autonomy Matrix "decides alone" section |
| G10 | Add routing expectation stub: "Routing map to be populated from ServiceNow admin console. Format: role_code, division → expected_category, expected_assignment_group" | System/Data Inventory appendix |

### Priority 3 (polish):

| Gap | Revision | Where to add |
|-----|----------|------|
| G3 | Define spec repository schema: Division, Role code, Job level, Laptop model/SKU, Software bundle ID, Refresh date, Confirmed by | System/Data Inventory |
| G4 | Document tracker columns: [Name, Type, Hidden?, Agent access] for all columns including hidden | System/Data Inventory |
| G5 | Define escalation format: Markdown summary posted to tracker "Notes" column + email draft to Priya with structured sections | FM-3 recovery path |
| G7 | Add field mapping: Tracker "Visible status" → Workday "onboarding_status"; Tracker "Start" → Workday "start_date" (read-only sync check) | Activity Catalog, "Sync" row |
| G11 | Add priority rubric: `score = (days_overdue × 2) + (sensitivity_flag × 3) + (stakeholder_escalation_count × 2)`. Score ≥ 7 → propose P1. Score 4–6 → propose P2. | New subsection under Escalation Triggers |

---

## Step 5: What This Tells You About Gate Readiness

The Agent Purpose Document is **structurally complete** — it has all the sections the checklist requires. But it would not survive a faithful build without revision because it lacks **operational parameters** (the reference data and calculation logic the builder needs to implement).

For the gate, this means:
- Your APD structure and delegation thinking are solid
- Under gate time pressure, prioritise adding at minimum: **case initiation trigger**, **classification rule**, and **SLA windows** — these are the three gaps that make the agent unbuildable without them
- The other gaps (schemas, formats, scoring rubrics) improve quality but a builder could reasonably ask about them and you could answer in a clarification round

