import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    
    return text

def simple_clean_text(text):
    text = re.sub(r'\n{2,}', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = '\n'.join([line.strip() for line in text.splitlines() if line.strip()])
    return text

def process_pdf(pdf_path, output_file):
    raw_text = extract_text_from_pdf(pdf_path)
    cleaned_text = simple_clean_text(raw_text)

    with open(output_file, 'w') as f:
        f.write(cleaned_text)
    
    print(f"Cleaned text extracted and saved to {output_file}")

pdf_path = "html.pdf"
output_file = "html.txt"
process_pdf(pdf_path, output_file)