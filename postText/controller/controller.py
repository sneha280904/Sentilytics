## <---------- IMPORTING REQUIRED MODULES ----------> 
## Importing Flask core functions and request tools
from flask import Blueprint, render_template

## Importing service from the service folder
from postText.service.service import service

service = service()  # Creating an instance of the service class

# Create a Blueprint for handling sentiment analysis
sentiment_bp = Blueprint('sentiment_bp', __name__)

## <---------- ROUTE: HOME PAGE ----------> 
## This route renders the homepage with the input form
@sentiment_bp.route('/')
def home():
    return render_template('index.html')

## <---------- ROUTE: ANALYZE SENTIMENT ----------> 
## This route processes the form data and returns sentiment analysis
@sentiment_bp.route('/analyze', methods=['POST'])
def analyze():
    ## Calling the analyze method from the service class to perform sentiment analysis
    return service.analyze()  # Call the analyze method from the service class
