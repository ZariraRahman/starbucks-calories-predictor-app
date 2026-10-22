
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Starbucks Calories Predictor",
    page_icon="☕",
    layout="centered"
)

@st.cache_resource
def load_model():
    return joblib.load("starbucks_calories_model.pkl")

try:
    model = load_model()
except Exception as e:
    st.error("Model load nahi hua. Check karein ke .pkl file app.py ke saath hai.")
    st.stop()

st.title("☕ Starbucks Calories Predictor")
st.write(
    "Starbucks drink ki nutritional details enter karein "
    "aur estimated calories predict karein."
)

st.subheader("Drink Details")

beverage_category = st.selectbox(
    "Beverage Category",
    [
        "Coffee",
        "Classic Espresso Drinks",
        "Signature Espresso Drinks",
        "Tazo Tea Drinks",
        "Shaken Iced Beverages",
        "Frappuccino Blended Coffee",
        "Frappuccino Light Blended Coffee",
        "Frappuccino Blended Crème",
        "Smoothies"
    ]
)

beverage = st.text_input("Beverage Name", "Caffè Latte")
beverage_prep = st.text_input("Beverage Preparation", "Grande Nonfat Milk")

st.subheader("Nutrition Details")
st.caption("Values numeric enter karein. Percent DV ke liye 10 likhein, 10% nahi.")

c1, c2 = st.columns(2)

with c1:
    total_fat = st.number_input("Total Fat (g)", min_value=0.0, value=5.0)
    trans_fat = st.number_input("Trans Fat (g)", min_value=0.0, value=0.0)
    saturated_fat = st.number_input("Saturated Fat (g)", min_value=0.0, value=3.0)
    sodium = st.number_input("Sodium (mg)", min_value=0.0, value=ро)
