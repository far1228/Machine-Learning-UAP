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

# =============================
# INLINE CSS (GABUNG TOTAL)
# =============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

* { font-family: 'Inter', sans-serif; }

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #FFF5F7 0%, #FCE7F3 50%, #FBCFE8 100%) !important;
}

h1 {
    font-family: 'Space Grotesk', sans-serif !important;
    background: linear-gradient(135deg, #F9A8D4 0%, #F472B6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    text-align: center;
    font-size: 3rem;
}

.stButton > button {
    background: linear-gradient(135deg, #F9A8D4 0%, #F472B6 100%);
    color: white;
    font-weight: 600;
    padding: 0.8rem 1.8rem;
    border-radius: 12px;
    border: none;
    box-shadow: 0 4px 14px rgba(249,168,212,0.4);
    width: 100%;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #F472B6 0%, #EC4899 100%);
    transform: translateY(-2px);
}

textarea {
    border-radius: 12px !important;
}

div[data-testid="stSuccess"] {
    background: #FFF7ED;
    border-left: 4px solid #FB923C;
    border-radius: 12px;
}

div[data-testid="stWarning"] {
    background: #FEF3C7;
    border-left: 4px solid #FBBF24;
    border-radius: 12px;
}

div[data-testid="stError"] {
    background: #FEE2E2;
    border-left: 4px solid #F87171;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# =============================
# HEADER
# =============================
st.markdown("# 🎯 Sentiment Analysis")
st.caption("Machine Learning Dashboard — Ujian Akhir Praktikum")
st.markdown("<br>", unsafe_allow_html=True)

# =============================
# PREPROCESSING
# =============================
def clean_text(text):
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
    model = tf.keras.models.load_model("models/lstm_model.h5")
    with open("models/tokenizer_lstm.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    return model, tokenizer

@st.cache_resource
def load_distilbert():
    path = "models/bertmodels/distilbert"
    tokenizer = DistilBertTokenizerFast.from_pretrained(path)
    model = DistilBertForSequenceClassification.from_pretrained(path)
    model.eval()
    return model, tokenizer

@st.cache_resource
def load_bert():
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
        ["LSTM", "DistilBERT", "BERT"]
    )

with col2:
    mode = st.radio(
        "Input Mode",
        ["Input Manual", "Batch (Dataset Bersih)"]
    )

use_cleaning = st.checkbox("Enable text preprocessing", value=True)

st.markdown("---")

# =============================
# MODE 1 — INPUT MANUAL
# =============================
if mode == "Input Manual":
    st.markdown("### ✍️ Manual Input")

    text = st.text_area(
        "Enter your text",
        height=150,
        placeholder="Example: I love this product!"
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
