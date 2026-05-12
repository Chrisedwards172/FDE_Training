# Deliverable 2 — Delegation Suitability Matrix

> **Input:** Micro-task inventory from Deliverable 1 (18 micro-tasks across 2 work streams)  
> **Scoring:** 7 delegation suitability dimensions per `atx-scoring.md`

---

## Suitability Gate (Pre-Filter)

Before scoring, filter tasks that are not agent candidates:

| Task cluster | Gate result | Reason |
|---|---|---|
| Receive & parse driver signal | **Pass** — scored as part of "Assess damage credibility" | Unstructured input (voicemail/message) interpretation is the first micro-task within the triage judgment; scored below as the Input Structure dimension of "Assess damage credibility" |
| Pull route context + account info | **Route to automation/RPA** | Deterministic lookup; no judgment; H determinism, H input structure |
| Instruct driver (post-decision) | **Route to automation/RPA** | Once decision made, instruction is deterministic message send |
| Log exception in dispatch console | **Route to automation/RPA** | Structured form fill; no judgment |
| Receive dispute & identify invoice | **Pass** — proceeds to scoring | Requires parsing free-text email to extract invoice reference |
| Match invoice to surcharge/fee line | **Route to automation/RPA** | Deterministic data join on INVOICE_NO across CSVs |
| Check customer dispute history | **Route to automation/RPA** | Deterministic lookup in DISPUTES_OPEN + CRM |
| Apply credit (execution) | **Conditional** — standard path is automatable; manual override is not | Split: standard credit = automation; override = human |
| Notify customer | **Pass** — proceeds to scoring | Requires contextual composition (not template-only) |

**4 tasks routed to automation/RPA** (not agent territory): route/account lookup, driver instruction relay, exception logging, invoice-to-surcharge matching, dispute history lookup.

---

## Suitability Scoring Table

| Task cluster | Input Structure | Decision Determinism | Tool Coverage | Context Complexity | Exception Rate | Latency Constraint | Risk/Compliance | Key drivers | **Archetype** |
|---|---|---|---|---|---|---|---|---|---|
| **Assess damage credibility** | L | L | L | H | M | H | M | No visual data; verbal-only input; driver vs customer conflict; time pressure | **Human-only** |
| **Determine account sensitivity** | H | M | H | M | L | M | M | CRM data available but "key account" not systematically flagged; heuristic knowledge | **Agent-led + human oversight** |
| **Decide: return/leave/hold/re-attempt** | L | L | L | H | H | H | H | Highest-judgment task; synthesises ambiguous inputs under time pressure; wrong call = lost goods or lost customer | **Human-led + agent support** |
| **Escalate to Duty Manager** | M | M | M | M | M? | H | H | Threshold exists (>£500) but §4.3 undocumented; context packaging needed | **Human-led + agent support** |
| **Classify dispute type** | M | M | H | M | M | L | L | Customer language needs interpretation but maps to finite set of codes; batch data available | **Agent-led + human oversight** |
| **Determine if claim is valid** | L | L | M | H | H | L | H | Requires cross-referencing delivery exception with billing data; no documented validation rules; financial judgment | **Human-led + agent support** |
| **Decide credit amount** | M | L | L | H | H | L | H | No visible policy (Sandra chose half); discretionary; audit implications | **Human-only** |
| **Choose mechanism (standard/override/ticket)** | M | L | M | M | M | M | H | Trade-off between speed, audit compliance, and Aurum constraints; compliance risk is high | **Human-led + agent support** |
| **Notify customer** | M | H | H | L | L | M | L | Template-able for standard cases; contextual for disputes with history; CRM/email available | **Agent-led + human oversight** |
| **Coordinate billing ↔ Customer Ops** | L | L | L | H | H | M | M | No shared queue; no protocol; organisational boundary; every dispute crosses it | **Human-led + agent support** |

---

## Archetype Distribution

| Archetype | Count | Task clusters |
|---|---|---|
| **Fully Agentic** | 0 | — |
| **Agent-led + Human Oversight** | 3 | Determine account sensitivity, Classify dispute type, Notify customer |
| **Human-led + Agent Support** | 5 | Decide return/leave/hold/re-attempt, Escalate to Duty Manager, Determine claim validity, Choose mechanism, Coordinate billing↔Ops |
| **Human-only** | 2 | Assess damage credibility, Decide credit amount |
| **Routed to RPA/automation** | 4 | Route/account lookup, Instruction relay, Exception logging, Invoice matching, Dispute history lookup |

**No task cluster is fully agentic.** This is a high-judgment, time-pressured, ambiguous-input domain. The richest agentic opportunity is in the *support* layer — accelerating human decisions with pre-assembled context, pattern detection, and data matching — not in replacing the decisions themselves.

---

## Archetype Rationale

### Human-only: Assess damage credibility

The dispatcher must judge whether a pallet is actually damaged based on a driver's verbal description over voicemail, with no visual evidence, while the customer (an unauthorised warehouse worker) insists otherwise. No system, API, or structured data supports this judgment today. Tool/API Availability = L. Input Structure = L. Even with photo evidence (future state), the damage-vs-cosmetic determination is a liability call, not a pattern-matching exercise. **Adjacent archetype rejected (Human-led + agent support):** an agent could surface account value and route pressure, but the core judgment (is the damage real?) cannot be delegated — it carries insurance and contractual liability `[Artefact 1]`.

### Human-only: Decide credit amount

