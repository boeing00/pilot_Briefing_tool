import io
from pypdf import PageObject, PdfWriter

def create_sample_aviation_pdf():
    # A standard simple PDF generator
    writer = PdfWriter()
    page = PageObject.create_blank_page(width=612, height=792)
    writer.add_page(page)
    
    # We can also write standard text to a PDF or generate sample text
    # Let's save a text-based sample file as well
    print("Sample PDF generator ready")

if __name__ == "__main__":
    create_sample_aviation_pdf()
