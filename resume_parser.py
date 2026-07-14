import fitz  # PyMuPDF

def extract_resume_text(pdf_path):
    """
    Extract all text from a PDF resume.
    """
    text = ""
    try:
        document = fitz.open(pdf_path)
        for page in document:
            text += page.get_text()
        document.close()
        return text
    except Exception as e:
        print("Error reading resume:", e)
        return ""