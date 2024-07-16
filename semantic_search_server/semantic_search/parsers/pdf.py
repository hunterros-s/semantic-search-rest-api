import semantic_search
from pypdf import PdfReader

from semantic_search.utils import chunk

# should probably do OCR at some point. this is pretty poor at most pdfs.

def process_pdf(path):
    reader = PdfReader(path)

    content = []

    for page in reader.pages:
        content.append(page.extract_text())
    
    text = " ".join(content)

    chunks = chunk(text)

    return chunks