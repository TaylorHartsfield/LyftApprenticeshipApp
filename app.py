from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def string_to_cut():
    srting_to_cut = request.json['string_to_cut']


def string_cutter(string):
    cut_string = [string[i] for i in range(len(string)) if (i+1)%3==0]
    return ''.join(cut_string)

if __name__=="__main__":
    app.run()
