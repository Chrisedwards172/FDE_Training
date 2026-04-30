from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Colour palette
DARK_NAVY = RGBColor(0x1B, 0x2A, 0x4A)
ACCENT_BLUE = RGBColor(0x2E, 0x86, 0xAB)
ACCENT_TEAL = RGBColor(0x00, 0xB4, 0xD8)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GREY = RGBColor(0xF0, 0xF0, 0xF0)
DARK_GREY = RGBColor(0x33, 0x33, 0x33)
AMBER = RGBColor(0xF4, 0xA2, 0x61)
RED_ACCENT = RGBColor(0xE7, 0x6F, 0x51)
GREEN_ACCENT = RGBColor(0x2A, 0x9D, 0x8F)

def add_bg(slide, color=DARK_NAVY):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_text_box(slide, left, top, width, height, text, font_size=18, color=WHITE, bold=False, alignment=PP_ALIGN.LEFT, font_name="Calibri"):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font_name
    p.alignment = alignment
    return txBox

def add_bullet_slide(slide, left, top, width, height, items, font_size=16, color=WHITE):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
        p.font.name = "Calibri"
        p.space_after = Pt(8)
    return txBox

def add_rect(slide, left, top, width, height, fill_color):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()
    return shape

# ============================================================
# SLIDE 1 — Title
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_rect(slide, 0, 0, 13.333, 0.08, ACCENT_TEAL)
add_text_box(slide, 1, 1.5, 11, 1.5, "Onboarding Provisioning Coordinator", 44, WHITE, True)
add_text_box(slide, 1, 3.2, 11, 1, "AI Agent Design for HR Ops — Aldridge & Sykes", 24, ACCENT_TEAL, False)
add_text_box(slide, 1, 4.5, 11, 0.8, "Prepared for: Priya Aggarwal, HR Ops Lead  |  Sponsor: CFO", 16, RGBColor(0xAA, 0xAA, 0xAA))
add_text_box(slide, 1, 5.5, 11, 0.8, "FDE Assessment  •  Week 2 Practice  •  April 2026", 14, RGBColor(0x88, 0x88, 0x88))

# ============================================================
# SLIDE 2 — The Problem
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_rect(slide, 0, 0, 13.333, 0.08, ACCENT_TEAL)
add_text_box(slide, 0.8, 0.4, 11, 0.7, "THE PROBLEM", 14, ACCENT_TEAL, True)
add_text_box(slide, 0.8, 1.0, 11, 1.2, "Onboarding delays are costing trust — and the CFO knows it", 32, WHITE, True)

# Left column
add_rect(slide, 0.8, 2.5, 5.5, 4.2, RGBColor(0x22, 0x35, 0x55))
add_text_box(slide, 1.1, 2.7, 5, 0.5, "What's happening today", 18, ACCENT_TEAL, True)
add_bullet_slide(slide, 1.1, 3.3, 5, 3.2, [
    "• 3-person team managing ~190 setups/year across 4 offices",
    "• 15% of hires are non-standard (conversions, rehires, secondments)",
    "• Equipment spec changes happen silently — auto-routing fails 3–5×/year",
    "• Tom Reeves waited 5 days for a laptop; the director emailed the CFO",
    "• Priya's Excel tracker is the real system of record, not Workday",
], 15, RGBColor(0xDD, 0xDD, 0xDD))

# Right column
add_rect(slide, 7, 2.5, 5.5, 4.2, RGBColor(0x22, 0x35, 0x55))
add_text_box(slide, 7.3, 2.7, 5, 0.5, "Why it matters", 18, AMBER, True)
add_bullet_slide(slide, 7.3, 3.3, 5, 3.2, [
    "• Consulting division generates the most complaints",
    "• Silent failures erode trust — nobody knows until the hire complains",
    "• Previous Power Automate attempt failed on contractors (2023)",
    "• Priya spends ~1.5 hrs/case on monitoring and chasing — not judgment",
    "• CFO mandate: \"make the consulting directors stop complaining\"",
], 15, RGBColor(0xDD, 0xDD, 0xDD))

