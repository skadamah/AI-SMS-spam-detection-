import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

    # 1. BALANCED DATASET (To stop false positives)
data = {
    'text': [
        # --- SCAMS (Labelled 'scam') ---
        "Your Momo account is blocked. Call 0241112223 to verify now.",
        "Congrats! You won 5000 GHS from MTN. Send 50 GHS for processing.",
        "Urgent: Your bank account has a problem. Click this link: bit.ly/gh-secure",
        "Flash: You have received a bonus of 100 GHS. Dial *170# to check.",
        "You have received 2000 GHS from 055... enter your PIN to claim.",
        
        # --- REAL CONFIRMATIONS (Labelled 'safe') ---
        "Payment of 1.00 GHS to MTN for data bundle was successful. Ref: 1029384.",
        "Your account has been credited with 50.00 GHS by Kojo Mensah. Fee: 0.50.",
        "You have successfully transferred 20.00 GHS to 0244123456. Ref: 882910.",
        "Dear Customer, your MTN MoMo PIN has been changed successfully.",
        "Hey, are we still meeting at the Engineering Gate for the study group?",
        "Please send me the notes for the Network Security class."
    ],
    'label': ['scam', 'scam', 'scam', 'scam', 'scam', 'safe', 'safe', 'safe', 'safe', 'safe', 'safe']
}

df = pd.DataFrame(data)

# 2. THE AI BRAIN
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(df['text'], df['label'])

# 3. THE FRONTEND
st.set_page_config(page_title="SDG 16 AI Guardian", page_icon="🛡️")
st.title("🛡️ AI SMS Guardian")
st.subheader("Targeting SDG 16: Peace, Justice, and Strong Institutions")
st.write("Detecting Mobile Money (MoMo) Fraud in Ghana using Machine Learning.")

user_input = st.text_area("Paste the SMS message here:", placeholder="e.g. Your Momo account is blocked...")

if st.button("Analyze Message"):
    if user_input:
        prediction = model.predict([user_input])[0]
        
        if prediction == 'scam':
            st.error(" SCAM DETECTED: This message appears to be fraudulent. Do NOT respond or click any links.")
        else:
            st.success(" SAFE: This message appears to be legitimate.")
    else:
        st.warning("Please enter a message first.")

st.info("This tool protects the financial justice of Ghanaians by stopping digital fraud.")