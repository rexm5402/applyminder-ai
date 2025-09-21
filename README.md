# ApplyMinder AI — Agentic Resume Optimizer

ApplyMinder AI is a lightweight tool that helps job seekers improve their chances of getting noticed by recruiters. It reads a resume and a job description, extracts important ATS-relevant keywords, and produces an optimized resume and a tailored cover letter. The project was designed to be simple to run locally while still offering an option to use OpenAI for deeper personalization.

---

## Why This Project?

Most companies use Applicant Tracking Systems (ATS) to filter resumes before a human recruiter ever sees them. Many strong candidates are rejected because their resumes do not match the keywords listed in the job description.  
ApplyMinder AI was built to solve this problem: **aligning resumes with job requirements automatically** while saving time during the job application process.

---

## Features

- **Resume Parsing** — Extracts text from PDF resumes using `pdfplumber`.
- **Keyword Extraction** — Identifies the most relevant skills and phrases from a job description.
- **Resume Optimization** — Generates a new, tailored resume that highlights the right keywords.
- **Cover Letter Generation** — Creates a draft cover letter aligned with the job role.
- **Dual Modes**  
  - *Offline Mode:* Local keyword-driven optimization (no API key required).  
  - *Online Mode:* Optional OpenAI integration for more personalized content.  
- **Outputs** — Stores the optimized resume, cover letter, and keyword list in the `outputs/` folder.

---

## Tech Stack

- **Python 3.11**
- **FastAPI** — for the backend API
- **pdfplumber** — PDF text extraction
- **Jinja2** — template rendering
- **Uvicorn** — ASGI server
- **OpenAI API (optional)** — for advanced personalization

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/rexm5402/applyminder-ai.git
cd applyminder-ai

2. Set Up Virtual Environment
python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
.venv\Scripts\activate      # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Add Your Resume
samples/resume.pdf

5. Run the App
python -m uvicorn app.main:api --reload

