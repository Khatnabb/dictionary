from flask import Flask, render_template, request, jsonify, redirect, url_for
from query import *
import json, pyodbc
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

conx_string = "driver={SQL SERVER}; server=localhost\SQLEXPRESS; database=otdict; trusted_connection=YES;"

with pyodbc.connect(conx_string) as conx:
    cursor = conx.cursor()

auth = HTTPBasicAuth()

users = {
    "Erkhbayarb": generate_password_hash("Erkhbayarb123$"),
    "Erkhembayare": generate_password_hash("Erkhembayare123$"),
    "Khatantuul": generate_password_hash("Erkhembayare123$")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/home')
def home():
    return render_template('dict.html')

@app.route('/contribute')
def contribute():
    return render_template('contribute.html')

@app.route('/proofread/', methods = ['POST', 'GET'])
@auth.login_required
def proofread():

    cursor.execute("SELECT * FROM newEntries")
    data = cursor.fetchall()

    return render_template('proofread.html', newEntries = data)

@app.route('/addNew', methods=['POST','GET'])
def addNew():

    if request.method == "POST":
        
        postingterm = request.form['postingterm']
        postingdef = request.form['postingdef']

        cursor.execute("INSERT INTO newEntries (Term, Def) VALUES (?,?)", (postingterm, postingdef))
        cursor.commit()
        return redirect(url_for('contribute'))

@app.route('/addNewProofread', methods=['POST','GET'])
def addNewProofread():

    if request.method == "POST":
        
        term = request.form['term']
        definition = request.form['definition']

        cursor.execute("INSERT INTO otdictionary (Term, Def) VALUES (?,?)", (term, definition))
        cursor.commit()
        return redirect(url_for('proofread'))

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


@app.route('/save/<idx>', methods=['GET', 'POST'])
def save(idx):
    if request.method == 'POST':

        cursor.execute("INSERT INTO otdictionary(Term, Def) SELECT Term, Def FROM [otdict].[dbo].[newEntries] WHERE ID = {}; DELETE FROM [otdict].[dbo].[newEntries]  WHERE ID = {};".format(idx,idx))
        cursor.commit()
        
    return redirect(url_for('proofread'))

@app.route('/delete/<idx>', methods=['GET', 'POST'])
def delete(idx):
    if request.method == 'POST':

        cursor.execute("DELETE FROM [otdict].[dbo].[newEntries]  WHERE ID = ?", idx)
        cursor.commit()
        
    return redirect(url_for('proofread'))

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/home/<searchinput>')
# def api_search(searchinput):

#     from query import get_searched_word, Royischeckingtheword

#     words = get_searched_word(searchinput=searchinput)
 
#     return  json.dumps({ 'words': words})

# if __name__ == "__main__":
#     app.run(debug=True)