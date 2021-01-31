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

    FROM  [otdictionary]

    WHERE Term = '{}' """.format(searchinput)
    
    df = sql_link(q)
    df = {'Term': list(df['Term']),
          'Definition': list(df['Term_definition']), 
          'Description': list(df['Term_description']),
          'Field': list(df['Field'])}
    return df

def capture_not_found(word):

    count = check_for_duplicates(word)

    if count == 0:
        cursor.execute("INSERT INTO search_not_found (Term_not_found, Search_frequency) VALUES (?,1)", word)
    else:
        cursor.execute("UPDATE  [search_not_found] SET Search_frequency = Search_frequency + 1 WHERE Term_not_found=(?)", word)
    cursor.commit()

def contribute_word(data):
    # print(data)
    cursor.execute("INSERT INTO added_terms (Term_added, Definition_added, Description_added, Field, OT_email) VALUES (?,?,?,?,?)", (data['new-term'],data['new-definition'], data['new-description'], data['field-option'], data['email']))
    cursor.commit()

def contribute_word_proofread(data):

    cursor.execute("INSERT INTO otdictionary (Term, Term_definition, Term_description, Field) VALUES (?,?,?,?)", (data['term'], data['definition'], data['description'], data['field-options']))
    cursor.commit()

def update_contributed_word(data):
        
    cursor.execute("UPDATE added_terms SET Term_added = ?, Definition_added = ?, Description_added =?, Field =? WHERE ID = ?", (data['term'], data['definition'], data['description'], data['field'], data['id']))
    cursor.commit()

def modify_contributed_word(idx,mode):
    if mode == "save":
        cursor.execute("INSERT INTO otdictionary(Term, Term_definition, Term_description, Field) SELECT Term_added, Definition_added, Description_added, Field FROM  [added_terms] WHERE ID = {}; DELETE FROM  [added_terms]  WHERE ID = {};".format(idx,idx))
    elif mode == "delete":
        cursor.execute("DELETE FROM  [added_terms]  WHERE ID = ?", idx)
    cursor.commit()
def get_tables():

    cursor.execute("SELECT * FROM added_terms")
    data = cursor.fetchall()

    cursor.execute("SELECT * FROM search_not_found ORDER BY Search_frequency DESC")
    search_freq = cursor.fetchall()

    return data, search_freq

def get_searched_word_mn(searchinput):

    q = """SELECT Term, Term_definition, Term_description, Field

    FROM  [otdictionary]

    WHERE Term_definition LIKE N'%{}%' """.format(searchinput)
          
    df = sql_link(q)
    df = {'Term': list(df['Term']),
          'Definition': list(df['Term_definition']), 
          'Description': list(df['Term_description']),
          'Field': list(df['Field'])}
    return df

def auto_complete_en(span):
    q = """SELECT Term, Term_definition

    FROM  [otdictionary]

    WHERE Term LIKE '{}%' """.format(span)  
    df = sql_link(q)
    
    return list(df['Term'])
 

def auto_complete_mn(span):
    q = """SELECT Term_definition

    FROM  [otdictionary]

    WHERE Term_definition LIKE N'%{}%' """.format(span)
    df = sql_link(q)

    return list(df['Term_definition'])

def check_for_duplicates(searchinput):
    q= """SELECT COUNT(*) as count 
    FROM  [search_not_found] 
    WHERE Term_not_found = '{}' """.format(searchinput)
    df = sql_link(q)

    return df['count'][0]

def get_sub_emails():
    q = """SELECT Email 
           FROM subscribed_emails"""
    df = sql_link(q)

    return list(df['Email'])