Sandra chose £170 on a £340 surcharge with no documented guideline. The disputes CSV shows another credit (CR-2026-00814, £88) to the same customer for a different invoice — also GOODWILL, also without a clear formula. There is no visible credit policy: no percentage rule, no approval threshold, no delegation authority documented anywhere in the artefacts. Until a credit policy exists, this is pure human discretion. **Adjacent archetype rejected (Human-led + agent support):** an agent could suggest a range based on historical precedent, but without a policy guardrail, any autonomous action carries financial and audit risk. The compliance dimension alone (H) keeps this human-only `[Artefact 2, CREDITS CSV]`.

### Human-led + agent support: Decide return/leave/hold/re-attempt

The decision synthesises: driver assessment (unreliable — no photos), customer refusal authority (warehouse worker ≠ site manager), account value (Stein-Allen = "the big one"), route pressure (6 drops), and time of day. Context Complexity = H, Decision Determinism = L, Exception Rate = H. **But the agent can materially help:** surface the account tier from CRM, show the route remaining (drops + time), pull prior refusal history for this account, and present options with trade-offs. The human decides; the agent accelerates context assembly from ~5 min to seconds. **Adjacent archetype rejected (Agent-led + oversight):** the liability and route-cascade consequences of a wrong autonomous call are too high for oversight-only; the human must own the decision `[Artefact 1, scenario brief]`.

### Human-led + agent support: Determine if claim is valid

Requires cross-referencing a billing dispute with a delivery exception (different systems, different teams). Did the delivery actually arrive damaged? Was an exception logged? Is the customer's claim consistent with dispatch records? Today, Sandra must manually link these. An agent could: (a) match the dispute invoice to any delivery exception logged for that route/date, (b) surface the delivery scan record and GPS data, (c) flag inconsistencies. But the *validity determination* is judgment — especially when the exception record is incomplete (§4.3 is "TBD") and the customer's claim can't be verified from system data alone `[Artefact 2 + Artefact 4]`.

### Human-led + agent support: Choose mechanism (standard/override/Aurum ticket)

Three options exist, each with different speed, compliance, and cost profiles. The standard credit path is auditable (AUDIT_REF present in CSV). The manual override is fast but leaves no trail. The Aurum ticket is correct but takes 48h. An agent could present the options with compliance flags (e.g. "Override: fast but no audit entry — compliance risk") and recommend standard path with auto-generated AUDIT_REF. But the final choice — especially the decision to bypass audit — cannot be delegated. **Adjacent archetype rejected (Agent-led + oversight):** the audit bypass decision carries personal accountability; Risk/Compliance = H `[Artefact 2 internal note, CREDITS CSV]`.

### Human-led + agent support: Coordinate billing ↔ Customer Ops

No shared queue exists. Billing deflects to Ops via template response (Artefact 2, msg 2). The customer must re-explain. Context is lost. An agent could: route the dispute to the correct team with context pre-attached, flag when a dispute has already bounced, and alert when customer wait exceeds threshold. But the organisational coordination (who owns this dispute?) is a human protocol problem — not solvable by an agent alone `[Artefact 2]`.

### Human-led + agent support: Escalate to Duty Manager

The £500 threshold exists in the SOP but the SOP is stale. The real escalation criteria are undocumented. An agent could flag when a consignment's value exceeds threshold and pre-assemble the context package for the Duty Manager. But the *decision to escalate* (and the judgment that the threshold applies in this specific case) remains human — especially given the SOP gap on damages `[Artefact 4]`.

### Agent-led + human oversight: Determine account sensitivity

CRM holds account data (contract type, rate card, credit limit, account manager). The Customer Master CSV shows structured fields. An agent could classify accounts by tier (B2B_VOLUME > B2B_STANDARD; higher credit limit = higher sensitivity) and flag accordingly. Human oversight needed because "key account" status includes informal knowledge (Stein-Allen = "the big one" per driver, but nothing in the system flags this) `[Artefact 1, CUSTOMER_MASTER CSV]`.

### Agent-led + human oversight: Classify dispute type

Customer emails use natural language ("fuel surcharge on a delivery that arrived damaged") that maps to system codes (FUEL_SURCH_DAMAGE, REDELIVERY_FEE, DIM_WEIGHT per disputes CSV). Input is semi-structured (invoice numbers referenced), output is a finite set of codes. An agent could classify with high confidence for clear cases and flag ambiguous ones for human review. Tool coverage = H (CRM API + batch exports). Risk/Compliance = L (classification error is correctable) `[Artefact 2, DISPUTES_OPEN CSV]`.

### Agent-led + human oversight: Notify customer

Standard notifications are template-able (acknowledgements, status updates, timeline promises). For cases with history (repeat disputants like Hayes & Sons), tone and content need calibration — human reviews before send. CRM and email APIs available (Tool/API = H). Low compliance risk. **Adjacent archetype rejected (Fully agentic):** because some notifications reference financial outcomes or make promises (timelines, credit amounts), a human should review dispute-resolution notifications before send `[Artefact 2, scenario brief]`.

---

## Feed-Forward Summary

**Primary signal for D3 (Volume × Value):**
- Delivery Exceptions: high volume (180/day), high judgment, low tool coverage → Human-led + agent support
- Billing Disputes: lower volume (60/day) but highest handling time (28 min), cross-system complexity, compliance risk → mixed (Human-only + Human-led + Agent-led)

**The agent opportunity is in the support layer**, not the decision layer. The primary agentic target should be the work stream where agent support most reduces handling time without requiring autonomous judgment.