# ============================================================
# SLIDE 3 — Volume × Value
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_rect(slide, 0, 0, 13.333, 0.08, ACCENT_TEAL)
add_text_box(slide, 0.8, 0.4, 11, 0.7, "WHERE TO FOCUS", 14, ACCENT_TEAL, True)
add_text_box(slide, 0.8, 1.0, 11, 0.8, "Volume × Value: New-hire system setup is the primary target", 28, WHITE, True)

# Four boxes for work streams
ws_data = [
    ("New-hire System\n& Access Setup", "~190/yr  •  3 hrs/case", "Score: 8", "PRIMARY TARGET", GREEN_ACCENT),
    ("Compliance Training\nAssignment", "~220/yr  •  45 min/case", "Score: 6", "WAVE 2 (Saba blocked)", AMBER),
    ("Buddy Matching\n& Welcome", "~220/yr  •  90 min total", "Score: 4", "RULES / AUTOMATION", RGBColor(0x88, 0x88, 0x88)),
    ("Edge-case\nResolution", "~30–50/yr  •  4 hrs/case", "Score: 5", "HUMAN + AGENT ASSIST", RGBColor(0x88, 0x88, 0x88)),
]

for i, (title, volume, score, label, accent) in enumerate(ws_data):
    x = 0.8 + i * 3.1
    add_rect(slide, x, 2.3, 2.8, 4.0, RGBColor(0x22, 0x35, 0x55))
    # Accent bar at top of card
    add_rect(slide, x, 2.3, 2.8, 0.06, accent)
    add_text_box(slide, x + 0.2, 2.5, 2.4, 1.0, title, 17, WHITE, True)
    add_text_box(slide, x + 0.2, 3.5, 2.4, 0.5, volume, 13, RGBColor(0xAA, 0xAA, 0xAA))
    add_text_box(slide, x + 0.2, 4.1, 2.4, 0.5, score, 22, accent, True)
    add_text_box(slide, x + 0.2, 4.8, 2.4, 0.5, label, 12, accent, True)

add_text_box(slide, 0.8, 6.5, 12, 0.5, "Agentic Value Score = Volume × Non-Deterministic Decision Effort (1–25 scale).  ≥8 = consider agentic.  System Setup wins on tool coverage + lived-work evidence.", 13, RGBColor(0x88, 0x88, 0x88))

# ============================================================
# SLIDE 4 — Delegation Architecture
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_rect(slide, 0, 0, 13.333, 0.08, ACCENT_TEAL)
add_text_box(slide, 0.8, 0.4, 11, 0.7, "DELEGATION ARCHITECTURE", 14, ACCENT_TEAL, True)
add_text_box(slide, 0.8, 1.0, 11, 0.8, "Not everything is agentic — and that's the point", 28, WHITE, True)

arch_data = [
    ("Fully Agentic", "1 task", "Status monitoring\n(ServiceNow poll)", GREEN_ACCENT),
    ("Agent-led\n+ Human Oversight", "4 tasks", "Routing override\nTracker sync\nStandard routing\nInitial chase", ACCENT_TEAL),
    ("Human-led\n+ Agent Support", "5 tasks", "Non-std classification\nEquipment spec\nEscalation priority\nEdge-case routing\nManager escalation", AMBER),
    ("Human Only\nor RPA", "3 tasks", "Prior cert check\nSaba assignment\nSaba tracking", RED_ACCENT),
]

for i, (title, count, examples, accent) in enumerate(arch_data):
    x = 0.8 + i * 3.1
    add_rect(slide, x, 2.2, 2.8, 4.5, RGBColor(0x22, 0x35, 0x55))
    add_rect(slide, x, 2.2, 2.8, 0.06, accent)
    add_text_box(slide, x + 0.2, 2.4, 2.4, 0.8, title, 16, accent, True)
    add_text_box(slide, x + 0.2, 3.2, 2.4, 0.4, count, 13, RGBColor(0xAA, 0xAA, 0xAA), True)
    add_text_box(slide, x + 0.2, 3.7, 2.4, 2.5, examples, 13, RGBColor(0xDD, 0xDD, 0xDD))

