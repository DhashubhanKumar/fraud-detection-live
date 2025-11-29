import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. Load the trained model
model = joblib.load('saved_models/XGBoost_best.pkl')

# 2. Page Configuration
st.set_page_config(
    page_title="FraudGuard AI",
    page_icon="🛡️",
    layout="centered"
)

# 3. Header
st.title("🛡️ FraudGuard AI")
st.markdown("### Real-time Transaction Security System")
st.markdown("---")

# 4. Inputs (Simulating Real Data)
# In production, these come from the Bank's API. Here, we use sliders.

col1, col2 = st.columns(2)
with col1:
    amount = st.number_input("Transaction Amount ($)", min_value=0.0, max_value=50000.0, value=100.0)
with col2:
    time_val = st.number_input("Time (Seconds)", min_value=0.0, value=0.0)

st.write(" ")
st.subheader("🔒 Encrypted Transaction Features")
st.caption("These features (V1-V28) are anonymized by the banking system.")

# Key features that usually impact Fraud
col3, col4, col5 = st.columns(3)
with col3:
    v4 = st.slider("V4 (Vector 4)", -5.0, 5.0, 0.0)
with col4:
    v11 = st.slider("V11 (Vector 11)", -5.0, 5.0, 0.0)
with col5:
    v14 = st.slider("V14 (Vector 14)", -5.0, 5.0, 0.0)

# 5. Prediction Logic
if st.button("Analyze Transaction", type="primary"):
    
    # We need to construct a row with EXACTLY 30 columns
    # Order: [Time, V1, V2 ... V28, Amount]
    
    input_data = [time_val]
    
    # Loop to fill V1 to V28
    for i in range(1, 29):
        if i == 4: input_data.append(v4)
        elif i == 11: input_data.append(v11)
        elif i == 14: input_data.append(v14)
        else: input_data.append(0.0) # Assume average for others
        
    input_data.append(amount)
    
    # Create DataFrame (Columns must match training!)
    cols = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
    df_input = pd.DataFrame([input_data], columns=cols)
    
    # Predict
    prediction = model.predict(df_input)[0]
    probability = model.predict_proba(df_input)[0][1]

    st.markdown("---")
    if prediction == 1:
        st.error(f"🚨 **FRAUD DETECTED**")
        st.write(f"Risk Probability: **{probability:.2%}**")
        st.write("Action: **Transaction Blocked**")
    else:
        st.success(f"✅ **Transaction Approved**")
        st.write(f"Risk Probability: **{probability:.2%}**")