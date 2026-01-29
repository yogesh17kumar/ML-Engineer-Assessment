import streamlit as st
import joblib
import numpy as np
import os

# Safe path (works everywhere)
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except:
    BASE_DIR = os.getcwd()

model = joblib.load(os.path.join(BASE_DIR, "fraud_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))

st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🚨",
    layout="centered"
)

st.markdown("""
<style>
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
h1, h4 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🚨 Fraud Detection System</h1>", unsafe_allow_html=True)
st.markdown("<h4>Real-time Transaction Risk Analysis</h4>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🧾 Transaction Details")

amount = st.number_input("💰 Transaction Amount", min_value=1)
location = st.selectbox("📍 Location Changed?", ["No", "Yes"])
device = st.selectbox("📱 New Device Used?", ["No", "Yes"])
hour = st.slider("⏰ Transaction Hour", 0, 23)

st.markdown("</div>", unsafe_allow_html=True)

if st.button("🔍 Analyze Transaction"):
    loc = 1 if location == "Yes" else 0
    dev = 1 if device == "Yes" else 0

    X = np.array([[amount, loc, dev, hour]])
    X = scaler.transform(X)

    prob = model.predict_proba(X)[0][1]

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    if prob >= 0.5:
        st.error(f"🚨 Fraud Detected | Risk: {prob:.2f}")
    else:
        st.success(f"✅ Legit Transaction | Risk: {prob:.2f}")
    st.markdown("</div>", unsafe_allow_html=True)
