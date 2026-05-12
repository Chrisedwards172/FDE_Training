# Checklist — Build-Loop Response Memo (D#5)

> Use **after** generating your Build-Loop Response Memo to verify completeness.

## Completeness Check

### Signal Coverage

- [ ] Every discrepancy between spec and build output is identified as a signal
- [ ] No signals skipped or hand-waved ("minor issue, not worth addressing")
- [ ] Signals cover different parts of the fixture (not all from one section)

### Classification Accuracy

- [ ] Each signal is classified into exactly one of the 5 categories
- [ ] Classification reasoning is stated (why this category, not the adjacent one)
- [ ] **Spec gaps are owned** — not blamed on the builder
- [ ] **Builder misreads cite clear spec text** that the builder should have followed
- [ ] **Unjustified additions are not conflated with creative interpretation** — distinguish "builder added feature X not in spec" from "builder interpreted vague requirement as feature X"

### Evidence Quality

- [ ] Every signal shows **spec text quoted** alongside **build output quoted**
- [ ] The quotes are specific (line-level), not summaries
- [ ] The reader can verify the classification from the evidence alone

### Response Tone

- [ ] Spec gap responses: own the fix ("I need to revise the spec to clarify...")
- [ ] Builder misread responses: collaborative correction ("The spec states X; the build implements Y. Please align to spec.")
- [ ] Unjustified addition responses: collaborative removal ("This feature isn't in the spec. Please remove unless you identified a requirement I missed — if so, flag it.")
- [ ] Legitimate unknown responses: acknowledge + revise ("Good catch — the spec didn't cover this. Adding to spec revision.")

### Spec Revisions

- [ ] Every spec gap has a revised spec text that would prevent the ambiguity
- [ ] Revisions are precise (not "clarify the requirement" — show the new wording)
- [ ] Revisions include worked examples where the ambiguity was in semantics

## Anti-Pattern Self-Check

| Anti-pattern | Signal | Fix |
|---|---|---|
| **First-impression diagnosis** | Classification based on gut feeling without reading spec alongside code | Re-read spec and code side by side for every signal |
| **Everything is a builder misread** | Most signals classified as Category 2 | Re-examine — is the spec actually clear enough? Many "misreads" are spec gaps |
| **Tone mismatch** | Blaming the builder for spec gaps, or owning builder errors | Match tone to category — see taxonomy document |
| **Revision by addition** | Adding paragraphs of clarification instead of precise rewording | One clear sentence beats three vague ones |

## Feed-Forward

The diagnostic skill practised here applies directly to D#9 (self-spec build-loop reflection) — same taxonomy, same response structure, but applied to YOUR OWN spec output.

