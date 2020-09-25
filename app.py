from flask import Flask, render_template
from query import *
import json 

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('dict.html')



@app.route('/home/<searchinput>')
def api_search(searchinput):

    from query import get_searched_word
    words = get_searched_word(searchinput=searchinput)
    return  json.dumps({ 'words': words})

# @app.route('/login')
# def login():
#     return "<h1>Login</h1>"
if __name__ == "__main__":
    app.run(debug=True)