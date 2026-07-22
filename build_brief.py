from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Faircreek_ASF_Integrated_Planning_Brief_v2.pdf"

NAVY = colors.HexColor("#26303f")
SLATE = colors.HexColor("#526273")
ORANGE = colors.HexColor("#ef7d10")
PALE = colors.HexColor("#f3f5f7")
LINE = colors.HexColor("#d7dde4")
GREEN = colors.HexColor("#356b5b")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Title2", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=25, leading=29, textColor=NAVY, alignment=TA_CENTER, spaceAfter=8))
styles.add(ParagraphStyle(name="Subtitle2", parent=styles["Normal"], fontName="Helvetica", fontSize=10.5, leading=15, textColor=SLATE, alignment=TA_CENTER, spaceAfter=18))
styles.add(ParagraphStyle(name="H1x", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=NAVY, spaceBefore=11, spaceAfter=8, keepWithNext=True))
styles.add(ParagraphStyle(name="H2x", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=11.5, leading=14, textColor=GREEN, spaceBefore=7, spaceAfter=4, keepWithNext=True))
styles.add(ParagraphStyle(name="Bodyx", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.25, leading=13.2, textColor=colors.HexColor("#202a35"), spaceAfter=7))
styles.add(ParagraphStyle(name="Smallx", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.8, leading=10.5, textColor=colors.HexColor("#27333f")))
styles.add(ParagraphStyle(name="Callout", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=NAVY, borderColor=LINE, borderWidth=0.8, borderPadding=10, backColor=PALE, spaceAfter=12))
styles.add(ParagraphStyle(name="Bulletx", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.1, leading=12.8, leftIndent=14, firstLineIndent=-8, bulletIndent=4, spaceAfter=4))
styles.add(ParagraphStyle(name="TableHead", parent=styles["Smallx"], fontName="Helvetica-Bold", textColor=colors.white))
styles.add(ParagraphStyle(name="TableText", parent=styles["Smallx"]))


def P(text, style="Bodyx"):
    return Paragraph(text, styles[style])


def bullet(text):
    return Paragraph("• " + text, styles["Bulletx"])


def table(headers, rows, widths):
    data = [[P(h, "TableHead") for h in headers]] + [[P(str(cell), "TableText") for cell in row] for row in rows]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#fafbfc")]),
    ]))
    return t


