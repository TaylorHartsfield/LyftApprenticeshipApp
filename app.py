from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def string_to_cut():
    '''
    A POST request route that recieves a JSON object containing a string value
    and returns the parsed string by calling the string_cutter function, or an error
    if the entry was not a valid JSON object'''
    string_to_cut = request.json
    if string_to_cut:
        cut_string = string_cutter(string_to_cut['string_to_cut'])
        return jsonify({"return_string": cut_string})
    return jsonify({"error": "Invalid Entry"})


def string_cutter(string):
    '''function to parse over the string parameter
    and return a new string with every 3rd character
    from the parameter string'''
    if len(string)<3: #edge case to handle input less than 3 characters
        return f'Cannot cut a string with less than 3 characters: {string}'
    cut_string = [string[i] for i in range(len(string)) if (i+1)%3==0] 
    return ''.join(cut_string)


if __name__=="__main__":
    app.run()
