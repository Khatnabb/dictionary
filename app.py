from flask import Flask, render_template, request, jsonify, redirect, url_for
from query import *
import json, pyodbc

app = Flask(__name__)

conx_string = "driver={SQL SERVER}; server=localhost\SQLEXPRESS; database=words; trusted_connection=YES;"

with pyodbc.connect(conx_string) as conx:
    cursor = conx.cursor()
    


@app.route('/home')
def home():
    return render_template('dict.html')

@app.route('/contribute')
def contribute():
    return render_template('contribute.html')

@app.route('/login')
def login():
    return render_template('edit.html')

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

    from query import get_searched_word
    words = get_searched_word(searchinput=searchinput)
    return  json.dumps({ 'words': words})

if __name__ == "__main__":
    app.run(debug=True)