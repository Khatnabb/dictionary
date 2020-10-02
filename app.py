from flask import Flask, render_template, request, jsonify
from query import *
import json 

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('dict.html')

@app.route('/contribute')
def contribute():
    return render_template('contribute.html')

@app.route('/login', methods=['POST','GET'])
def login():

    if request.method == "POST":
    # term = request.form['ug']
    # utga = request.form['utga']
        print(request.data)
        data = dict(request.args)
        print(data)
        # data = request.json
        
        return json.dumps({'data': data})

    # return json.dumps({'term':term, 'utga':utga})


@app.route('/home/<searchinput>')
def api_search(searchinput):

    from query import get_searched_word
    words = get_searched_word(searchinput=searchinput)
    return  json.dumps({ 'words': words})

if __name__ == "__main__":
    app.run(debug=True)