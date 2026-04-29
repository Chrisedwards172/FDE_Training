# Gate 1 — Live Walkthrough Preparation

**Participant:** Chris Edwards
**Format:** ~3 min you-led summary → ~7 min coach challenge
**Rule:** No slides. Walk the coach through the document. Defend boundaries with reasoning; update cleanly when challenged.

---

## Part A — 3-Minute Summary Script

Use this as a backbone. Speak to the document — point at sections as you go. Target ≤ 3 minutes.

### Opening (≈ 30 seconds)

> "This is an First Notification Of Loss FNOL intake-to-acknowledgement agent for a mid-size insurer processing 300 claims per day. The team of 12 specialists is structurally over capacity — 22 minutes per claim, 110 specialist-hours of work against 96 hours of team capacity — which explains the 31% SLA breach and 18% routing error. The claimant feels both: late acknowledgement and wrong adjuster on first contact." Credibility, confidence, poor reviews, complaints.

**Why this works:** Names the scenario numbers (Pack §7 anti-pattern: generic framing). Frames from both claimant and business perspective (Criterion 1). Shows you read the scenario, not a template.

### Delegation boundary (≈ 60 seconds)

> "I decomposed FNOL processing into 15 tasks. The boundary sits at one non-negotiable: the client's insistence on human oversight for high-value or ambiguous claims. I drew the line at codifiability — if a step is a deterministic lookup or rule application against a named system, it's fully agentic. If it requires judgment under uncertainty with downstream payment implications, a specialist must act before state changes externally.
>
> Concretely: intake, extraction, routine coverage validation, routine triage, routine routing, and routine ack are all fully agentic. Coverage-ambiguous resolution, severity override on escalated claims, escalated routing confirmation, and escalated ack review all require a logged human decision before the agent proceeds. Final coverage/liability decision is human-only — out of pipeline scope entirely.
>
> The conditional rows matter: if U1 fails — the client can't articulate what 'high-value or ambiguous' means — escalation classification drops from fully agentic to human-led, and the whole escalated branch becomes unbuildable. If U2 fails — the SOAP endpoint doesn't behave as assumed — routine coverage validation drops classification too."

**Why this works:** Justifies each boundary with codifiability, not vibes (Criterion 2). Names the conditional fallbacks — shows you've thought about what happens when assumptions break.

### Agent spec — the load-bearing piece (≈ 45 seconds)

> "Three capabilities along the delegation seams. Capability A: intake and extraction — receives raw FNOL, persists to DMS, extracts fields, creates the Claim in CRM. Hand-off at state EXTRACTED with a confidence score. Capability B: coverage validation and triage — calls the SOAP endpoint, assigns severity, evaluates the escalation trigger, routes. This is where the human/agent boundary is operationalised — rule R-B-6 is the escalation classifier with five named triggers. Capability C: acknowledgement and audit — issues the ack and, critically, persists every human decision as an immutable event.
>
> The Claim entity has a 13-state machine. Every transition maps to a named business rule. Every external write carries an idempotency key. Every escalation has a code, an SLA, and a named recipient. Four integration contracts — CRM REST, Policy Admin SOAP, DMS REST, and three ack channels — each with endpoint, auth, request/response shape, timeout, retry, and fallback. The four build-blocking scope-outs — U2 through U5 — are named, not hidden."

**Why this works:** Spec precision (Criterion 3) — names states, rules, idempotency, integration contracts. Named scope-outs beat silent omissions.

### Validation and honesty (≈ 45 seconds)

> "Validation has four layers: happy path, edge cases, loud failures, and quiet failures. The quiet failures are the ones that matter — the agent is wrong and no one notices.
>
> Six quiet-failure detectors: mis-mapped SOAP fields where both values are valid but swapped; wrong-but-plausible routing where the adjuster never overturns; severity drift where the rubric returns valid but outdated output; template variable substitution failure where the send API accepts the message but the claimant sees raw brackets; extraction degradation just above the confidence gate; and the 0.85-to-0.95 confidence band that passes intake but triggers escalation downstream — a spec tension I surfaced during consolidation as U27.
>
> The boundary tests are paired: BV-1 probes whether the agent faithfully applies a routine classification near the escalation threshold. BV-2 is the adversarial counterpart — it injects a synthesised boundary violation to prove the M5 detector itself works. Without BV-2, BV-1 proves nothing.
>
> 28 assumptions, all agent-identified, none rated High — because no coach session exists in this window to validate them. 8 genuine unknowns. The single highest-leverage question for a client conversation is U1: can you walk me through five recent claims your specialists flagged as ambiguous and tell me what tipped each one?"

**Why this works:** Quiet-failure focus (Criterion 4). Honest about what you don't know (Criterion 5). U27/U28 show you caught your own spec's gaps.

---

## Part B — Anticipated Coach Challenges and Prepared Responses

### Challenge 1: "Why did you draw the human/agent boundary here?"

**Likely probe points:** T7 (escalation trigger), T5 (ambiguous coverage), T9 vs T10 (routine vs escalated routing).

**Response framework:**

