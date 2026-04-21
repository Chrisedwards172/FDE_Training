# Stakeholder Presentation — HR Onboarding Coordination

A non-technical overview of the spec in [`../spec-hr-onboarding-coordination.md`](../spec-hr-onboarding-coordination.md), intended for HR Ops leadership, compliance, and finance stakeholders who will sponsor or block the build.

## Files

| File | Purpose |
|---|---|
| `HR-Onboarding-Coordination-Stakeholder-Overview.pptx` | The generated deck (10 slides, 16:9) |
| `build_stakeholder_deck.py` | The script that produces the deck. Edit this to change content; do not hand-edit the `.pptx` |

## Design language

Claude-inspired: typography-first, single warm coral accent (`#D97757`), deep ink on warm off-white, generous whitespace, no clip-art or gradients. 16:9, Calibri (swap to `Inter` or `Söhne` by editing the `FONT_HEAD` / `FONT_BODY` constants if those fonts are installed).

## Deck outline

1. **Title** — "HR Onboarding Coordination"
2. **The problem** — 220+ hires, ~40 tasks, 6 systems, with the HR Ops lead's quote
3. **Why agentic, why now** — what fits the routine 85% vs. what must stay with the judgment 15%
4. **The proposal** — three capabilities (Orchestrator, Buddy Match Proposer, Training Assigner)
5. **The delegation boundary** — what the agent handles vs. what humans always decide
6. **What success looks like** — four measurable outcomes (three targets + one non-negotiable)
7. **What we still need to validate** — the three highest-leverage open questions
8. **What could go wrong** — four failure modes and how the design absorbs each
9. **What we're asking for** — three specific asks, in order
10. **Close** — questions, reactions, objections

## Regenerating the deck

```powershell
cd Spec-Generation\presentation
py build_stakeholder_deck.py
```

Requires `python-pptx`. Install with `py -m pip install python-pptx` if it isn't already on the machine.

## When to update

- After any change to the spec's **success metrics**, **delegation boundary**, or **capability count** — those are the slides stakeholders remember.
- After a coach session moves an assumption from `[ASSUMED]` to `[TESTED]` — update slide 7 to reflect what's now validated.
- Do **not** add rubric detail or physical calendar dates — both are sealed per `CLAUDE.md`.

