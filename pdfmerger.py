import os
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

for pdf in os.listdir(os.dir):
    if pdf.endswith(".pdf"):
        merger.append(pdf)

merger.write("merger_pdf.pdf")
merger.close()
