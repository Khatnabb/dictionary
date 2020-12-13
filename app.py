from flask import Flask, render_template, request, jsonify, redirect, url_for
# from query import *
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
    return render_template('index.html')

@app.route('/home/<string:searchinput>/lang/<lang>')
def api_main_search(searchinput,lang):
    
    import re
    from query import get_searched_word_en,get_searched_word_mn, check_for_duplicates
    
    regex = re.compile('[@_!#$%^&*<>?\|}{~:.;:!=]')

    if (regex.search(searchinput) == None):
        if lang == "EN-MN":
        
            try:
                words = get_searched_word_en(searchinput=searchinput)
                return json.dumps({'words': words})

            except IndexError:
            
                count = check_for_duplicates(searchinput)
                if count == 0:
                    cursor.execute("INSERT INTO notfound1 (Term, Frequency) VALUES (?,1)", searchinput)
                    cursor.commit()
                else:
                    cursor.execute("UPDATE [otdict].[dbo].[notfound1] SET Frequency = Frequency + 1 WHERE Term=(?)", searchinput)
                    cursor.commit()
                # return redirect(url_for('proofread'))

                return {'response': 'The word you searched is not found, we will add this word soon!'}, 400
                
        elif lang == "MN-EN":

            try:
                words = get_searched_word_mn(searchinput=searchinput)
                return json.dumps({'words': words})

            except IndexError:

                count = check_for_duplicates(searchinput)
                if count == 0:
                    cursor.execute("INSERT INTO notfound1 (Term, Frequency) VALUES (?,1)", searchinput)
                    cursor.commit()
                else:
                    cursor.execute("UPDATE [otdict].[dbo].[notfound1] SET Frequency = Frequency + 1 WHERE Term=(?)", searchinput)
                    cursor.commit()
                # return redirect(url_for('proofread'))

                return {'response': 'The word you searched is not found, we will add this word soon!'}, 400
        
    else:
        return {'response': 'The word cannot contain special characters in it'}, 400

@app.route('/home/check/<searchinput>/')
def api_contribute_search(searchinput):
    
    import re
    from query import get_searched_word_en

    regex = re.compile('[@_!#$%^&*<>?\|}{~:.;:,!-=]')
    if (regex.search(searchinput) == None):
        
        try:
            words = get_searched_word_en( searchinput = searchinput)
            return json.dumps({'words': words})

        except IndexError:

            return {'response': 'The word you searched is not found, we will add this word soon!'}, 400
        
    else:
        return {'response': 'The word cannot contain special characters in it'}, 400

@app.route('/home/autocomplete/<string:searchinput>/lang/<lang>')
def api_autocomplete(searchinput,lang):
    
    import re
    from query import auto_complete, auto_complete_mn
    
    regex = re.compile('[@_!#$%^&*<>?\|}{~:.;:,!-=]')
    if (regex.search(searchinput) == None):
        if lang == "EN-MN":
            try:
                words = auto_complete(span=searchinput)
                
                return json.dumps({'words': words})
                # return json.dumps({'words': words[:10]})
            except IndexError:
                return {'response': 'The word you searched is not found'}, 400
            else:
                return {'response': 'The word cannot contain special characters in it'}, 400
        else:
            try:
                words = auto_complete_mn(span=searchinput)
                
                return json.dumps({'words': words})
                # return json.dumps({'words': words[:10]})
            except IndexError:
                return {'response': 'Хайсан үг олдсонгүй кккк'}, 400
            else:
                return {'response': 'The word cannot contain special characters in it'}, 400


@app.route('/contribute')
def contribute():
    return render_template('contribute.html')

@app.route('/contribute/addnew', methods=['POST','GET'])
def contribute_add_new():

    if request.method == "POST":

        postingterm = request.form['postingterm']
        postingdef = request.form['postingdef']
        postingemail = request.form['email']    
        
        cursor.execute("INSERT INTO newEntries (Term, Def,Email) VALUES (?,?,?)", (postingterm, postingdef,postingemail))
        cursor.commit()
        return render_template('index.html')


@app.route('/proofread/', methods = ['POST', 'GET'])
@auth.login_required
def proofread():

    cursor.execute("SELECT * FROM newEntries")
    data = cursor.fetchall()

    cursor.execute("SELECT * FROM notfound1 ORDER BY Frequency DESC")
    search_freq = cursor.fetchall()

    return render_template('proofread.html', newEntries = data, notFound = search_freq)

@app.route('/proofread/addnew', methods=['POST','GET'])
def addNewProofread():  

    if request.method == "POST":
        
        term = request.form['term']
        definition = request.form['definition']

        cursor.execute("INSERT INTO otdictionary (Term, Def) VALUES (?,?)", (term, definition))
        cursor.commit()
        return redirect(url_for('proofread'))

@app.route('/proofread/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':

        idx = request.form['id']
        term = request.form['term']
        definition = request.form['definition']
        cursor.execute("UPDATE newEntries SET Term = ?, Def = ?  WHERE ID = ?", term, definition, idx)
        cursor.commit()
        return redirect(url_for('proofread'))


@app.route('/proofread/save/<idx>', methods=['GET', 'POST'])
def save(idx):
    if request.method == 'POST':

        cursor.execute("INSERT INTO otdictionary(Term, Def) SELECT Term, Def FROM [otdict].[dbo].[newEntries] WHERE ID = {}; DELETE FROM [otdict].[dbo].[newEntries]  WHERE ID = {};".format(idx,idx))
        cursor.commit()
        
    return redirect(url_for('proofread'))

@app.route('/proofread/delete/<idx>', methods=['GET', 'POST'])
def delete(idx):
    if request.method == 'POST':

        cursor.execute("DELETE FROM [otdict].[dbo].[newEntries]  WHERE ID = ?", idx)
        cursor.commit()
        
    return redirect(url_for('proofread'))

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/home/<searchinput>')
# def api_search(searchinput):

#     from query import get_searched_word_en, Royischeckingtheword

#     words = get_searched_word_en(searchinput=searchinput)
 
#     return  json.dumps({ 'words': words})

# if __name__ == "__main__":
#     app.run(debug=True)