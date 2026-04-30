# Live Clarification Round — Prep Deck

> **Format:** 10-minute simulated stakeholder interview. Coach plays Priya Aggarwal (HR Ops Lead). She's impatient, sceptical, answers some questions precisely and others vaguely or contradictorily.
>
> **Your goal:** Ask focused discovery questions. Detect evasion. Adapt. Every question must target a specific design decision.
>
> **This is not a presentation.** You do not present your deliverables. You ask questions that would change your design.

---

## Opening (30 seconds)

> "Priya, thanks for the time. I've been looking at how your team manages new-hire provisioning — the equipment, access, badges. I've got a few specific questions that will shape what we recommend. I'll keep these tight."

**Don't:** explain what you've built. **Do:** get straight to questions.

---

## Must-Ask Questions (pick 5, adapt order based on flow)

### Q1 — Routing failures: frequency and scope
**Ask:** "When Tom's laptop went to the wrong queue because the consulting spec changed — how often does that happen? Is it just consulting, or other divisions too?"

**What you need:** Frequency (monthly? quarterly?) and scope (consulting only or cross-division). If rare → scale back spec repository. If frequent → confirms core value prop.

**If she's vague ("it happens sometimes"):** Push: "Can you think of two specific cases apart from Tom's? What division were they in?"

**Design decision:** Spec repository scope (consulting-only vs all-division) and whether location-code validation is needed.

---

### Q2 — Escalation patterns: codifiable or pure judgment?
**Ask:** "When you flag something as Red vs Amber — is there a pattern? Like, consulting always goes Amber, partner hires always go Red?"

**What you need:** Whether escalation rules exist (even informal). If yes → agent can propose risk levels. If pure judgment → agent can only surface context.

**If she says "it depends":** Push: "Give me the last Red you set. What made it Red instead of Amber?"

**Design decision:** Autonomy matrix — does "propose risk level" stay in the agent-proposes tier, or drop to context-only?

---

### Q3 — Rehires and conversions: volume and rules
**Ask:** "How often do you get contractor-to-FTE conversions or rehires? And when you decide reactivate vs new record — is there a rule?"

**What you need:** Volume (is 15-20% the right HITL estimate?) and whether any heuristics exist (e.g. <1yr = reactivate).

**If she deflects to IT ("IT decides"):** Push: "But you must recommend something to IT. What do you base that on?"

**Design decision:** ET-1 classification logic — can the agent propose, or is it always human-initiated?

---

### Q4 — Building access: same system across offices?
**Ask:** "Does building access go through ServiceNow for all offices, or is it different?"

**What you need:** Whether the autonomy matrix's "request building access via ServiceNow" applies everywhere.

**This is a quick-answer question** — use if conversation is flowing fast. Skip if time is tight.

**Design decision:** System/Data Inventory — new integrations needed? Email-based for some offices?

---

### Q5 — High-sensitivity: how do you know at day one?
**Ask:** "Tom's notes say 'Director's hire from Deloitte.' How do you know at the start which hires are sensitive? Is it always consulting-director-level, or do you find out later?"

**What you need:** Whether sensitivity criteria are articulable at record-creation time, or if they emerge mid-onboarding.

**If she says "I just know":** Push: "If you were off sick the week Tom started, would the coordinator have flagged him the same way? What would they need to know?"

**Design decision:** ET-3 auto-inference rules — can the agent flag at day one, or does it need reactive detection (inbound emails)?

---

### Q6 — Previous automation failures
**Ask:** "You mentioned that automation attempts fell through the cracks. What specifically was tried, and what broke?"

**What you need:** Whether previous failure was technical (integration issues) or design-level (didn't handle edge cases). Changes what OPC must visibly address to earn Priya's trust.

**Design decision:** Risk framing — if Power Automate failed on contractors, the OPC must explicitly show it won't repeat this.

---

### Q7 — Who updates routing rules when specs change?
**Ask:** "When the consulting spec changed — whose job was it to update ServiceNow routing? Did anyone tell your team?"

**What you need:** Whether a governance path exists or it's a gap. If gap → OPC can detect but not fix root cause. If path exists → OPC can trigger it.

**If she says "nobody's job":** That's the answer. Don't push further — note it and move on.

**Design decision:** Whether to recommend a governance process (organisational change, not agent scope).

---

## Evasion Detection Cheat Sheet

| Signal | What it means | Your move |
|--------|--------------|-----------|
| "We follow the process" | She's giving you the SOP, not lived work | "The email about Tom suggests the process didn't work. How often does that gap show up?" |
| "It depends" | There ARE patterns, she hasn't articulated them | "Give me two cases where it went differently. What made the difference?" |
| "Everything is fine most of the time" | She's protecting her team or minimising | "When it's not fine — what does that look like? Worst onboarding this year?" |
| "The team just knows" | Tacit knowledge — the real risk | "If a coordinator was off sick for a week, what would break?" |
| Gives a number then hedges | The number is roughly right but she's not confident | Take the number. Don't chase precision — chase patterns. |
| Contradicts an earlier answer | Complexity lives in the contradiction | "Earlier you said X, but just now you said Y. Can you help me understand?" |

---

## Time Management

| Minute | What to do |
|--------|-----------|
| 0:00–0:30 | Opening — set context, no preamble |
| 0:30–2:30 | Q1 (routing failures) — this grounds the whole conversation |
| 2:30–4:30 | Q2 (escalation patterns) — the highest-design-impact question |
| 4:30–6:00 | Q3 (rehires/conversions) — volume and heuristics |
| 6:00–7:30 | Q5 (sensitivity detection) — feeds directly into autonomy matrix |
| 7:30–9:00 | Q6 or Q7 — pick based on what's still ambiguous |
| 9:00–9:30 | Quick clarification on anything that contradicted earlier answers |
| 9:30–10:00 | "Thank you — one last thing: what would make you trust this enough to let it run?" |

---

## Closing Question (if time allows)

> "If we built something that handles the routine monitoring and flags problems before the directors call you — what would make you trust it enough to not check the tracker yourself every morning?"

**Why this works:** It surfaces Priya's trust criteria — the real adoption barrier. Her answer shapes the OPC's reporting and notification design more than any technical question.

---

## What NOT to do

- ❌ Don't present your deliverables — she hasn't asked to see them
- ❌ Don't ask "tell me about your process" — she'll read it as bluffing
- ❌ Don't ask about systems she wouldn't know (API availability, Workday field exposure) — those are IT questions
- ❌ Don't bluff domain knowledge — if you're unsure about something, say so and ask
- ❌ Don't fill silences with talking — let her answer, even if she pauses
- ❌ Don't chase precision on numbers — patterns matter more than exact counts

---

## Key Assumptions to Validate (if answers come naturally)

| # | What you assumed | What changes if wrong |
|---|---|---|
| Consulting is the main pain point | If audit/tax are equally bad → OPC scope expands |
| ~15% non-standard hire rate | If higher → HITL rate rises, coverage KPI drops |
| Tracker is stable (~2yr layout) | If unstable → need schema-resilient integration or migration |
| Priya updates tracker first, Workday later | If reversed → data flow architecture changes |
| Nobody owns routing governance | If someone does → different fix path |

