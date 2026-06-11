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
    leftMargin=16 * mm, rightMargin=16 * mm,
    topMargin=14 * mm, bottomMargin=12 * mm,
    title="Mohammad Saud - Resume",
    author="Mohammad Saud",
)

name_st = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=22,
                         leading=26, textColor=INK)
title_st = ParagraphStyle("title", fontName="Helvetica", fontSize=9.5,
                          leading=13, textColor=ACCENT, spaceBefore=2)
contact_st = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.5,
                            leading=12, textColor=SOFT, spaceBefore=3)
h_st = ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=10.5,
                      leading=13, textColor=ACCENT, spaceBefore=9, spaceAfter=2)
role_st = ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=9.5,
                         leading=12.5, textColor=INK, spaceBefore=4)
body_st = ParagraphStyle("body", fontName="Helvetica", fontSize=8.8,
                         leading=12, textColor=SOFT, alignment=TA_LEFT)
bullet_st = ParagraphStyle("bullet", parent=body_st, leftIndent=9,
                           bulletIndent=0, spaceBefore=1)

def rule():
    return HRFlowable(width="100%", thickness=0.7, color=LINE,
                      spaceBefore=1, spaceAfter=3)

def b(text):
    return Paragraph(u"<bullet><font color='#C2491D'>–</font></bullet> " + text, bullet_st)

story = [
    Paragraph("MOHAMMAD SAUD", name_st),
    Paragraph("Digital Content and Communications Officer @ CeRDI &nbsp;|&nbsp; "
              "Digital Health Innovator &nbsp;|&nbsp; Aspiring Project Manager &amp; Business Analyst",
              title_st),
    Paragraph("Ballarat, Victoria, Australia &nbsp;·&nbsp; msaud1959@gmail.com &nbsp;·&nbsp; "
              "linkedin.com/in/mohammadsaud &nbsp;·&nbsp; github.com/msaud1959", contact_st),
    Spacer(1, 4),

    Paragraph("PROFILE", h_st), rule(),
    Paragraph("IT student at Federation University Australia working at the intersection of software, data and "
              "people. Professional experience in research-data publishing, GIS/spatial data, web content, QA and "
              "stakeholder communication at CeRDI; founder of KidneyMate, a chronic kidney disease self-management "
              "app developed through the FORGE Pre-Accelerator. Aiming for project management and business analysis "
              "roles in agile teams.", body_st),

    Paragraph("EXPERIENCE", h_st), rule(),
    Paragraph("Digital Content and Communications Officer — CeRDI, Federation University "
              "<font color='#4F5763' size='8'>&nbsp;&nbsp;2024 – Present</font>", role_st),
    b("Contributed to <b>Visualising Australasia's Soils (VAS)</b>: preparing, checking and publishing soil and "
      "land research data for a public knowledge portal."),
    b("Digitised and restructured the <b>Victorian Resources Online (VRO)</b> archive — decades of legacy "
      "scientific content made searchable and reusable."),
    b("Handled <b>GIS and spatial datasets</b> (QGIS) behind interactive map portals."),
    b("Managed web content and digital assets; performed <b>software testing/QA</b> and wrote internal documentation."),
    b("Liaised with researchers and project stakeholders to verify and ship content accurately."),

    Paragraph("Founder — KidneyMate (FORGE Pre-Accelerator) "
              "<font color='#4F5763' size='8'>&nbsp;&nbsp;2025</font>", role_st),
    b("Designed and built a cross-platform CKD self-management app (Flutter, Supabase, PostgreSQL): diet and fluid "
      "tracking, symptom logging, medication reminders and patient education."),
    b("Validated the problem through research and customer discovery; pitched the venture to mentors and judges."),

    Paragraph("PROJECTS", h_st), rule(),
    b("<b>KidneyMate</b> — CKD self-management app; founder, product and development. Flutter · Supabase · SQL."),
    b("<b>Visualising Australasia's Soils</b> — research-data portal work at CeRDI. QGIS · metadata · QA · documentation."),
    b("<b>RetailSenseAI</b> — retail decision-support system (university team project): requirements, data "
      "modelling, analytics dashboards and final business-case presentation. Python · SQL."),

    Paragraph("EDUCATION", h_st), rule(),
    Paragraph("Bachelor of Information Technology — Federation University Australia "
              "<font color='#4F5763' size='8'>&nbsp;&nbsp;2023 – Present</font>", role_st),
    b("Focus areas: software development, databases and SQL, data analytics, IT project management."),

    Paragraph("SKILLS", h_st), rule(),
]

skills_rows = [
    ["Development", "Flutter · Dart · Supabase · PostgreSQL · SQL & database design · Python · HTML/CSS/JS · Git"],
    ["Data & GIS", "QGIS · spatial data management · data analytics · dashboards & visualisation · Excel"],
    ["Digital & quality", "Web content & digital asset management · testing/QA · documentation · research & reporting"],
    ["Professional", "Leadership · stakeholder & client engagement · teamwork & agile · problem-solving · pitching"],
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
    Paragraph("HIGHLIGHTS", h_st), rule(),
    b("Selected for the <b>FORGE Pre-Accelerator</b> (health-tech venture program), Ballarat."),
    b("Pitched KidneyMate to mentors, judges and a live audience."),
    b("Professional research-centre role held concurrently with full-time study."),
]

doc.build(story)
print("Wrote", OUT)
