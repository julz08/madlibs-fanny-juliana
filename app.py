from sunau import AUDIO_FILE_ENCODING_MULAW_8
from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

@app.route('/madlib', methods=['GET'])
def fill_in_blank():
    return render_template("madlib.html", url=url_for('complete'))
    
@app.route('/complete', methods=['GET', 'POST'])
def complete():
    if request.method == "POST":
        animal = request.form['animal']
        adjective = request.form['adjective']
        verb1 = request.form['verb1']
        food1 = request.form['food1']
        food2 = request.form['food2']
        object = request.form['object']
        verb2 = request.form['verb2']
        name = request.form['name']
        place = request.form['place']
        return render_template("complete.html", animal=animal, adjective=adjective, verb1=verb1, food1=food1, food2=food2, object=object, verb2=verb2, name=name, place=place)
    return 'Error!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)