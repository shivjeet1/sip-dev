from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document

def save_as_txt(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

def save_as_pdf(text, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    c.drawString(100, 750, text)
    c.save()

def save_as_docx(text, output_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)

def save_text(text, output_path, file_type):
    if file_type == 'txt':
        save_as_txt(text, output_path)
    elif file_type == 'pdf':
        save_as_pdf(text, output_path)
    elif file_type == 'docx' or file_type == 'doc':
        save_as_docx(text, output_path)

