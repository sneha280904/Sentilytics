from flask import Flask, request, render_template, jsonify
from model.model import analyze_sentiment
from database.database import insert_post

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text')
    method = request.form.get('method', 'vader')
    sentiment = analyze_sentiment(text, method)
    insert_post(text, sentiment['label'], sentiment['score'])
    return jsonify(sentiment)

if __name__ == '__main__':
    app.run(debug=True)
