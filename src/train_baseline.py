import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

DATA_DIR = Path("data/raw")
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(parents=True, exist_ok=True)

def load_data():
    fake = pd.read_csv(DATA_DIR / "Fake.csv")
    real = pd.read_csv(DATA_DIR / "True.csv")
    fake["label"] = 1
    real["label"] = 0
    df = pd.concat([fake[["title","text","label"]], real[["title","text","label"]]], ignore_index=True)
    df["content"] = (df["title"].fillna("") + " " + df["text"].fillna("")).str.strip()
    return df[["content","label"]]

def train():
    df = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        df["content"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
    )
    pipe = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=50000, ngram_range=(1,2), stop_words="english")),
        ("clf", LogisticRegression(max_iter=2000, n_jobs=-1))
    ])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    print(classification_report(y_test, y_pred, digits=4))
    joblib.dump(pipe, MODEL_DIR / "baseline_model.joblib")
    print("Saved model to models/baseline_model.joblib")

if __name__ == "__main__":
    train()
