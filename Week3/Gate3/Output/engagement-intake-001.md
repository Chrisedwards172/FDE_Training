# Deliverable #2 — Engagement Intake & Scope

> **Engagement:** MedFlex — Agentic Transformation of Shift Matching  
> **Version:** Interim draft (Thursday EOD)  
> **Status:** Pre-pushback — will be revised against Marcus's Friday memo

---

## 1. Business Context

**MedFlex** is a healthcare staffing agency (200 employees, 5-state US region) that matches travel nurses to hospital shift requests. Revenue: $14M. Target: $200M in 24 months post-Series B.

**Core business model:** B2B with hospital systems (demand side) and B2C with travel nurses (supply side). MedFlex earns margin on placements — hospitals pay MedFlex, MedFlex pays the nurse. Speed and match quality determine competitive position.

**Competitive landscape:** Hospitals submit shift requests to multiple agencies simultaneously. The first agency to propose a credentialed, available nurse wins the placement. MedFlex competes on speed, match quality, and relationship — in that order.

**Current operations:** 8 coordinators manually match ~960 shifts/day. Average time-to-fill: 4.2 hours. Mismatch rate: 7%. No-show rate: 12%.

**Prior AI attempts:** Two failed projects — a customer-facing chatbot (hospitals rejected it in a competitive market) and a recommendation engine (coordinators didn't trust it, feared job security, accuracy was poor).

---

## 2. Stakeholder Map

| Stakeholder | Role | Authority | Type | Disposition | Conflicting incentives |
|---|---|---|---|---|---|
| **Marcus Reyes** (CEO) | Sponsor, point of contact | Budget, go/no-go | **Decision-maker** | Supportive but sceptical (burned twice). Wants speed and ROI. | Wants full automation ("automate as much as possible") but hasn't reconciled this with coordinator adoption risk. |
| **Kim** (Senior Coordinator / Head of Ops) | Operational lead, undisclosed | Day-to-day workflow authority | **Influencer / potential blocker** | Unknown — not available in discovery | Likely protective of her team's expertise and job security. May resist if agent threatens coordinator role. Marcus deferred operational detail to her repeatedly. |
| **Aaron** (IT) | Technical infrastructure | System access, API decisions | **Potential blocker** | Unknown — not available | Controls ServiceNow, nurse DB, integration surface. Could block if systems aren't API-accessible. Must be engaged in Phase 0. |
| **Linda** (Compliance) | Credential verification | Regulatory compliance sign-off | **Influencer** | Unknown — not available | Separate process — may resist if agent scope creeps into compliance territory. |
| **8 Coordinators** | End users of the agent | None (but adoption determines success) | **Potential blockers (adoption)** | Likely resistant (rejected recommendation engine, fear job security) | Want to keep their jobs. Have tacit knowledge the system can't capture yet. Will sabotage if threatened. |
| **Hospital administrators** | Customers (demand side) | Placement acceptance/rejection | **External influencer** | Neutral — want fast, accurate matches | Don't care about MedFlex's internal process; care about speed and quality. Will switch agencies if service degrades. |
| **Travel nurses** | Workers (supply side) | Availability, show/no-show | **External influencer** | Neutral — want good shifts, fair pay | May be registered with multiple agencies. Loyalty is to pay rate and shift quality, not to MedFlex specifically. |
| **Board / investors** | Governance | Funding, growth targets | **Decision-maker (funding)** | Pressure for ROI on Series B | Want $200M in 24 months. May push for faster/bigger scope than is safe. |

**Key conflict:** Marcus wants "automate everything" but his coordinators rejected the last AI tool. The engagement must navigate this by designing for coordinator empowerment (agent-assisted), not coordinator replacement (fully agentic).

---

## 3. Constraints

| Constraint | Source | Impact on design |
|---|---|---|
| **8-week timeline** | CEO expectation (discovery confirmed: "show me ROI in 8 weeks") | MVP must be narrow: one workflow, agent-assisted, measurable improvement |
| **Two failed AI projects** | Chatbot + recommendation engine | Design must be visibly different: internal (not customer-facing), transparent (not black box), empowering (not replacing) |
| **Coordinator adoption risk** | Discovery: team feared job security, rejected recommendation engine | Progressive autonomy model. Coordinator reviews all matches in Phase 1. |
| **Free-text intake (email)** | ServiceNow receives raw free text from hospitals | Agent must parse unstructured text — this is an NLP/reasoning challenge, not a form-fill |
| **Competitive speed pressure** | Hospitals submit to multiple agencies. First response wins. | Time-to-fill reduction is the primary value metric, not accuracy alone |
| **5-state regulatory landscape** | US healthcare staffing is state-regulated (nursing licenses, certifications) | Agent must check credential status against shift location. Compliance team owns verification; agent reads the result. |
| **No nurse confirmation model** | Silence = acceptance. Nurse doesn't confirm shifts. | Contributes to 12% no-show rate. Agent should introduce proactive confirmation. |
| **Concurrency** | Same nurse submitted to multiple hospitals simultaneously | Agent needs a locking/reservation model to prevent double-booking |
| **Budget** | Series B just closed — funding available but Board expects ROI. No specific budget disclosed. | Design for cost-awareness: LLM inference cost per request must be tracked. Phase 0 should include cost modelling. |

---

## 4. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Coordinator rejection** — team refuses to use agent (repeats recommendation engine failure) | High | Critical | Agent-led + coordinator oversight (not fully agentic). Coordinator approves all matches in Phase 1. Progressive autonomy only after demonstrated trust. |
| **Matching accuracy insufficient** — agent proposes wrong nurses | Medium | High | Confidence scoring with human review threshold. Agent explains reasoning (transparent, not black box). Measure acceptance rate. |
| **Free-text parsing errors** — agent misinterprets hospital requests | Medium | Medium | Human-in-the-loop for low-confidence parses. Feedback loop: coordinators correct parses, agent learns. |
| **Stale credential data** — nurse card shows valid but credential has lapsed | Medium | High (compliance + reputational) | Agent cross-references credential expiry date against shift date. Flag any credential expiring within 7 days of shift. |
| **No-show rate doesn't improve** — root cause is competitive poaching, not MedFlex's process | Medium | Medium | Proactive confirmation workflow. No-show risk scoring based on nurse history, shift distance, time-of-day. Even partial improvement is measurable. |
| **ServiceNow API limitations** — IT can't provide real-time API access | Low–Medium | High | Fallback: batch export + polling. Design agent to work with delay. Confirm with Aaron (IT) in Phase 0. |
| **CEO scope creep** — Marcus pushes to include compliance verification, hospital portal, nurse app | High | Medium | Hold scope boundary with D#2 out-of-scope list. Propose compliance as Phase 2 if business grows. |
| **8-week timeline is unrealistic for full MVP** | Medium | Medium | Phase 0 (2 weeks): integration + data access confirmed. Phase 1 (6 weeks): agent-assisted matching for standard cases. Not all 960 decisions/day — start with structurally simple matches. |

---

## 5. MVP Scope (Phase 1: 8 weeks)

### In scope

| Component | Description | Rationale |
|---|---|---|
| **Free-text intake parsing** | Agent parses hospital shift requests from ServiceNow (email-originated) into structured fields: credentials required, shift timing, facility, location, special requirements | Removes highest-waste cognitive step. Every match starts with parsing — fixing this accelerates everything downstream. |
| **Agent-assisted shift matching** | Agent proposes top-N candidate nurses ranked by: credential match, availability, proximity, hospital feedback history. Coordinator reviews and approves/modifies. | Core value delivery. Addresses the binding constraint (manual search) without triggering adoption risk (coordinator still decides). |
| **Credential expiry guard** | Agent checks credential expiry date against shift date before proposing a nurse. Flags any credential expiring within 7 days. | Directly reduces the credential component of the 7% mismatch rate. Low-effort, high-signal. |
| **Proactive nurse confirmation** | Agent sends confirmation request to the nurse (SMS/email) after coordinator approves match. Nurse must confirm within a time window. If no confirmation, agent flags for rebooking. | Addresses 12% no-show rate. Changes from "silence = acceptance" to "confirmation required." |
| **Coordinator dashboard** | Single view: incoming requests (parsed), agent-proposed matches (ranked), match history, acceptance/rejection tracking | Adoption enabler. Gives coordinators a tool that's better than their current workflow, not a threat to it. |

**Geographic scope:** All 5 states from day one. The matching logic is state-agnostic (credential status is already validated per-state by the compliance team). No reason to geo-limit the MVP — the agent reads credential status, it doesn't verify by state.

### Out of scope (with rationale)

| Excluded | Rationale | When it could come in |
|---|---|---|
| **Credential/compliance verification** | Separate team, separate process. CEO explicitly scoped it out. Coach feedback confirmed: focus on matching. | Phase 2 — when business growth creates compliance team capacity pressure |
| **Hospital-facing portal or channel changes** | Hospitals submit via email/portal/phone today. Pack §3 explicitly excludes this. | Not planned — channel strategy is sales/marketing, not FDE |
| **Nurse-facing mobile app** | Nurses reached by phone/SMS/email today. Pack §3 explicitly excludes this. | Not planned |
| **Pricing engine / margin optimisation** | Pack §3 explicitly excludes. Pricing is MedFlex's existing process. | Not planned |
| **Fully autonomous matching (no coordinator review)** | Two failed AI projects. Coordinator adoption is the top risk. Phase 1 must build trust before removing oversight. | Phase 2–3 — after demonstrated accuracy and coordinator trust. Progressive autonomy. |
| **Multi-hospital concurrent submission orchestration** | Complex concurrency problem. Requires locking model and real-time state management. Important but not MVP. | Phase 2 — after basic matching is working |
| **No-show prediction model** | Requires historical data analysis. Value is clear but dependent on data availability. | Phase 2 — agent accumulates placement history data in Phase 1, builds predictive model in Phase 2 |

---

## 6. Phasing

| Phase | Duration | Deliverable | Success metric |
|---|---|---|---|
| **Phase 0: Integration & Data** | Weeks 1–2 | ServiceNow API access confirmed. Nurse DB schema mapped. Credential status field validated. Sample data flowing. | Data pipeline operational. No code yet — integration contracts only. |
| **Phase 1: Agent-Assisted Matching** | Weeks 3–8 | Free-text parsing + candidate ranking + coordinator review dashboard + credential expiry guard + proactive confirmation. | Time-to-fill < 2h on agent-assisted matches. Coordinator adoption > 80%. Mismatch rate < 5%. |
| **Phase 2: Progressive Autonomy** | Months 3–6 | Agent auto-submits simple matches (high-confidence, standard credentials, confirmed availability). Coordinator oversight for complex/edge cases. No-show prediction. Concurrent submission management. | Time-to-fill < 1h overall. Decisions/coordinator/day > 500. |

