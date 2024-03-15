import PyPDF2 
import sys 

# first argument is the watermark pdf that we have
water_mark_pdf = sys.argv[1]
# second and further arguments are stored in a list here
remaining_pdf = sys.argv[2:]

# create a PDFWriter object to write watermarked pages
output = PyPDF2.PdfWriter()

# this program takes in a number of pdf files, watermarks each page in each pdf, and outputs one single pdf merging all files
def watermark(water_mark_pdf, pdf_list):
    # reader object to access pages of watermark. Once the reader object is created, any page can be accessed. 
    reader_watermark = PyPDF2.PdfReader(water_mark_pdf)
    # looping through all pdfs sent 
    for pdf in pdf_list:
        # create a reader object for each pdf to access pages of each pdf
        pdf_reader = PyPDF2.PdfReader(pdf)
        # go through each page one by one in pdf
        for i in range(len(pdf_reader.pages)):
            # get the page one by one
            page = pdf_reader.pages[i]
            # merge with watermark page
            page.merge_page(reader_watermark.pages[0])
            # add it to the output object
            output.add_page(page)
    # finally, write out the merged and watermarked pdf
    with open('watermarked.pdf', 'wb') as file:
        output.write(file)

watermark(water_mark_pdf, remaining_pdf)