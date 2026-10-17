from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

if __name__ == "__main__":
    pdf_path = "1947.pdf"   # change this to your PDF name
    text = extract_text_from_pdf(pdf_path)

    print("PDF loaded successfully.")
    print("Number of characters extracted:", len(text))
    print("\nFirst 500 characters:\n")
    print(text[:500])