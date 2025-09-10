import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_keywords(job_desc: str, top_n=15):
    words = re.findall(r"\b[a-zA-Z]{4,}\b", job_desc)
    freq = {}
    for w in words:
        w_lower = w.lower()
        freq[w_lower] = freq.get(w_lower, 0) + 1
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w, _ in sorted_words[:top_n]]
