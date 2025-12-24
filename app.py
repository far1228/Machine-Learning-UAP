import streamlit as st
import pandas as pd
import numpy as np
import pickle
import re
import tensorflow as tf
import torch

from tensorflow.keras.preprocessing.sequence import pad_sequences
from transformers import (
    BertTokenizerFast,
    DistilBertTokenizerFast,
    BertForSequenceClassification,
    DistilBertForSequenceClassification
)

# =============================
# KONFIGURASI
# =============================
st.set_page_config(
    page_title="Sentiment Analysis | ML Dashboard",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Load Custom CSS
def load_css():
    with open("style/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

try:
    load_css()
except:
    st.warning("⚠️ File CSS tidak ditemukan. Pastikan file 'style/style.css' ada.")

# Header Section
st.markdown("# 🎯 Sentiment Analysis")
st.caption("Machine Learning Dashboard — Ujian Akhir Praktikum")

st.markdown("<br>", unsafe_allow_html=True)

# =============================
# PREPROCESSING
# =============================
def clean_text(text):
    """Membersihkan teks dari URL, mention, dan karakter khusus"""
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text.strip()

LABEL_MAP = {0: "Negative", 1: "Neutral", 2: "Positive"}
EMOJI_MAP = {0: "😞", 1: "😐", 2: "😊"}

# =============================
# LOAD MODEL
# =============================
@st.cache_resource
def load_lstm():
    with st.spinner("⏳ Loading LSTM model..."):
        model = tf.keras.models.load_model("models/lstm_model.h5")
        with open("models/tokenizer_lstm.pkl", "rb") as f:
            tokenizer = pickle.load(f)
    return model, tokenizer

@st.cache_resource
def load_distilbert():
    with st.spinner("⏳ Loading DistilBERT model..."):
        path = "models/bertmodels/distilbert"
        tokenizer = DistilBertTokenizerFast.from_pretrained(path)
        model = DistilBertForSequenceClassification.from_pretrained(path)
        model.eval()
    return model, tokenizer

@st.cache_resource
def load_bert():
    with st.spinner("⏳ Loading BERT model..."):
        path = "models/bertmodels/bert"
        tokenizer = BertTokenizerFast.from_pretrained(path)
        model = BertForSequenceClassification.from_pretrained(path)
        model.eval()
    return model, tokenizer

# =============================
# KONFIGURASI MODEL
# =============================
st.markdown("### ⚙️ Configuration")

col1, col2 = st.columns(2)

with col1:
    model_choice = st.selectbox(
        "Select Model",
        ["LSTM", "DistilBERT", "BERT"],
        help="Choose the model for sentiment analysis"
    )

with col2:
    mode = st.radio(
        "Input Mode",
        ["Input Manual", "Batch (Dataset Bersih)"],
        help="Select input method"
    )

use_cleaning = st.checkbox(
    "Enable text preprocessing",
    value=True,
    help="Clean text from URLs, mentions, and special characters"
)

model_descriptions = {
    "LSTM": {"desc": "Sequential model optimized for text processing", "icon": "🔄"},
    "DistilBERT": {"desc": "Lightweight transformer model", "icon": "⚡"},
    "BERT": {"desc": "State-of-the-art transformer model", "icon": "🚀"}
}

st.info(f"{model_descriptions[model_choice]['icon']} **{model_choice}:** {model_descriptions[model_choice]['desc']}")

st.markdown("---")

# =============================
# MODE 1 — INPUT MANUAL
# =============================
if mode == "Input Manual":
    st.markdown("### ✍️ Manual Input")

    text = st.text_area(
        "Enter your text",
        height=150,
        placeholder="Example: I love this product!",
    )

    if st.button("🔍 Analyze Sentiment"):
        if text.strip() == "":
            st.warning("⚠️ Please enter some text first")
        else:
            text_in = clean_text(text) if use_cleaning else text

            if model_choice == "LSTM":
                model, tokenizer = load_lstm()
                seq = tokenizer.texts_to_sequences([text_in])
                pad = pad_sequences(seq, maxlen=100)
                pred = np.argmax(model.predict(pad, verbose=0), axis=1)[0]

            elif model_choice == "DistilBERT":
                model, tokenizer = load_distilbert()
                inputs = tokenizer(text_in, return_tensors="pt", truncation=True, padding=True, max_length=128)
                with torch.no_grad():
                    pred = torch.argmax(model(**inputs).logits, dim=1).item()

            else:
                model, tokenizer = load_bert()
                inputs = tokenizer(text_in, return_tensors="pt", truncation=True, padding=True, max_length=128)
                with torch.no_grad():
                    pred = torch.argmax(model(**inputs).logits, dim=1).item()

            st.success(f"Hasil Prediksi: **{LABEL_MAP[pred]} {EMOJI_MAP[pred]}**")

# =============================
# MODE 2 — BATCH DATASET
# =============================
else:
    st.markdown("### 📊 Batch Processing")
    st.info("📁 Dataset: **data/clean_tweets.csv**")

    try:
        # 🔴 INI SATU-SATUNYA BARIS YANG DIBENARKAN
        df = pd.read_csv("data/clean_tweets.csv", sep=";")

        st.dataframe(df.head(10), use_container_width=True)

        if st.button("🔍 Run Batch Prediction"):
            texts = df["text"].astype(str).tolist()
            if use_cleaning:
                texts = [clean_text(t) for t in texts]

            if model_choice == "LSTM":
                model, tokenizer = load_lstm()
                seq = tokenizer.texts_to_sequences(texts)
                pad = pad_sequences(seq, maxlen=100)
                preds = np.argmax(model.predict(pad, verbose=0), axis=1)

            elif model_choice == "DistilBERT":
                model, tokenizer = load_distilbert()
                inputs = tokenizer(texts, return_tensors="pt", truncation=True, padding=True, max_length=128)
                with torch.no_grad():
                    preds = torch.argmax(model(**inputs).logits, dim=1).numpy()

            else:
                model, tokenizer = load_bert()
                inputs = tokenizer(texts, return_tensors="pt", truncation=True, padding=True, max_length=128)
                with torch.no_grad():
                    preds = torch.argmax(model(**inputs).logits, dim=1).numpy()

            df["prediction"] = [LABEL_MAP[p] for p in preds]
            df["emoji"] = [EMOJI_MAP[p] for p in preds]

            st.success("✅ Batch prediction completed")
            st.dataframe(df.head(50), use_container_width=True)

    except Exception as e:
        st.error(f"❌ Error: {e}")
