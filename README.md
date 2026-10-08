# 🔍 VeritasAI — Real-Time Fact-Checking & Credibility Engine

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Grounding-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Chrome Extension](https://img.shields.io/badge/Manifest_V3-Chrome_Ext-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

<p align="center">
  <b>Automated fact-checking and credibility verification platform grounded against live Google News Wire RSS feeds with 1-click Manifest V3 Chrome Extension integration.</b>
</p>

</div>

---

## 🌟 Key Highlights

* 🌐 **Live Google News Wire RSS Grounding:** Dynamically fetches and corroborates claims in real-time against verified journalism sources.
* 🧩 **Manifest V3 Chrome Extension:** Enables 1-click context-menu fact-checking directly on social feeds (X/Twitter, Reddit, Facebook, news websites).
* 🎯 **Dynamic Credibility Scoring Dial:** Delivers multi-factor credibility percentages ($0\text{--}100\%$) weighted by lexical stance and corroboration strength.
* ⚡ **FastAPI High-Throughput Inference:** Low-latency async verification API for fast client responses.
* 🤖 **Hybrid NLP Architecture:** Supports TF-IDF + Calibrated Classifiers, Random Forests, and fine-tuned BERT Transformer checkpoints.

---

## 📁 Repository Architecture
```
veritas-ai/
│
├── extension/                   # Manifest V3 Chrome Extension
│   ├── manifest.json            # Extension configuration & permissions
│   ├── background.js            # Background service worker (Context menus)
│   ├── content.js               # In-page toast/notification overlay on social feeds
│   ├── popup.html               # Extension UI & dynamic credibility dial
│   └── popup.js                 # API bridge & live source rendering
│
├── src/
│   ├── api.py                   # FastAPI real-time fact-checking server
│   ├── prepare_data.py          # Data preprocessing, cleaning & balancing
│   ├── train_baseline.py        # TF-IDF + Logistic Regression training
│   ├── train_rf_baseline.py     # TF-IDF + Random Forest training
│   ├── fine_tune_bert.py        # BERT transformer fine-tuning pipeline
│   ├── predict_news.py          # Interactive prediction CLI (Baseline)
│   └── predict_rf_news.py       # Interactive prediction CLI (Random Forest)
│
├── fetch_real_news.py           # Live Google News Wire RSS scraper (gnews)
├── check_version.py             # Dependency verification
├── .gitignore                   # Excludes heavy datasets and model binaries
└── README.md                    # Project documentation
```

---

## 🚀 Quick Start Guide

### 1. Clone & Set Up Backend

```bash
# Clone the repository
git clone https://github.com/iamwarriorofmyuniverse-coder/veritas-ai.git
cd veritas-ai

# Create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate   # On Windows (PowerShell)
# source .venv/bin/activate  # On Linux/macOS

# Install dependencies
pip install fastapi uvicorn gnews pydantic scikit-learn pandas numpy joblib transformers torch
```

### 2. Start the VeritasAI Fact-Checking Server

```bash
python src/api.py
```
*API will run at `http://localhost:8000` with interactive Swagger docs at `http://localhost:8000/docs`.*

---

## 🧩 Installing the Chrome Extension

1. Open Google Chrome and navigate to `chrome://extensions/`.
2. Enable **Developer mode** (toggle in the top-right corner).
3. Click **Load unpacked**.
4. Select the `extension/` folder inside this repository.
5. **Usage:** Highlight any text on any webpage or social feed $\rightarrow$ Right-click $\rightarrow$ Select **"🔍 Fact-Check with VeritasAI"**!

---

## 👤 Author
* **C. Dharshan**
* GitHub: [@iamwarriorofmyuniverse-coder](https://github.com/iamwarriorofmyuniverse-coder)
