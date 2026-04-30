# Closed Build Loop — Run 002 (Post-Discovery Revision)

> **Agent Purpose Document:** `agent-purpose-document-001.md` (revised with discovery responses)  
> **Diagnostic taxonomy:** `spec-ambiguity-vs-builder-mistakes.md` + Week 2 delegation boundary gaps  
> **Comparison:** Run 001 found 11 gaps (9 spec ambiguity, 2 delegation boundary). This run evaluates the revised APD.

---

## Step 1: Builder Response (simulated)

### What I can build confidently (no clarification needed):

1. **Case initiation trigger** — poll Workday daily at 06:00 UTC for hires with start_date ≤ today+14 not in tracker. Create tracker row. Apply ET-1 classification rule. ✅ Clear.

2. **ET-1 classification logic** — boolean rule: hire_type ∉ FTE OR rehire_flag OR conversion_flag OR pre-existing employee ID OR Dublin rehire. Standard vs non-standard is deterministic. ✅ Clear.

3. **ET-1 rehire sub-classification** — gap < 1yr → propose reactivate; ≥ 1yr → new; Dublin → always new. Agent proposes, human confirms. ✅ Clear.

4. **SLA breach detection** — ticket age vs window table (laptop=5d, software=3d, badge=2d, specialist=7d). Business days only. Use custom "expected delivery date" if available. ✅ Clear.

5. **Confidence scoring** — three-component formula: match (0.5) + freshness (0.3) + location (0.2). Each sub-score defined with thresholds. Gate at 80%. ✅ Clear.

6. **Priority escalation scoring** — formula: (days_overdue × 2) + (sensitivity_weight × 3) + (stakeholder_escalation_count × 2). Five sensitivity tiers defined. Score thresholds → P1/P2/one-level. ✅ Clear.

7. **ET-3 high-sensitivity determination** — 6-tier precedence: manual flag > partner-sponsored/keyword > consulting ≥ Manager > Dublin > client-facing imminent > reactive email signal. ✅ Clear.

8. **Daily monitoring cadence** — 08:00 UTC, check all active cases for SLA breaches, routing mismatches, risk flag changes, inbound stakeholder emails. ✅ Clear.

9. **Daily lightweight sync** — 09:00 UTC, sync status + validate start date. Never sync notes/flags. ✅ Clear.

10. **Weekly full reconciliation** — Friday 17:00 UTC, all sync fields + employment status validation + divergence flagging. ✅ Clear.

11. **Division-based escalation routing** — consulting/Dublin → Dev; audit/tax → Sarah; edge cases/Red → Priya. ✅ Clear.

12. **Location-aware building access** — Manchester/Leeds → ServiceNow (agent acts, notified). Birmingham → draft email to facilities company (agent proposes). Dublin → draft email to office manager (agent proposes). ✅ Clear.

13. **Autonomy matrix** — four tiers, each with specific entries and delegation levels. Priority jump thresholds explicit. ✅ Clear.

14. **ServiceNow ticket creation for standard FTEs** — confidence ≥ 80%, auto-routing matches, standard hire type. ✅ No ambiguity about when agent can proceed autonomously.

### What I need to clarify before building:

**Q1: How does the agent detect "inbound stakeholder emails about specific hires"?**
The spec says the agent monitors for reactive sensitivity signals (ET-3 rule 6, daily monitoring, auto-elevate in autonomy matrix). But:
- Does the agent scan ALL emails to the HR Ops shared inbox?
- Or only emails to a specific mailbox?
- How does it match an email to a specific hire? By name in subject line? By ticket number?
- What's the false-positive tolerance? If a hiring manager emails about something unrelated, does it trigger?

**Q2: What does the agent do between case initiation and ticket creation?**
The spec defines case initiation (06:00 poll) and ticket creation (confidence-gated). But the provisioning orchestration flow between them isn't sequenced:
- Does the agent create ALL tickets (laptop, software, badge, building access) at once?
- Or does it sequence them (e.g. laptop first, then software after laptop is allocated)?
- Is there a dependency between tickets?

**Q3: How does the agent determine `partner_sponsored` and `client_facing` attributes?**
ET-3 rules 4 and 5 reference these as fields. Are they:
- Workday fields? (If so, what are the field names?)
- Inferred from other data? (role type, department?)
- Manually tagged by Priya in the tracker notes?
The spec says keyword detection in notes for partner-sponsored ("director's hire", "CFO", "partner", "poach", "competitor") — so is keyword detection the ONLY source, or is there also a structured field?

**Q4: What is the tracker column schema?**
The spec references specific tracker columns by name ("Visible status", "Start", "Workday status", "Risk flag", notes). But I need the complete column list to build the integration:
- What are ALL column headers (visible + hidden)?
- What data types? (free text, dropdown, date?)
- Which columns does the agent read? Write? Both?

