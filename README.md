🧠 Sentiment Analysis App (NLP with Transformers)
🏫 A Personal NLP Project – Real-Time Sentiment Classifier!

This project is a real-time web application that classifies text as Positive, Negative, or Neutral using advanced NLP models.
Built with Streamlit and Hugging Face Transformers, it lets you explore sentiment analysis in an interactive way.

📌 Project Overview
The app leverages pre-trained transformer models to analyze sentiment in English text and display results instantly.

💬 Sentiment Classes: Positive, Negative, Neutral

📈 Model Confidence: Displayed per prediction

🧠 Models Supported: BERT, DistilBERT, and more

⚙️ Tech Stack: Python, Streamlit, Transformers

📱 Interface: Fully responsive web UI

sentiment-analysis-app/
├── app.py                  # Main Streamlit application
├── utils/
│   ├── preprocess.py       # Text preprocessing utilities
│   ├── model_loader.py     # Model loading and prediction
│   └── visualization.py    # Visualization functions
├── models/                 # Saved model files (optional)
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore file
└── README.md               # Project documentation
⚙️ How to Run
✅ Option 1: Local Environment (Recommended)

Clone the repository:

bash
Copy
Edit
git clone https://github.com/SatyajitMishra001/sentiment-analysis-app.git
cd sentiment-analysis-app
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
Linux/macOS:

bash
Copy
Edit
source venv/bin/activate
Windows:

bash
Copy
Edit
venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
The app will open in your browser at http://localhost:8501.

✅ Option 2: Customize Model

If you’d like to use a different transformer model:

Open utils/model_loader.py.

Change the MODEL_NAME variable:

python
Copy
Edit
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"
Save and re-run the app.

✅ Using the App
Enter text into the input box.

Click "Analyze".

View:

Sentiment classification

Model confidence score

Sentiment distribution visualization

Optionally upload a file for batch processing.

Export results to CSV.

📝 Notes from the Author
"This project demonstrates how simple it is to build a powerful NLP tool using Streamlit and transformers. If you’re new to NLP, this app can be a great way to learn about real-time sentiment analysis and model serving."

🙌 Special Thanks
Hugging Face 🤗

Streamlit Community

Open-source contributors

💬 Final Thoughts
If you’re learning NLP, Streamlit, or transformers, this project is a perfect place to start.
Feel free to fork, customize, and enhance the app to suit your needs.

📬 Contact
Satyajit Mishra
Email-Satyajitmishraa01@gmail.com
linkdin-www.linkedin.com/in/satyajit-mishra-427a33332

Project Link:
https://github.com/SatyajitMishra001/sentiment-analysis-app
