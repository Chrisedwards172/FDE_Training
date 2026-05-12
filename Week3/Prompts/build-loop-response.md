# Prompt — Build-Loop Response Memo (D#5)

> **This is a lightweight trigger prompt.** Use `build-loop-response-checklist.md` to verify output after generation. The diagnostic taxonomy is in `../SupportingDocs/Reference/spec-ambiguity-vs-builder-mistakes.md` — read it end-to-end before using this prompt.

## Instruction

Produce **Deliverable #5 — Build-Loop Response Memo** based on your Wednesday afternoon diagnosis of the **Cascade Public Libraries Hold Queue** fixture.

**Input dependencies:**
- Your Wednesday solo build-loop exercise notes/submission (Cascade Libraries fixture)
- `Reference/spec-ambiguity-vs-builder-mistakes.md` — the 4-category diagnostic taxonomy
- The fixture itself: spec + build output from `W3D3-BuildLoop-Exercise.md`

**What this deliverable must contain:**

For each signal (discrepancy between spec and build output), classify and respond:

### Classification Categories
1. **Spec gap** — spec was ambiguous or incomplete; you own the fix → write a spec revision
2. **Builder misread** — spec was clear but builder interpreted it wrong → write a direct correction (collaborative tone)
3. **Unjustified implementation choice** — builder added something not in the spec → write a collaborative removal request
4. **Test/environment issue** — failure is in test setup or environment, not spec or code → write a diagnostic fix
5. **Legitimate unknown** — builder surfaced something the spec genuinely didn't cover → acknowledge, revise spec, confirm

### Per-Signal Structure
For each signal, provide:
- **Signal description** — what you observed (quote the code/output)
- **Classification** — which category (1–5) and why
- **Evidence** — quote the spec alongside the build output to show the gap/misread
- **Response** — the corrective action in the right tone for the category
- **Spec revision** (if applicable) — the rewritten spec text that would prevent this in the next build loop

**Critical check:** Most missed classifications come from stopping at the surface signal ("the test is wrong") without reading the spec alongside the code. For every signal, show the spec text AND the build output side by side.

## Output Location

- Gate (Friday): `../Gate3/Output/build-loop-response-{NNN}.md`

## After Generation

1. Run through `build-loop-response-checklist.md`
2. Check: does every signal have spec text AND build output quoted side by side?
3. Check: are you sure the "builder misread" signals aren't actually spec gaps? (Most common error)
4. Check: is the tone right per category? (Spec gaps = own it; builder misreads = collaborative correction, not blame)
5. Check: do spec revisions actually fix the ambiguity, or just add more words?
