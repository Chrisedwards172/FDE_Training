# Discovery Synthesis — Marcus Reyes Role-Play (Thursday Morning)

> **Session:** Thursday 09:30–~10:30 CET  
> **Stakeholder:** Marcus Reyes (CEO), played by coach  
> **Format:** Combined squad session (~17 participants)  
> **Participant:** Chris Edwards  

---

## 1. New Facts Confirmed (not in scenario pack)

| Fact | Source (timestamp) | Confidence | Design impact |
|---|---|---|---|
| Revenue: **$14M current → $200M target in 2 years** (~14x growth) | Marcus @ 52:02 | Stated | "10x" is actually ~14x. The growth target is revenue-driven, not volume-driven. |
| **ServiceNow** is the centralized request system — all channels (email, portal, phone) land in ServiceNow | Marcus @ 17:22 | Stated | Integration target identified. ServiceNow is the intake queue. |
| Hospital requests arrive as **free text** in ServiceNow — coordinators see raw free text | Marcus @ 17:40, 16:22 | Stated | Agent opportunity: NLP parsing of free-text shift requests into structured data. This is where agent reasoning adds value a rule engine can't. |
| **Email is the biggest channel** for hospital requests | Marcus @ 8:10 | Stated | Email parsing is the primary intake pathway. |
| Compliance/credential verification is a **separate team, separate process** — not the coordinator team | Marcus @ 6:58, 19:13, 20:52 | Stated repeatedly | Coordinator matching assumes credentials are already verified. Scope implication: credential verification is OUT of scope for this engagement. |
| Nurse credential status is **shown on the nurse's profile card** — coordinators can see it at matching time | Marcus @ 34:19 | Stated | Agent can read credential status as a structured field. The agent doesn't need to verify credentials — just check the status. |
| **Nurses self-update availability** in a system | Marcus @ 19:49, 34:52 | Stated | Agent can read availability data. But see Contradiction #1 below. |
| Matching is **fully manual** — experienced coordinators faster due to **tribal/gut knowledge** | Marcus @ 15:49, 47:15 | Stated | The matching skill is partially tacit. 10+ year coordinators have pattern knowledge. Agent needs to capture and systematise this. |
| **Same nurse submitted to multiple hospitals simultaneously** | Marcus @ 55:36 | Stated | **Concurrency problem.** When hospital confirms, nurse is withdrawn from other submissions. This is a key design challenge. |
| Nurse notification: **SMS or email** (nurse preference). **No confirmation required** — silence = acceptance | Marcus @ 40:05, 44:23 | Stated | Explains the 12% no-show rate partly — nurses don't actively confirm. |
| Nurses must notify **within 24 hours** if they can't attend. Shifts typically **2–3 days in advance** | Marcus @ 45:26, 45:32 | Stated | Tight backfill window. Agent needs rapid rebooking capability. |
| **No-shows discovered reactively** — hospital calls MedFlex | Marcus @ 38:08 | Stated | No proactive no-show detection. Agent opportunity: predictive flagging + proactive confirmation. |
| No direct financial cost of mismatch — **reputational impact**, once had to give a discount | Marcus @ 25:32, 50:06 | Stated | Risk is relationship-based, not financial penalty. |
| Training new coordinators is **time-intensive** — Marcus wants to minimize this if team grows | Marcus @ 29:25 | Stated | Agent can reduce training burden by encoding matching logic. |
| Marcus's two concerns about AI: **(1) matching accuracy, (2) team adoption/job security fears** | Marcus @ 46:01 | Stated directly | Design must address both: transparent matching logic + coordinator role evolution (not replacement). |

---

## 2. Contradictions Identified

### Contradiction 1: Nurse availability is "fine" vs. 12% no-show rate

**What Marcus said:** "So far so good, no problem there" regarding nurse self-updated availability (34:52). "Correct" when asked if availability data is kept up to date (21:07).

**What the scenario says:** 12% no-show rate. Nurses don't confirm assignments (silence = acceptance). Hospital discovers no-shows, not MedFlex.

**The gap:** If availability data is accurate and reliable, why is there a 12% no-show rate? Either (a) nurses' self-reported availability is unreliable (they mark available but aren't really), (b) competitive poaching — nurses accept assignments from other agencies after being submitted, or (c) the notification-without-confirmation model means nurses sometimes don't see the notification. Marcus's "no problem" is contradicted by the 12% no-show figure. The scenario pack's sample contradiction ("When a nurse calls in sick they call Kim, and Kim updates the schedule by hand") wasn't directly surfaced, but the structural inconsistency is the same: the "source of truth" for availability isn't as reliable as claimed.