> "The boundary principle is codifiability plus reversibility. T9 — routine routing — is fully agentic because it's a deterministic lookup on four keys against a rule table, and the assignment is reversible — if the adjuster overturns it within 24 hours, M2 catches it. T10 — escalated routing — requires human sign-off because the claim is on the oversight branch, and committing the claim to an escalated queue has downstream payment implications the client reserved to humans.
>
> The key conditional is U1. If the client can articulate the trigger criteria — reserve threshold, coverage ambiguity, prior-loss — then T7 is fully agentic rule application. If it's tacit, T7 drops and the whole escalated branch needs redesigning. I don't pretend to know which it is — that's the first client question I'd ask."

### Challenge 2: "What happens when this assumption is wrong?"

**Most likely targets:** U1, U2, U13, U15.

**For U1 (high-value or ambiguous is not codifiable):**
> "If U1 fails, T7 drops from fully agentic to human-led with agent support. The agent can still surface evidence — extraction outputs, severity rubric score, prior-loss flags — but a specialist makes the branch decision on every claim that isn't unambiguously routine. M5 becomes harder to measure because the trigger is no longer deterministic. The architecture survives — the escalated branch still exists — but throughput drops because the specialist is now in the loop earlier, and M3's 70% no-touch target is likely unreachable."

**For U2 (SOAP doesn't behave as assumed):**
> "If p95 is 45 seconds instead of 15, the routine-path SLA budget goes from ~2 minutes to ~90 seconds, which still fits in the 2-hour window — the reserve absorbs it. If the SOAP endpoint doesn't expose the four fields I assumed, Cap B's routine path drops to agent-led with human oversight, and the specialist validates coverage manually. The spec has a named fallback — COVERAGE_TIMEOUT with ESC-COVERAGE-TIMEOUT — and the escalation SLA is 60 minutes. The architecture doesn't break; throughput degrades."

**For U13 (routing rules are tacit):**
> "If routing rules don't exist in codifiable form, T9 drops from fully agentic to human-led with agent support. The agent surfaces the evidence — peril, severity, geography — and a specialist selects the queue. M2's 3% target is probably unreachable because the human routing is the same process that produces 18% errors today. The honest answer is: the agent can still add value on intake, extraction, coverage validation, and ack — but routing stays human until the rules are codified."

**For U15 (0.85 threshold is wrong):**
> "If 0.85 is too low, the agent over-reaches on garbled intake — a quiet failure. FQ-5 detects this via a 7-day rolling mean confidence drop. If 0.85 is too high, escalation rate rises and M3 softens. The threshold is an internal tunable — I'd calibrate it on 200 historical FNOLs before go-live, targeting M3 ≥ 70% subject to M2 ≥ 97% and M5 = 100%. The spec gap U27 is related — the 0.85-to-0.95 band passes R-A-4 but triggers R-B-6 escalation. That's either intentional as a 'safe to proceed but escalation-eligible' zone, or a spec defect that needs a re-tune."

### Challenge 3: "How would you know this agent is failing in production?"

**Response framework:**

> "Three detection tiers. Loud failures surface immediately — SOAP outage, CRM 5xx, ack send failure. Each has a named escalation code, an SLA, and a recovery path. These are easy.
>
> Quiet failures are what I spent the most time on. Six named detectors:
> - FQ-1: SOAP field mis-mapping — 5% sample cross-check by claims ops lead.
> - FQ-2: wrong-but-plausible routing — per-rule M2 below 97% on a 5-day window.
> - FQ-3: severity drift — KL divergence against a 90-day baseline, *if* the baseline exists (U22).
> - FQ-4: template substitution failure — pre-send lint gate catches unbound variables before the message leaves; post-send detection depends on claimant feedback signal (U24).
> - FQ-5: extraction model degradation — rolling mean confidence drop.
> - FQ-6: the 0.85-0.95 confidence band — overturn rate on band-claims above population mean.
>
> The boundary detector is BV-2's territory — R-C-11 counts any escalated-branch routing write without a preceding HumanDecision as a boundary violation and fires a P0 page within 5 minutes. That's the M5 = 100% enforcement mechanism."

### Challenge 4: "Your confidence threshold has a collision — explain."

> "Yes — U27. R-A-4 gates intake at extraction_confidence ≥ 0.85. R-B-6 flags extraction_confidence < 0.95 as a low-confidence-intake escalation driver. The band 0.85-to-0.95 passes intake but triggers escalation downstream. I surfaced this during consolidation — it's either an intentional two-tier design where intake is liberal but triage is conservative, or it's a spec defect. If intentional, it should be documented explicitly as a design decision with the band's behaviour named. If unintentional, R-B-6's threshold needs re-tuning. I flagged it rather than silently picking a side."

### Challenge 5: "Why 28 assumptions and no HUMAN ones?"

> "The scenario file had no participant-supplied HUMAN assumptions section populated at generation time — all 28 are agent-identified. The Pack said 'at least 5 genuine unknowns' — I have 8, each naming the specific rule or integration that breaks. No entry is rated High because no coach session exists in this window to validate anything — claiming High confidence without validation would violate the thinking-discipline primer. The 11 Low entries are integration shapes and regulatory questions I genuinely don't know. The 17 Medium entries are things I have a defensible default for but would need production data or client confirmation."

### Challenge 6: "What would you build first?"

> "Capability A — intake and extraction. It has the fewest external dependencies (DMS write + CRM claim creation), both are REST, and it produces the Claim record that everything downstream consumes. I'd build A, prove idempotency and the confidence gate work against synthetic data, then move to B (pending U2 SOAP WSDL) and C in parallel. The four build-blocking scope-outs — U2, U3, U4, U5 — are the real gating items; I'd have those client conversations in week 1 while building A against mocks."

### Challenge 7: "The 18% routing error — how do you know your agent will do better?"

> "I don't — until U6 is resolved. The 18% could measure adjuster-overturned routings or operational re-queues. If it's overturns, M2 is directly comparable — routing errors the adjuster catches. If it's re-queues, the agent 'improves' the metric just by reaching adjusters at all, which is a hollow comparison. The honest answer: the agent's advantage is deterministic rule application against a codified table (U13). If the rules are good, the error rate drops because the agent doesn't fatigue, rush, or pattern-match from memory. If the rules themselves are bad, the agent will be consistently wrong — FQ-2 detects this via per-rule M2 below 97% on a 5-day window."

### Challenge 8: "What's the weakest part of this spec?"

> "U1. Everything downstream of the escalation trigger depends on it being codifiable. If the client says 'our specialists just know' — which is plausible for experienced insurance claims handlers — the escalated branch is unbuildable as specified, M5 loses its falsifiability, and BV-1/BV-2 test nothing. The mitigation is the first client question: walk me through five recent claims you flagged as ambiguous, tell me what tipped each one. If the answer is a rule, we codify it. If the answer is genuinely tacit, we redesign the boundary — the agent surfaces evidence and a specialist makes every branch decision, which is a viable but more human-intensive architecture."

---

## Part C — Quick-Reference Cheat Sheet

Keep this in peripheral vision during the walkthrough. Don't read from it — use it to anchor numbers.

| Scenario number | What it is |
|---|---|
| 300 | FNOLs per day |
| 12 | Specialists today |
| 22 min | Average handling time |
| 110 hrs | Daily cognitive load (300 × 22 min) |
| 96 hrs | Team capacity (12 × 8h) |
| 31% | SLA breach rate |
| 18% | Routing error rate |
| 2 hours | SLA window |

| Key spec numbers | Where they come from |
|---|---|
| 0.85 | Extraction confidence gate (R-A-4, U15) |
| 0.95 | Escalation trigger threshold (R-B-6, U27 tension) |
| 15s | SOAP timeout (U2) |
| 13 states | Claim state machine |
| 15 tasks | Delegation work inventory |
| 3 capabilities | A (Intake), B (Coverage/Triage), C (Ack/Audit) |
| 28 assumptions | 0 HUMAN, 28 AGENT, 11 Low, 17 Medium |
| 8 unknowns | Genuine, each build-blocking or boundary-defining |
| 6 quiet-failure detectors | FQ-1 through FQ-6 |
| 4 build-blocking scope-outs | U2 (SOAP), U3 (CRM), U4 (DMS), U5 (Ack channels) |

| Escalation codes to know cold | Trigger |
|---|---|
| ESC-AMBIG | Coverage ambiguous |
| ESC-HIVAL | High-value claim |
| ESC-EXTRACTION-LOWCONF | Confidence < 0.85 |
| ESC-BOUNDARY-VIOLATION | M5 = 100% enforcement — P0, 5-min page |
| ESC-ROUTING-NOMATCH | Routing rule miss |

| Key assumptions to defend | One-liner |
|---|---|
| U1 | "High-value or ambiguous" is codifiable |
| U2 | SOAP WSDL and shape — build-blocking |
| U13 | Routing rules exist in codifiable form |
| U15 | 0.85 confidence threshold — tunable |
| U27 | R-B-6 / R-A-4 threshold collision — spec gap I found |

---

## Part D — Walkthrough Mindset Reminders

1. **Point at the document.** The coach is reading it. Say "section 2, row T7" not "the escalation thing."
2. **Lead with the boundary.** The Pack tests delegation justification heavily. Your strongest material is the 15-row work inventory with conditional fallbacks.
3. **When challenged, name the assumption.** "That depends on U1" is stronger than "I think so."
4. **Update cleanly under pressure.** If the coach breaks an assumption, say: "If that's true, here's what changes: [row X drops classification, metric Y loses its baseline, capability Z needs redesign]." Don't defend a dead position.
5. **The claimant is a person.** If you default to business-efficiency language, pause and name the claimant impact: late ack, wrong adjuster, repeated information-gathering.
6. **Quiet failure is your differentiator.** Most specs stop at loud failures. FQ-1 through FQ-6 and the BV-1/BV-2 pair are what show depth.
7. **"I don't know" is a valid answer** — followed by "and here's how I'd find out" (the test question from the assumption entry).