add_text_box(slide, 0.8, 6.9, 12, 0.4, "5 different archetypes across 13 task clusters.  Previous Power Automate failure (2023) validated this: fully-agentic broke on contractors.", 13, RGBColor(0x88, 0x88, 0x88))

# ============================================================
# SLIDE 5 — The Agent: OPC
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_rect(slide, 0, 0, 13.333, 0.08, ACCENT_TEAL)
add_text_box(slide, 0.8, 0.4, 11, 0.7, "THE AGENT", 14, ACCENT_TEAL, True)
add_text_box(slide, 0.8, 1.0, 11, 0.8, "Onboarding Provisioning Coordinator (OPC)", 32, WHITE, True)

add_text_box(slide, 0.8, 2.0, 11, 0.6, "Ensure every new hire has correct IT equipment, system access, and badge — detecting failures early and escalating with context before stakeholders complain.", 17, RGBColor(0xDD, 0xDD, 0xDD))

# KPIs
add_rect(slide, 0.8, 2.9, 12.0, 0.06, ACCENT_TEAL)
add_text_box(slide, 0.8, 3.1, 12, 0.4, "KPI TARGETS", 14, ACCENT_TEAL, True)

kpi_data = [
    ("95%", "Accuracy", "Correct spec at\nticket time"),
    ("80%", "Coverage", "Standard hires\nhandled autonomously"),
    ("24hr", "Throughput", "Max gap between\nstatus checks"),
    ("≤£5", "Cost/case", "Agent operational\ncost"),
    ("15–20%", "HITL Rate", "Cases needing\nhuman decision"),
]

for i, (value, label, desc) in enumerate(kpi_data):
    x = 0.8 + i * 2.4
    add_text_box(slide, x, 3.6, 2.2, 0.6, value, 28, ACCENT_TEAL, True, PP_ALIGN.CENTER)
    add_text_box(slide, x, 4.3, 2.2, 0.4, label, 14, WHITE, True, PP_ALIGN.CENTER)
    add_text_box(slide, x, 4.7, 2.2, 0.8, desc, 12, RGBColor(0xAA, 0xAA, 0xAA), False, PP_ALIGN.CENTER)

# Objectives
add_rect(slide, 0.8, 5.6, 12.0, 0.06, ACCENT_TEAL)
add_text_box(slide, 0.8, 5.8, 12, 0.4, "THREE OBJECTIVES", 14, ACCENT_TEAL, True)
add_bullet_slide(slide, 0.8, 6.2, 12, 1.2, [
    "1. Eliminate silent provisioning failures — detect spec mismatches at ticket-creation time, not day 5",
    "2. Reduce escalation cycle time — surface SLA breaches with context before the CFO gets involved",
    "3. Free Priya from routine monitoring — reserve human attention for judgment calls",
], 15, RGBColor(0xDD, 0xDD, 0xDD))

# ============================================================
# SLIDE 6 — Autonomy Matrix
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_rect(slide, 0, 0, 13.333, 0.08, ACCENT_TEAL)
add_text_box(slide, 0.8, 0.4, 11, 0.7, "AUTONOMY BOUNDARIES", 14, ACCENT_TEAL, True)
add_text_box(slide, 0.8, 1.0, 11, 0.8, "What the agent decides alone vs what needs Priya", 28, WHITE, True)

