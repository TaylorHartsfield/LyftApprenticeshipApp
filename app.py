from flask import Flask, request

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    return "Hello"


def string_cutter(string):
    return_value = [string[i] for i in range(len(string)) if (i+1)%3==0]
    return ''.join(return_value)

if __name__=="__main__":
    app.run()
