import streamlit as st
import requests

st.set_page_config(page_title="BMI Calculator", page_icon="🧮")

st.title("BMI Calculator")
st.write("Enter your weight and height to calculate your BMI.")

weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (m)", min_value=0.1)

if st.button("Calculate BMI"):
    try:
        response = requests.get(
            "http://localhost:5176/bmi",
            params={"weight": weight, "height": height}
        )
        if response.status_code == 200:
            data = response.json()
            st.success(f"Your BMI is **{data['bmi']:.2f}** — *{data['category']}*")
        else:
            st.error("Something went wrong with the backend.")
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to the backend. Is it running?")
