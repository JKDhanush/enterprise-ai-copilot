from pypdf import PdfReader
from docx import Document


def load_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def load_docx(file_path):

    doc = Document(file_path)

    text = "\n".join(
        para.text for para in doc.paragraphs
    )

    return text