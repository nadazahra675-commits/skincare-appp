import streamlit as st
import joblib
import numpy as np

# تحميل الموديل المحفوظ
model = joblib.load('skincare_clean_model.pkl')

st.title("🧴 Skincare Product Analyzer")
st.write("Enter product details to predict the economic tier based on ingredients and price.")

price = st.number_input("Product price ($)", min_value=1.0, max_value=300.0, value=25.0)
ingredient_count = st.number_input("Number of ingredients in the product", min_value=1, max_value=100, value=12)

if st.button("Product Analysis"):
    features = np.array([[price, ingredient_count]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("✅ **Conclusion: The product is considered economical and reasonably priced. (Affordable).")
    else:
        st.warning("⚠️ :**The product is considered high-priced/luxury-tier. (Premium).")