**Design implication:** Agent should include proactive confirmation workflow + no-show risk scoring. Don't trust availability data at face value.

### Contradiction 2: Compliance is "not an issue" vs. 7% mismatch rate includes credential mismatches

**What Marcus said:** "Not an issue" regarding compliance (20:52). Repeatedly deflected compliance questions as a "separate team, separate process."

**What the scenario says:** "Mismatch rate (wrong credentials for facility type): 7%." If credentials are verified by a separate team before matching, and credential status is visible on the nurse card, why are 7% of matches credential mismatches?

**Possible explanations:** (a) Credential status on the nurse card lags behind actual state (stale data), (b) coordinators bypass credential checks under time pressure (competitive urgency), (c) the "7% mismatch" includes soft-match failures (hospital preferences), not just credential violations. Marcus partially confirmed (c) at 9:58 — mismatch includes hospitals selecting competitors' nurses based on feedback quality, not just credential gaps.

**Design implication:** Agent should not rely solely on nurse card credential status. Agent should cross-reference credential expiry dates against shift dates. The "mismatch" metric needs decomposition — hard credential violations vs. soft preference mismatches.

### Contradiction 3: "Automate everything" vs. tacit coordinator knowledge + adoption fears

**What Marcus said:** "My goal is to automate as much as possible" (42:37). "Nothing I can recall" when asked about parts that shouldn't be handed over. BUT also: experienced coordinators have "gut feeling" (47:15), team "refused the previous solution" (46:01), "lack of training and lack of trust" caused recommendation engine failure, and "thinking that it might be risk for their job security" (46:48).

**The gap:** Marcus wants full automation but his own team has already rejected an AI recommendation engine. The coordinators who do the work have tacit knowledge the system can't capture yet, and they're scared of being automated away.

**Design implication:** DO NOT design for fully agentic matching. Design for agent-led + coordinator oversight — the agent does the matching, the coordinator reviews and approves. This is the architecture that (a) captures tacit knowledge over time via coordinator feedback, (b) addresses adoption fears, and (c) doesn't repeat the recommendation engine failure.

### Near-Contradiction 4: Nurse submitted to multiple hospitals simultaneously

**What Marcus said:** Same nurse submitted to multiple hospitals. When one confirms, they withdraw from others. If multiple hospitals confirm the same nurse simultaneously — "then we rework our proposal" (56:01).

**The gap:** This is a concurrency race condition. It partially explains no-shows (a nurse gets confirmed by two hospitals through different agencies) and creates a design challenge: the agent must track which nurses are "in flight" across simultaneous submissions and handle withdrawal/rebooking atomically.

**Design implication:** Agent needs a reservation/locking model — when a nurse is submitted, they're "soft-locked" until the hospital responds or a timeout expires. Concurrent submissions require a priority queue.

---

## 3. What Marcus Deferred (information gaps)

| Topic | Deferred to | What we still don't know | Impact on design |
|---|---|---|---|
| Day-to-day coordinator workflow details | "Head of operations" | Exact cognitive steps in matching decision — what coordinators look at, in what order, for how long | Need to assume from scenario pack + artefacts |
| Compliance verification process details | "Legal team" / "Compliance" (Linda) | How state regulatory databases are accessed, API availability, verification cadence | Design assumption: credential status is on nurse card; agent reads that field |
| Systems/IT architecture | "Aaron in IT" | Database schema, ServiceNow API, integration capabilities | Design assumption: ServiceNow API available; nurse DB accessible |
| Quality score reliability | Vague: "Trust me, it's reliable" | What the quality score measures, how it's calculated, whether it correlates with the 7% mismatch | Design assumption: quality score exists but needs validation |
| Financial impact of no-shows | "Not black and white" | Actual cost per no-show, impact on contracts | Design can use reputational risk framing — not hard financial numbers |

---

## 4. Coach Feedback (post-session debrief)

The coach broke character at ~57 minutes and gave direct feedback:

1. **Too much time on compliance** — Marcus said it was a separate process early on. The squad kept asking. Coach said: "As soon as I said that's separate thing, nothing to do with the currency. Done." Lesson: when the CEO explicitly scopes something out, don't keep probing it.