tiers = [
    ("AGENT DECIDES ALONE", GREEN_ACCENT, [
        "Monitor all ServiceNow tickets daily",
        "Detect SLA breaches",
        "Update tracker with current status",
        "Daily sync (status + start date) → Workday",
        "Raise tickets for standard FTEs (confidence ≥80%)",
        "Validate location codes on tickets",
    ]),
    ("AGENT ACTS → HUMAN NOTIFIED", ACCENT_TEAL, [
        "One-level priority reset (P4→P3)",
        "Flag Amber risk with reason",
        "Auto-elevate on inbound stakeholder email",
        "Manchester/Leeds building access via ServiceNow",
    ]),
    ("AGENT PROPOSES → HUMAN APPROVES", AMBER, [
        "Equipment spec for stale/unknown roles",
        "Priority jump >1 level (needs Priya)",
        "Tickets for non-standard hire types",
        "Red risk flag (Priya confirms)",
        "Birmingham/Dublin building access (draft email)",
        "Rehire sub-classification (reactivate vs new)",
    ]),
    ("HUMAN TAKES OVER", RED_ACCENT, [
        "Classify non-standard hires",
        "CFO-level escalation calibration",
        "ServiceNow/Workday data conflicts",
        "Start date decisions",
        "IT negotiation for record reactivation",
    ]),
]

for i, (title, accent, items) in enumerate(tiers):
    x = 0.8 + i * 3.1
    h = 4.5
    add_rect(slide, x, 2.2, 2.8, h, RGBColor(0x22, 0x35, 0x55))
    add_rect(slide, x, 2.2, 2.8, 0.06, accent)
    add_text_box(slide, x + 0.15, 2.35, 2.5, 0.6, title, 11, accent, True)
    add_bullet_slide(slide, x + 0.15, 2.95, 2.5, h - 1.0, ["• " + item for item in items], 11, RGBColor(0xDD, 0xDD, 0xDD))

# ============================================================
# SLIDE 7 — Escalation Triggers
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_rect(slide, 0, 0, 13.333, 0.08, ACCENT_TEAL)
add_text_box(slide, 0.8, 0.4, 11, 0.7, "ESCALATION TRIGGERS", 14, ACCENT_TEAL, True)
add_text_box(slide, 0.8, 1.0, 11, 0.8, "6 triggers — each with a named target and urgency", 28, WHITE, True)

triggers = [
    ("ET-1", "Non-standard hire detected", "Division coordinator\n(Dev or Sarah)", "4 hours"),
    ("ET-2", "Spec/location confidence <80%", "Priya", "Before ticket"),
    ("ET-3", "SLA breach + high-sensitivity", "Priya", "Immediate"),
    ("ET-4", "Auto-routing mismatch", "Division coordinator", "2 hours"),
    ("ET-5", "Priority jump >1 level", "Priya", "Before action"),
    ("ET-6", "Agent confidence <70%", "Division coordinator", "Before action"),
]

y_start = 2.2
for i, (code, condition, target, urgency) in enumerate(triggers):
    y = y_start + i * 0.75
    bg_color = RGBColor(0x22, 0x35, 0x55) if i % 2 == 0 else RGBColor(0x1E, 0x30, 0x50)
    add_rect(slide, 0.8, y, 11.7, 0.65, bg_color)
    add_text_box(slide, 1.0, y + 0.1, 1.0, 0.45, code, 14, ACCENT_TEAL, True)
    add_text_box(slide, 2.2, y + 0.1, 4.5, 0.45, condition, 14, WHITE)
    add_text_box(slide, 7.0, y + 0.1, 3.0, 0.45, target, 12, RGBColor(0xDD, 0xDD, 0xDD))
    add_text_box(slide, 10.2, y + 0.1, 2.0, 0.45, urgency, 12, AMBER, True)

# Sensitivity rules
add_rect(slide, 0.8, 6.8, 11.7, 0.06, ACCENT_TEAL)
add_text_box(slide, 0.8, 7.0, 11.7, 0.4, "HIGH-SENSITIVITY AUTO-INFERENCE — confirmed with Priya:", 13, ACCENT_TEAL, True)

sens_items = "Consulting ≥ Manager → Amber baseline  |  Dublin → elevated  |  Partner-sponsored → Red from day one  |  Client-facing + imminent start → elevated  |  Inbound stakeholder email → auto-elevate"
add_text_box(slide, 0.8, 7.3, 11.7, 0.3, sens_items, 12, RGBColor(0xAA, 0xAA, 0xAA))

