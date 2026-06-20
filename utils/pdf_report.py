from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime



def generate_pdf(
        filename,
        final_score,
        resume_skills,
        matched_skills,
        missing_skills,
        status,
        email
):
    
    today = datetime.now().strftime("%d-%m-%Y")

    pdf = SimpleDocTemplate(filename, pagesize=letter)


    styles = getSampleStyleSheet()


    content = []


    content.append(
        Paragraph(
            "================="
            "AI Resume Report"
            "=================",
            styles["Title"]
        )
    )

    content.append(
        Paragraph(
            f"Generated On: {today}",
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            f"Candidate Email: {email}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 10)
    )


    content.append(
        Paragraph(
            f"Overall Score: {final_score}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Status: {status}",
            styles["Heading2"]
        )
    )


    content.append(Spacer(1,20))


    content.append(
        Paragraph(
            "Resume Skills:",
            styles["Heading2"]
        )
    )


    content.append(
        Paragraph(
            ", ".join(resume_skills),
            styles["Normal"]
        )
    )


    content.append(Spacer(1,20))


    content.append(
        Paragraph(
            "Matched Skills:",
            styles["Heading2"]
        )
    )


    for skill in matched_skills:
        content.append(
            Paragraph(
                    f"✓ {skill}",
            styles["Normal"]
            )
        )


    content.append(Spacer(1,20))


    content.append(
        Paragraph(
            "Missing Skills:",
            styles["Heading2"]
        )
    )


    for skill in missing_skills:
        content.append(
            Paragraph(
                f"✗ {skill}",
                styles["Normal"]
            )
        )


    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )   
    )

    for skill in missing_skills:
        content.append(
            Paragraph(
                f"• Improve {skill}",
                styles["Normal"]
            )
        )



    pdf.build(content)