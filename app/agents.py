import os
from jinja2 import Template

try:
    import openai
except Exception:
    openai = None

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def _offline_resume(resume_text, job_desc, keywords):
    header = "=== Optimized Resume (Offline Mode) ===\n"
    kline = "Targeted Keywords: " + ", ".join(keywords[:15]) + "\n\n"
    tips = (
        "- Add metrics to bullets (e.g., +23% perf, -120ms latency).\n"
        "- Mirror 5–8 keywords from the JD near the top summary.\n"
        "- Keep bullets action verbs (Built, Designed, Deployed).\n\n"
    )
    return header + kline + tips + resume_text

def optimize_resume(resume_text, job_desc, keywords):
   
    if not (OPENAI_API_KEY and openai):
        return _offline_resume(resume_text, job_desc, keywords)

    try:
        openai.api_key = OPENAI_API_KEY
        prompt = f"""
You are an ATS resume optimization assistant.
Rewrite the resume bullets to align with this job description and the target keywords.
Keep structure and truthfulness; add plausible metrics. Return plain text only.

JOB DESCRIPTION:
{job_desc}

TARGET KEYWORDS:
{", ".join(keywords)}

RESUME (ORIGINAL):
{resume_text}
"""
        
        resp = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.3,
            max_tokens=1200,
        )
        return resp.choices[0].text.strip()
    except Exception:
        return _offline_resume(resume_text, job_desc, keywords)

def generate_cover_letter(name, job_desc, keywords):
    template = Template("""
Dear Hiring Manager,

I’m excited to apply for this role. Based on the job description, I bring hands-on experience with {{ keywords[:10]|join(', ') }},
and I’ve shipped projects where I drove measurable outcomes (quality, performance, or cost).

Highlights:
- Matched to JD focus areas using: {{ keywords[:6]|join(', ') }}.
- Strong ownership from problem definition through delivery and iteration.
- Clear communication, documentation, and bias to action.

I would love to contribute to your team and learn more about the role.

Best regards,
{{ name }}
""")
    return template.render(name=name, keywords=keywords)
