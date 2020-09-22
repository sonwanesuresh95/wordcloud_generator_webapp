from flask import Flask, render_template, request
import os
from generate_wordcloud import generate_cloud

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['Get', 'POST'])
def index():
    return render_template('index.html')


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    try:
        text = request.form['text']
        path = generate_cloud(text)
        return render_template('index.html',path=path)
    except Exception as e:
        return render_template('error_msg.html')


if __name__ == '__main__':
    app.run()
