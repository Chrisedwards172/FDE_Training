# Build-Loop Response — Cascade Public Libraries Hold Queue

> **Exercise:** W3D3 Afternoon Build-Loop  
> **Participant:** Chris Edwards  
> **Fixture:** Cascade Public Libraries — Hold Queue Management & Notification  
> **Taxonomy:** `spec-ambiguity-vs-builder-mistakes.md` (4 categories + legitimate clarification)

---

### Signal 1 — 72-hour notification window uses calendar hours

**Classification:** Spec gap

**Rationale (1 sentence with citation):** R3 states "72 hours to claim the hold" but my Assumptions section flags that "the definition of '72 hours' in R3 as calendar hours vs business hours is not specified" — I left this unresolved and the builder had to pick.

**Response:**

This one's on me. I flagged the calendar-vs-business-hours question in my Assumptions section but never resolved it before handing off to the builder — I wrote "flagged for FDE review" and then didn't do the review. The builder implemented calendar hours, which matches the default I stated in the assumption, so the code is defensible. But I should have closed this before the build started.

---

### Signal 2 — Accessibility-priority implemented as a weight (0.25x) instead of a queue jump

**Classification:** Builder misread

**Rationale (1 sentence with citation):** R4 specifies "Accessibility-priority patrons jump to queue position 1 when they place a hold" — a positional override, not a weight multiplier; the 0.25x constant doesn't exist anywhere in my spec.

**Response:**

I need to flag this back to the builder. R4 is explicit: accessibility-priority patrons jump to position 1. I wrote it as a positional override, not a weighted calculation. The `PriorityWeights.ACCESSIBILITY = 0.25` constant the builder introduced has no basis in my spec — only R5 defines a weight (0.5x for Academic). Here's what needs to change:

1. When an accessibility-priority patron places a hold, move them to queue position 1.
2. If another accessibility-priority patron is already at position 1, apply FIFO between them (that's R4's exception clause).
3. Remove the `PriorityWeights.ACCESSIBILITY = 0.25` constant entirely.
4. `compute_effective_position` should only apply weighting for Academic-tier patrons (R5). Accessibility-priority patrons are at position 1 by rule, not by arithmetic.

---

### Signal 3 — Auto-checkout handler adds a 3-day return reminder

**Classification:** Unjustified implementation choice

**Rationale (1 sentence with citation):** R7 specifies auto-checkout and R10 specifies auto-return at end of loan period, but I didn't ask for a return reminder anywhere in my spec.

**Response:**

I can see why the builder added this — a 3-day return reminder is a sensible library feature and shows good product instinct. But it's not in my spec, and I need to keep the build aligned to what I've specified so I can track scope. The builder should remove the `schedule_reminder()` call from `auto_checkout_handler.py` for now. If the builder thinks it's genuinely worth adding, they should file a spec-change request back to me and I'll evaluate it properly — I'd want to define which channel it uses, whether it applies to manual checkouts too, and what happens if the patron has already returned the book before the reminder fires.

---

### Signal 4 — OverDrive refresh test fails in 2026 due to date-bound fixture

**Classification:** Test/environment issue

**Rationale (1 sentence with citation):** The builder's implementation of `overdrive_refresh.py` correctly implements my R8 (advance queue by number of new copies), but the test fixture `overdrive_refresh_2025_q4.json` encodes queue state from Q4 2025 that breaks when CI runs in 2026.

**Response:**

The builder's implementation is correct — it does exactly what R8 asks. The problem is the test fixture, not the code. `overdrive_refresh_2025_q4.json` has an `expected_advances` field frozen to a Q4 2025 queue state, so it fails when the clock moves forward. My preferred fix:

1. **Best option:** Refactor the test to build its own queue state in setup (create N patrons with holds, fire the refresh, assert queue advanced by N). That decouples the test from calendar time entirely.
2. **Acceptable short-term:** Regenerate the fixture for the current quarter — but that just postpones the same breakage next quarter.

The builder should not touch the implementation — it's doing the right thing.

---

### Signal 5 — Duplicate hold check blocks format-distinct holds on same title

**Classification:** Builder misread

**Rationale (1 sentence with citation):** My R11 explicitly states "if a patron places holds on the ebook and audiobook editions of the same title, the system treats them as two separate holds" — but the builder's duplicate check uses `patron_has_active_hold_on_title(patron, title_id)` which matches on `title_id` alone, blocking the second format.

**Response:**

