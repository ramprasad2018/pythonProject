from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello New World!</p>"

@app.route("/test")
def test():
    return "<p>Hello Test</p>"
