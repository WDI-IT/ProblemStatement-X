from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route("/scores", methods=['POST'])
def index():
    json_input = request.json
    lists = json_input["lists"]
    scores = generate_scores(lists)
    return jsonify({"scores" : scores})


def generate_scores(dictionary):
    scores = dict()
    for key in dictionary:
        total_score = 0
        for i in dictionary[key]:
            num_vowels = count_vowels(i)
            if num_vowels == 0:
                continue
            if num_vowels%2 == 0:
                total_score = total_score + 2
            else:
                total_score = total_score + 1
        scores[key] = total_score
    return scores


def count_vowels(string):
    vowels = 0
    for i in string:
        if(i=='a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i=='y'):
            vowels = vowels + 1
    return vowels


if __name__ == "__main__":
    app.run(debug=True)
