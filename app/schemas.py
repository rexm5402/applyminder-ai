from pydantic import BaseModel
from typing import List

class OptimizeRequest(BaseModel):
    job_description: str
    name: str
    email: str
    phone: str
    linkedin: str
    github: str

class OptimizeResponse(BaseModel):
    optimized_resume: str
    cover_letter: str
    keywords: List[str]
