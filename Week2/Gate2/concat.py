import os

os.chdir(r"C:\Users\ChrisEdwards1\IdeaProjects\FDE_Training\Week2\Gate2")

files = [
    'Output/cognitive-load-map-001.md',
    'Output/delegation-suitability-matrix-001.md',
    'Output/volume-value-analysis-001.md',
    'Output/agent-purpose-document-001.md',
    'Output/system-data-inventory-001.md',
    'Output/discovery-questions-001.md',
    'Output/CLAUDE-001.md',
]

header = '# Gate 2 \u2014 Chris Edwards\n\n**Scenario:** Apex Distribution Ltd \u2014 Customer Operations\n**Date:** 06.05.2026\n\n---\n\n'

parts = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        parts.append(fh.read())

# Add D7 heading prefix
parts[-1] = '# Deliverable 7 \u2014 CLAUDE.md\n\n' + parts[-1]

combined = header + '\n\n---\n\n'.join(parts)

with open('Gate2-Chris-Edwards.md', 'w', encoding='utf-8-sig') as out:
    out.write(combined)

print(f'Done. {len(combined)} chars')
print(repr(combined[:200]))


