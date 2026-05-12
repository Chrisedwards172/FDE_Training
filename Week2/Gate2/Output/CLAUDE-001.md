# CLAUDE.md — Dispatcher Decision Support Agent (DDSA)

> **Project:** Agentic transformation of Customer Operations, Apex Distribution Ltd  
> **Agent:** Dispatcher Decision Support Agent (DDSA)  
> **Scope:** Delivery Exceptions work stream (~180/day)  
> **Archetype:** Human-led + Agent Support

---

## Project Purpose

The DDSA is an internal decision-support agent for the dispatch team at Apex Distribution Ltd. When a delivery exception arrives (refused delivery, damage dispute, missed window), the agent assembles the decision context — account profile, route pressure, exception history, consignment value — in seconds rather than minutes, so the dispatcher can make the triage call faster and with better information.

**The agent does NOT make triage decisions.** It presents context and options. The dispatcher decides.

---

## Business Context

- **Organisation:** Apex Distribution Ltd, Birmingham, UK. Regional carrier, 800 employees, 180 vehicles, ~3,500 deliveries/day.
- **Function:** Customer Operations (35 people), Delivery Exceptions work stream
- **Volume:** ~180 exceptions/day, avg 12 min handling time
- **Stakeholder:** Sarah Whitmore, COO. Sceptical of chatbots and consultants. Burned by 2024 chatbot and billing RPA failures. Open to internal tools that make her team faster.
- **Political context:** CEO wants AI savings; Sarah wants something that actually works and doesn't alienate her team or customers.

---

## Domain Entities

| Entity | Definition | Source system |
|---|---|---|
| **Exception Case** | A delivery exception requiring dispatcher triage (refusal, damage, missed window, driver issue) | Created by DDSA from Driver App signal |
| **Account** | Customer account with contract, credit limit, sensitivity classification | CRM (Salesforce) |
| **Route** | A driver's planned delivery sequence for the day; includes drops, GPS position, time estimates | Dispatch console / Driver App |
| **Consignment** | The goods being delivered; has a value, a manifest, and a delivery status | Order system (unconfirmed) |
| **Context Card** | The assembled decision-support artifact displayed to dispatchers — 4 sections (Account, Route, History, Value) | DDSA output |
| **Sensitivity Flag** | Classification of account as High / Standard / Unknown based on credit limit + escalation history | DDSA-generated |

---

## System Integrations

| System | Status | Access | Constraint |
|---|---|---|---|
| CRM (Salesforce) | ✅ Available | REST API (Read) | None |
| Driver App | ⚠️ API unconfirmed | Read (webhook/poll) | Must confirm outbound signal capability `[S1]` |
| Dispatch Console | ⚠️ Limited | Read (limited API) | Citrix/Java; route data may be inaccessible `[S2]` |
| GPS/Telematics | ⚠️ Via Driver App | Read | Freshness interval unknown `[S3]` |
| Voicemail (dispatch line) | ⚠️ Shadow system | Unstructured audio | Primary signal channel when dispatchers busy; needs transcription if drivers prefer it over app `[S1 related]` |
| Dispatcher informal knowledge | ❌ Not digitised | None | Account sensitivity known verbally; DDSA proxy = credit limit + escalation history `[A6]` |
| Aurum Billing | 🚫 Out of scope | None | DDSA does not interact with billing — by design |

---

## Delegation Boundaries

### The agent MAY (decides alone):
- Poll Driver App for inbound exception signals
- Pull account records and exception history from CRM
- Pull route data and GPS from available APIs
- Assemble and display the context card
- Calculate route pressure score
- Classify account sensitivity (credit limit >£40K AND prior escalation in 90 days)
- Log performance metrics (card delivery time, adoption)

### The agent MAY (acts, dispatcher notified):
- Flag account as high-sensitivity on the context card
- Prioritise exceptions in queue when driver wait >15 minutes
- Surface "repeat pattern" alerts for accounts with 2+ exceptions in 30 days

### The agent MAY (proposes, dispatcher approves):
- Present triage options with trade-off notes
- Suggest "check with site manager" when refusing party appears unauthorised
- Propose Duty Manager escalation when consignment value >£500

