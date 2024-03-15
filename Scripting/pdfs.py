import PyPDF2

# pdf are also binary, so use rb for reading
with open('./pdfs/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    # len(file.pages) --> gives number of pages in this PDF
    print(len(reader.pages))
    # get the first page in this case --> can be indexed based on pages
    print(reader.pages[0])
    # we can rotate a page 
    print(reader.pages[0].rotate(90))