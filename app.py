from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

@app.route('/madlib')
def fill_in_blank():
    return render_template("madlib.html")


    
@app.route('/complete')
def compl():
    return render_template("complete.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)