from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to this request"

@app.route('/test', methods=['POST'])
def string_to_cut():
    string = request.json
    if string:
        cut_srting = string_cutter(string['string_to_cut'])
        return jsonify({"return_string": cut_string})
    return jsonify({"error": "Invalid Entry"})




def string_cutter(string):
    cut_string = [string[i] for i in range(len(string)) if (i+1)%3==0]
    return ''.join(cut_string)

if __name__=="__main__":
    app.run()
