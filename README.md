# 📊 Sentilytics: Social Media Sentiment Analyzer

> **Analyze public emotions across social media using Machine Learning and NLP.**

---

## 📚 Project Overview

**Sentilytics** is an end-to-end sentiment analysis system designed to classify user emotions on social media platforms as **Positive**, **Negative**, or **Neutral**.  
It leverages **Natural Language Processing (NLP)** and **Machine Learning** to extract insights from posts/comments/tweets in real time or from historical data.

This project demonstrates how companies and analysts can understand public opinion, brand reputation, or market trends using social media sentiment.

---

## 🚀 Features

- Preprocesses raw social media text (stopword removal, lemmatization, etc.)
- Classifies sentiment using **ML models** (Logistic Regression, Naive Bayes, or any chosen classifier)
- Visualizes sentiment distribution using **Matplotlib** and **Seaborn**
- Supports data import from CSV (or scraped content)
- Easily extendable to Twitter, Instagram, or other platforms

---

## 🛠️ Tech Stack

- **Languages:** Python  
- **Libraries/Tools:** Pandas, NumPy, Scikit-learn, NLTK, Matplotlib, Seaborn  
- **ML Algorithms:** Logistic Regression, SVM, Naive Bayes (pluggable)  
- **NLP Techniques:** Tokenization, Stopword Removal, Lemmatization, TF-IDF

---

## 📂 Project Structure

```bash
Sentilytics/
│
├── database/
  ├── database.py/          # database connected to postgresql
├── model/
  ├── model.py/             # Sentiment model
├── static/
  ├── style.css/            # Css for the frontend
  ├── logo.png/             # Logo for the page title
├── templates/
  ├── index.html/           # HTML file for the frontend
├── .env                    # all api keys and the secret values and password
├── .gitignore              #file that are to be ignore from git commit
├── app.py                  # Main script for training and prediction
├── requirements.txt        # Required Python packages
└── README.md               # Project documentation
```

---

## ⚙️ How to Run

1. **Clone the Repository**
```bash
git clone https://github.com/sneha280904/Sentilytics.git
cd Sentilytics
```

2. **Create Virtual Environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install Requirements**
```bash
pip install -r requirements.txt
```

4. **Run Analysis**
```bash
python app.py
```

---

## 📊 Example Output

- **Sentiment Breakdown:**  
  Pie chart or bar chart of positive, negative, and neutral sentiment.

- **Top Keywords:**  
  WordClouds per sentiment class.

- **Accuracy Score:**  
  ML model performance on test data.

---

## 📎 Future Improvements

- Integrate real-time Twitter scraping with Tweepy
- Add deep learning-based sentiment model (e.g., BERT)
- Deploy via Streamlit or Flask as a web app
- Build a dashboard with Plotly or Power BI

---

## 🙋‍♀️ About Me

I’m **Sneha Gupta**, a B.Tech. AIML student passionate about building intelligent systems using NLP, Python, and Machine Learning.  
Let's connect on [LinkedIn](https://www.linkedin.com/in/sneha-gupta-a78839261/) and build AI that understands emotions! 😊

---
