import pymupdf
from docx import Document


# ----------------------------
# PDF Text Extraction
# ----------------------------

def pdf_text_extraction(file_path):

    # Open PDF file
    doc = pymupdf.open(file_path)

    text = ""

    # Extract text from every page
    for page in doc:
        text += page.get_text("text", sort=True)

    # Close PDF
    doc.close()

    return text


# ----------------------------
# DOCX Text Extraction
# ----------------------------

def docx_extract_text(file_path):

    # Open DOCX file
    doc = Document(file_path)

    text_content = []

    # Extract every paragraph
    for para in doc.paragraphs:
        text_content.append(para.text)

    # Convert list into single string
    return "\n".join(text_content)


# ----------------------------
# Test Code
# ----------------------------

if __name__ == "__main__":

    # Test PDF
    pdf_text = pdf_text_extraction("sample.pdf")

    print("--------- PDF TEXT ---------")
    print(pdf_text)


    # Test DOCX
    docx_text = docx_extract_text("your_file.docx")

    print("\n--------- DOCX TEXT ---------")
    print(docx_text)