import PyPDF2 
import sys 

inputs = sys.argv[1:]

def merge_pdf(pdf_list):
    # creating a merger object to append all pdfs together
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    # write out a single combined pdf
    merger.write('merged.pdf')

merge_pdf(inputs)