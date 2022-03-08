from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/new')
def new():
    return '<html><body><h1>H1</h1><h2>H2</h2></body></html>';

@app.route('/add')
def add():
    return 'add';

if __name__ == '__main__':
    app.run();