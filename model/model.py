import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline

# Download VADER lexicon if not already
nltk.download('vader_lexicon')

# Initialize VADER
vader = SentimentIntensityAnalyzer()

# ✅ Function to analyze sentiment
def analyze_sentiment(text, method='vader'):
    if method == 'vader':
        score = vader.polarity_scores(text)['compound']
        label = "positive" if score > 0.05 else "negative" if score < -0.05 else "neutral"
        return {'label': label, 'score': round(score, 2)}
    
    else:
        # ✅ Lazy-load and cache Hugging Face model only once
        if not hasattr(analyze_sentiment, "_hf_pipeline"):
            analyze_sentiment._hf_pipeline = pipeline(
                "sentiment-analysis",
                model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
            )
        result = analyze_sentiment._hf_pipeline(text)[0]
        return {'label': result['label'].lower(), 'score': round(result['score'], 2)}
