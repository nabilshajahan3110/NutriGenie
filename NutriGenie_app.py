import streamlit as st
from modules.prompt_engine import get_nutrition_response

st.set_page_config(page_title="NutriGenie", layout="centered")
st.title("🥗 NutriGenie – Your AI Nutrition Assistant")

# User profile input
with st.form("user_info"):
    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    weight = st.number_input("Weight (kg)", min_value=10, max_value=200, value=70)
    goal = st.selectbox("Health Goal", ["Weight Loss", "Muscle Gain", "Diabetes Management", "General Wellness"])
    allergies = st.text_input("Allergies (comma-separated)")
    submitted = st.form_submit_button("Save")

if submitted:
    st.success("Profile saved!")

# Chat input
st.subheader("💬 Ask NutriGenie a Question")
user_query = st.text_input("e.g., Can I eat mangoes if I’m diabetic?")

if user_query:
    profile = {
        "age": age,
        "weight": weight,
        "goal": goal,
        "allergies": allergies
    }
    response = get_nutrition_response(user_query, profile)
    st.markdown(response)