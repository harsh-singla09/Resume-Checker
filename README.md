# AI Resume Checker 🚀

An AI-powered Resume Analysis System that compares a candidate's resume with a job description and provides an ATS-style compatibility score.

The application extracts resume information, analyzes skills, compares them with job requirements, identifies missing skills, and generates a detailed PDF analysis report.

---

## Features ✨

### Resume Processing

* Upload Resume in PDF/DOCX format
* Extract text from resumes
* Clean and preprocess resume content

### AI/NLP Analysis

* Skill extraction from resume and job description
* Skill synonym matching
* Fuzzy skill matching
* TF-IDF based text similarity analysis

### Resume Evaluation

* Resume skill detection
* Job description skill detection
* Matched skills identification
* Missing skills identification
* ATS-style final score calculation
* Resume match status

### Report Generation

* Professional result dashboard
* Downloadable PDF report
* Candidate details included
* Analysis date included

---

## Project Workflow

```
Resume Upload
       |
       ↓
Text Extraction
       |
       ↓
Text Cleaning
       |
       ↓
Skill Extraction
       |
       ↓
Job Description Matching
       |
       ↓
Similarity Analysis
       |
       ↓
Final Resume Score
       |
       ↓
PDF Report Generation
```

---

## Tech Stack 🛠️

### Backend

* Python
* Flask

### NLP / Machine Learning

* Scikit-learn
* TF-IDF Vectorization
* RapidFuzz

### Document Processing

* PyMuPDF
* python-docx

### Report Generation

* ReportLab

### Frontend

* HTML
* Bootstrap
* Jinja2 Templates

---

## Project Structure

```
AI-Resume-Checker

│
├── app.py                  # Flask application
│
├── model/
│   ├── similarity.py       # Resume similarity calculation
│   └── skill_matcher.py    # Skill matching logic
│
├── utils/
│   ├── extractor.py        # PDF/DOCX extraction
│   ├── text_cleaner.py     # Text preprocessing
│   ├── skill_extractor.py  # Skill extraction
│   └── pdf_report.py       # PDF generation
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── uploads/                # Uploaded resumes
│
├── reports/                # Generated reports
│
└── README.md
```

---

## Installation ⚙️

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Move into the project folder:

```bash
cd AI-Resume-Checker
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

Start Flask server:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## How It Works

1. User uploads a resume.
2. Resume text is extracted from PDF/DOCX.
3. Text is cleaned and processed.
4. Skills are detected using NLP techniques.
5. Job description skills are extracted.
6. Resume and job description are compared.
7. A final compatibility score is generated.
8. User can download a PDF analysis report.

---

## Example Output

The system provides:

```
Final Score: 82%

Status:
Good Match

Matched Skills:
✓ Python
✓ Flask
✓ SQL

Missing Skills:
✗ Machine Learning
✗ Docker
```

---

## Future Improvements

* User authentication
* Database storage
* Resume history dashboard
* Advanced NLP models
* AI-based resume suggestions
* Cloud deployment

---

## Author

HARSH SINGLA

GitHub:
(https://github.com/harsh-singla09)

LinkedIn:
(https://www.linkedin.com/in/harsh-singla-ai/)



