
import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove punctuation
    tokens = text.split()  # Use simple split instead of nltk.word_tokenize
    stop_words = set([
        'a', 'an', 'the', 'and', 'or', 'in', 'on', 'at', 'to', 'from',
        'is', 'are', 'was', 'were', 'it', 'this', 'that', 'with', 'for', 'of'
    ])
    tokens = [t for t in tokens if t not in stop_words]
    return " ".join(tokens)