# ============================================================
# SLIDE 8 — Systems & Integration
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_rect(slide, 0, 0, 13.333, 0.08, ACCENT_TEAL)
add_text_box(slide, 0.8, 0.4, 11, 0.7, "SYSTEMS & INTEGRATION", 14, ACCENT_TEAL, True)
add_text_box(slide, 0.8, 1.0, 11, 0.8, "What the agent connects to — and what's missing", 28, WHITE, True)

systems = [
    ("Workday", "REST API", "✅", "Read + daily/weekly sync", GREEN_ACCENT),
    ("ServiceNow", "REST API", "✅", "Read/Write tickets (Mcr, Leeds)", GREEN_ACCENT),
    ("Master Tracker", "Graph API", "⚠️", "Read/Write — stable but fragile", AMBER),
    ("Outlook", "Graph API", "✅", "Notifications + reactive signals", GREEN_ACCENT),
    ("Spec + Location Repo", "New build", "🆕", "Must create — critical dependency", RED_ACCENT),
    ("Birmingham Facilities", "Email only", "⚠️", "Draft email → coordinator sends", AMBER),
    ("Dublin Office Mgr", "Email only", "⚠️", "Draft email → coordinator sends", AMBER),
    ("Saba LMS", "No API", "🚫", "Out of scope — Wave 2", RGBColor(0x88, 0x88, 0x88)),
]

y_start = 2.2
for i, (name, api, status, note, accent) in enumerate(systems):
    y = y_start + i * 0.58
    bg_color = RGBColor(0x22, 0x35, 0x55) if i % 2 == 0 else RGBColor(0x1E, 0x30, 0x50)
    add_rect(slide, 0.8, y, 11.7, 0.5, bg_color)
    add_text_box(slide, 1.0, y + 0.05, 2.5, 0.4, name, 14, WHITE, True)
    add_text_box(slide, 3.7, y + 0.05, 1.8, 0.4, api, 12, RGBColor(0xAA, 0xAA, 0xAA))
    add_text_box(slide, 5.7, y + 0.05, 0.5, 0.4, status, 14, accent, True, PP_ALIGN.CENTER)
    add_text_box(slide, 6.5, y + 0.05, 5.5, 0.4, note, 12, RGBColor(0xDD, 0xDD, 0xDD))

# Governance callout
add_rect(slide, 0.8, 7.0, 11.7, 0.4, RGBColor(0x3D, 0x1F, 0x1F))
add_text_box(slide, 1.0, 7.05, 11.3, 0.35, "⚠  GOVERNANCE GAP: Nobody owns the routing-update chain (Procurement → IT → HR Ops). Agent detects mismatches but cannot fix root cause.", 13, RED_ACCENT, True)

# ============================================================
# SLIDE 9 — Failure Modes
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_rect(slide, 0, 0, 13.333, 0.08, ACCENT_TEAL)
add_text_box(slide, 0.8, 0.4, 11, 0.7, "FAILURE MODES", 14, ACCENT_TEAL, True)
add_text_box(slide, 0.8, 1.0, 11, 0.8, "What could go wrong — and how we recover", 28, WHITE, True)

failures = [
    ("FM-1", "Stale spec repository", "Agent orders wrong equipment\n(same failure as today, now blamed on AI)", "Timestamp every spec; escalate to human\nif >90 days stale for consulting division"),
    ("FM-2", "False-positive SLA alerts", "Alert fatigue — Priya ignores\nagent notifications", "Require 2 consecutive missed checkpoints;\nprovide confidence score with each alert"),
    ("FM-3", "Escalation without context", "Priya must investigate from scratch —\nadds work instead of saving it", "Every escalation includes: hire profile,\nstakeholder context, timeline, recommended action"),
    ("FM-4", "Agent acts beyond boundary", "Resets priority when reason was valid\n(e.g. start date pushed back)", "Priority jumps >1 level require Priya's\napproval before execution"),
]

