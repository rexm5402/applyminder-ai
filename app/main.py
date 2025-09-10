from fastapi import FastAPI, UploadFile, Form
from app.schemas import OptimizeResponse
from app.utils import extract_text_from_pdf, extract_keywords
from app.agents import optimize_resume, generate_cover_letter
import os, json

api = FastAPI(title="ApplyMinder AI")

@api.post("/optimize", response_model=OptimizeResponse)
async def optimize(
    resume: UploadFile,
    job_description: str = Form(...),
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    linkedin: str = Form(...),
    github: str = Form(...)
):
    os.makedirs("uploads", exist_ok=True)
    resume_path = f"uploads/{resume.filename}"
    with open(resume_path, "wb") as f:
        f.write(await resume.read())

    
    resume_text = extract_text_from_pdf(resume_path)
    keywords = extract_keywords(job_description)

   
    optimized_resume = optimize_resume(resume_text, job_description, keywords)
    cover_letter = generate_cover_letter(name, job_description, keywords)

    
    os.makedirs("outputs", exist_ok=True)
    resume_file = "outputs/optimized_resume.txt"
    cover_file = "outputs/cover_letter.txt"
    json_file = "outputs/keywords.json"

    with open(resume_file, "w") as f: f.write(optimized_resume)
    with open(cover_file, "w") as f: f.write(cover_letter)
    with open(json_file, "w") as f: json.dump(keywords, f, indent=2)

    return OptimizeResponse(
        optimized_resume=resume_file,
        cover_letter=cover_file,
        keywords=keywords
    )
