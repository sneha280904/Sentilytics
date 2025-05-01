## <---------- IMPORTING REQUIRED MODULES ---------->
## Importing Flask core functions and request tools
from flask import Flask, request, render_template, jsonify
## Importing the sentiment analysis function from model module
from model.model import analyze_sentiment
## Importing the function to insert analyzed post data into the database
from database.database import insert_post

## <---------- INITIALIZE FLASK APP ---------->
## Creating an instance of the Flask app
app = Flask(__name__)

## <---------- ROUTE: HOME PAGE ---------->
## This route renders the homepage with the input form
@app.route('/')
def home():
    return render_template('index.html')

## <---------- ROUTE: ANALYZE SENTIMENT ---------->
## This route processes the form data and returns sentiment analysis
@app.route('/analyze', methods=['POST'])
def analyze():
    ## Get the user input text from the form
    text = request.form.get('text')
    ## Get the selected method, default to 'vader'
    method = request.form.get('method', 'vader')
    ## Perform sentiment analysis using the chosen method
    sentiment = analyze_sentiment(text, method)
    ## Save the post and its sentiment result to the database
    insert_post(text, sentiment['label'], sentiment['score'])
    ## Return the sentiment result as JSON
    return jsonify(sentiment)

## <---------- APP ENTRY POINT ---------->
## Start the Flask app with debug mode enabled
if __name__ == '__main__':
    app.run(debug=True)
