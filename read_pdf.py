import Quartz
import sys

def extract_text_from_pdf(pdf_path):
    pdf_url = Quartz.NSURL.fileURLWithPath_(pdf_path)
    pdf_doc = Quartz.PDFDocument.alloc().initWithURL_(pdf_url)
    if not pdf_doc:
        print(f"Could not load PDF: {pdf_path}")
        return
    
    text = ""
    for i in range(pdf_doc.pageCount()):
        page = pdf_doc.pageAtIndex_(i)
        page_text = page.string()
        if page_text:
            text += page_text + "\n"
    return text

print(extract_text_from_pdf("final .pdf"))
