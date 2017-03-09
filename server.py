from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lambdaschool')
def lambdaschool():
    return render_template('lambdaschool.html')

app.run(debug = True)
