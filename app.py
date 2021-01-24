from flask import Flask, render_template, request, jsonify, redirect, url_for
from config import base_config
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import json, pyodbc
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from config import users
from query import cursor

def init(env, resp):
	resp(b'200 OK', [(b'Content-Type', b'text/plain')])
	return [b"Hello WSGI World"]

app = Flask(__name__)
app.config.from_object(base_config)
app.wsgi_app = DispatcherMiddleware(init, {app.config['ABS_PREFIX']: app.wsgi_app})

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main_search')
def api_main_search():
    
    import re
    from query import get_searched_word_en,get_searched_word_mn, check_for_duplicates
    
    regex = re.compile('[@_!#$%^&*<>?\|}{~:.;:!=]')
    data = dict(request.args)
    searchinput = data['input_search']
    lang = data['language']
    
    if (regex.search(searchinput) == None):
        if lang == "EN-MN":
        
            try:
                words = get_searched_word_en(searchinput=searchinput)
                # print(words)
                # return json.dumps({'words': words})
                return {'words': words}

            except IndexError:
            
                 count = check_for_duplicates(searchinput)
                 if count == 0:
                     cursor.execute("INSERT INTO search_not_found (Term_not_found, Search_frequency) VALUES (?,1)", searchinput)
                     cursor.commit()
                 else:
                     cursor.execute("UPDATE [otdict].[dbo].[search_not_found] SET Search_frequency = Search_frequency + 1 WHERE Term_not_found=(?)", searchinput)
                     cursor.commit()
                 # return redirect(url_for('proofread'))

                 return {'response': 'The word you searched is not found, we will add this word soon!'}, 400
                
        elif lang == "MN-EN":

            try:
                words = get_searched_word_mn(searchinput=searchinput)
    
                return {'words': words}

            except IndexError:

                count = check_for_duplicates(searchinput)
                if count == 0:
                    cursor.execute("INSERT INTO search_not_found (Term_not_found, Search_frequency) VALUES (?,1)", searchinput)
                    cursor.commit()
                else:
                    cursor.execute("UPDATE [otdict].[dbo].[search_not_found] SET Search_frequency = Search_frequency + 1 WHERE Term_not_found=(?)", searchinput)
                    cursor.commit()
                # return redirect(url_for('proofread'))

                return {'response': 'The word you searched is not found, we will add this word soon!'}, 400
        
    else:
        return {'response': 'The word cannot contain special characters in it'}, 400

@app.route('/check/<searchinput>/')
def api_contribute_search(searchinput):
    
    import re
    from query import get_searched_word_en

    regex = re.compile('[@_!#$%^&*<>?\|}{~:.;:,!-=]')
    if (regex.search(searchinput) == None):
        
        try:
            words = get_searched_word_en(searchinput = searchinput)
            return {'words': words}

        except IndexError:

            return {'response': 'The word you searched is not found, we will add this word soon!'}, 400
    else:
        return {'response': 'The word cannot contain special characters in it'}, 400

@app.route('/api/autocomplete')
def api_autocomplete():
    
    import re
    from query import auto_complete_en, auto_complete_mn

    data = dict(request.args)
    searchinput = data['input_search']
    lang = data['language']

    regex = re.compile('[@_!#$%^&*<>?\|}{~:.;:,!-=]')
    if (regex.search(searchinput) == None) and searchinput != "":
        if lang == "EN-MN":
            try:
                words = auto_complete_en(span=searchinput)
                
                return json.dumps({'words': words})
                
            except:
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
        return {'response': 'Тусгай тэмдэгт агуулж болохгүй'}, 400


@app.route('/contribute')
def contribute():
    return render_template('contribute.html')

@app.route('/api/add_not_found_word/<word>', methods=['POST','GET'])
def add_not_found_word(word):
    from query import check_for_duplicates
    count = check_for_duplicates(word)

    if count == 0:
        cursor.execute("INSERT INTO search_not_found (Term_not_found, Search_frequency) VALUES (?,1)", word)
        cursor.commit()
    else:
        cursor.execute("UPDATE [otdict].[dbo].[search_not_found] SET Search_frequency = Search_frequency + 1 WHERE Term_not_found=(?)", word)
        cursor.commit()

    return word

@app.route('/contribute/addnew', methods=['POST','GET'])
def contribute_add_new():

    if request.method == "POST":

        newterm = request.form['new-term']
        newdefinition = request.form['new-definition']
        newdescription = request.form['new-description']
        field = request.form['field-option']
        submitemail = request.form['submit-email']    
        
        cursor.execute("INSERT INTO added_terms (Term_added, Definition_added, Description_added, Field, OT_email) VALUES (?,?,?,?,?)", (newterm, newdefinition,newdescription,field,submitemail))
        cursor.commit()
        return render_template('index.html')

@app.route('/proofread/', methods = ['POST', 'GET'])
@auth.login_required
def proofread():

    cursor.execute("SELECT * FROM added_terms")
    data = cursor.fetchall()

    cursor.execute("SELECT * FROM search_not_found ORDER BY Search_frequency DESC")
    search_freq = cursor.fetchall()
    # print (data, search_freq)
    return render_template('proofread.html', added_terms = data, search_freq = search_freq)

@app.route('/proofread/addnew', methods=['POST','GET'])
def addnew_proofread():  

    if request.method == "POST":
        
        term = request.form['term']
        definition = request.form['definition']
        description = request.form['description']
        field = request.form['field']

        cursor.execute("INSERT INTO otdictionary (Term, Term_definition, Term_description, Field) VALUES (?,?,?,?)", (term, definition, description, field))
        cursor.commit()
        return redirect(url_for('proofread'))

@app.route('/proofread/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':

        idx = request.form['id']
        term = request.form['term']
        definition = request.form['definition']
        cursor.execute("UPDATE added_terms SET Term_added = ?, Definition_added = ?  WHERE ID = ?", term, definition, idx)
        cursor.commit()
        return redirect(url_for('proofread'))


@app.route('/proofread/save/<idx>', methods=['GET', 'POST'])
def save(idx):
    if request.method == 'POST':

        cursor.execute("INSERT INTO otdictionary(Term, Term_definition) SELECT Term_added, Definition_added FROM [otdict].[dbo].[added_terms] WHERE ID = {}; DELETE FROM [otdict].[dbo].[added_terms]  WHERE ID = {};".format(idx,idx))
        cursor.commit()
        
    return redirect(url_for('proofread'))

@app.route('/proofread/delete/<idx>', methods=['GET', 'POST'])
def delete(idx):
    if request.method == 'POST':

        cursor.execute("DELETE FROM [otdict].[dbo].[added_terms]  WHERE ID = ?", idx)
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

