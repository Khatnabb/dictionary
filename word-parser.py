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
   
unwantedwords = ['/',':','Mongolia','˘','20','28','$','(SI)','ˇ','˙','ˆ˘','˝ˆ','˛','˚˙˜','!',',',
                 '"#','%&!','-','(','˚˜˙˜',')','2019','2018','3-','*','+ˆ','Œ','the','and','to','2020',
                 'it','for','not','a','an','OT','at','of','Oyu','Tolgoi','June','July','August','September',
                 'October','November','December','have','has','had','was','his','ON','in','The','&','To','be',
                 'on','+976','or','as','with','no','FOR','from','is','less','A','s','within','72','64','70','days',
                 '13','4.','.','her','IP','"','-ˇ','1','4','30','Jeff','3','','3%2(˝%%(','dimitrios.kastis@riotinto.com',
                 '˝','*ˇ','!ˇ˜','ˆ','ˇ˙','him','by','are','29','12','how','did','happen','?','(IP)','2',')-%0','ˇ˘','˙˙','#','Title:','ﬁ',
    'ﬂ','˜˜','"˘','˝ˇ','·',').','3ˆ','%4','˙ˇ','%˙˘','4˘','˝ˆ˘ˆˆ','5˚%%$','Type:','Group:','Orange','Date:','As','up',
    'It','Action:','cm','2.37','Then,','One','PM','01:00','At','about','#1.','#22','happen?:','What','happened','5163','9902',
    '˛˘','˙˝','!ˇ˜˘','-˘','˚˜˜','ˆˆ˘ˇˇˆ','(6','"70','"˝3','(%˚$%2','Time:','-552','$%726886˝%','11','USA','10:45','Country','Contact','97%',
    '500','(7,660','lbs)','(98%)','lbs.','Date/Time:','Unit:','Contact:','Chris','Aitchison','9908','6034','happened:','While','that','were',
    'factors:','but','this','learnings:','On','14:30','12th','500m','120mm','#6','#8.','There','all','old','Admin','2018,','hours','No','CAT',
    'NOTICE','13:30pm,','0mm','9/15/2018','Saturday,','99902762','Andrew','Curtis','N/A','40m',';','#1','Date','/Time','˛#˛˛˛',
    'ext','6169','1880','9','0','5','509','when','Day','Business','UB','must','Time','All','minutes','#2','happened,','why','May','02nd','am,',
    'made','approx.','4m','where','May,','Engineer','Senior','before','night','day','shift','th','two','been','07:30','D01.','Country:','Steve','Price',
    'used','most','being','March,','time','last','banner:','21:00','group:','Tumurkhuyag,','Tuvshinbayar','976+','between','Notification','information','Wednesday,','notification',
    'closed.','opened.','Two','opened','open.','one','person:','Tsend','Risk:','initial','Initial']
lst = list()
for path in pdf_path:
    dictionary = khatnas_dict(path)
    for word in dictionary.split():
        if word not in unwantedwords:
            lst.append(word)
            
    
df = pd.DataFrame(lst)
df.to_csv(r'C:\Users\KhatantuulB\Desktop\Python project\dictionary\output\parsedwords.csv')
