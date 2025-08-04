import pdfplumber
from docx import Document
import os

#from pathlib import Path
"""
def load_file(file_path): 
    if file_path.endswith(".txt"):
        return Path(file_path).read_text(encoding="utf-8")
    raise ValueError("TXT file is required!")

"""

def load_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_pdf_file(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def load_docx_file(path: str) -> str:
    doc = Document(path)
    text = []
    for para in doc.paragraphs:
        clean_para = para.text.strip()
        if clean_para:
            text.append(clean_para)

    return "\n".join(text)



def load_document(path: str) -> str:
    ext = os.path.splitext(path)[-1].lower()
    if ext == ".txt":
        return load_text_file(path)
    elif ext == ".pdf":
        return load_pdf_file(path)
    elif ext == ".docx":
        return load_docx_file(path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")