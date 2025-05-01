import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline

nltk.download('vader_lexicon')

vader = SentimentIntensityAnalyzer()
hf_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text, method='vader'):
    if method == 'vader':
        score = vader.polarity_scores(text)['compound']
        label = "positive" if score > 0.05 else "negative" if score < -0.05 else "neutral"
        return {'label': label, 'score': round(score, 2)}
    else:
        result = hf_pipeline(text)[0]
        return {'label': result['label'].lower(), 'score': round(result['score'], 2)}
