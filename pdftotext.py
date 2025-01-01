import pdfplumber

def pdf_to_text(pdf_file, output_file):
    text = ''
    # Open the PDF file
    with pdfplumber.open(pdf_file) as pdf:
        # Iterate through each page
        for page in pdf.pages:
            text += page.extract_text() + '\n'

    # Save extracted text to a file
    with open(output_file, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

# Usage
pdf_to_text('output.pdf', 'output.txt')