for i, (code, title, bad_output, recovery) in enumerate(failures):
    y = 2.2 + i * 1.25
    add_rect(slide, 0.8, y, 11.7, 1.1, RGBColor(0x22, 0x35, 0x55))
    add_text_box(slide, 1.0, y + 0.1, 1.0, 0.4, code, 14, RED_ACCENT, True)
    add_text_box(slide, 2.2, y + 0.1, 2.5, 0.4, title, 14, WHITE, True)
    add_text_box(slide, 2.2, y + 0.5, 4.0, 0.6, bad_output, 11, RGBColor(0xAA, 0xAA, 0xAA))
    add_text_box(slide, 7.5, y + 0.1, 0.1, 0.9, "→", 20, ACCENT_TEAL, False, PP_ALIGN.CENTER)
    add_text_box(slide, 8.0, y + 0.15, 4.2, 0.8, recovery, 12, GREEN_ACCENT)

# ============================================================
# SLIDE 10 — Implementation Roadmap
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_rect(slide, 0, 0, 13.333, 0.08, ACCENT_TEAL)
add_text_box(slide, 0.8, 0.4, 11, 0.7, "IMPLEMENTATION ROADMAP", 14, ACCENT_TEAL, True)
add_text_box(slide, 0.8, 1.0, 11, 0.8, "Three waves — Wave 1 funds the rest", 28, WHITE, True)

waves = [
    ("WAVE 1", "Self-funding foundation", GREEN_ACCENT, [
        "Onboarding Provisioning Coordinator (OPC)",
        "Workday + ServiceNow API integrations",
        "Equipment Spec + Location Repository",
        "Master Tracker interface",
        "Escalation context assembly",
    ], "Target: ≤12 month payback"),
    ("WAVE 2", "Compounding", AMBER, [
        "Compliance training routing agent",
        "Saba LMS workaround (RPA or integration)",
        "Routing rules engine",
        "Reuses Wave 1 Workday integration",
    ], "Requires: Saba access solution"),
    ("WAVE 3", "AI-native operations", RGBColor(0x88, 0x88, 0x88), [
        "Buddy matching automation",
        "Edge-case agent assist",
        "Multi-agent coordination",
        "Reuses all Wave 1–2 assets",
    ], "Lower priority; reuses all prior work"),
]

for i, (title, subtitle, accent, items, note) in enumerate(waves):
    x = 0.8 + i * 4.1
    add_rect(slide, x, 2.2, 3.8, 4.5, RGBColor(0x22, 0x35, 0x55))
    add_rect(slide, x, 2.2, 3.8, 0.06, accent)
    add_text_box(slide, x + 0.2, 2.4, 3.4, 0.5, title, 20, accent, True)
    add_text_box(slide, x + 0.2, 2.9, 3.4, 0.4, subtitle, 13, RGBColor(0xAA, 0xAA, 0xAA))
    add_bullet_slide(slide, x + 0.2, 3.4, 3.4, 2.5, ["• " + item for item in items], 12, RGBColor(0xDD, 0xDD, 0xDD))
    add_text_box(slide, x + 0.2, 6.2, 3.4, 0.4, note, 11, accent, True)

add_text_box(slide, 0.8, 7.0, 12, 0.4, "Compounding thesis: each wave builds shared integrations (Workday API, ServiceNow API, Graph API, Tracker interface) that reduce marginal cost of subsequent agents.", 13, RGBColor(0x88, 0x88, 0x88))

# ============================================================
# SLIDE 11 — What We Still Need to Confirm
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_rect(slide, 0, 0, 13.333, 0.08, ACCENT_TEAL)
add_text_box(slide, 0.8, 0.4, 11, 0.7, "OPEN QUESTIONS", 14, ACCENT_TEAL, True)
add_text_box(slide, 0.8, 1.0, 11, 0.8, "Honest unknowns — what we still need from you and IT", 28, WHITE, True)

