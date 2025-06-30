from flask import Flask, render_template, request, jsonify
from model.bert_sentiment import load_model
from responses.logic import get_response

app = Flask(__name__)
classifier = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    result = classifier(user_input)[0]
    sentiment = result['label']
    reply = get_response(sentiment)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
