import joblib
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\b(click here|subscribe|share|like|follow)\b', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def load_model():
    return joblib.load('models/baseline_model_calibrated.joblib')

def predict_news(text, model):
    cleaned = clean_text(text)
    pred = model.predict([cleaned])[0]
    return "Fake News" if pred == 1 else "Real News"

if __name__ == "__main__":
    model = load_model()
    print("Model loaded! Enter news text to classify (type 'exit' to quit):")
    while True:
        news = input("\nEnter news: ")
        if news.strip().lower() == 'exit':
            break
        result = predict_news(news, model)
        print(f"Prediction: {result}")
