import streamlit as st
import pickle
import re


model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))


def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = text.split()
    stop_words = set([
        'a', 'an', 'the', 'and', 'or', 'in', 'on', 'at', 'to', 'from',
        'is', 'are', 'was', 'were', 'it', 'this', 'that', 'with', 'for', 'of'
    ])
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)


st.title("🎬 Sentiment Analysis - Movie Reviews")
review = st.text_area("Enter a review to analyze:")

if st.button("Predict Sentiment"):
    clean = preprocess(review)
    vector = vectorizer.transform([clean])
    prediction = model.predict(vector)[0]
    st.success(f"Sentiment: {prediction.upper()}")