2. **Didn't catch contradictions clearly** — One squad member asked directly "I don't think we caught any contradictions, did we?" The key contradiction surfaced late was the multi-hospital submission model.

3. **Should focus on one problem well** — Coach: "I would prefer you at least solve one business problem, but solve it properly." The primary business problem is **matching workflow optimisation**, not compliance verification.

4. **The matching cognitive load wasn't fully mapped** — Benoit noted the squad didn't get deep enough into the jobs-to-be-done within matching to identify breakpoints and delegation opportunities.

---

## 5. Answers to Pre-Prepared Discovery Questions

| Discovery question | Answer from session | Confidence |
|---|---|---|
| **Q1. How does a coordinator decide?** | Match qualification + availability on specific slot. Experienced people do it faster (gut feeling). 10+ year coordinators have patterns. All manual against free-text requests. | Medium — Marcus deferred operational detail to head of ops |
| **Q2. Why did the AI projects fail?** | Chatbot: customer-facing in competitive market — hospitals didn't want to chat with one of many agency bots. Recommendation engine: "too many mistakes" — combination of technical gaps + insufficient training. Team distrusted it + feared job security. | High — direct from Marcus |
| **Q3. Credential verification — real process?** | Separate team does onboarding + periodic rechecks. Status shown on nurse profile card. Coordinators just see the card. | High — consistent across multiple answers |
| **Q4. 7% mismatch root cause?** | Hospital-flagged. Partially credential mismatch, partially hospital preference (selecting competitors' nurses based on feedback). They'd rather submit a partial match than nothing. | Medium — Marcus was vague on the split |
| **Q5. 12% no-show root cause?** | Nurses don't actively confirm (silence = acceptance). Competitive market — may go to other agencies. Hospital discovers no-show reactively. MedFlex can offboard repeat offenders. | Medium — multiple factors, Marcus was honest about not knowing all reasons |
| **Q6. Systems landscape?** | ServiceNow (centralized queue), nurse database, credential status on nurse cards. All manual matching. Email = biggest channel. SMS/email for nurse notification. | High |
| **Q7. Nurse availability source of truth?** | Nurses self-update in a system. Marcus says "no problem." **Contradicted by 12% no-show rate.** | Low — self-reported data, unreliable |
| **Q8. Hospital preferences?** | Exist but informal. Competitive market means hospitals choose from multiple agencies. Hospitals provide feedback but no industry-standard ranking. MedFlex marks feedback in their system. | Medium |
| **Q9. Time pressure dynamics?** | Average 4.2h to fill. Queue-driven — more requests = longer time. Competitive urgency: faster response = higher win rate. | High |
| **Q10. 8-week timeline?** | Not a hard deadline. Marcus wants "best proposal for what I can get in 8 weeks" and to "start getting money back" on investment. Flexible on scope within the timeline. | High — Marcus was clear: show ROI in 8 weeks, not complete transformation |

---

## 6. Design Implications Summary

### Primary target confirmed: **Shift Matching Workflow**

The agent opportunity is in the matching process — specifically:
1. **Free-text intake parsing** (email/ServiceNow → structured shift request) — agent reasoning vs pure NLP
2. **Candidate matching** (multi-constraint: credentials + availability + proximity + preferences + hospital feedback) — agent reasoning over context
3. **Concurrent submission management** (same nurse → multiple hospitals; withdrawal on confirmation) — agent coordination
4. **No-show prediction and proactive confirmation** — agent pattern detection

### Out of scope (confirmed by CEO):
- Credential/compliance verification (separate team, separate process)
- Hospital-facing portal changes
- Nurse-facing app
- Pricing/margin optimization

### Architecture direction:
- **Agent-led + coordinator oversight** — NOT fully agentic. Matches the trust problem (two failed AI projects) and adoption risk (team job security fears).
- **Coordinator evolves from "finder" to "reviewer"** — agent proposes match, coordinator approves (especially for edge cases, high-value hospitals, and preference-heavy requests).
- **Progressive autonomy** — simple matches (credentials match, availability confirmed, no preference conflicts) can go faster; complex matches (preferences, partial matches, competitive situations) get human review.

### The "10x" answer:
Current: $14M revenue, 8 coordinators, ~960 decisions/day, 4.2h time-to-fill.
Target: $200M in 2 years (~14x), same or slightly larger team, <1h time-to-fill.
The agent must enable **each coordinator to handle 14x the volume** by removing the manual search/matching cognitive load and leaving them with review/approve/exception handling.

