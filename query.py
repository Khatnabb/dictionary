import pyodbc
import pandas as pd

def sql_link(query, server='localhost\SQLEXPRESS', database='words',index_col=None, driver='{SQL SERVER}'):
    
    driver = "{SQL SERVER}"
    server = "localhost\SQLEXPRESS"
    database = "otdict"

    conn_str = 'DRIVER=%s;SERVER=%s;DATABASE=%s;Trusted_Connection=yes' % (driver, server, database)

    conn = pyodbc.connect(conn_str)
    df = pd.read_sql(query, conn, index_col)
    conn.close()
    return df

def get_searched_word(searchinput):

    q = """SELECT Def

    FROM [otdict].[dbo].[otdictionary]

    WHERE Term = '%s' """ % searchinput
    df = sql_link(q)

    return df['Def'][0]


def auto_complete(span):
    q = """SELECT Term, Def

    FROM [otdict].[dbo].[otdictionary]

    WHERE Term LIKE '{}%' """.format(span)  
    df = sql_link(q)
    
    return list(df['Term'])

def save_to_main(idx):
    q = """                  INSERT INTO otdictionary(Term, Def)
                             SELECT Term, Def FROM [otdict].[dbo].[newEntries]
                             WHERE ID = {};
                             DELETE FROM [otdict].[dbo].[newEntries]
                             WHERE ID = {}; """.format(idx,idx)
    df = sql_link(q)
    return df
    

# def Royischeckingtheword(word):
#     import re

#     regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

#     if(regex.search(word) == None):
#         return word
#     else:
#         return word