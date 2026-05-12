# Deliverable 4 — Agent Purpose Document

> **Agent:** Dispatcher Decision Support Agent (DDSA)  
> **Primary target:** Delivery Exceptions (Work Stream 1, score 16)  
> **Archetype:** Human-led + Agent Support

---

## Assumption Log (Scenario & Design Assumptions)

| # | Type | Assumption | Confidence | Test |
|---|------|-----------|------------|------|
| A1 | AGENT | Reconciliation file (T-2 lag) does not surface manual override credits until the next batch cycle — Sandra's unaudited credits are invisible for 24–48h | Medium | Ask Sarah: "When Sandra applies a goodwill credit, how quickly does finance see it?" |
| A2 | AGENT | Exception logging in the dispatch console happens after the decision is communicated to the driver — there is a gap between verbal instruction and system record | Medium | Ask Sarah: "Do dispatchers log exceptions before or after calling the driver back?" |
| A3 | AGENT | ~80% of ETA inquiries are standard lookup; ~20% require dispatch/driver contact | Low | Ask Sarah: "What proportion of 'where's my delivery' calls need a dispatcher, vs just a system lookup?" |
| A4 | AGENT | Dispatchers currently spend ~5 min of the 12 min/case on context assembly (pulling route, account, history) before making the triage decision | Low | Ask Sarah: "When a driver calls in with an exception, how long does it take your team to pull up the context before they can decide?" |
| A5 | AGENT | The Driver App has a messaging API or webhook capability that can surface inbound signals to external systems | Medium | Ask IT/Sarah: "Can the Driver App push notifications to other systems, or is it self-contained?" |
| A6 | AGENT | Stein-Allen account value and sensitivity is known informally by dispatchers but not flagged in CRM or any system | Medium | Ask Sarah: "How does a new dispatcher know which accounts are sensitive? Is it written down anywhere?" |
| A7 | AGENT | The £500 high-value escalation threshold from the SOP is still approximately correct even though the SOP is stale | Low | Ask Sarah: "Is there a value threshold for Duty Manager escalation? Is it still £500?" |
| A8 | AGENT | Dispatchers handle delivery exceptions individually (not batched) — each case gets immediate attention as it arrives | Medium | Ask Sarah: "Do dispatchers work exceptions one at a time as they come in, or batch them?" |
| A9 | AGENT | Sarah's scepticism of chatbots does not extend to internal decision-support tools for her own dispatchers | Medium | Ask Sarah: "When you say you're sceptical of AI — is that customer-facing AI specifically, or any AI tool including internal ones?" |

---

## Agent Identity

```
Agent Name:        Dispatcher Decision Support Agent (DDSA)
Job to be Done:    When a delivery exception arrives (refused delivery, damage dispute, 
                   missed window), assemble the decision context — account profile, route 
                   pressure, exception history, consignment value — in seconds rather 
                   than minutes, so the dispatcher can make the triage call faster and 
                   with better information. The agent does NOT make the triage decision.

Business context:  Customer Operations, Apex Distribution Ltd. 35-person team handling 
                   ~180 delivery exceptions/day across Midlands, South, and East England. 
                   COO (Sarah Whitmore) wants to reduce exception handling time without 
                   introducing customer-facing automation. Two prior AI projects failed 
                   (customer chatbot 2024; RPA for billing 2024).
```

---

## Primary Objectives

1. **Reduce context-assembly time** — from ~5 min to <30 seconds per exception case, so dispatchers spend their 12 minutes on judgment, not lookup `[ASSUMED — A4]`
2. **Surface decision-relevant data proactively** — account sensitivity, route pressure (drops remaining + time), prior exception history for this account/driver, consignment value — before the dispatcher asks
3. **Detect patterns invisible to individual dispatchers** — repeat refusals from the same site, drivers with above-average exception rates, accounts trending toward escalation

---

## KPIs

> **Note on KPI template:** The standard ATX KPIs (Accuracy, Coverage, Throughput, Cost/case, HITL rate) assume an autonomous agent. DDSA is Human-led + Agent Support — HITL rate is 100% by architecture (not a metric to minimise). The KPIs below measure what matters for a support agent: speed, completeness, adoption, and signal quality.

| KPI | Target | Acceptable floor/ceiling | Measurement |
|---|---|---|---|
| **Context assembly time** | <30 seconds from signal receipt to full context display | Ceiling: 60 seconds (above this, dispatcher waits too long) | Time from inbound signal to context card visible to dispatcher |
| **Context completeness** | 90% of cases where all 4 context elements (account, route, history, value) are surfaced without dispatcher having to look them up manually | Floor: 75% | % of cases where dispatcher does not need to open a second system |
| **Dispatcher adoption** | 80% of dispatchers actively using the context card within 4 weeks | Floor: 60% | Usage analytics (card views per exception case) |
| **Exception handling time reduction** | 25% reduction in mean handling time (12 min → 9 min) | Floor: 15% reduction | Before/after mean handling time from dispatch console logs `[ASSUMED — A4]` |
| **False-alert rate** | <10% of account-sensitivity flags are overridden by dispatcher as irrelevant | Ceiling: 20% | % of flagged cases where dispatcher dismisses the flag |

