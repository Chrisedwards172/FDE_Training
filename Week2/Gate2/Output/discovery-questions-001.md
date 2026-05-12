# Deliverable 6 — Discovery Questions for the Main Stakeholder

> **Stakeholder:** Sarah Whitmore, COO, Apex Distribution Ltd  
> **Format:** 10-minute live clarification round. She's impatient, sceptical, and will deflect some questions.  
> **Strategy:** Lead with the questions whose answers would cause the largest design changes. Ask ~5–7; have extras ready.

---

## Priority 1 — Must-Ask (Design-Changing)

### Q1: Context assembly time — is it really the bottleneck?

**Ask:** "When Mark called in about the Stein-Allen pallet — how long did it take Sandra to pull up his route, the account, and decide what to tell him? Roughly?"

**Tension targeted:** A4 — the entire DDSA value proposition rests on context assembly taking ~5 min of the 12 min/case. If it's actually 1 minute (because dispatchers know their routes cold), the agent saves negligible time.

**Design decision:** If context assembly <2 min → DDSA's primary value shifts from speed to pattern detection (repeat accounts, driver trends). KPI targets and objectives change. If >5 min → current design is validated.

**If she hedges ("it varies"):** Push: "Give me the worst case and the best case. For a dispatcher who's been here 6 months vs Sandra who knows everything — how different is it?"

---

### Q2: Driver App API — can it push signals outward?

**Ask:** "The Driver App — when Mark sent that message, did it just sit in the app until Sandra checked, or does it pop up somewhere else too? Does it ping a screen, send a notification?"

**Tension targeted:** S1 — DDSA's real-time triggering depends entirely on the Driver App surfacing signals to external systems. If it's a self-contained app with no outbound capability, the entire architecture needs rethinking.

**Design decision:** If Driver App can push → DDSA detects exceptions in real-time (current design). If self-contained → fallback to polling dispatch console (adds 2–5 min latency, degrades the "seconds not minutes" promise). Architecture changes fundamentally.

**If she says "I'd have to check with IT":** That's an honest answer — note it. Ask: "Do dispatchers currently see Driver App messages on their dispatch console screen, or do they have to switch to a separate app?"

---

### Q3: Dispatch console — what can we actually read from it?

**Ask:** "The dispatch console — the Java thing on Citrix. If we wanted to pull route data from it automatically — drops remaining, driver position — is that something IT has done before, or is it completely locked down?"

**Tension targeted:** S2 — "limited API surface" is vague. The DDSA needs route data. If the console is truly a black box with no data export, route pressure scoring (a core context card element) is impossible.

**Design decision:** If some API exists → integrate as primary route data source. If zero API and no export → derive route data from GPS + planned route (less accurate); or accept "Route data: unavailable" on the context card. Changes the context completeness KPI target.

**If she deflects to IT:** Ask: "Has anyone ever built a report or export from the dispatch console? Even a manual CSV dump?"

---

### Q4: The £500 threshold — is it real?

**Ask:** "The SOP mentions £500 for Duty Manager escalation on high-value consignments. Your team still use that number? Or has it moved?"

**Tension targeted:** A7 — ET-1 is built around this threshold. If the SOP threshold is stale (like the rest of the SOP), the agent would trigger false escalations or miss real ones.

**Design decision:** If £500 is still correct → ET-1 stays as designed. If different (e.g. £1,000 or "it depends on the account") → need a different escalation rule. If "we don't really escalate on value anymore" → remove ET-1 entirely and redesign escalation around account sensitivity instead.

---

### Q5: What killed the chatbot and the RPA project?

**Ask:** "The chatbot in 2024 and the billing RPA — what specifically went wrong? Was it a technology problem, or did the team reject it, or did customers hate it?"

**Tension targeted:** A9 — Sarah is "sceptical of chatbots and consultants." Understanding exactly what failed tells me what the DDSA must visibly avoid. If the chatbot failed because it made decisions customers disagreed with → confirms DDSA's "never recommend, only present options" rule. If the RPA failed because of Aurum schema changes → confirms avoiding Aurum in Wave 1.

**Design decision:** If team rejection was the cause → dispatcher adoption KPI becomes the primary risk; need change management built into rollout. If customer hatred → confirms internal-only tool framing. If technology brittleness → need to address schema resilience explicitly for dispatch console integration.

---

## Priority 2 — High-Value (Ask if Time Allows)