class BriefDoc(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(filename, pagesize=letter, rightMargin=0.65 * inch, leftMargin=0.65 * inch, topMargin=0.67 * inch, bottomMargin=0.62 * inch, title="Faircreek Adult Spiritual Formation Integrated Planning Brief - Version 2")
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="normal")
        self.addPageTemplates(PageTemplate(id="brief", frames=frame, onPage=self.decorate))

    def decorate(self, canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(doc.leftMargin, 0.47 * inch, letter[0] - doc.rightMargin, 0.47 * inch)
        canvas.setFillColor(SLATE)
        canvas.setFont("Helvetica", 7.5)
        canvas.drawString(doc.leftMargin, 0.28 * inch, "Faircreek Adult Spiritual Formation Integrated Planning Brief - Version 2")
        canvas.drawRightString(letter[0] - doc.rightMargin, 0.28 * inch, f"Page {doc.page}")
        canvas.restoreState()


story = []
story += [Spacer(1, 0.25 * inch), P("Faircreek Adult Spiritual Formation", "Title2"), P("Integrated Planning Brief - Version 2 | Foundations Roadmap Alignment | July 22, 2026", "Subtitle2")]
story += [P("Purpose. This revision aligns the July 5 planning brief with the completed six-course Foundations roadmap, current teaching-team work, and the decision to attribute the curriculum to <b>The Irresistible Church Network</b>. It preserves the larger formation vision: curriculum serves the pathway; it does not define the whole pathway.", "Callout")]
story += [P("Executive Summary", "H1x")]
story += [P("Faircreek is developing a reproducible adult formation pathway that helps people know, practice, and become more like Jesus through the work of the Holy Spirit. The pathway should apprentice adults into Scripture, prayer, community, generosity, service, and embodied local discipleship rather than merely transfer information.")]
story += [P("The Foundations roadmap is now a concrete first-year curriculum spine: six three-week courses, 18 weekly gatherings, and 54 teaching sessions. The recommended newcomer sequence begins with following Jesus, supplies the Bible's overarching story, develops a Trinitarian understanding of God and identity in Christ, establishes spiritual habits, and concludes with a practical method for reading Scripture well.")]
story += [P("The courses may still be offered independently or in rotation. The sequence is a recommended pathway, not a prerequisite system. Broader Adult Spiritual Formation modules may later extend beyond Foundations and use three-to-six-week formats according to subject, teacher capacity, and ministry need.")]

story += [P("1. Planning Thesis", "H1x")]
story += [P("Adult spiritual formation should be organized around the question: <b>What does a Christian need to know, practice, and become in order to live the abundant life in Christ?</b> The answer is a formation ecology held together by sound theology, trusted relationships, local examples, and repeatable rhythms.")]
for item in [
    "Move from curriculum-first planning to formation-pathway planning.",
    "Aim at whole-person transformation: mind, desires, will, habits, imagination, relationships, and public witness.",
    "Recover daily Christian competence in Scripture, prayer, community, generosity, service, and discernment.",
    "Use shared structures without erasing teacher personality or local leadership.",
    "Build toward replication by retaining outlines, resources, session plans, and lessons learned.",
]: story.append(bullet(item))

story += [P("2. What Has Advanced Since Version 1", "H1x")]
story += [table(["Planning area", "Earlier status", "Version 2 status"], [
    ["Foundations curriculum", "One possible input requiring review.", "Six courses are mapped into an 18-week curriculum spine."],
    ["Attribution", "Campus-specific language appeared in the source brief.", "Use The Irresistible Church Network for all curriculum attribution."],
    ["Course order", "No sequence established.", "A recommended newcomer pathway is defined while preserving standalone use."],
    ["Teaching teams", "Potential invitees and co-leaders were exploratory.", "A public roadmap now identifies serving, invited, and open team capacity."],
    ["Delivery length", "Six weeks was treated as the default working unit.", "Foundations courses use three weeks; other ASF modules may use three to six weeks."],
    ["Digital roadmap", "Not yet built.", "Mac-primary Git repository and synchronized public GitHub site are operational."],
], [1.25*inch, 2.25*inch, 3.7*inch])]

story += [P("3. Theological and Formation Frame", "H1x")]
story += [P("Formation is Spirit-enabled but not passive. God transforms; adults participate through practices of trust and obedience. Practices are means of responsive participation, never techniques for earning God's favor.")]
story += [table(["Formation priority", "Leadership application"], [
    ["Scripture", "Teach adults to read, meditate, interpret, remember, discuss, and obey Scripture."],
    ["Prayer", "Model personal and corporate prayer with practical, low-threat opportunities to participate."],
    ["Community", "Treat relationships, groups, mentoring, and mutual service as formation environments."],
    ["Generosity", "Connect stewardship to trust, freedom, mission, and love of neighbor."],
    ["Service and witness", "Help adults discern gifts, serve locally, and represent Jesus publicly."],
    ["Rest and other practices", "Teach rest early; evaluate fasting, solitude, and other practices with theological care."],
], [1.45*inch, 5.75*inch])]
story += [P("Guardrails", "H2x")]
for item in [
    "Keep the gospel, the Holy Spirit, Scripture, prayer, baptism, communion, and the church central.",
    "Review imported material for theological alignment, maturity fit, usefulness, and resource intensity.",
    "Pair national resources with local leaders who can model practices and respond pastorally.",
    "Avoid reducing formation to class attendance or measurable information transfer.",
]: story.append(bullet(item))

story += [P("4. Resource Posture", "H1x")]
story += [table(["Resource", "Best use", "Faircreek review question"], [
    ["Foundations from The Irresistible Church Network", "Introductory Christian formation and a repeatable first-year curriculum spine.", "Does each course fit Faircreek's theology, audience, and desired depth?"],
    ["BibleProject", "Whole-Bible framing, literary context, themes, and visual learning.", "How will local leaders connect viewing to practice and discussion?"],
    ["Practicing the Way", "Apprenticeship language, practices, and sustainable rhythms.", "Where is qualification or adaptation needed for Faircreek?"],
    ["Leader-developed material", "Local needs, testimony, competence, and embodied examples.", "What minimum template and artifacts are required for reuse?"],
], [1.55*inch, 2.7*inch, 2.95*inch])]

story += [P("5. Foundations Roadmap", "H1x")]
story += [P("Recommended newcomer sequence", "H2x")]
story += [table(["Course", "Three-week movement", "Formation contribution"], [
    ["1. How to Follow Jesus", "Invitation; Way of Jesus; Clash of Kingdoms", "Begins with Jesus's invitation, authority, way of life, and reordered priorities."],
    ["2. Understanding the Story of the Bible", "Story; Old Testament; New Testament", "Supplies creation, covenant, Messiah, church, and restoration as the narrative frame."],
    ["3. Understanding Who God Is", "Father; Son; Holy Spirit", "Develops a Trinitarian understanding of God's character, salvation, and empowerment."],
    ["4. Understanding Your New Identity", "Way God Sees Us; New Reality; New Family", "Applies the gospel to identity in Christ, life in the Spirit, and belonging in God's family."],
    ["5. How to Establish Spiritual Habits", "Reframing; Getting Started; Stretching Faith", "Moves theology into rhythms of prayer, Scripture, surrender, generosity, rest, and community."],
    ["6. How to Read the Bible Well", "Observation; Interpretation; Application", "Deepens the Bible-reading method introduced in the habits course and uses the whole-Bible context already learned."],
], [1.6*inch, 2.25*inch, 3.35*inch])]
story += [P("Sequence rationale", "H2x")]
story += [P("The sequence starts relationally with Jesus rather than academically with Bible mechanics. It then provides the biblical story, clarifies who God is, establishes identity, forms sustainable habits, and concludes with a deeper Scripture-reading method. Because The Irresistible Church Network offers these courses in rotation, Faircreek may schedule them independently when ministry timing requires it.")]

story += [P("6. Delivery Model", "H1x")]
story += [table(["Element", "Working model"], [
    ["Foundations course length", "Three weekly gatherings per course; approximately 90 minutes per gathering."],
    ["Full curriculum", "Six courses; 18 weeks; 54 short teaching sessions."],
    ["Scheduling", "Offer sequentially where possible, or rotate standalone courses across seasons."],
    ["Leadership", "Use credible local teaching teams who introduce content, guide discussion, and model the practices."],
    ["Structure", "Welcome and setup; short teaching segments; table discussion; bottom line; response and next step."],
    ["Broader ASF modules", "Use three-to-six-week formats as subject matter and capacity require; do not force every ministry topic into Foundations."],
    ["Replication", "Retain facilitator notes, adaptations, participant feedback, resources, and post-course lessons."],
], [1.65*inch, 5.55*inch])]
story += [P("Pilot-year posture", "H2x")]
for item in [
    "Let leaders lead within clear theology, outcomes, and a recognizable weekly structure.",
    "Treat the first cycle as a learning pilot; document changes rather than improvising invisibly.",
    "Use participant feedback to test accessibility, depth, discussion quality, and practical application.",
    "Evaluate whether parallel offerings are sustainable given rooms, teachers, childcare, and communication." ,
]: story.append(bullet(item))

story += [P("7. Leadership and Teaching Teams", "H1x")]
story += [P("The original brief called for an exploratory group of elders, spouses, former leaders, teachers, facilitators, and spiritually credible couples. The roadmap now includes a visible teaching-team section with confirmed, invited, and open capacity. This is progress, but public listing should not be confused with assignment readiness.")]
story += [table(["Leadership responsibility", "Expected practice"], [
    ["Pastoral ownership", "Pastor Matt frames the purpose, theological boundaries, and invitation to serve."],
    ["ASF coordination", "Dr. T organizes discovery, curriculum alignment, facilitator support, documentation, and review."],
    ["Teaching teams", "Prepare the guide, contextualize responsibly, guide discussion, model practice, and return usable notes."],
    ["Review loop", "Debrief each course with leaders and participants before repeating or expanding it."],
], [1.65*inch, 5.55*inch])]

story += [P("8. Decision Register for Pastor Matt and the ASF Team", "H1x")]
story += [table(["Decision", "Current working position", "Still needed"], [
    ["Adult threshold", "Roadmap currently says adults and does not publish a minimum age.", "Choose age 16, age 18, or a pastoral eligibility statement."],
    ["Women and leadership", "No doctrinal position is asserted in the roadmap.", "Clarify teaching, facilitation, modeling, and team expectations before assignments."],
    ["Course sequence", "Six-step newcomer pathway recommended; courses remain standalone.", "Pastor Matt's affirmation or requested revision."],
    ["Launch and cadence", "Three-week courses are ready as a curriculum model.", "Choose dates, frequency, breaks, registration approach, and room plan."],
    ["Curriculum minimums", "The source guides remain authoritative.", "Define the adaptations and artifacts each team must return."],
    ["Parallel classes", "Potentially feasible.", "Confirm room, teacher, childcare, communications, and demand constraints."],
    ["Public site", "GitHub site is synchronized with the Mac-primary repository.", "Confirm audience, visibility, and whether leader names should remain public."],
], [1.35*inch, 3.2*inch, 2.65*inch])]

story += [P("9. Updated Action Plan", "H1x")]
story += [table(["Step", "Owner", "Output", "Status / timing"], [
    ["1. Review Version 2", "Pastor Matt + Dr. T", "Agreement on formation thesis, sequence, and decision register.", "Next leadership review"],
    ["2. Confirm teaching-team posture", "Pastor Matt", "Invitation, eligibility, roles, and expectations.", "Before assignments"],
    ["3. Choose pilot calendar", "ASF team", "Dates for the first course cycle, breaks, rooms, and registration.", "After leadership review"],
    ["4. Assign first course", "ASF team", "Lead team, backup, preparation schedule, and materials.", "6-8 weeks before launch"],
    ["5. Run and observe", "Teaching team", "Three-week course with participant feedback and leader notes.", "Pilot cycle"],
    ["6. Debrief and revise", "Pastor Matt + ASF team", "What to retain, adapt, remove, or clarify before the next course.", "Within two weeks"],
    ["7. Continue pathway", "ASF team", "Next course offered sequentially or by rotation as ministry timing requires.", "Ongoing"],
    ["8. Annual synthesis", "Dr. T / ASF team", "Reusable Faircreek structure and year-two recommendations.", "End of pilot year"],
], [0.95*inch, 1.25*inch, 3.7*inch, 1.3*inch])]

pastor_questions = [P("10. Questions for Pastor Matt", "H1x")]
for item in [
    "Does the formation-pathway thesis accurately name Faircreek's pastoral need?",
    "Do you affirm the six-course recommended sequence, while allowing courses to be offered in rotation?",
    "Which course should launch first, and what season should it begin?",
    "What leadership guardrails must be settled before teaching teams are assigned?",
    "Should the public roadmap display named teaching-team candidates or only confirmed assignments?",
    "What evidence after the first course would indicate that the pilot is producing formation rather than attendance alone?",
]: pastor_questions.append(bullet(item))
story.append(KeepTogether(pastor_questions))

story += [P("11. Final Assessment", "H1x")]
story += [P("Faircreek now has more than an aspiration: it has a coherent formation thesis, a defined first-year curriculum spine, a recommended newcomer sequence, emerging teaching-team capacity, and synchronized digital infrastructure. The next step is pastoral review and a bounded pilot—not further expansion of the curriculum list.", "Callout")]
story += [P("The strongest formulation remains: <b>Faircreek should build a reproducible adult formation pathway that apprentices people into practices of abiding in Christ.</b> Foundations from The Irresistible Church Network can serve that pathway well when it is theologically reviewed, locally embodied, and evaluated for actual formation.")]

story += [P("Source and Method Note", "H1x")]
story += [P("This document revises the July 5, 2026 Faircreek Adult Spiritual Formation Integrated Planning Brief using the completed six-course Foundations roadmap, the supplied facilitator guides, and subsequent planning decisions. It is a working leadership document, not a verbatim meeting transcript. The Irresistible Church Network facilitator guides remain authoritative for course content, timing, and speaker notes.")]

doc = BriefDoc(str(OUTPUT))
doc.build(story)
print(OUTPUT)
