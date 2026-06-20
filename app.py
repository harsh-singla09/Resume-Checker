from flask import Flask, render_template, request, send_file
import os

from utils.extractor import pdf_text_extraction, docx_extract_text
from utils.text_cleaner import clean_text
from utils.skill_extractor import (extract_skills, missing_skill, extract_skill_categories)

from model.skill_matcher import matched_skill
from model.similarity import calculate_similarity

from utils.pdf_report import generate_pdf





app = Flask(__name__)


# Folder for uploaded resumes
UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)



@app.route("/")
def home():

    return render_template("index.html")



@app.route("/submit", methods=["POST"])
def submit():

    email = request.form.get("email")

    resume = request.files.get("resume")

    job_description = request.form.get("job_description")


    # Check file exists

    if resume is None or resume.filename == "":
        return "Please upload a resume"



    # Save uploaded file

    file_path = os.path.join(
        UPLOAD_FOLDER,
        resume.filename
    )

    resume.save(file_path)



    # ----------------------------
    # Text Extraction
    # ----------------------------

    filename = resume.filename.lower()


    if filename.endswith(".pdf"):

        extracted_text = pdf_text_extraction(file_path)


    elif filename.endswith(".docx"):

        extracted_text = docx_extract_text(file_path)


    else:

        return "Only PDF and DOCX files are allowed"


    cleaned_resume_text = clean_text(extracted_text)

#---------------------------
# For job description
#---------------------------

    cleaned_jd_text = clean_text(job_description)

    resume_skills = extract_skills(cleaned_resume_text)

    jd_skills = extract_skills(cleaned_jd_text)

    resume_skill_categories = extract_skill_categories(cleaned_resume_text)

    jd_skill_categories = extract_skill_categories(cleaned_jd_text)

    missing_skills = missing_skill(resume_skills, jd_skills)

    matched_skills = matched_skill(resume_skills, jd_skills)

#---------------------------
#Count of skills
#---------------------------

    resume_skill_count = len(resume_skills)
    jd_skill_count = len(jd_skills)
    matched_skill_count = len(matched_skills)


#-------------------------------------
#For Skill Score
#--------------------------------------

    if jd_skill_count > 0:
        skill_score = round(
            (matched_skill_count / jd_skill_count) * 100,
            2
        )
    else:
        skill_score = 0

#-------------------------------------
#For Resume Match Score
#-------------------------------------

    match_score = calculate_similarity(
    cleaned_resume_text,
    cleaned_jd_text
)
    
#----------------------------------
#For Final Score 
#----------------------------------

    final_score = round(
    (0.7 * skill_score) +
    (0.3 * match_score),
    2
)

    if final_score >= 85:
        status = "Excellent Match"

    elif final_score >= 70:
        status = "Good Match"

    elif final_score >= 50:
        status = "Average Match"

    else:
        status = "Needs Improvement"


#-------------------------------------
#For Render In Page
#-------------------------------------

    # Store report data temporarily

    app.config["REPORT_DATA"] = {

    "email": email,

    "final_score": final_score,

    "status": status,

    "resume_skills": resume_skills,

    "matched_skills": matched_skills,

    "missing_skills": missing_skills
    }


    return render_template(
        "result.html",
        resume_skills=resume_skills,
        jd_skills=jd_skills,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        resume_skill_categories=resume_skill_categories,
        jd_skill_categories=jd_skill_categories,
        final_score=final_score,
        status=status,
    )
    


@app.route("/download_report")
def download_report():

    data = app.config.get("REPORT_DATA")

    if data is None:
        return "Please analyze a resume first."

    file_path = "reports/resume_report.pdf"

    generate_pdf(
        file_path,
        data["final_score"],
        data["resume_skills"],
        data["matched_skills"],
        data["missing_skills"],
        data["status"],
        data["email"]
    )

    return send_file(
        file_path,
        as_attachment=True
    )


if __name__ == "__main__":

    app.run(debug=True)