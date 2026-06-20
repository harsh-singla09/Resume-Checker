from rapidfuzz import fuzz

SKILL_CATEGORIES = {

    "Programming Languages": [
        "python",
        "java",
        "c++",
        "javascript",
        "c"
    ],


    "Web Development": [
        "html",
        "css",
        "flask",
        "django",
        "react"
    ],


    "Databases": [
        "sql",
        "mysql",
        "postgresql",
        "mongodb"
    ],


    "Data Science": [
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn"
    ],


    "Machine Learning": [
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "scikit-learn"
    ],


    "Tools": [
        "git",
        "github",
        "docker",
        "linux"
    ]

}


def extract_skills(text):

    text = text.lower()

    found_skills = []


    for category, skills in SKILL_CATEGORIES.items():

        for skill in skills:

            if skill in text or fuzzy_skill_match(text, skill):

                found_skills.append(skill)


    return list(set(found_skills))

def fuzzy_skill_match(text, skill, threshold=85):

    words = text.split()


    for word in words:

        score = fuzz.ratio(
            word,
            skill
        )

        if score >= threshold:
            return True


    return False

def extract_skill_categories(text):

    text = text.lower()

    found_categories = {}


    for category, skills in SKILL_CATEGORIES.items():

        matched = []


        for skill in skills:

            if skill in text:
                matched.append(skill)


        if matched:
            found_categories[category] = matched


    return found_categories


def missing_skill(resume_skills, jd_skills):

    missing_skills = []

    for skill in jd_skills:

        if skill not in resume_skills:
            missing_skills.append(skill)

    return missing_skills





