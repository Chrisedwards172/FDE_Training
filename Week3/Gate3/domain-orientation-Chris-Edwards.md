# Domain Orientation — Healthcare Staffing (MedFlex Context)

> **Purpose:** AI-accelerated domain orientation per the Week 3 time budget. Build enough context to listen intelligently during discovery — not to become a domain expert.

---

## Industry Context

**Healthcare staffing agencies** sit between hospitals (demand) and nurses (supply), filling temporary or per-diem shifts. It's a $20B+ US market growing at ~7% annually, driven by chronic nursing shortages and hospital cost pressure.

**MedFlex's position:** Regional (5 states), 200 employees, B2B (hospital systems) and B2C (travel nurses). Series B = growth-stage, not startup. Board expects significant expansion in 24 months.

---

## The Matching Problem

The core workflow is **shift matching** — hospitals need a nurse with specific credentials for a specific shift; coordinators find one from the available pool.

### What makes it hard (cognitive dimensions):

1. **Multi-constraint optimisation:** Each match weighs: credentials (hard constraint), proximity, availability, nurse preferences, hospital preferences, cost (bill rate vs. pay rate), compliance status, historical performance.

2. **Credential complexity:** US healthcare credentials are state-regulated. A nurse licensed in Ohio may not work in Pennsylvania without reciprocity or compact license. Credentials include:
   - State nursing license (RN, LPN, NP — each state has its own board)
   - Specialty certifications (ICU, NICU, OR, L&D, etc.)
   - BLS/ACLS/PALS (life support certs — expire and need renewal)
   - Background checks (state and federal)
   - Facility-specific requirements (orientation, drug screening, TB testing)
   - Nurse Licensure Compact (NLC): 41 states participate — a compact license lets a nurse work in any member state

3. **Time pressure:** Emergency shifts may need filling in hours. Planned shifts give days. The mix determines whether matching can be batch (agent + review) or must be real-time (agent-led).

4. **Relationship dynamics:** Hospitals develop preferences for specific nurses. Nurses develop preferences for specific units/hospitals. These are often informal — in coordinators' heads, not in systems.

5. **No-shows and cancellations:** 12% no-show rate means the agency needs rapid backfill capability. Predictive no-show risk (based on nurse history, shift timing, distance) is a natural agent capability.

---

## Regulatory Landscape (5-state region)

- **State nursing boards** — each state has its own licensing authority, verification portal, and renewal timeline
- **Joint Commission** — hospital accreditation body; requires credentialed staff
- **CMS (Centers for Medicare & Medicaid)** — federal requirements for facilities receiving Medicare/Medicaid
- **HIPAA** — patient data privacy (the agent must not access patient records; it handles staffing data)
- **NLC (Nurse Licensure Compact)** — simplifies multi-state practice but not all states participate
- **Background check requirements** vary by state — some require state + federal, some accept portable background checks

**Key risk:** If MedFlex sends a nurse with lapsed or wrong credentials, the hospital faces regulatory penalty. The 7% mismatch rate is not just a quality issue — it's a compliance risk.

---

## Why Prior AI Projects Failed (hypotheses to validate)

### Chatbot (hospitals rejected)
Likely causes:
- Hospitals don't want to interact with a bot — they want a coordinator who understands urgency
- Chatbot couldn't handle the multi-constraint matching (just did intake, not matching)
- Hospital administrators value the relationship with "their coordinator"
- **Design implication:** Don't put AI between the hospital and MedFlex. Put it behind the coordinator.

### Recommendation engine (nobody used)
Likely causes:
- Recommendations didn't match how coordinators actually decide (wrong criteria, missing relationship data)
- Coordinators didn't trust the recommendations (black box)
- The engine suggested nurses but coordinators still had to verify credentials manually
- **Design implication:** The agent must do the work, not just suggest. And it must be transparent about why.

---

## Where Agents Could Add Value (pre-discovery hypotheses)

| Workflow step | Current state | Agent opportunity | Delegation hypothesis |
|---|---|---|---|
| **Shift intake** (hospital submits request) | Email/portal/phone → coordinator manually parses | Agent parses structured + unstructured intake, normalises to standard format | Agent-led + oversight |
| **Credential matching** (hard constraint check) | Coordinator manually checks state databases | Deterministic lookup — RPA first, agent for interpretation of edge cases (compact licenses, pending renewals) | RPA for clear matches; agent for edge cases |
| **Availability matching** | Coordinator checks system + calls/texts nurses | Agent reads availability system, contacts nurses for confirmation | Agent-led + oversight (if system is reliable); Human-led if availability data is stale |
| **Preference matching** (soft constraints) | Coordinator uses relationship knowledge | Agent surfaces historical data (past placements, ratings, preferences) — but tribal knowledge is hard to systematise | Human-led + agent support |
| **No-show prediction** | Reactive — scramble when nurse doesn't show | Agent flags risk based on patterns (nurse history, shift timing, distance, weather) | Agent-led + oversight |
| **Compliance verification** | Manual check against state portals | Agent monitors license/cert status, flags expirations proactively | Agent-led + oversight (or RPA for simple expiry checks) |
| **Backfill orchestration** | Coordinator manually re-matches when cancelation/no-show | Agent auto-identifies backup nurses from availability pool | Agent-led + oversight (time pressure argues for more autonomy) |

---

## Key Questions the Domain Raises

1. **Is credential verification deterministic or judgment-heavy?** If states have clean APIs with clear pass/fail, it's RPA. If it requires interpreting equivalencies, it's agent territory.
2. **Is the matching problem solvable with rules, or does it require reasoning?** If 80% of matches are credentials + proximity + availability, a rule engine works. If relationship preferences and hospital politics matter, an agent that reasons over context adds value.
3. **Where is the data?** If nurse availability is in a system, the agent can use it. If it's in Kim's head, the agent has a cold-start problem.
4. **What's the trust barrier?** Two failed AI projects = high scepticism. The agent must prove value before expanding scope. MVP must be narrow and visibly useful.

---

## "10x Without 10x-ing" — What It Actually Means

Marcus's aspiration decoded:
- Currently: 8 coordinators × 120 decisions/day = 960 decisions/day
- 10x: 9,600 decisions/day with roughly the same headcount
- That means the agent must handle the volume increase — either by making decisions autonomously or by making coordinators 10x more efficient

**Architectural implication:** This isn't about incremental efficiency. It's about fundamentally changing the coordinator's role from "find and match" to "review and approve agent matches." The agent must be the primary matching mechanism, not a recommendation sidebar.

**But:** "10x without 10x-ing" is also CEO aspiration language. The real question is: what's the first credible step? An 8-week MVP that proves the agent can handle one workflow (e.g., credential verification + simple shift matching) at coordinator-equivalent quality is more valuable than a blueprint for 10x that never ships.

