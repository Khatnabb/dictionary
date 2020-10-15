from flask import Flask, render_template, request, jsonify, redirect, url_for
from query import *
import json, pyodbc

app = Flask(__name__)

conx_string = "driver={SQL SERVER}; server=localhost\SQLEXPRESS; database=otdict; trusted_connection=YES;"

with pyodbc.connect(conx_string) as conx:
    cursor = conx.cursor()
    

@app.route('/home')
def home():
    return render_template('dict.html')

@app.route('/contribute')
def contribute():
    return render_template('contribute.html')

@app.route('/proofread/', methods = ['POST', 'GET'])
def proofread():

    cursor.execute("SELECT * FROM newEntries")
    data = cursor.fetchall()

    return render_template('proofread.html', newEntries = data)

# @app.route('/proofread/<string:idx>', methods = ['POST', 'GET'])
# def update(idx):
#     if request.method == "GET":

#         cursor.execute("SELECT * FROM newEntries WHERE ID = ?", idx)
#         edit_data = cursor.fetchall()
        
#         return render_template('proofread.html', newEntries = edit_data)

#     if request.method == "POST":

#         newterm = request.form['newterm']
#         newdef = request.form['newdef']
        
#         cursor.execute("""  INSERT INTO otdictionary(Term, Def)
#                             SELECT Term, Def FROM [otdict].[dbo].[newEntries]

#                             WHERE Term = '{}';

#                             DELETE FROM [otdict].[dbo].[newEntries]

#                             WHERE Term = '{}';""", (newterm))
#         cursor.commit()

@app.route('/addNew', methods=['POST','GET'])
def addNew():

    if request.method == "POST":
        
        postingterm = request.form['postingterm']
        postingdef = request.form['postingdef']

        cursor.execute("INSERT INTO newEntries (Term, Def) VALUES (?,?)", (postingterm, postingdef))
        cursor.commit()
        return redirect(url_for('contribute'))

@app.route('/home/<searchinput>')
def api_search(searchinput):
    
    import re
    from query import get_searched_word

    regex = re.compile('[@_!#$%^&*<>?\|}{~:.;:,!-=]')
    if (regex.search(searchinput) == None):
        
        try:
            words = get_searched_word(searchinput=searchinput)
            return json.dumps({'words': words})
        except IndexError:
            return {'response': 'The word you searched is not found'}, 400
        
    else:
        return {'response': 'The word cannot contain special characters in it'}, 400

@app.route('/home/autocomplete/<searchinput>')
def api_autocomplete(searchinput):
    
    import re
    from query import auto_complete

    regex = re.compile('[@_!#$%^&*<>?\|}{~:.;:,!-=]')
    if (regex.search(searchinput) == None):
        
        try:
            words = auto_complete(span=searchinput)
            return json.dumps({'words': words})
        except IndexError:
            return {'response': 'The word you searched is not found'}, 400
        
    else:
        return {'response': 'The word cannot contain special characters in it'}, 400

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':

        idx = request.form['id']
        term = request.form['term']
        definition = request.form['definition']
        cursor.execute("UPDATE newEntries SET Term = ?, Def = ?  WHERE ID = ?", term, definition, idx)
        cursor.commit()
        return redirect(url_for('proofread'))


@app.route('/save/<string:idx>', methods=['GET', 'POST'])
def save():
    if request.method == 'POST':

        idx = request.form['id']
        term = request.form['term']
        definition = request.form['definition']
        
        cursor.execute("""    INSERT INTO otdictionary(Term, Def)
#                             SELECT Term, Def FROM [otdict].[dbo].[newEntries]

#                             WHERE Term = '{}';

#                             DELETE FROM [otdict].[dbo].[newEntries]

#                             WHERE Term = '{}';""", (term))
        cursor.commit()


if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/home/<searchinput>')
# def api_search(searchinput):

#     from query import get_searched_word, Royischeckingtheword

#     words = get_searched_word(searchinput=searchinput)
 
#     return  json.dumps({ 'words': words})

# if __name__ == "__main__":
#     app.run(debug=True)