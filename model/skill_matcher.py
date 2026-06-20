def matched_skill(resume_skills,jd_skills):
    matched_skills = []

    for skill in jd_skills:
        if skill in resume_skills:
            matched_skills.append(skill)

    return matched_skills