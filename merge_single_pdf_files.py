#!/usr/bin/env python3

# Python 3.9.5

# merge_single_pdf_files.py

import os
from PyPDF2 import PdfMerger

# Merge single-page PDF files to a multi-page PDF document.

p = 'C:\\Users\\...\\PDFs'
os.chdir(p)

pdf_merger = PdfMerger()
pdf_result = "merged_file.pdf"

for file in os.listdir(p):
    if file.endswith(".pdf"):
        pdf_merger.append(file)

pdf_merger.write(pdf_result)
pdf_merger.close()
