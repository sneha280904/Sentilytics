## <---------- Import libraries for sentiment analysis ---------->
import nltk  ## Natural Language Toolkit for text processing
from nltk.sentiment.vader import SentimentIntensityAnalyzer  ## VADER sentiment analysis tool
from transformers import pipeline  ## Hugging Face pipeline for transformer models

## <---------- Download required NLTK data ---------->
nltk.download('vader_lexicon')  ## Download VADER lexicon for sentiment analysis

## <---------- Initialize sentiment analyzers ---------->
vader = SentimentIntensityAnalyzer()  ## Initialize VADER analyzer
hf_pipeline = pipeline("sentiment-analysis")  ## Load Hugging Face sentiment analysis pipeline

## <---------- Function to analyze sentiment using selected method ---------->
def analyze_sentiment(text, method='vader'):  ## Analyze sentiment using either VADER or Hugging Face
    if method == 'vader':  ## If method is VADER
        score = vader.polarity_scores(text)['compound']  ## Get compound sentiment score
        label = "positive" if score > 0.05 else "negative" if score < -0.05 else "neutral"  ## Determine label
        return {'label': label, 'score': round(score, 2)}  ## Return result as a dictionary
    else:  ## If method is Hugging Face transformer
        result = hf_pipeline(text)[0]  ## Run the transformer model and get result
        return {'label': result['label'].lower(), 'score': round(result['score'], 2)}  ## Return result in lowercase label
