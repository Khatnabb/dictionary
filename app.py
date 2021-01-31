from flask import Flask, render_template, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth
from config import base_config, users
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.security import generate_password_hash, check_password_hash
import json

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
    
    from query import get_searched_word_en,get_searched_word_mn, check_for_duplicates, capture_not_found
    
    data = dict(request.args)
    searchinput = data['input_search']
    lang = data['language']
    
    if lang == "EN-MN":
    
        try:
            words = get_searched_word_en(searchinput=searchinput)

            return {'words': words}

        except:
            capture_not_found(searchinput)

    elif lang == "MN-EN":

        try:
            words = get_searched_word_mn(searchinput=searchinput)
            return {'words': words}

        except:
            capture_not_found(searchinput)
                
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
            return {'title':'Warning','response': 'The word you searched is not found, we will add this word soon!','icon':'warning'}, 400
    else:
        return {'title':'Warning','response': 'The word cannot contain special characters in it','icon':'warning'}, 400

@app.route('/api/autocomplete')
def api_autocomplete():
    
    import re
    from query import auto_complete_en, auto_complete_mn

    data = dict(request.args)
    searchinput = data['input_search']
    lang = data['language']

    regex = re.compile('[@_!#$%^&*<>?\|}{~:.;:!-=](\d+)(,\s*\d+)*')
    if (regex.search(searchinput) == None):
        if lang == "EN-MN":
            try:
                words = auto_complete_en(span=searchinput)
                
                return json.dumps({'words': words})
                
            except:
                return {'title': 'Warning','response': 'The word you searched is not found','icon':'warning'}, 400        
                  
        else:
            try:
                words = auto_complete_mn(span=searchinput)
                
                return json.dumps({'words': words})
            except IndexError:
                return {'title':'Анхаарна уу','response': 'Хайсан үг олдсонгүй', 'icon':'warning'}, 400
                
    else:
        if lang == "EN-MN":

            return {'title': 'Warning','response': 'The word cannot contain special characters and numbers in it', 'icon':'warning'}, 400
        else:
            return {'title': 'Анхаарна уу','response': 'Тусгай тэмдэгт болон тоо агуулж болохгүй', 'icon':'warning'}, 400

@app.route('/api/add_not_found_word/<word>', methods=['POST','GET'])
def add_not_found_word(word):
    capture_not_found(word)

@app.route('/contribute/addnew', methods=['POST','GET'])
def contribute_add_new():
    
    if request.method == "POST":
        
        data = request.form.to_dict()
        # print(data)
        mandatory_keys = ['new-term', 'new-definition', 'field-option', 'email']
        is_valid = True
        # print(data)
        for key in mandatory_keys:
            if key not in data or data[key] is None or data[key] == '':
                is_valid = False 
        from query import contribute_word
        # print(is_valid)
        if is_valid:
            contribute_word(data)
            return {'title': 'Received','response': 'Thank you for your contribution','icon':'success'}, 200
        else:
            return {'title': 'Warning','response': 'Please fill the required fields','icon':'warning'}, 400

        # return 'hi'
            
@app.route('/proofread/', methods = ['POST', 'GET'])
@auth.login_required
def proofread():

    from query import get_tables
    data, search_freq = get_tables()
    return render_template('proofread.html', added_terms = data, search_freq = search_freq)

@app.route('/proofread/addnew', methods=['POST','GET'])
def addnew_proofread():  

    if request.method == "POST":
        
        data = request.form.to_dict()

        from query import contribute_word_proofread
        contribute_word_proofread(data)

        return redirect(url_for('proofread'))

@app.route('/proofread/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':

        data = request.form.to_dict()

        from query import update_contributed_word
        update_contributed_word(data)
    return redirect(url_for('proofread'))


@app.route('/proofread/save/<idx>', methods=['GET', 'POST'])
def save(idx):

    if request.method == 'POST':
        from query import modify_contributed_word
        modify_contributed_word(idx,"save")

    return {'title': 'Warning','response': 'Please fill the required fields','icon':'warning'}, 200

@app.route('/proofread/delete/<idx>', methods=['GET', 'POST'])

def delete(idx):

    if request.method == 'POST':
        from query import modify_contributed_word
        modify_contributed_word(idx,"delete")

    return {'title': 'Warning','response': 'Please fill the required fields','icon':'warning'}, 200

if __name__ == "__main__":
    app.run(debug=True)