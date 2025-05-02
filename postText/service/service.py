## <---------- IMPORTING REQUIRED MODULES ----------> 
## Importing Flask core functions and request tools
from flask import Flask, render_template, jsonify, request

## Importing the sentiment analysis function from model module
from model.model import analyze_sentiment

## Importing the function to insert analyzed post data into the database
from database.renderDatabase import insert_post

## <---------- SERVICE CLASS DEFINITIONS ----------> 
class service:
    ## <---------- ANALYZE METHOD: PROCESS SENTIMENT ANALYSIS ----------> 
    ## This method processes the form data, performs sentiment analysis, and returns the result as JSON
    def analyze(self):  # Add self parameter to bind to the class instance
        ## <---------- GETTING INPUT TEXT FROM THE FORM ----------> 
        ## Get the user input text from the form
        text = request.form.get('text')

        ## <---------- GETTING SENTIMENT ANALYSIS METHOD ----------> 
        ## Get the selected method, default to 'vader'
        method = request.form.get('method', 'vader')
        
        ## <---------- PERFORMING SENTIMENT ANALYSIS ----------> 
        ## Perform sentiment analysis using the chosen method
        sentiment = analyze_sentiment(text, method)

        ## <---------- INSERTING DATA INTO DATABASE ----------> 
        ## Save the post and its sentiment result to the database
        insert_post(text, method, sentiment['label'], sentiment['score'])
        
        ## <---------- RETURNING SENTIMENT RESULT AS JSON ----------> 
        ## Return the sentiment result as JSON
        return jsonify(sentiment)
