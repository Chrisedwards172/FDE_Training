# Gate 3 — Discovery Prep: Marcus Reyes Role-Play

> **Session:** Thursday 09:30–10:30 CET (60 min)  
> **Format:** Squad-based, coach plays Marcus Reyes (CEO)  
> **Goal:** Extract design-shaping information, catch 2–3 planted contradictions, avoid generic questions

---

## Pre-Discovery: What I Already Know (from the pack)

| Fact | Source | Confidence |
|---|---|---|
| 200 employees, 5-state US region | Pack §3 | Stated |
| 8 coordinators, ~120 decisions/coordinator/day (~960 total/day) | Pack §3 | Stated |
| Avg time-to-fill: 4.2 hours, target <1 hour | Pack §3 | Stated |
| Mismatch rate: 7% (wrong credentials for facility type) | Pack §3 | Stated |
| No-show rate: 12% | Pack §3 | Stated |
| Hospitals submit via email, portal, or phone | Pack §3 | Stated |
| Compliance: license checks, background, training certs — done manually against state regulatory databases | Pack §3 | Stated |
| Two failed AI projects: chatbot (hospitals rejected), recommendation engine (nobody used) | Pack §3 | Stated |
| Marcus: ops + growth background, not engineering | Pack §3 | Stated |
| Series B just closed, board wants 10x growth in 24 months | Pack §3 | Stated |
| Marcus wants results in 8 weeks | Pack §3 | Stated |

**What I don't know (design-shaping gaps):**

- How coordinators actually make matching decisions (the cognitive work)
- What systems they use (EHR, scheduling tool, CRM, spreadsheets?)
- What "credentials" means concretely (state licenses, certifications, facility-specific requirements?)
- Why the chatbot failed specifically (UX? trust? wrong problem?)
- Why the recommendation engine failed (bad data? wrong workflow? adoption?)
- What causes the 12% no-show rate
- What causes the 7% mismatch rate
- How nurses express availability and preferences
- What happens when a shift goes unfilled
- Whether the 5-state footprint means 5 different regulatory regimes
- Who Kim, Aaron, and Linda are and what they control

---

## Discovery Questions — Organised by Priority

### Tier 1: Design-Shaping (MUST ASK — answers change architecture)

**Q1. The matching decision itself:**
"When a coordinator picks a nurse for a shift, walk me through the actual decision — not the process, the moment they decide. What are they weighing? What makes one nurse better than another for a specific shift?"

*Why this matters:* This is the core cognitive work. If it's codifiable (credentials + proximity + availability = score), the agent can lead. If it's relationship knowledge ("Dr. Chen prefers nurses who've worked his floor before"), it's harder to delegate.

**Q2. The two failed AI projects:**
"The chatbot and the recommendation engine — can you tell me specifically what went wrong with each? Not 'it didn't work' — what did the hospitals or coordinators actually say when they rejected them?"

*Why this matters:* My architecture must avoid repeating those failure modes. If the chatbot failed because hospitals don't trust AI decisions, then a fully agentic matching agent will fail too. If the recommendation engine failed because coordinators ignored its suggestions, then "agent-led + oversight" needs a different UX than a recommendation list.

**Q3. Credential verification — the real process:**
"You mentioned compliance is done manually against state regulatory databases. Walk me through a real verification — a coordinator gets a shift request, how do they check that the nurse is credentialed for that facility type?"

*Why this matters:* If verification is a database lookup (structured, deterministic), it's RPA territory. If it involves judgment (interpreting credential equivalencies across states, expired-but-renewable licenses), it's agent territory.

**Q4. The 7% mismatch rate — root cause:**
"The 7% mismatch rate — is that the coordinator picking the wrong nurse, or is it the credentials being out of date, or is it the hospital's requirements being unclear?"

*Why this matters:* Different root causes need different agent interventions. Wrong pick = better matching logic. Stale credentials = real-time verification. Unclear requirements = better intake.

