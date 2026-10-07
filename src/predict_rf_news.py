import joblib
import numpy as np

print("Loading NEW 99% model...")
model = joblib.load('models/rf_kaggle_detector.joblib')
vectorizer = joblib.load('models/tfidf_kaggle_vectorizer.joblib')
print("✅ Model and vectorizer loaded! Enter news text. Type 'exit' to quit.")

while True:
    text = input("Enter news text: ").strip()
    if text.lower() == 'exit':
        break
    
    # Clean text same as training
    text = text.lower()
    text_vec = vectorizer.transform([text])
    
    prediction = model.predict(text_vec)[0]
    probabilities = model.predict_proba(text_vec)[0]
    confidence = np.max(probabilities)
    
    label = "🟢 REAL News" if prediction == 0 else "🔴 FAKE News"
    
    print(f"{label} (Confidence: {confidence:.2f})")
