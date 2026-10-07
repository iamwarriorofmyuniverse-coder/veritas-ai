# 📰 Fake News Detection System (Machine Learning & NLP)

An end-to-end Natural Language Processing (NLP) and Machine Learning project designed to classify news articles and statements as either **Real News** or **Fake News**.

---

## 🌟 Overview
With the exponential growth of online media and social platforms, misinformation spreads rapidly. This project implements multiple classification pipelines:
1. **Baseline Model:** TF-IDF Vectorization with Logistic Regression / Calibrated Classifier.
2. **Random Forest Pipeline:** Feature extraction with TF-IDF and Random Forest classification.
3. **Deep Learning / Transformer (BERT):** Fine-tuned BERT model for semantic sequence classification.

---

## 📁 Project Structure
```
fake_news_app/
│
├── src/
│   ├── prepare_data.py          # Data preprocessing, cleaning & balancing
│   ├── train_baseline.py        # TF-IDF + Logistic Regression training
│   ├── train_rf_baseline.py     # TF-IDF + Random Forest training
│   ├── fine_tune_bert.py        # BERT transformer fine-tuning pipeline
│   ├── predict_news.py          # Interactive prediction CLI (Baseline model)
│   └── predict_rf_news.py       # Interactive prediction CLI (Random Forest)
│
├── fetch_real_news.py           # Script to fetch real-world news via News API
├── check_version.py             # Environment & package dependency verification
├── .gitignore                   # Excludes heavy binaries, datasets (.csv), and .venv
└── README.md                    # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/iamwarriorofmyuniverse-coder/fake-news-detection.git
cd fake-news-detection
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Or activate on Linux / macOS
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install scikit-learn pandas numpy joblib transformers torch datasets
```

---

## 🚀 How to Run

### 1. Train the Baseline Model
```bash
python src/train_baseline.py
```

### 2. Predict on Custom News (Interactive CLI)
```bash
python src/predict_news.py
```

---

## 👤 Author
* GitHub: [@iamwarriorofmyuniverse-coder](https://github.com/iamwarriorofmyuniverse-coder)
