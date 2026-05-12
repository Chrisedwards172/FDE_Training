# Deliverable #1 — Problem Framing & Success Metrics

> **Engagement:** MedFlex — Agentic Transformation of Shift Matching  
> **Version:** Interim draft (Thursday EOD)  
> **Status:** Pre-pushback — will be revised against Marcus's Friday memo

---

## 1. The Stated Request vs. the Real Problem

### What Marcus asked for
*"10x the business without 10x-ing the coordinators"* — in 8 weeks.

### What this actually means
Marcus's $14M → $200M revenue target in 24 months requires MedFlex to handle ~14x the current shift volume with roughly the same coordinator headcount. Today, 8 coordinators make ~960 matching decisions/day with a 4.2-hour average time-to-fill. At 14x volume, that's ~13,400 decisions/day — impossible with manual matching.

### The real problem (grounded in discovery)
**MedFlex's matching process is entirely manual, cognitively intensive, and dependent on tribal knowledge — making it the binding constraint on business growth.**

Specifically:
1. **Free-text intake creates unnecessary cognitive load.** Hospital requests arrive as unstructured email/portal submissions into ServiceNow. Coordinators manually parse requirements (credentials needed, shift timing, facility type) before they can even begin matching. This is pure waste — parsing, not deciding.

2. **Matching is a multi-constraint search performed from memory and manual lookup.** Coordinators search across credentials, availability, proximity, hospital preferences, and nurse preferences — simultaneously. Experienced coordinators (10+ years) do this faster because they've internalised patterns; new coordinators take significantly longer. The knowledge isn't systematised.

3. **Speed is the competitive weapon, and MedFlex is losing.** Hospitals submit to multiple agencies. The first agency to respond with a qualified match wins. At 4.2 hours average time-to-fill, MedFlex loses to faster competitors — even when they have the better nurse.

4. **The no-confirmation model creates avoidable failures.** Nurses are notified by SMS/email but don't confirm — silence equals acceptance. 12% don't show up. MedFlex only discovers this when the hospital calls. This damages the relationship MedFlex lives on.

5. **Concurrent submission creates race conditions.** The same nurse gets submitted to multiple hospitals. When one confirms, MedFlex must withdraw from others. If two hospitals confirm simultaneously, MedFlex must "rework the proposal" — losing time and credibility.

### What this is NOT about
- **Not about credential verification.** Compliance is a separate team with a separate process. Credential status is already on the nurse profile card. The agent reads the status; it doesn't verify credentials. [CONFIRMED: Marcus, discovery session]
- **Not about replacing coordinators.** The recommendation engine failed because coordinators didn't trust it and feared for their jobs. The solution must evolve the coordinator role, not eliminate it.
- **Not about building a chatbot.** The chatbot failed because hospitals don't want to interact with a bot in a competitive market. The agent is internal — hospitals never see it.

---

## 2. Stakeholder-Specific Success Criteria

### For MedFlex (the business)
| What success looks like | Why it matters |
|---|---|
| Handle 14x volume with ≤2x coordinator growth | Enables $200M revenue target without proportional headcount cost |
| Time-to-fill < 1 hour (from 4.2h) | Competitive advantage: first agency to respond wins the placement |
| Coordinator adoption > 80% within 8 weeks of launch | Avoids recommendation engine failure mode (built but not used) |
| Reduced training time for new coordinators | Enables flexible team scaling as business grows |

### For hospitals (the customers)
| What success looks like | Why it matters |
|---|---|
| Faster response to shift requests | Hospitals submit to multiple agencies — speed wins |
| Better credential match (reduce mismatch component of 7% rate) | Fewer rejected submissions = stronger agency relationship |
| Fewer no-shows (reduce from 12%) | No-shows disrupt hospital operations and erode trust in MedFlex |
| Consistent quality regardless of which coordinator handles it | Hospital experience shouldn't depend on whether they get the 10-year veteran or the new hire |

### For nurses (the workers)
| What success looks like | Why it matters |
|---|---|
| Better shift matches to preferences and proximity | Nurses who get preferred assignments are less likely to no-show or defect to competitors |
| Proactive confirmation instead of silence-equals-acceptance | Reduces accidental no-shows from missed notifications |
| Transparent process (know why they were/weren't matched) | Trust in the agency; reduces defection to competitors |

---

## 3. Measurable KPIs

Two time horizons apply: the **8-week MVP** (Phase 1 — what Marcus sees first) and the **6-month mark** (Phase 2 — progressive autonomy). Success is measured at both; the 8-week targets are the gate for continued investment.

| KPI | Baseline (current) | Target (8-week MVP) | Target (6-month) | How measured |
|---|---|---|---|---|
| **Time-to-fill** | 4.2 hours avg | < 2 hours | < 1 hour | ServiceNow: timestamp(request received) → timestamp(hospital confirmation) |
| **Decisions per coordinator per day** | ~120 | ~200 (agent-assisted) | ~500+ (agent-led) | Agent dashboard: matches reviewed/approved per coordinator per shift |
| **Mismatch rate** | 7% | < 5% | < 3% | Hospital rejection reason codes (credential vs. preference) |
| **No-show rate** | 12% | < 8% | < 5% | Hospital-reported no-shows / total confirmed placements |
| **Coordinator adoption** | N/A (new system) | > 80% using agent daily | > 95% | Login/usage metrics: % of coordinators who use agent for > 50% of matches |
| **Agent match acceptance rate** | N/A | > 60% of agent-proposed matches accepted by coordinator | > 80% | Coordinator accept/reject/modify on agent proposals |
| **Intake parsing accuracy** | Manual (no baseline) | > 90% of free-text requests correctly parsed | > 95% | Spot-check sample: parsed fields vs. coordinator interpretation |

---

## 4. The "8 Weeks" Decoded

Marcus clarified in discovery: 8 weeks is not "complete transformation" — it's "show me what I can get for my investment." The 8-week deliverable should be an MVP that demonstrates measurable value on the primary matching workflow, not a full agentic transformation of all four workflow components.

**8-week MVP scope:** Agent-assisted matching for the highest-volume, most-structured shift requests (standard credential matches with availability confirmed). Coordinator reviews and approves. More complex matches (preference-heavy, competitive situations, partial matches) remain coordinator-led with agent context support.

**What "ROI in 8 weeks" looks like:** If the agent reduces average matching time from 4.2 hours to 2 hours on even 50% of requests, that's ~480 coordinator-hours/day saved — visible, measurable, and defensible to the board.

