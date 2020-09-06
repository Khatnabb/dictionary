from flask import Flask, render_template
from words import *
app = Flask(__name__)
dictionary = dictionary
@app.route('/home')
def home():
    return render_template('dict.html', dictionary = dictionary)


if __name__ == "__main__":
    app.run(debug=True)
