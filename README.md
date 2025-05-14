# 🧮 Simple BMI App

A minimal full-stack Body Mass Index (BMI) calculator built with:

- ⚙️ **C# .NET 9.0** backend (REST API)
- 🧼 **Python Streamlit** frontend
- 📦 Docker / Deploy-ready structure (optional)
- 🌐 Built for easy GitHub deployment + local testing

---

## 📸 Preview

![BMI UI Preview](https://via.placeholder.com/700x300.png?text=Simple+BMI+App+Preview)

---

## 🚀 How it works

1. The **Streamlit frontend** takes in your weight and height.
2. It makes a request to the **C# API** endpoint `/bmi`.
3. The backend calculates BMI and returns the result + category (e.g., "Overweight").

---

## 📁 Project Structure

SimpleBmiApp/
├── BmiApi/ # .NET 9 API project
│ └── Controllers/ # BMI calculation logic
├── streamlit_ui/ # Python frontend
│ ├── app.py # Streamlit app
│ └── venv/ # Virtual environment (not pushed to GitHub)
├── .gitignore
└── README.md