---

## Failure Modes

### FM-1: Stale context card — data doesn't match reality

**Bad output:** Agent surfaces account info or route data that is outdated (e.g. route has already been re-sequenced by dispatch but GPS hasn't caught up). Dispatcher acts on wrong context.

**Consequence:** Wrong triage decision (e.g. "driver has 6 drops remaining" when actually 3 have been reassigned). Trust erosion — dispatcher stops consulting the card.

**Recovery:** Timestamp every data element on the context card. Flag data freshness ("GPS: 3 min ago" vs "GPS: 22 min ago — may be stale"). If GPS is >15 min stale, mark route pressure as "unverified" rather than displaying a number.

### FM-2: Over-alerting on account sensitivity — alert fatigue

**Bad output:** Agent flags too many accounts as "sensitive" because the classification rule is too broad (e.g. all B2B_VOLUME accounts flagged when only 2–3 are genuinely sensitive to the dispatchers).

**Consequence:** Dispatchers ignore sensitivity flags entirely. The signal becomes noise.

**Recovery:** Start with a conservative rule (only flag accounts where credit limit > £40K AND prior escalation in last 90 days). Tune based on dispatcher override rate. If override rate >20%, tighten the rule.

### FM-3: Agent surfaces incomplete history — dispatcher makes decision without key context

**Bad output:** Agent shows "no prior exceptions for this account" when in fact there were exceptions logged in the dispatch console that the agent can't read (limited API surface).

**Consequence:** Dispatcher treats a repeat-offender account as a first-time refusal. Wrong calibration of response.

**Recovery:** Display "History: CRM only — dispatch console history not available" so the dispatcher knows the limitation. Include a "check dispatch console" prompt for high-value accounts. Log cases where dispatcher overrides to add context manually — these are integration gap signals.

### FM-4: Agent acts beyond delegation boundary — makes or implies a triage recommendation

**Bad output:** Agent displays "Recommended action: return to depot" based on pattern matching, and dispatcher follows it without applying their own judgment (authority drift).

**Consequence:** Agent is effectively making triage decisions by proxy. When a recommendation is wrong and cargo is lost, accountability is unclear.

**Recovery:** The agent MUST NOT present recommendations as actions. It presents context and options, never a single recommendation. UI design: display "Options: Return / Leave / Hold / Re-attempt" with trade-offs for each — never highlight one. If the system detects a dispatcher always selecting the first-displayed option, flag to operations lead.

---

## Delegation Archetype

**Human-led + Agent Support**

**Rationale (from D2):** Delivery exception triage scores: Input Structure = L, Decision Determinism = L, Context Complexity = H, Exception Rate = H, Latency Constraint = H, Risk/Compliance = H. The core decision (return/leave/hold/re-attempt) cannot be delegated — it carries liability for lost goods and customer relationships. But the context-assembly step is where most time is wasted and where the agent creates measurable value.

**Adjacent archetype rejected (Agent-led + oversight):** The 2024 chatbot failed because it made decisions customers disagreed with. An agent-led exception triage system would face the same trust problem internally — dispatchers won't accept an AI making calls that could lose a £2,000 pallet or a key account. Sarah is explicitly sceptical of autonomous AI; a support tool that makes her team faster (not redundant) is the politically viable and technically correct architecture.

**Adjacent archetype rejected (Human-only):** The agent doesn't decide but it materially changes the decision quality and speed. Without it, dispatchers spend 5 minutes pulling context from 3 systems. With it, they spend 30 seconds reviewing a pre-assembled card. That's not "human-only" — it's human-led with substantive agent contribution.

---

## Escalation Triggers

| # | Condition | Target | Urgency |
|---|---|---|---|
| ET-1 | Consignment value >£500 AND no Duty Manager currently on shift | Operations Lead | Immediate — driver is waiting |
| ET-2 | Account classified as high-sensitivity AND exception is 2nd+ in 30 days for this account | Dispatcher + account manager notification | Within exception handling window |
| ET-3 | Driver has been waiting >15 minutes with no dispatcher response (all lines busy — like Mark's situation) | Queue priority escalation — next available dispatcher sees it first | Automatic |
| ET-4 | Context card cannot be assembled (system outage — CRM or Driver App unreachable) | Alert dispatcher: "Context unavailable — proceed manually" | Immediate — do not block dispatcher |
| ET-5 | Agent confidence in account classification <70% (new account, sparse history) | Flag to dispatcher: "Account sensitivity unknown — check manually" | Within context card display |

---

## Autonomy Matrix

### AGENT DECIDES ALONE (no human input):
- Poll Driver App for inbound exception signals (continuous)
- Pull route data, GPS position, drops remaining from dispatch console / Driver App
- Pull account record from CRM (contract type, credit limit, account manager, prior exceptions)
- Pull exception history for this account (last 90 days from CRM)
- Assemble context card and display to next available dispatcher
- Calculate route pressure score (drops remaining × time-of-day factor)
- Classify account sensitivity using rule: credit limit >£40K AND prior escalation in 90 days

### AGENT ACTS, DISPATCHER NOTIFIED:
- Flag account as high-sensitivity on the context card (dispatcher can override)
- Prioritise exception in queue if driver wait time >15 minutes (ET-3)
- Log context card delivery timestamp for performance metrics
- Surface "repeat pattern" alert if 2+ exceptions from same account in 30 days

### AGENT PROPOSES, DISPATCHER DECIDES:
- Present triage options (Return / Leave / Hold / Re-attempt) with trade-off notes per option
- Suggest "check with site manager" option if refusing party appears unauthorised (based on contact role in CRM ≠ "site manager" or "operations manager")
- Propose Duty Manager escalation when value >£500 threshold detected (ET-1)

### AGENT MUST NOT:
- Make or recommend a specific triage decision (return/leave/hold/re-attempt)
- Contact the driver directly with instructions (only dispatcher does this)
- Contact the customer or recipient
- Override a dispatcher's flag or decision
- Modify dispatch routes or assignments
- Apply any credits, financial adjustments, or billing changes
- Access or interact with Aurum Billing in any way
- Present a single "recommended action" — always present options with trade-offs

---

## Activity Catalog

| Activity | Trigger | Inputs | Outputs | Autonomy tier |
|---|---|---|---|---|
| Detect inbound exception | Driver App signal (message/voicemail transcript) | Driver ID, route code, message content | Exception case created; routed to dispatcher queue | Decides alone |
| Assemble context card | Exception case created | CRM account data, route data (GPS, drops), exception history (90 days), consignment manifest | Formatted context card with 4 sections: Account, Route, History, Value | Decides alone |
| Classify account sensitivity | Context card assembly | Credit limit, contract type, escalation history | Sensitivity flag (High/Standard/Unknown) | Acts, dispatcher notified |
| Detect driver wait breach | Continuous monitoring of open exceptions | Exception creation timestamp, dispatcher assignment status | Queue priority escalation (ET-3) | Acts, dispatcher notified |
| Present triage options | Context card viewed by dispatcher | All context elements + trade-off logic | Options display with per-option notes | Proposes, dispatcher decides |
| Detect repeat pattern | Context card assembly | Account exception history (90 days) | "Repeat pattern" alert on context card | Acts, dispatcher notified |
| Propose Duty Manager escalation | Value >£500 detected in consignment manifest | Consignment value, Duty Manager availability | Escalation proposal on context card | Proposes, dispatcher decides |

---

## Operating Parameters

### Context card contents (4 sections):

**1. Account**
- Customer name, contract type (B2B_VOLUME / B2B_STANDARD), credit limit
- Account manager name
- Sensitivity flag (High / Standard / Unknown) with rule basis
- Last 3 exceptions for this account (date, type, outcome)

**2. Route**
- Route code, driver name, current GPS position (+ freshness timestamp)
- Drops remaining on route (count + next drop ETA)
- Route pressure score: `(drops_remaining × 1.5) + (hours_until_depot_close × 2)`
- If GPS >15 min stale: "⚠️ Route data may be stale"

**3. History**
- Exception count for this account (30 / 90 / 365 days)
- Exception count for this driver (30 days)
- Most common exception type for this account
- If repeat pattern detected: "⚠️ 2nd+ exception in 30 days — escalation risk"

**4. Value**
- Consignment value (from manifest/CRM if available)
- If >£500: "⚠️ High-value threshold — Duty Manager escalation may apply"
- If value unknown: "Value: not available — ask driver or check manifest"

### Response time SLA:
- Context card must be assembled and displayed within 30 seconds of signal receipt
- If any data source is unreachable, display partial card with "unavailable" markers — never block on a timeout

---

## System Dependencies

| System | What DDSA needs | Access type | Constraint |
|---|---|---|---|
| CRM (Salesforce) | Account records, case history, communications | Read (REST API) | None — API available |
| Driver App | Inbound exception signals, GPS, route progress | Read (API/webhook) | `[ASSUMED — A5]` API availability not confirmed |
| Dispatch console | Route data, drops remaining, driver assignment | Read (limited API) | Major constraint — "limited API surface" per scenario. May need screen-scrape or data export as fallback. |
| Aurum Billing | **None** — DDSA does not interact with billing | N/A | Out of scope by design |