**Q5: What is the escalation context package format?**
FM-3 says every escalation must include hire profile, stakeholder context, ticket timeline, what agent tried, recommended action. ET-3 says "with full context package." But:
- Is this an email? A tracker comment? A Teams message? A structured JSON?
- Is there a template?
- Where is it delivered — to the division coordinator's inbox, to a shared channel, or into the tracker?

**Q6: How does the "expected ServiceNow routing group" get established?**
The location_score formula compares office location code against "expected ServiceNow routing group." But where does the expected mapping come from?
- Is it in the spec+location repository?
- Is it a static config file?
- Who maintains it?

### What I said I couldn't build:

**C1: Inbound email monitoring for reactive sensitivity signals.** I can build email reading via Graph API, but without knowing the matching logic (how to link an email to a specific hire), I'll build something overly broad or overly narrow. Need: matching rules (subject line parse, sender lookup, or both).

---

## Step 2: Gap Diagnosis

| # | Gap | Builder question/inability | Category | Severity | Fix |
|---|-----|---------------------------|----------|----------|-----|
| G1 | Email-to-hire matching logic undefined | Q1: How to link inbound email to a specific hire | **Spec Ambiguity** | Medium | Add matching rules: search for hire full name in subject/body; match sender against hiring manager from Workday record; if no confident match, flag for human review |
| G2 | Provisioning orchestration sequence undefined | Q2: All tickets at once or sequenced? | **Spec Ambiguity** | Low | Add: create all tickets in parallel at initiation; no dependencies between ticket types. If dependencies exist, document them. |
| G3 | `partner_sponsored` and `client_facing` data source ambiguous | Q3: Workday field or inferred? | **Spec Ambiguity** | Medium | Clarify: `partner_sponsored` is keyword-detected from notes ONLY (no Workday field). `client_facing` — check if Workday has a "client-facing" flag; if not, this is ASSUMED and logged. |
| G4 | Tracker column schema missing | Q4: Complete column list | **Spec Ambiguity** | Medium | Add full schema table to System/Data Inventory or as APD appendix |
| G5 | Escalation context package format undefined | Q5: Template, channel, format | **Spec Ambiguity** | Low | Define: structured email to divsion coordinator with sections (Hire Profile, Sensitivity Level, Ticket Timeline, Actions Taken, Recommended Next Step) |
| G6 | Expected routing group mapping source undefined | Q6: Where is the mapping stored? | **Spec Ambiguity** | Low | Clarify: location → routing group mapping lives in the spec+location repository alongside equipment specs |

---

## Step 3: Comparison with Run 001

| Metric | Run 001 | Run 002 | Change |
|--------|---------|---------|--------|
| **Total gaps** | 11 | 6 | -5 (45% reduction) |
| **Spec Ambiguity** | 9 | 6 | -3 |
| **Delegation Boundary Gaps** | 2 | 0 | **Eliminated** ✅ |
| **Builder Misread** | 0 | 0 | — |
| **"Can build confidently" items** | 6 | 14 | +8 |
| **"Cannot build" items** | 3 | 1 | -2 |

### What was fixed from Run 001:

| Run 001 gap | Status in Run 002 |
|---|---|
| G1: SLA windows undefined | ✅ **Fixed** — full table with 4 ticket types, thresholds, business day rules |
| G2: Spec confidence scoring undefined | ✅ **Fixed** — three-component formula with thresholds and decay rates |
| G3: Spec repository schema missing | ⚠️ **Partially fixed** — renamed to "spec + location repository" but schema still not enumerated. Now Low severity. |
| G4: Tracker column schema undefined | ⚠️ **Still open** — columns referenced by name but full schema not provided |
| G5: Escalation context format undefined | ⚠️ **Still open** — content defined (FM-3) but format/channel not specified |
| G6: High-sensitivity source ambiguous | ✅ **Fixed** — 6-tier precedence with confirmed sources per tier |
| G7: Standard fields for sync undefined | ✅ **Fixed** — daily sync (status + start date) and weekly reconciliation explicitly defined |
| G8: Case initiation trigger undefined | ✅ **Fixed** — Workday poll, 14-day lookahead, tracker row creation, ET-1 application |
| G9: Non-standard classification logic missing | ✅ **Fixed** — boolean rule with 5 conditions + Dublin entity constraint |
| G10: Expected routing map missing | ⚠️ **Partially fixed** — referenced in location_score formula but storage location not named. Now Low severity. |
| G11: Priority scoring logic missing | ✅ **Fixed** — full formula with 5 sensitivity tiers and 3 score-to-action thresholds |

### New gaps in Run 002 (emerged from added complexity):

