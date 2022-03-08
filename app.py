from flask import Flask
import calculator;

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/new')
def new():
    return '<html><body><h1>H1</h1><h2>H2</h2></body></html>';

@app.route('/add')
def add():
    return str(calculator.add(4.5, 7.8));

if __name__ == '__main__':
    app.run();