R11 is clear on this one — I specifically wrote that ebook and audiobook holds on the same title are treated as separate holds. The builder's duplicate check in `place_hold.py` calls `patron_has_active_hold_on_title(patron, title_id)`, which checks `title_id` alone and blocks any second hold regardless of format. That contradicts R11. The builder needs to change the check to match on `(title_id, format_type)`:

```python
# Before (wrong — blocks format-distinct holds):
if patron_has_active_hold_on_title(patron, title_id):

# After (correct — allows different formats on same title):
if patron_has_active_hold_on_title_and_format(patron, title_id, format_type):
```

The hold-limit check above it is fine — both formats count toward the limit, which is what R11 says.

---

### Signal 6 — Paused holds receive a "we skipped you" email notification

**Classification:** Unjustified implementation choice

**Rationale (1 sentence with citation):** My R6 states paused holds are "skipped over when the title becomes available; the next eligible patron is notified instead" — I said the patron is skipped, not that they're told about being skipped.

**Response:**

I understand the builder's reasoning — telling a patron they were skipped feels like good UX. But I didn't specify it, and it introduces a question I haven't answered: does a patron who deliberately paused their hold want an email every time the title cycles through? For a popular title, that could mean multiple "we skipped you" notifications. The builder should remove the `send_email` call for paused holds in `handle_title_available`. If the business wants a skip notification, I'll add it as a proper requirement with frequency limits — probably notify once per pause period rather than once per availability event.

---

### Signal 7 — SMS notification is SMS-only (not dual-channel)

**Classification:** Spec gap

**Rationale (1 sentence with citation):** My R12 explicitly flags that "the business has not yet decided whether SMS-opted patrons should receive both email and SMS, or only SMS" — I left this unresolved and the builder had to pick something.

**Response:**

This is another one that's on me. I flagged the dual-channel vs SMS-only question in R12 as a pending business decision but didn't give the builder a clear interim instruction. The builder chose SMS-only, which is a reasonable default — I'm not going to ask for a change. What I am going to do is update my spec so the interim behaviour is explicit:

**Spec revision — R12 (revised):**
> "Notification channels: email by default. Patrons who registered a mobile number can opt-in to SMS notifications. **Interim behaviour (pending business decision):** SMS-opted patrons receive SMS only; email is suppressed. **Decision required before production:** confirm whether SMS-opted patrons should receive (a) SMS only, (b) both SMS and email, or (c) patron-configurable preference. Implement (a) until directed otherwise."

---

### Signal 8 — Builder question on Academic + Accessibility-priority intersection

**Classification:** Legitimate clarification request

**Rationale (1 sentence with citation):** My Assumptions section flags "Academic + Accessibility-priority intersection is not specified" pending FDE confirmation — the builder correctly identified the edge case and is blocking merge until I give direction.

**Response:**

Good catch from the builder, and exactly the right call to block the PR rather than ship a guess. The builder is right that my Assumptions section flags this without fully resolving it — that's my gap to close. Here's my direction:

**Go with interpretation (a): R4 wins. Accessibility-priority patrons jump to position 1; the Academic 0.5x weight does not apply.**

My reasoning: R4 is a positional override, not a weight. Once someone is at position 1, multiplying by 0.5 is semantically meaningless — and as the builder spotted, interpretation (b) creates a perverse outcome where academic+accessibility always beats accessibility-alone, which isn't the intent. The accessibility accommodation is an ADA/Marrakesh Treaty legal obligation; the academic weight is a partnership perk. The legal obligation takes precedence.

**Spec revision — Assumptions (revised):**
> "Academic + Accessibility-priority intersection: when a patron holds both modifiers, R4 (accessibility jump to position 1) takes precedence. The R5 academic weight (0.5x) does not apply when the patron is already at position 1 via R4. Between two accessibility-priority patrons at position 1, FIFO applies regardless of academic status."

The builder should implement interpretation (a) and unblock the PR.

---

## Reflection

The hardest diagnostic move for me was distinguishing spec gaps from adjacent categories. Signal 1 tempted me toward "acceptable variation" because my Assumptions section already stated calendar hours as the default — but I'd also flagged it "pending FDE review" without actually doing the review, which means the builder still had to guess. That taught me something concrete: flagging an assumption without resolving it before handoff is the same as not flagging it. Signal 6 was the second trap — my gut said "builder misread" because R6 doesn't mention notifying paused patrons, but the builder didn't contradict my spec, they added to it, making it an unjustified implementation choice with a completely different response tone. The move that kept me honest throughout was the ownership question: "whose artefact needs to change — my spec, the code, or the test?" If I ran this again, I'd read all eight signals before classifying any of them — the pattern emerges faster when you see them together.
