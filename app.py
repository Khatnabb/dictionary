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

@app.route('/login')
def login():
    cursor.execute("SELECT * FROM newEntries")
    data = cursor.fetchall()
    return render_template('edit.html', newEntries = data)

        
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

    regex = re.compile('[@_!#$%^&*()<>?\|}{~:.;:,!-=]')
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

    regex = re.compile('[@_!#$%^&*()<>?\|}{~:.;:,!-=]')
    if (regex.search(searchinput) == None):
        
        try:
            words = auto_complete(span=searchinput)
            return json.dumps({'words': words[:10]})
        except IndexError:
            return {'response': 'The word you searched is not found'}, 400
        
    else:
        return {'response': 'The word cannot contain special characters in it'}, 400

        
if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/home/<searchinput>')
# def api_search(searchinput):

#     from query import get_searched_word, Royischeckingtheword

#     words = get_searched_word(searchinput=searchinput)
 
#     return  json.dumps({ 'words': words})

# if __name__ == "__main__":
#     app.run(debug=True)