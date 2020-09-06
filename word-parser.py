from PyPDF2 import PdfFileReader
import easygui as eg
import pandas as pd
pdf_path = eg.fileopenbox(msg = 'Khatnaa', multiple=True)

import PyPDF2 as p2
def khatnas_dict(pdf_path):
   with open(pdf_path, "rb") as pdf:
       pdfread = p2.PdfFileReader(pdf)
       pageObj = pdfread.getPage(0)
       texts = pageObj.extractText()
       return texts
   
unwantedwords = ['/',':','Mongolia','˘']
lst = list()
for path in pdf_path:
    dictionary = khatnas_dict(path)
    for word in dictionary.split():
        if word not in unwantedwords:
            lst.append(word)
            
    
df = pd.DataFrame(lst)
df.to_csv(r'C:\Users\KhatantuulB\Desktop\Python project\dictionary\output\parsedwords.csv')
