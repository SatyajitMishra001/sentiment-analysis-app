
import streamlit as st
import pickle
import re

# Load model and vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Preprocessing function
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

# Streamlit UI
st.title("🎬 Sentiment Analysis - Movie Reviews")

movie_name = st.text_input("Enter the movie name:")
review = st.text_area("Enter your review:")

if st.button("Predict Sentiment"):
    if movie_name and review:
        clean = preprocess(review)
        vector = vectorizer.transform([clean])
        prediction = model.predict(vector)[0]

        # Normalize output
        if isinstance(prediction, int) or prediction in [0, 1]:
            label = "POSITIVE" if prediction == 1 else "NEGATIVE"
        elif str(prediction).lower() in ['positive', 'pos']:
            label = "POSITIVE"
        else:
            label = "NEGATIVE"

        st.markdown("---")
        st.subheader("🎞️ Movie Analysis Result")
        st.write(f"**Movie:** {movie_name}")
        st.success(f"**Sentiment:** {'🟢 ' + label if label == 'POSITIVE' else '🔴 ' + label}")
    else:
        st.warning("⚠️ Please enter both movie name and review.")

