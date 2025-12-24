# 🛫 Analisis Sentimen Twitter Maskapai Penerbangan
## Ujian Akhir Praktikum (UAP) Pembelajaran Mesin

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![NLP](https://img.shields.io/badge/NLP-Sentiment%20Analysis-green)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-LSTM%20%7C%20BERT-orange)

---

## 📖 Latar Belakang
Twitter merupakan salah satu media sosial yang banyak digunakan oleh pengguna untuk menyampaikan opini dan pengalaman mereka terhadap layanan maskapai penerbangan. Analisis sentimen terhadap tweet dapat membantu memahami persepsi publik secara otomatis menggunakan pendekatan **pembelajaran mesin** dan **deep learning**.

Proyek ini dikembangkan sebagai **Ujian Akhir Praktikum (UAP)** mata kuliah **Pembelajaran Mesin**, dengan fokus pada klasifikasi sentimen data teks serta penerapan **Neural Network** dan **Transfer Learning**, yang kemudian diintegrasikan ke dalam **aplikasi web sederhana berbasis Streamlit**.

---

## 🎯 Tujuan Proyek
Tujuan dari proyek ini adalah:
1. Mengimplementasikan **Neural Network dasar (Non-Pretrained)**
2. Mengimplementasikan **dua model pretrained (Transfer Learning)**
3. Membandingkan performa ketiga model menggunakan metrik evaluasi
4. Membangun aplikasi **Streamlit** untuk demonstrasi model secara lokal

---

## 📊 Dataset
- **Nama Dataset**: Twitter Airline Sentiment  
- **Jumlah Data**: > 14.000 tweet  
- **Sumber**: Kaggle  
- **Link Dataset**:  
  https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment  

### Kolom yang Digunakan
- `text` → Isi tweet  
- `airline_sentiment` → Label sentimen  

### Mapping Label
| Sentimen | Label |
|---------|-------|
| Negative | 0 |
| Neutral  | 1 |
| Positive | 2 |

---

## 🧹 Preprocessing Data
Tahapan preprocessing teks yang dilakukan:
- Case folding (lowercase)
- Menghapus URL
- Menghapus mention (@username)
- Menghapus angka dan simbol
- Normalisasi spasi

Hasil preprocessing disimpan dalam file:
clean_tweets.csv


---

## 🤖 Implementasi Model
Sesuai ketentuan modul UAP, proyek ini mengimplementasikan **3 model pembelajaran mesin**:

### 1️⃣ LSTM (Non-Pretrained)
Model neural network dibangun dari awal (from scratch) dengan arsitektur:
- Embedding Layer
- LSTM Layer
- Dense Softmax Output

**Konfigurasi utama:**
- Optimizer: Adam  
- Loss Function: Sparse Categorical Crossentropy  
- Epoch: 5  
- Batch Size: 64  

---

### 2️⃣ DistilBERT (Pretrained)
- Model: `distilbert-base-uncased`
- Pendekatan: Transfer Learning
- Framework: HuggingFace Transformers
- Fine-tuning pada dataset sentimen

Model ini unggul dalam efisiensi dan kecepatan pelatihan.

---

### 3️⃣ BERT (Pretrained)
- Model: `bert-base-uncased`
- Pendekatan: Transfer Learning
- Fine-tuning penuh
- Framework: HuggingFace Transformers

Model BERT mampu memahami konteks kalimat secara lebih mendalam.

---

## 📈 Evaluasi dan Analisis Model
Evaluasi dilakukan menggunakan:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Grafik Loss dan Accuracy

### Tabel Perbandingan Model
| Model | Akurasi | Analisis |
|------|--------|---------|
| LSTM (Non-Pretrained) | ±80% | Baseline cukup baik namun kurang memahami konteks panjang |
| DistilBERT | ±85% | Stabil dan efisien |
| BERT | **±88%** | Akurasi tertinggi dan performa terbaik |

---

## 🌐 Implementasi Website (Streamlit)
Model diintegrasikan ke dalam aplikasi **Streamlit** dengan fitur:
- Input teks tweet
- Pemilihan model klasifikasi
- Output prediksi sentimen
- Antarmuka sederhana dan interaktif

Aplikasi dijalankan **secara lokal**, sesuai ketentuan UAP.

---

## ▶️ Cara Menjalankan Aplikasi
### 1. Install Dependency
```bash
pip install -r requirements.txt
**2. Jalankan Streamlit**
streamlit run app.py
**3. Akses Aplikasi**
http://localhost:8501

📁 Struktur Repository
📦 Machine-Learning-UAP
 ┣ 📂 dashboardUAP
 ┃ ┣ 📂 data
 ┃ ┃ ┗ clean_tweets.csv
 ┃ ┣ 📂 bert_models
 ┃ ┃ ┣ bert
 ┃ ┃ ┗ distilbert
 ┃ ┣ 📜 app.py
 ┣ 📜 uap_machine_learning_fix.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md

📌 Kesimpulan

Berdasarkan hasil evaluasi, model BERT memberikan performa terbaik dalam analisis sentimen tweet maskapai penerbangan. Seluruh tahapan proyek telah sesuai dengan ketentuan Ujian Akhir Praktikum Pembelajaran Mesin.

📚 Referensi

Kaggle – Twitter Airline Sentiment

HuggingFace Transformers Documentation

TensorFlow & Keras Documentation

Modul UAP Pembelajaran Mesin