### Q6: How do new dispatchers learn which accounts are sensitive?

**Ask:** "If a new dispatcher started Monday and Mark called in about Stein-Allen — how would they know that's a big account? Is it written somewhere, or does someone tell them?"

**Tension targeted:** A6 — account sensitivity classification (credit limit + escalation history) is DDSA's proxy for informal knowledge. If dispatchers learn sensitivity verbally over months, the agent's classification will be weaker than an experienced dispatcher's intuition — and they'll distrust it.

**Design decision:** If informal-only → DDSA starts with weak classification and must build trust via tuning. If there IS a list somewhere → ingest it as seed data. If "they just know after a few weeks" → plan for high override rate initially (adjust false-alert ceiling from 20% to 30% in first quarter).

---

### Q7: Do exceptions get logged in Salesforce or only the dispatch console?

**Ask:** "When an exception is resolved — driver got their answer, moved on — where does that get recorded? Salesforce? The dispatch console? Both?"

**Tension targeted:** S4 — if CRM has no exception records, DDSA's "exception history" card section is empty for most accounts. Pattern detection (repeat refusals) requires historical data from somewhere.

**Design decision:** If Salesforce has cases → integrate directly (low effort, API available). If console-only → history is inaccessible via API (major gap). If neither → there is no exception history at all, and "repeat pattern" detection is impossible without building a new data store.

---

### Q8: What proportion of delivery exceptions are damaged-pallet vs other types?

**Ask:** "Of your 180 exceptions a day — roughly how many are refusals like Mark's (damage/cosmetic), versus missed windows, versus something else entirely?"

**Tension targeted:** D1 cognitive load map only covers refusals in detail (grounded in Artefact 1). If damage-refusals are 10% of exceptions and missed windows are 60%, the context card needs different content for the dominant case type.

**Design decision:** If damage-refusals dominate → current context card design (value + damage assessment) is correct. If missed windows dominate → add "delivery window status" and "customer notification history" to the context card. Content changes.

---

## Priority 3 — Depth (Use if Conversation Flows There)

### Q9: Voicemail vs app — which channel do drivers actually use?

**Ask:** "Mark left a voicemail. Do most drivers do that, or do they mostly use the app? What's the split?"

**Tension targeted:** Shadow system (voicemail as primary signal channel). If 70% of exceptions come via voicemail rather than the app, DDSA needs a voicemail transcription integration — or it misses most signals.

**Design decision:** If mostly app → integrate app only (current design). If mostly voicemail → add voicemail transcription as a critical integration (changes effort from Medium to High). If split → need both channels (increases complexity and cost).

---

### Q10: Sandra's line was busy — how often are all dispatchers unavailable?

**Ask:** "Mark said Sandra's line was busy. How often does it happen that a driver can't reach anyone — all lines occupied?"

**Tension targeted:** ET-3 (driver wait >15 min triggers queue escalation). If this is rare (once a week), ET-3 is a safety net. If it's daily (peak hours), it's a core operational problem and the DDSA needs more aggressive queue management.

**Design decision:** If rare → ET-3 stays as-is (safety net). If frequent (daily during peaks) → DDSA needs to manage exception queuing proactively (priority scoring based on wait time + route pressure + account sensitivity). Becomes a primary function, not an edge case trigger.

---

## Follow-Up Probes (for evasion)

| If Sarah says... | Push with... |
|---|---|
| "It depends" / "It varies" | "Can you give me two specific examples where it went differently? What made the difference?" |
| "I'd have to check with IT" | "Fair enough — but from your team's perspective, does the data ever come out of that system into anything else? A report, a spreadsheet, anything?" |
| "We follow the process" | "Mark's voicemail suggests the process doesn't quite match what the SOP says anymore. How often does that gap show up?" |
| "We haven't had problems with that" | "The two failed projects — what would have prevented those? If I could promise you one thing about this, what would it be?" |
| Contradicts an earlier answer | "Earlier you said X, but just now that sounds different. Can you help me understand which one's closer to reality?" |

---

## Closing Question (if time allows)

> "If we built a tool that gave your dispatchers instant context on every exception — account, route, history — but it never made a decision for them, never talked to a customer, and never touched Aurum... would you let it run for a month as a trial?"

**Why this works:** Tests adoption feasibility directly. Sarah's answer reveals her real threshold for trying something new — and any constraints we haven't surfaced (union issues, IT approval process, dispatcher pushback risk).

