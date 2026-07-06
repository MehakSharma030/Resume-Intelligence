from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(
        match_score,
        skills,
        missing_skills,
        recommendations,
        ai_analysis):

    file_path = "resume_analysis_report.pdf"

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        "Resume Analysis Report",
        styles['Title']
    )

    story.append(title)
    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>Match Score:</b> {match_score}%",
            styles['Normal']
        )
    )

    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            f"<b>Detected Skills:</b> {', '.join(skills)}",
            styles['Normal']
        )
    )

    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            f"<b>Missing Skills:</b> {', '.join(missing_skills)}",
            styles['Normal']
        )
    )

    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            "<b>Recommendations:</b>",
            styles['Heading2']
        )
    )

    for rec in recommendations:
        story.append(
            Paragraph(rec, styles['Normal'])
        )

    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            "<b>AI Career Analysis:</b>",
            styles['Heading2']
        )
    )

    story.append(
        Paragraph(ai_analysis.replace("\n", "<br/>"),
                  styles['Normal'])
    )

    doc.build(story)

    return file_path