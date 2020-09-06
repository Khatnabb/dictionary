from PyPDF2 import PdfFileReader


pdf_path = r"C:\Users\Erkhembayare\Desktop\Dictionary\input\pdf.pdf"


import PyPDF2 as p2
def khatnas_dict(pdf_path):
   with open(pdf_path, "rb") as pdf:
       pdfread = p2.PdfFileReader(pdf)
       pageObj = pdfread.getPage(0)
       texts = pageObj.extractText()
       # x = pdfread.getFields()
       # t = pdfread.getDocumentInfo()
       # texts = pdfread.extractText()
       
       return texts
   
   
dictionary = khatnas_dict(pdf_path)

lists = list()
for word in dictionary:
    lists.append(word)
   
   
lists = dictionary.split()
lists1 = list()
for word in lists:
    if not word == 'Mongolia':
        lists1.append(word)