# Confirmed column
add_rect(slide, 0.8, 2.2, 5.8, 4.8, RGBColor(0x22, 0x35, 0x55))
add_rect(slide, 0.8, 2.2, 5.8, 0.06, GREEN_ACCENT)
add_text_box(slide, 1.0, 2.35, 5.4, 0.4, "CONFIRMED (from Priya)", 14, GREEN_ACCENT, True)
add_bullet_slide(slide, 1.0, 2.85, 5.4, 4.0, [
    "✓  Routing failures are recurring (~3–5/yr), cross-division",
    "✓  Escalation patterns are codifiable (consulting, Dublin, partner)",
    "✓  Tracker layout stable ~2 years; header-based reading works",
    "✓  HR Ops can modify tickets but not routing config",
    "✓  Building access varies by office (ServiceNow / email)",
    "✓  Coordinator assignment by division (Dev / Sarah)",
    "✓  Daily lightweight sync + weekly full reconciliation preferred",
    "✓  Power Automate failed on non-standard hires (2023)",
], 13, RGBColor(0xDD, 0xDD, 0xDD))

# Still unknown column
add_rect(slide, 6.9, 2.2, 5.8, 4.8, RGBColor(0x22, 0x35, 0x55))
add_rect(slide, 6.9, 2.2, 5.8, 0.06, AMBER)
add_text_box(slide, 7.1, 2.35, 5.4, 0.4, "STILL TO CONFIRM (IT / Finance)", 14, AMBER, True)
add_bullet_slide(slide, 7.1, 2.85, 5.4, 4.0, [
    "?  Workday API field availability (hire type, employment history)",
    "?  ServiceNow API service account permissions for HR Ops",
    "?  Saba LMS bulk upload or RPA tolerance (Wave 2)",
    "?  Fully loaded HR Ops hourly cost (for ROI model)",
    "?  SSO/RBAC constraints on service accounts",
    "?  SLA fulfilment windows per ticket type (estimated, not confirmed)",
    "?  Spec confidence scoring weights (initial estimates, needs tuning)",
], 13, RGBColor(0xDD, 0xDD, 0xDD))

add_text_box(slide, 0.8, 7.2, 12, 0.3, "Every unknown is logged as an assumption with a confidence level and a test. We don't bluff — we mark what we don't know.", 13, RGBColor(0x88, 0x88, 0x88))

# ============================================================
# SLIDE 12 — Next Steps
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide)
add_rect(slide, 0, 0, 13.333, 0.08, ACCENT_TEAL)
add_text_box(slide, 0.8, 0.4, 11, 0.7, "NEXT STEPS", 14, ACCENT_TEAL, True)
add_text_box(slide, 0.8, 1.0, 11, 0.8, "What we need from you to move forward", 32, WHITE, True)

steps = [
    ("1", "IT Discovery Session", "Confirm Workday API fields, ServiceNow service account, and SLA windows with Raj (HRIS) and IT team", "This week"),
    ("2", "Spec Repository Pilot", "Build the equipment spec + location-code repository as a SharePoint List; populate with current specs from each division", "2 weeks"),
    ("3", "Governance Recommendation", "Propose a quarterly routing-review process linking Procurement → IT → HR Ops so spec changes trigger routing updates", "Present to CFO"),
    ("4", "OPC Prototype", "Build and test against 10 real onboarding cases (recent, with known outcomes) — validate accuracy and HITL rate", "4 weeks"),
]

for i, (num, title, desc, timeline) in enumerate(steps):
    y = 2.5 + i * 1.15
    add_rect(slide, 0.8, y, 11.7, 1.0, RGBColor(0x22, 0x35, 0x55))
    add_text_box(slide, 1.0, y + 0.15, 0.5, 0.5, num, 28, ACCENT_TEAL, True, PP_ALIGN.CENTER)
    add_text_box(slide, 1.8, y + 0.1, 2.5, 0.4, title, 16, WHITE, True)
    add_text_box(slide, 1.8, y + 0.5, 6.5, 0.4, desc, 12, RGBColor(0xAA, 0xAA, 0xAA))
    add_text_box(slide, 10.0, y + 0.2, 2.2, 0.4, timeline, 13, AMBER, True, PP_ALIGN.RIGHT)

output_path = r"C:\Users\ChrisEdwards1\IdeaProjects\FDE_Training\Week2\Output\OPC-Stakeholder-Deck.pptx"
prs.save(output_path)
print(f"Saved to {output_path}")

