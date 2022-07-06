#!/usr/bin/env python3

# Python 3.9.5

# split_pdf_document_into_separate_pages.py

# Dependencies
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

p = 'C:\\Users\\...\\your_directory' # Change working directory
os.chdir(p)

pdf_file = 'filename.pdf'

input_PDF = PdfFileReader(open(pdf_file, 'rb'))

pages = range(input_PDF.numPages)

for page in pages:
    output = PdfFileWriter()
    output.addPage(input_PDF.getPage(page))
    with open("Document_page_%s.pdf" % page + 1, 'wb') as output_pdf:
        output.write(output_pdf)
