from flask import Flask, request, jsonify, make_response
from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Text Processing API!"


@app.route('/tokenize', methods=['POST'])
def tokenize_text():
    data = request.get_json()
    text = data.get('text')

    if not text:
        response = make_response(
            jsonify({'error': 'Please provide the text parameter'}), 400)
        return response

    blob = TextBlob(text)
    words = list(blob.words)
    sentences = list(blob.sentences)

    response = make_response(
        jsonify({'words': words, 'sentences': [str(s) for s in sentences]}), 200)
    return response


@app.route('/correct', methods=['POST'])
def correct_text():
    data = request.get_json()
    text = data.get('text')
    if not text:
        response = make_response(
            jsonify({'error': 'Please provide the text parameter'}), 400)
        return response

    corrected_text = TextBlob(text).correct()
    response = make_response(
        jsonify({'corrected_text': str(corrected_text)}), 200)
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5001)
