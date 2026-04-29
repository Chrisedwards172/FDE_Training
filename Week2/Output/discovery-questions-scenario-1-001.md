# Discovery Questions for Priya Aggarwal (HR Ops Lead)

> **Deliverable #6** | Scenario 1 (enriched) | Practice run
> 
> Questions prioritised by design impact — highest first. Top 5 are "must-ask" in the 10-minute live round.

---

## Assumption Log

| # | Type | Assumption | Confidence | Test |
|---|------|-----------|------------|------|
| A1 | AGENT | These questions are designed for the practice scenario (Aldridge & Sykes); the gate scenario will require fresh questions tied to its specific tensions | High | N/A — this is practice |

---

## Priority 1 (Must-Ask — Design-Changing)

### Q1: Silent routing failure frequency

**Question:** "When Tom's laptop ticket got stuck because the consulting spec changed — how often does that happen? Once a quarter? Once a month? And is it always consulting, or do other divisions have spec changes that ServiceNow doesn't pick up?"

**Tension targeted:** Artefact 1.1 shows one instance of silent auto-routing failure. The OPC's value proposition depends on this being a *recurring* problem, not a one-off. If it's once a year, the spec-matching capability isn't worth building.

**Design decision at stake:** If failures happen monthly across multiple divisions → OPC needs a comprehensive spec repository with cross-division coverage and quarterly refresh governance. If it's rare and consulting-only → a simple consulting-specific spec check is sufficient, and the OPC's primary value shifts entirely to monitoring/escalation (not spec matching).

---

### Q2: Tracker as source of truth — team access and format stability

**Question:** "Your tracker has hidden columns with risk flags and notes that seem critical for prioritisation. Do your two coordinators see those columns? And how often does the tracker format change — do you add or move columns regularly?"

**Tension targeted:** Deliverable #5 identifies the tracker as a single point of failure and the de facto coordination system [Artefact 1.2]. The agent needs to read it reliably. If column positions shift, the integration breaks.

