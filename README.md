# ✈️ Twitter Airline Sentiment Analysis
Ujian Akhir Praktikum (UAP) – Pembelajaran Mesin

---

## 📖 Overview
This project implements a **machine learning–based sentiment analysis system** for airline-related tweets.
The system classifies tweets into **Negative**, **Neutral**, or **Positive** sentiment categories.

The application is built as a **simple web-based system using Streamlit** and integrates:
- One **Non-Pretrained Neural Network model (LSTM)**
- Two **Pretrained models (DistilBERT and BERT)** using transfer learning

This project is developed to fully satisfy the requirements of the **Final Practical Exam (UAP)** for the *Machine Learning* course.

---

## 📂 Dataset
- **Dataset Name**: Twitter Airline Sentiment
- **Data Type**: Text Data
- **Total Samples**: ±14,000 tweets
- **Sentiment Classes**:
  - Negative
  - Neutral
  - Positive

### Data Source
The dataset is publicly available on Kaggle:
https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment

---

## 🧹 Text Preprocessing
Text preprocessing steps applied in this project:
- Convert text to lowercase
- Remove URLs
- Remove user mentions (@username)
- Remove numbers and non-alphabet characters
- Trim extra whitespace

Preprocessing can be enabled or disabled directly from the Streamlit interface.

---

## 🧠 Models Implementation

### 🔹 LSTM (Non-Pretrained Model)
- Framework: TensorFlow / Keras
- Trained from scratch without pretrained weights
- Used as a baseline model for comparison

Saved model files:
