from PyPDF2 import PdfFileMerger
import os
from os import walk

print(os.path.abspath(os.getcwd()))
pdfs = []
for (dirpath, dirnames, filenames) in walk(os.path.abspath(os.getcwd())):
    for file in filenames:
        if(file.endswith(".pdf")):
            print(file)
            pdfs.append(file)
    break

print(pdfs)

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