**Q5. The 12% no-show rate — root cause:**
"What's driving the 12% no-shows? Is it nurses cancelling, nurses not confirming, scheduling conflicts, or something else?"

*Why this matters:* If no-shows are predictable (nurses with history of no-shows, shifts at certain times), an agent could flag risk. If they're unpredictable (emergencies), the agent needs rapid backfill capability.

### Tier 2: Architecture-Shaping (SHOULD ASK — answers refine design)

**Q6. Systems landscape:**
"What systems do coordinators use day to day? I'm looking for the actual tools — scheduling software, CRM, spreadsheets, state portals, anything."

*Why this matters:* Integration surface. APIs available? Batch-only? Screen-scraping required? This determines what the agent can access.

**Q7. Nurse availability — source of truth:**
"How does a coordinator know which nurses are available right now? Is there a system, or is it phone calls and texts?"

*Why this matters:* If availability is in a system, the agent can read it. If it's in coordinators' heads or on Kim's spreadsheet, the agent has a data gap. Watch for contradiction: Marcus may say "our app is the source of truth" but later reveal manual overrides.

**Q8. Hospital preferences:**
"Do hospitals have preferences beyond credentials? Like specific nurses they want, or nurses they don't want? How is that tracked?"

*Why this matters:* If preferences are informal ("Dr. Chen prefers Maria"), they're tribal knowledge the agent can't access unless systematised. If they're in a system, the agent can incorporate them.

**Q9. Time pressure dynamics:**
"When a shift request comes in, how urgent is it typically? Is there a spread — some are planned a week out, some are 'we need someone in 4 hours'?"

*Why this matters:* Different urgency = different agent behaviour. Planned shifts can use batch matching with human review. Emergency fills need autonomous rapid matching.

**Q10. The 8-week timeline:**
"You said 8 weeks. Is that board pressure, or is there a specific event driving that timeline — a contract renewal, a growth milestone?"

*Why this matters:* If it's arbitrary, I can negotiate phasing. If it's a hard deadline (contract renewal), my scope must fit.

### Tier 3: Contradiction Probes (LISTEN FOR — follow up when inconsistency appears)

Based on the pack's sample contradictions, I should listen for:

| Surface claim | Possible contradiction | Follow-up probe |
|---|---|---|
| "Our app tracks nurse availability" | Kim updates schedules manually when nurses call in | "If a nurse calls in sick right now, how quickly is the system updated? Who updates it?" |
| "All credentials verified before roster" | Credential lapses caught reactively via state pings | "What happens between a credential expiring and you finding out? How long is the gap?" |
| "7% mismatch is hospital-flagged" | Quality score mentioned as reliable | "You mentioned a quality score — does that capture the same thing as the 7% mismatch, or is it different?" |

**Contradiction-catching technique:** When Marcus says something that sounds too clean, follow up with a specific scenario: "Let's say a nurse's license expired yesterday and a shift request comes in today — what actually happens?"

---

## Notes Template (for during the session)

### What Marcus said (capture key quotes):

| Topic | What he said | Timestamp | Contradiction? |
|---|---|---|---|
| | | | |

### Contradictions caught:

| # | Claim 1 | Claim 2 | My follow-up | His response |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### Deferred to others (names Marcus dodged to):

| Name | Role | What was deferred | Design implication |
|---|---|---|---|
| Kim | Senior coordinator | | |
| Aaron | IT | | |
| Linda | Compliance | | |

### Key unknowns still open after session:

1. 
2. 
3. 

---

## Post-Discovery: Immediate Actions (Thursday afternoon)

1. **Synthesise discovery notes** into structured form (above tables filled in)
2. **Run D#1 prompt** (problem-framing.md) — translate Marcus's answers into the real problem
3. **Run D#2 prompt** (engagement-intake.md) — stakeholder map, scope, risks shaped by discovery
4. **Run D#3 prompt** (solution-architecture.md) — architecture choices grounded in what I learned
5. **Submit interim D#1–D#3** by 23:59 to squad lead (rough is fine — it feeds Friday's pushback)