**Design decision at stake:** If coordinators don't see hidden columns → the agent's context advantage over the coordinators is significant (it surfaces Priya's private knowledge). If the format is unstable → agent needs schema-resilient reading (field matching by header name, not position), or the tracker must be migrated to a structured store (SharePoint List). This changes the Wave 1 build effort from "read Excel" to "build and migrate to a new coordination system."

---

### Q3: Escalation priority — rules or pure judgment?

**Question:** "When you decide whether a stuck ticket is Amber or Red, and whether to chase IT directly or email formally — is there a pattern? Like, the director's hire always goes Red, anyone in consulting gets escalated faster? Or is it different every time?"

**Tension targeted:** Deliverable #2 scored escalation priority calibration as "Human-led + Agent Support" (Decision Determinism = Low). If there ARE patterns (even informal ones), the agent could propose priority levels. If it's truly case-by-case judgment, the agent can only surface context.

**Design decision at stake:** If patterns exist → codify them as escalation rules in the autonomy matrix (agent proposes Red/Amber based on rules; human confirms). If purely situational → agent role shrinks to "assemble context" only; the autonomy matrix's "Agent proposes" tier loses entries. This materially changes KPIs — coverage target drops if the agent can't propose escalation levels.

---

### Q4: Non-standard hire classification — conversion/rehire volume and patterns

**Question:** "James O'Connor's record was frozen and flagged as a duplicate. How often do you get rehires or contractor-to-FTE conversions? And when you decide whether to reactivate vs create new — is there a rule, or do you work it out each time with IT?"

**Tension targeted:** Deliverable #2 rates non-standard classification as "Human-led + Agent Support." The escalation trigger (ET-1) fires for all non-standard types. If conversions and rehires follow patterns, the agent could classify with higher confidence.

**Design decision at stake:** If there are clear rules (e.g. "rehire gap <2 years → always reactivate; >2 years → new record") → agent can classify autonomously for rule-matching cases, lowering HITL rate. If case-by-case → agent remains a context-assembler for human decision. This shifts the HITL rate target from 15–20% to potentially 25–30%.

---

### Q5: Who updates ServiceNow routing rules when specs change?

**Question:** "When the consulting laptop spec changed last quarter, who was supposed to update ServiceNow routing? Did anyone tell your team it was changing? Or did you find out when Tom's ticket went wrong?"

**Tension targeted:** Artefact 1.1 reveals a governance gap — spec changes happen without routing updates. The OPC's spec repository is only valuable if there's a process for keeping it current.

**Design decision at stake:** If there's a governance path (division ops notifies HR Ops, who can update routing) → spec repository maintenance is achievable and OPC can trust its data. If nobody owns this (changes happen silently) → the spec repository will go stale too, and OPC needs a fallback: require human confirmation for every ticket where spec was last updated >X days. This changes the agent's confidence thresholds and escalation frequency.

---

## Priority 2 (High-Value — Refining the Design)

### Q6: Workday sync timing and consequences

**Question:** "You update the tracker first and refresh Workday end-of-week. Has a stale Workday record ever caused a problem downstream — payroll set up with wrong details, or someone querying Workday and getting outdated info?"

**Tension targeted:** Deliverable #5 notes Workday is not real-time [Artefact 1.2]. If stale Workday data causes downstream issues, the OPC should sync more frequently.

**Design decision at stake:** If stale data causes problems → OPC should sync tracker→Workday daily (not weekly), changing the "Agent acts, human notified" tier. If no downstream issues → weekly batch sync is fine and the agent's Workday write frequency stays low (lower risk, lower API cost).

---

### Q7: What triggers a hire becoming "high sensitivity"?

**Question:** "Tom's notes say 'Director's hire from Deloitte; sensitive about onboarding speed.' How do you know which hires are sensitive? Is it always director-level or consulting-division hires, or is it something you pick up from context — like a particular hiring manager or client-facing role?"

**Tension targeted:** The OPC's escalation logic depends on identifying "high sensitivity" hires early. If criteria exist, the agent can flag proactively. If it's tacit, the human must tag.

**Design decision at stake:** If criteria are articulable (division = consulting AND level ≥ senior → high sensitivity) → agent auto-flags at record creation. If tacit → human must manually tag risk level, and the agent relies on the tracker's "Risk flag" column being populated before it can calibrate escalation priority. This affects ET-3 trigger design.

---

### Q8: Previous automation attempts

**Question:** "The scenario mentions you've tried to automate before and things 'fell through the cracks.' What specifically was tried? Was it ServiceNow auto-routing, or something else? What broke?"

**Tension targeted:** Scenario brief quotes Priya: "every time we try to automate, something falls through the cracks because the edge cases never look the same twice." Understanding what failed before shapes what the OPC avoids.

**Design decision at stake:** If previous automation failed because edge cases weren't handled → confirms OPC needs robust exception detection (current design). If it failed because of system integration issues → may indicate hidden technical constraints not in the scenario (auth problems, rate limits, data quality issues worse than described). Changes risk assessment in Deliverable #5.

---

## Priority 3 (Depth — Useful But Not Design-Breaking)

### Q9: Badge and building access — same system or separate?

**Question:** "Badge ordering and building access — does that go through ServiceNow along with the laptop, or is there a separate facilities system?"

**Tension targeted:** Deliverable #5 assumption A4 from Deliverable #1 (badge via ServiceNow). If separate, OPC needs another integration.

**Design decision at stake:** If same system → no new integration needed. If separate → System/Data Inventory needs a new row; integration effort for Wave 1 increases.

---

### Q10: Coordinator workload distribution

**Question:** "How do you and the two coordinators split the work? Is it by division, by alphabet, round-robin — or do you just pick up whatever's next?"

**Tension targeted:** Deliverable #1 assumption A3. Affects how the OPC routes escalations (does it escalate to "the coordinator handling this case" or to Priya generically?).

**Design decision at stake:** If cases are assigned to specific coordinators → OPC escalation targets must be case-specific (route to the assigned coordinator). If ad hoc → OPC can escalate to a shared queue. Changes ET-1 and ET-4 target role from "HR Coordinator" to potentially a named person per case.

---

## Follow-up Probes (for stakeholder evasion)

If Priya gives vague answers, probe with:

- **If she says "it depends":** "Can you give me two recent cases where it went differently — what made the difference?"
- **If she says "we follow the process":** "The email about Tom's laptop suggests the process didn't work as documented. How often does that happen?"
- **If she says "everything is fine most of the time":** "When it's not fine — what does that look like? What's the worst onboarding you've had this year?"
- **If she says "the team just knows":** "If one of your coordinators was off sick for a week, what would break? What do they carry in their heads that isn't written down?"

