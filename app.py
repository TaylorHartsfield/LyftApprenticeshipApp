from flask import Flask, request

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    return "Hello"