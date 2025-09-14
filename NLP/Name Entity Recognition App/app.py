from flask import Flask, render_template, request
from markupsafe import Markup
import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entity', methods=['POST', 'GET'])
def entity():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            readable_file = file.read().decode('utf-8', errors='ignore')
            docs = nlp(readable_file)
            docs_html = Markup(displacy.render(docs, style='ent', jupyter=False, options={'distance': 90}))
            return render_template('index.html', html=docs_html, text=readable_file)
        else:
            return render_template('index.html', html=None, text=None)
    else:
        return render_template('index.html', html=None, text=None)

if __name__ == '__main__':
    app.run(debug=True)
