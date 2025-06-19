
import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load model and vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t.isalpha()]
    tokens = [t for t in tokens if t not in stopwords.words("english")]
    return " ".join(tokens)

st.title("🎬 Sentiment Analysis - Movie Reviews")
review = st.text_area("Enter a review to analyze:")

if st.button("Predict Sentiment"):
    clean = preprocess(review)
    vec = vectorizer.transform([clean])
    prediction = model.predict(vec)[0]
    st.success(f"Sentiment: {prediction.upper()}")
