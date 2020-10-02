import pyodbc
import pandas as pd
# conx_string = "driver={SQL SERVER}; server=localhost\SQLEXPRESS; database=words; trusted_connection=YES;"

# query = "SELECT TOP 20 Term FROM dict"

# with pyodbc.connect(conx_string) as conx:
#     cursor = conx.cursor()
#     cursor.execute(query)
#     data = cursor.fetchall()

def sql_link(query, server='localhost\SQLEXPRESS', database='words',index_col=None, driver='{SQL SERVER}'):
    
    driver = "{SQL SERVER}"
    server = "localhost\SQLEXPRESS"
    database = "words"

    conn_str = 'DRIVER=%s;SERVER=%s;DATABASE=%s;Trusted_Connection=yes' % (driver, server, database)

    conn = pyodbc.connect(conn_str)
    df = pd.read_sql(query, conn, index_col)
    conn.close()
    return df

def get_searched_word(searchinput):

    q = """SELECT [Term],[Def],[Rel]

    FROM [words].[dbo].[dict]

    WHERE Term = '%s' """ % searchinput
    df = sql_link(q)
    return df['Def'][0]


