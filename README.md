# ✈️ Analisis Sentimen Twitter Maskapai Penerbangan
Ujian Akhir Praktikum (UAP) – Pembelajaran Mesin

---

## 📖 Gambaran Umum
Proyek ini merupakan implementasi **sistem analisis sentimen berbasis pembelajaran mesin** yang diterapkan pada tweet terkait maskapai penerbangan.  
Sistem ini mengklasifikasikan sentimen teks ke dalam tiga kelas, yaitu **Negative**, **Neutral**, dan **Positive**.

Aplikasi dikembangkan dalam bentuk **website sederhana menggunakan Streamlit** dan mengintegrasikan:
- **1 model Neural Network Non-Pretrained (LSTM)**
- **2 model Pretrained (DistilBERT dan BERT)** dengan pendekatan *transfer learning*

Proyek ini dibuat untuk memenuhi seluruh ketentuan **Ujian Akhir Praktikum (UAP) Mata Kuliah Pembelajaran Mesin**.

---

## 📂 Dataset
- **Nama Dataset** : Twitter Airline Sentiment  
- **Jenis Data** : Data Teks  
- **Jumlah Data** : ±14.000 tweet  
- **Kelas Sentimen** :
  - Negative  
  - Neutral  
  - Positive  

### Sumber Dataset
Dataset diperoleh dari Kaggle (CrowdFlower):  
https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment  

Dataset ini bersifat **open-access** dan banyak digunakan dalam penelitian analisis sentimen.

---

## 🧹 Pra-pemrosesan Data
Tahapan pra-pemrosesan teks yang digunakan pada proyek ini adalah:
- Mengubah teks menjadi huruf kecil
- Menghapus URL
- Menghapus mention (@username)
- Menghapus angka dan karakter non-alfabet
- Menghilangkan spasi berlebih

Pra-pemrosesan dapat **diaktifkan atau dinonaktifkan** langsung melalui antarmuka aplikasi Streamlit.

---

## 🧠 Model yang Digunakan

### 🔹 LSTM (Non-Pretrained)
Model **Neural Network** yang dilatih dari awal (*from scratch*) tanpa menggunakan bobot pretrained.  
Model ini digunakan sebagai **baseline** untuk perbandingan performa.

File model:
models/lstm_model.h5
models/tokenizer_lstm.pkl


---

### 🔹 DistilBERT (Pretrained)
Model pretrained berbasis **Transformer** yang menggunakan pendekatan *transfer learning*.  
Model ini lebih ringan dan efisien dibandingkan BERT.

Direktori model:
models/bertmodels/distilbert/


---

### 🔹 BERT (Pretrained)
Model pretrained berbasis **Transformer** dengan performa terbaik untuk tugas analisis sentimen.  
Digunakan sebagai model dengan akurasi tertinggi.

Direktori model:
models/bertmodels/bert/


---

## 🏷️ Pemetaan Label Sentimen
| Label | Sentimen |
|------|----------|
| 0 | Negative |
| 1 | Neutral |
| 2 | Positive |

---

## 📊 Evaluasi Model
Evaluasi dilakukan terhadap ketiga model menggunakan metrik:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Grafik Loss dan Accuracy

Seluruh proses pelatihan dan evaluasi model terdokumentasi dalam file:
notebooks/UAP_Machine_Learning_fix.ipynb


---

## 📈 Perbandingan Model
| Model | Akurasi | Analisis |
|------|---------|----------|
| LSTM | 0.78| Model baseline |
| DistilBERT | XX% | Efisien dan memiliki akurasi tinggi |
| BERT | XX% | Akurasi terbaik dengan komputasi lebih besar |

---

## 🌐 Implementasi Aplikasi (Streamlit)
Aplikasi Streamlit menyediakan fitur:
- Input teks secara manual
- Prediksi batch menggunakan dataset
- Pemilihan model (LSTM, DistilBERT, BERT)
- Opsi pra-pemrosesan teks
- Menampilkan hasil prediksi sentimen beserta emoji

Dataset batch yang digunakan:
data/clean_tweets.csv

(dengan pemisah `;`)

---

## ▶️ Cara Menjalankan Aplikasi

**1. Install seluruh dependency:**
```bash
pip install -r requirements.txt
**2. Jalankan aplikasi Streamlit:**
