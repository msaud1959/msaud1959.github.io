# Generates assets/Mohammad-Saud-Resume.pdf (one page, A4).
# Re-run after editing:  python tools/make_resume.py
# -*- coding: utf-8 -*-
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)

ACCENT = HexColor("#C2491D")
INK = HexColor("#181A1F")
SOFT = HexColor("#4F5763")
LINE = HexColor("#D8D2C6")

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "assets", "Mohammad-Saud-Resume.pdf")

doc = SimpleDocTemplate(
    OUT, pagesize=A4,
    leftMargin=15 * mm, rightMargin=15 * mm,
    topMargin=12 * mm, bottomMargin=10 * mm,
    title="Mohammad Saud - Resume",
    author="Mohammad Saud",
)

name_st = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=21,
                         leading=25, textColor=INK)
title_st = ParagraphStyle("title", fontName="Helvetica", fontSize=9,
                          leading=12.5, textColor=ACCENT, spaceBefore=2)
contact_st = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.5,
                            leading=12, textColor=SOFT, spaceBefore=3)
h_st = ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=10,
                      leading=12.5, textColor=ACCENT, spaceBefore=8, spaceAfter=2)
role_st = ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=9.5,
                         leading=12.5, textColor=INK, spaceBefore=4)
body_st = ParagraphStyle("body", fontName="Helvetica", fontSize=8.6,
                         leading=11.6, textColor=SOFT, alignment=TA_LEFT)
bullet_st = ParagraphStyle("bullet", parent=body_st, leftIndent=9,
                           bulletIndent=0, spaceBefore=1)

def rule():
    return HRFlowable(width="100%", thickness=0.7, color=LINE,
                      spaceBefore=1, spaceAfter=3)

def b(text):
    return Paragraph(u"<bullet><font color='#C2491D'>–</font></bullet> " + text, bullet_st)

story = [
    Paragraph("MOHAMMAD SAUD", name_st),
    Paragraph("Founder &amp; Project Manager — KidneyMate &nbsp;|&nbsp; Digital Content and Communications Officer @ CeRDI &nbsp;|&nbsp; "
              "Aspiring Project Manager &amp; Business Analyst", title_st),
    Paragraph("Ballarat, Victoria, Australia &nbsp;·&nbsp; msaud1959@gmail.com &nbsp;·&nbsp; "
              "linkedin.com/in/mohammadsaud &nbsp;·&nbsp; github.com/msaud1959", contact_st),
    Spacer(1, 3),

    Paragraph("PROFILE", h_st), rule(),
    Paragraph("Bachelor of IT graduate (Federation University Australia, June 2026, Distinction average) working at the "
              "intersection of software, data and people. Founder and Project Manager of KidneyMate, a chronic kidney "
              "disease self-management app developed from capstone to startup through the FORGE Pre-Accelerator "
              "(supported by LaunchVic). Professional experience in research-data publishing, GIS, web content, QA and "
              "stakeholder communication at CeRDI. Two-time NASA Space Apps Challenge awardee. Aiming for project "
              "management and business analysis roles in agile teams.", body_st),

    Paragraph("EXPERIENCE", h_st), rule(),
    Paragraph("Founder &amp; Project Manager — KidneyMate (FORGE Pre-Accelerator, supported by LaunchVic) "
              "<font color='#4F5763' size='8'>&nbsp;&nbsp;Jan 2026 – Present</font>", role_st),
    b("Building Australia's first chronic kidney disease self-management app — leading product direction, planning "
      "and roadmap, team coordination, market validation, pitch preparation and pilot-readiness."),
    b("Refined the problem, pitch and revenue model with mentors, clinicians and startup experts through FORGE."),

    Paragraph("Digital Content and Communications Officer — CeRDI, Federation University (Co-op Placement) "
              "<font color='#4F5763' size='8'>&nbsp;&nbsp;Oct 2025 – Present</font>", role_st),
    b("Contributed to the refreshed <b>Visualising Australasia's Soils (VAS)</b> website — a FAIR, interoperable "
      "soils knowledge system for Australia and New Zealand (Soil CRC project)."),
    b("Digitised and restructured the <b>Victorian Resources Online (VRO)</b> archive; handled GIS/spatial datasets (QGIS)."),
    b("Managed web content and digital assets; performed testing/QA, documentation and researcher liaison."),

    Paragraph("Product Owner &amp; Lead Developer — CKD App Capstone, Federation University "
              "<font color='#4F5763' size='8'>&nbsp;&nbsp;2025</font>", role_st),
    b("Led a six-person agile team over two semesters (sprints, stand-ups and backlog in Jira): symptom and "
      "well-being tracking, medication management, diet/fluid monitoring and automated reminders."),
    b("Designed the Supabase database schema and authentication; presented to industry leaders in Oct 2025."),

    Paragraph("Team Member (Technology) — Officeworks, Ballarat "
              "<font color='#4F5763' size='8'>&nbsp;&nbsp;Apr 2025 – Present</font>", role_st),
    b("Advise 30–40 customers per shift on tech products; earlier customer-service roles at 7-Eleven and Coles (2023–2025)."),

    Paragraph("EDUCATION", h_st), rule(),
    Paragraph("Bachelor of Information Technology — Federation University Australia "
              "<font color='#4F5763' size='8'>&nbsp;&nbsp;Jun 2023 – Jun 2026</font>", role_st),
    b("Distinction average; High Distinctions across all Data and Business Analytics electives."),
    Paragraph("BSc Computer Science &amp; Engineering — BRAC University, Dhaka "
              "<font color='#4F5763' size='8'>&nbsp;&nbsp;Oct 2021 – Jun 2023 (credits transferred)</font>", role_st),

    Paragraph("SKILLS", h_st), rule(),
]

skills_rows = [
    ["Development", "Flutter · Dart · Supabase · PostgreSQL · SQL & database design · Python · Next.js · HTML/CSS/JS · Git"],
    ["Data & GIS", "QGIS · spatial data management · data analytics · dashboards & visualisation · Excel"],
    ["Digital & quality", "Web content & digital asset management · testing/QA · documentation · research & reporting"],
    ["Professional", "Leadership · project management · agile (Scrum/Jira) · stakeholder engagement · pitching"],
]
cell_l = ParagraphStyle("cl", parent=body_st, fontName="Helvetica-Bold", textColor=INK)
cell_r = ParagraphStyle("cr", parent=body_st)
table = Table(
    [[Paragraph(l, cell_l), Paragraph(r, cell_r)] for l, r in skills_rows],
    colWidths=[34 * mm, None],
)
table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 1),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
]))
story.append(table)

story += [
    Paragraph("HONOURS &amp; HIGHLIGHTS", h_st), rule(),
    b("<b>NASA Space Apps Challenge 2023 (Melbourne)</b> — People's Choice Winner: Star Sailors, a Next.js "
      "citizen-science platform on NASA Earth data."),
    b("<b>NASA Space Apps Challenge 2022</b> — Global Finalist Honourable Mention &amp; 2nd Runner-Up (Bangladesh), Team Atlas."),
    b("<b>Hult Prize 2022</b> — Semi-finalist (BRAC University), healthcare-sector SDG venture concept."),
    b("<b>Duke of Edinburgh Bronze Award</b>; community volunteering (Gontobbo Youth Foundation, Dhaka)."),
    b("Languages: English and Bengali (full professional proficiency)."),
]

doc.build(story)
print("Wrote", OUT)