| New gap | Source | Severity |
|---|---|---|
| G1 (email matching) | Added by reactive sensitivity signal feature (from discovery Q7) | Medium |
| G2 (ticket sequencing) | Exposed now that case initiation is defined — what happens next? | Low |
| G3 (partner/client fields) | Added specificity on sensitivity rules exposed field-source ambiguity | Medium |

---

## Step 4: Severity Assessment

| Severity | Count | Gaps | Impact |
|----------|-------|------|--------|
| **Medium** | 3 | G1 (email matching), G3 (field sources), G4 (tracker schema) | Builder will make reasonable but potentially wrong assumptions |
| **Low** | 3 | G2 (sequencing), G5 (escalation format), G6 (routing map location) | Builder can make sensible defaults; unlikely to cause build failure |

**No High-severity gaps remain.** In Run 001, G8 (case initiation), G9 (classification), and G6 (sensitivity) were all High-severity — all three are now resolved.

---

## Step 5: Recommended Revisions (Run 002)

### Priority 1 (fix before peer review):

**G1 — Email-to-hire matching logic:**
Add to § Operating Triggers > Daily monitoring:
> "Reactive email matching: search Outlook inbox for messages received since last check. For each message, extract sender and match against Workday `hiring_manager_email` or `manager_email` for all active onboarding cases. Search subject and body for hire's full name. If match found → link to case and evaluate reactive sensitivity rule. If no confident match (multiple potential hires, or sender not in Workday) → flag for coordinator review. False-positive tolerance: prefer false positives (flag something that isn't about a hire) over false negatives (miss an escalation email)."

**G3 — Field source clarification:**
Add to § ET-3 rules:
> "`partner_sponsored`: no structured Workday field exists for this. Determined by keyword detection in tracker notes column only. Keywords: 'director's hire', 'CFO', 'partner', 'poach', 'competitor', 'board'. If a structured field becomes available in Workday, prefer it over keyword matching."
>
> "`client_facing`: check Workday field `job_profile.client_facing_flag` if exposed by API. If field not available, infer from role_code: role codes starting with 'CONS-' in the consulting division are assumed client-facing. Log as assumption."

**G4 — Tracker schema:**
Add to System/Data Inventory or as APD appendix:

| Column | Data type | Visible? | Agent reads? | Agent writes? |
|--------|-----------|----------|-------------|--------------|
| Hire | Text | Yes | Yes | Yes (at initiation) |
| Start | Date (DD.MM) | Yes | Yes | No (validated only) |
| Type | Dropdown | Yes | Yes | Yes (at initiation) |
| Workday status | Dropdown | Yes | Yes | Yes (sync) |
| Visible status | Text | Yes | Yes | Yes (sync) |
| Notes | Free text | Hidden | Yes | No |
| Risk flag | Dropdown (Green/Amber/Red) | Hidden | Yes | Yes |
| Buddy override | Text | Hidden | No | No |

`[ASSUMED — column list based on Artefact 1.2; confirm complete list with Priya]`

### Priority 2 (nice to have):

**G2:** Add: "All ServiceNow tickets for a given onboarding are created in parallel at case initiation. No sequencing dependencies between ticket types."

**G5:** Add: "Escalation context is delivered as a formatted email to the division coordinator (or Priya for Red/CFO cases). Template sections: [1] Hire Profile (name, type, division, start date, sensitivity level), [2] Issue Summary (1–2 sentences), [3] Ticket Timeline (created → current status → SLA status), [4] Actions Taken (what agent already did), [5] Recommended Next Step."

**G6:** Add: "Location → routing group mapping is stored in the spec+location repository alongside equipment specs. Format: `office_code, expected_routing_group, expected_facilities_team`."

---

## Step 6: Build Readiness Assessment

| Dimension | Run 001 | Run 002 | Notes |
|-----------|---------|---------|-------|
| **Structurally complete** | ✅ | ✅ | All APD sections present in both |
| **Buildable without questions** | ❌ (6 of 15 items) | ✅ (14 of 15 items) | Only email matching requires clarification to build |
| **Delegation boundaries clear** | ❌ (2 gaps) | ✅ (0 gaps) | All tiers populated with specific actions; all decision authority named |
| **Operating parameters defined** | ❌ (missing SLA, confidence, triggers) | ✅ | SLA table, confidence formula, priority formula, operating triggers all defined |
| **Stakeholder-validated** | ❌ (all assumed) | Partial (8 confirmed, 7 still assumed) | Discovery responses upgraded key assumptions to confirmed |

**Overall: The revised APD is buildable.** A developer could implement ~93% of the agent (14 of 15 capability items) without asking questions. The remaining 6 gaps are Low-to-Medium severity — a builder would make reasonable defaults that could be corrected in review.

**The biggest improvement:** delegation boundary gaps are eliminated. In Run 001, the builder couldn't tell who decides in two critical areas (sensitivity flagging and non-standard classification). In Run 002, both have explicit rules with confirmed precedence and named decision-makers.

