# 🏠 House Price Prediction Web App

## 📌 Overview

This project is a **Machine Learning Web Application** that predicts house prices based on user inputs such as area (square feet) and number of bedrooms.
It integrates a trained ML model with a web interface and is deployed on the cloud for public access.

---

## 🚀 Features

* 📊 Predict house prices using Linear Regression
* 🌐 Web-based interface (accessible via browser)
* ⚡ FastAPI backend for handling requests
* 🎨 Modern UI with dark mode
* 📈 Dynamic price vs area graph visualization
* ☁️ Deployed on Render

---

## 🧠 Machine Learning Model

* Algorithm: Linear Regression
* Dataset: Ames Housing Dataset (Kaggle)
* Features used:

  * `sqft` (GrLivArea)
  * `bedrooms` (BedroomAbvGr)
* Target:

  * `price` (SalePrice)

---

## 🛠️ Tech Stack

### 🔹 Backend

* Python
* FastAPI
* Uvicorn

### 🔹 Frontend

* HTML, CSS, JavaScript
* Chart.js (for graph visualization)

### 🔹 ML Libraries

* Scikit-learn
* NumPy
* Pandas

### 🔹 Deployment

* GitHub
* Render

---

## 📁 Project Structure

```
house-price-app/
│
├── model.pkl
├── main.py
├── requirements.txt
└── templates/
    └── index.html
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/House-Price-Predictor.git
cd House-Price-Predictor
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run Backend

```
python -m uvicorn main:app --reload
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:8000/
```

---

## 🌐 Live Demo

👉 https://house-price-predictor-7kgy.onrender.com/

---

## 🎯 How It Works

1. User enters house details (area, bedrooms)
2. Frontend sends data to FastAPI backend
3. Backend loads trained ML model (`model.pkl`)
4. Model predicts house price
5. Result is displayed along with a graph

---

## 📸 Screenshots

<img width="1919" height="908" alt="image" src="https://github.com/user-attachments/assets/915c101c-7e20-434c-a652-66efbba64bd4" />
<img width="1919" height="891" alt="image" src="https://github.com/user-attachments/assets/e03b5418-3f89-40f2-802d-94df816dfe23" />


---

## 🎓 Learning Outcomes

* Integration of ML models with web applications
* Building REST APIs using FastAPI
* Frontend-backend communication using Fetch API
* Deployment of ML apps on cloud platforms

---

## 🚀 Future Improvements

* Add more features (bathrooms, location, etc.)
* Improve model accuracy
* Use advanced ML models
* Enhance UI/UX

---

## 👩‍💻 Author

**Gurleen Kaur**

---

## ⭐ Acknowledgements

* Kaggle (Ames Housing Dataset)
* FastAPI Documentation
* Scikit-learn Library

---
