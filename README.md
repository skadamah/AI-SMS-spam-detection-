# 🛡️ AI SMS Guardian — MoMo Fraud Detection
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://skadamah-momo-guardian.streamlit.app/)
An AI-powered web application built with **Streamlit** and **Scikit-learn** to detect Mobile Money (MoMo) fraud and phishing SMS messages targeting users in Ghana.

This project aligns with **UN Sustainable Development Goal 16 (Peace, Justice, and Strong Institutions)** by promoting digital financial security and mitigating fraud across mobile payment ecosystems.

---

## 📌 Problem Overview
Mobile Money (MoMo) is central to daily commerce in Ghana, making users frequent targets of social engineering, fraudulent transaction alerts, and phishing links. **AI SMS Guardian** provides instant, client-side NLP classification to distinguish fraudulent alerts from legitimate network confirmations and personal communications.

---

## 🛠️ Architecture & Tech Stack

- **Frontend UI:** Streamlit
- **NLP & Feature Extraction:** TfidfVectorizer (Term Frequency-Inverse Document Frequency)
- **Classifier:** MultinomialNB (Multinomial Naive Bayes)
- **Pipeline:** Scikit-learn unified pipeline (make_pipeline)
- **Data Processing:** Pandas

---

## 🚀 How It Works

1. **Dataset Representation:** Uses a balanced dataset of localized Ghanaian fraud patterns (fake MTN winning alerts, blocked account threats, unauthorized transfer claims) alongside legitimate MoMo transaction receipts and everyday personal text messages.
2. **Feature Extraction:** Transforms raw SMS strings into numerical feature matrices using TF-IDF vectorization to capture distinctive scam keywords and patterns.
3. **Inference Pipeline:** A Naive Bayes classifier predicts whether a test input is scam or safe in real time, alerting the user via the interactive Streamlit dashboard.

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repository
git clone https://github.com/skadamah/AI-SMS-spam-detection-.git
cd AI-SMS-spam-detection-

### 2. Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies
pip install streamlit pandas scikit-learn

### 4. Run the Application
streamlit run emerging.py

Open your browser at http://localhost:8501 to view and interact with the application.

---

## 🗺️ Roadmap & Enhancements
- [ ] Expand the training corpus with larger localized Ghanaian MoMo fraud datasets.
- [ ] Add prediction probability scores for borderline SMS texts.
- [ ] Deploy a live web demo via Streamlit Community Cloud.
- [ ] Expose an API endpoint via FastAPI for mobile app integration.
