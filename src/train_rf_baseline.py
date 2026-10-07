import pandas as pd
import re
import joblib
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

def clean_text(text):
    if pd.isna(text):
        return "missing text"
    text = str(text)
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    return text.lower().strip()

def train_model(data):
    print(f"Training {len(data)} Kaggle competition articles...")
    data['text'] = data['text'].apply(clean_text)
    data = data[data['text'] != "missing text"]
    
    X = data['text']
    y = data['label']
    
    vectorizer = TfidfVectorizer(ngram_range=(1, 1), max_features=5000)
    X_vec = vectorizer.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X_vec, y, test_size=0.2, random_state=42, stratify=y
    )
    
    model = RandomForestClassifier(
        n_estimators=100, 
        max_depth=15, 
        min_samples_split=10, 
        random_state=42
    )
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/rf_kaggle_detector.joblib')
    joblib.dump(vectorizer, 'models/tfidf_kaggle_vectorizer.joblib')
    print("✅ KAGGLE Model saved!")

if __name__ == "__main__":
    print("🚀 TRAINING WITH KAGGLE COMPETITION DATA (35K articles)...")
    df = pd.read_csv('data/train.csv')
    print(f"✅ Loaded: {len(df)} articles")
    print("Balance:", df['label'].value_counts().to_dict())
    train_model(df)
