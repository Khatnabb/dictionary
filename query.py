import pyodbc
import pandas as pd

conx_string = "driver={SQL SERVER}; server=localhost\SQLEXPRESS; database=otdict; trusted_connection=YES;"

with pyodbc.connect(conx_string) as conx:
    cursor = conx.cursor()

def sql_link(query, server='localhost\SQLEXPRESS',database='words',index_col=None, driver='{SQL SERVER}'):
    
    driver = "{SQL SERVER}"
    server = "localhost\SQLEXPRESS"
    database = "otdict"

    conn_str = 'DRIVER=%s;SERVER=%s;DATABASE=%s;Trusted_Connection=yes' % (driver, server, database)

    conn = pyodbc.connect(conn_str)
    df = pd.read_sql(query, conn, index_col)
    conn.close()
    return df

def get_searched_word_en(searchinput):

    q = """SELECT Term, Term_definition, Term_description, Field

    FROM [otdict].[dbo].[otdictionary]

    WHERE Term = '{}' """.format(searchinput)
    
    df = sql_link(q)
    df = {'Term': df['Term'][0],
          'Definition': df['Term_definition'][0], 
          'Description': df['Term_description'][0],
          'Field': df['Field'][0]}
    return df
    

def get_searched_word_mn(searchinput):

    q = """SELECT Term, Term_definition, Term_description, Field

    FROM [otdict].[dbo].[otdictionary]

    WHERE Term_definition LIKE N'%{}%' """.format(searchinput)
          
    df = sql_link(q)
    df = {'Term': df['Term'][0],
          'Definition': df['Term_definition'][0], 
          'Description': df['Term_description'][0],
          'Field': df['Field'][0]}
    return df

def auto_complete_en(span):
    q = """SELECT Term, Term_definition

    FROM [otdict].[dbo].[otdictionary]

    WHERE Term LIKE '{}%' """.format(span)  
    df = sql_link(q)
    
    return list(df['Term'])
 

def auto_complete_mn(span):
    q = """SELECT Term_definition

    FROM [otdict].[dbo].[otdictionary]

    WHERE Term_definition LIKE N'%{}%' """.format(span)
    df = sql_link(q)

    return list(df['Term_definition'])

def check_for_duplicates(searchinput):
    q= """SELECT COUNT(*) as count 
    FROM [otdict].[dbo].[search_not_found] 
    WHERE Term_not_found = '{}' """.format(searchinput)
    df = sql_link(q)

    return df['count'][0]
