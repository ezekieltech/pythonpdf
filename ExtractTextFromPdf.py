import PyPDF2

pdfFileObj = open('test2.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
t = pdfReader.numPages #to see the number of pages
print(t)
pageObj = pdfReader.getPage(0)
text = pageObj.extractText().encode('utf-8')
print(text)