### The agent MUST NOT:
- Make or recommend a specific triage decision (return/leave/hold/re-attempt)
- Contact drivers with instructions
- Contact customers or recipients
- Override dispatcher flags or decisions
- Modify routes or assignments in the dispatch console
- Apply credits, financial adjustments, or billing changes
- Access or interact with Aurum Billing
- Present a single "recommended action" — always options with trade-offs
- Block a dispatcher from proceeding if context card fails to load

---

## Escalation Triggers

| Code | Condition | Target | Urgency |
|---|---|---|---|
| ET-1 | Consignment value >£500, no Duty Manager on shift | Operations Lead | Immediate |
| ET-2 | High-sensitivity account + 2nd+ exception in 30 days | Dispatcher + account manager | Within handling window |
| ET-3 | Driver waiting >15 min, no dispatcher response | Queue priority escalation | Automatic |
| ET-4 | System outage (CRM or Driver App unreachable) | Alert dispatcher: proceed manually | Immediate |
| ET-5 | Account classification confidence <70% | Flag on context card | Within card display |

---

## Operating Parameters

### Context card SLA:
- Assembled within 30 seconds of signal receipt
- If any source unreachable: display partial card with "unavailable" markers — never block

### Account sensitivity rule:
```
High = credit_limit > £40,000 AND escalation_in_last_90_days = true
Standard = all others with sufficient history
Unknown = new account OR sparse history (confidence <70%)
```

### Route pressure score:
```
route_pressure = (drops_remaining × 1.5) + (hours_until_depot_close × 2)
```
If GPS >15 min stale → mark as "⚠️ unverified"

---

## Assumptions

All assumptions are logged in Deliverable 4 (A1–A9, design assumptions) and Deliverable 5 (S1–S9, system assumptions). Key ones affecting this CLAUDE.md:

- `[S1]` Driver App API/webhook capability unconfirmed — critical dependency
- `[S2]` Dispatch console limited API — route data may be unavailable
- `[A4]` Context assembly currently takes ~5 min — DDSA value prop depends on this
- `[A6]` Account sensitivity is informal knowledge — agent classification is a proxy

---

## Source Tagging Conventions

All artefacts in this project use:
- `[Artefact N]` — grounded in scenario sample artefact (1=voicemail, 2=billing email, 3=SMS, 4=SOP, 5=Aurum exports)
- `[INFERRED — scenario brief]` — derived from the scenario text
- `[ASSUMED — AN]` — design assumption (see D4 log)
- `[ASSUMED — SN]` — system assumption (see D5 log)

---

## Naming Conventions

- Files: `lowercase-hyphens.md`
- Entities: PascalCase (Exception Case, Context Card, Sensitivity Flag)
- Escalation codes: `ET-N`
- Assumption IDs: `AN` (design), `SN` (system)
- KPI measurements: camelCase (contextAssemblyTime, dispatcherAdoption)

---

## Scope Boundaries

### In scope (Wave 1):
- Delivery Exceptions work stream (~180/day)
- Context assembly and display for dispatchers
- Account sensitivity classification
- Pattern detection (repeat accounts, driver trends)
- Queue priority management (driver wait time)

### Out of scope:
- ETA Inquiries (automation candidate — separate project)
- Dispatch Adjustments (Wave 2 — blocked by console API)
- Billing Disputes (Wave 2 — requires Aurum integration)
- Customer-facing communication of any kind
- Route modification or driver instruction
- Any interaction with Aurum Billing system
- Credit application or financial adjustments

### Deferred (future waves):
- Voicemail transcription integration (if drivers primarily use phone not app)
- Dispatch console deep integration (when API surface is clarified)
- Cross-stream exception-to-dispute linking (Wave 2, billing agent)

---

## Output Placement

| Artefact type | Location |
|---|---|
| Context cards (runtime) | Displayed in dispatcher UI — not persisted as files |
| Performance metrics | Logged to metrics store (format TBD) |
| Exception case records | Written to CRM as Salesforce cases |
| Configuration (sensitivity rules, thresholds) | `config/` directory — version-controlled |
| Agent logs (debug, audit) | `logs/` — retained 90 days |
