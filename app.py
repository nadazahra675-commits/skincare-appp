import streamlit as st
import joblib
import numpy as np

# تحميل الموديل المحفوظ
model = joblib.load('skincare_clean_model.pkl')

st.title("🧴 Skincare Product Analyzer")
st.write("ادخلي تفاصيل المنتج للتنبؤ بالفئة الاقتصادية بناءً على المكونات والسعر:")

price = st.number_input("سعر المنتج ($)", min_value=1.0, max_value=300.0, value=25.0)
ingredient_count = st.number_input("عدد المكونات في المنتج", min_value=1, max_value=100, value=12)

if st.button("تحليل المنتج"):
    features = np.array([[price, ingredient_count]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("✅ **النتيجة:** المنتج يعتبر اقتصادي ومناسب للسعر (Affordable).")
    else:
        st.warning("⚠️ **النتيجة:** المنتج يعتبر مرتفع السعر/فئة فاخرة (Premium).")
