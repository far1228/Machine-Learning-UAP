# ✈️ Analisis Sentimen Twitter Maskapai Penerbangan

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![NLP](https://img.shields.io/badge/NLP-Sentiment%20Analysis-green)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-LSTM%20%7C%20BERT-orange)

### Ujian Akhir Praktikum (UAP) Pembelajaran Mesin

---

## 📖 Latar Belakang
Twitter merupakan salah satu media sosial yang banyak digunakan oleh pengguna untuk menyampaikan opini dan pengalaman mereka terhadap layanan maskapai penerbangan. Analisis sentimen terhadap tweet dapat membantu memahami persepsi publik secara otomatis menggunakan pendekatan **pembelajaran mesin** dan **deep learning**.

Proyek ini dikembangkan sebagai **Ujian Akhir Praktikum (UAP)** mata kuliah **Pembelajaran Mesin**, dengan fokus pada klasifikasi sentimen data teks serta penerapan *Neural Network* dan *Transfer Learning*, yang kemudian diintegrasikan ke dalam aplikasi web sederhana berbasis **Streamlit**.

---

## 🎯 Tujuan Proyek
* Mengimplementasikan **Neural Network** dasar (Non-Pretrained).
* Mengimplementasikan dua model pretrained (**Transfer Learning**).
* Membandingkan performa ketiga model menggunakan metrik evaluasi.
* Membangun aplikasi **Streamlit** untuk demonstrasi model secara lokal.

---

## 📊 Dataset
* **Nama Dataset:** Twitter Airline Sentiment
* **Jumlah Data:** > 14.000 tweet
* **Sumber:** [Kaggle](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)

### Kolom yang Digunakan:
* `text`: Isi tweet.
* `airline_sentiment`: Label sentimen.

### Mapping Label:
| Sentimen | Label |
| :--- | :---: |
| Negative | 0 |
| Neutral | 1 |
| Positive | 2 |

---

## 🧹 Preprocessing Data
Tahapan preprocessing teks yang dilakukan meliputi:
1. **Case folding**: Mengubah teks menjadi lowercase.
2. **Cleaning**: Menghapus URL, mention (@username), angka, dan simbol.
3. **Normalisasi**: Menghapus spasi berlebih.

*Hasil preprocessing disimpan dalam file: `clean_tweets.csv`*

---

## 🤖 Implementasi Model
Sesuai ketentuan modul UAP, proyek ini mengimplementasikan 3 model:

1. **LSTM (Non-Pretrained)**: Model neural network baseline yang dibangun dari awal.
2. **DistilBERT (Pretrained)**: Menggunakan `distilbert-base-uncased` via HuggingFace (Efisien & Cepat).
3. **BERT (Pretrained)**: Menggunakan `bert-base-uncased` untuk pemahaman konteks yang lebih mendalam.

---

## 📈 Evaluasi dan Analisis Model

### Tabel Perbandingan Model:
| Model | Akurasi | Analisis |
| :--- | :---: | :--- |
| **LSTM** | 78% | Cukup baik sebagai baseline, namun kurang menangkap konteks mendalam. |
| **DistilBERT** | 84% | Performa sangat stabil dan efisien meskipun arsitektur ringan. |
| **BERT** | **84%** | Performa terbaik dalam memahami konteks sentimen yang kompleks. |

### 🔍 Metode Evaluasi Model
Evaluasi performa model dilakukan secara menyeluruh sesuai dengan ketentuan Modul UAP Pembelajaran Mesin. Metrik evaluasi yang digunakan meliputi:

- **Classification Report**, yang mencakup nilai Accuracy, Precision, Recall, dan F1-Score untuk setiap kelas sentimen.
- **Confusion Matrix**, untuk menganalisis kesalahan prediksi model pada masing-masing kelas.
- **Grafik Loss dan Accuracy**, yang digunakan untuk memantau proses pelatihan dan validasi model selama training.

Evaluasi ini diterapkan pada ketiga model, yaitu model **Non-Pretrained (LSTM)** serta dua model **Pretrained (DistilBERT dan BERT)**, sehingga perbandingan performa dapat dilakukan secara objektif.

---

## ▶️ Cara Menjalankan Aplikasi

1. **Install Dependency:**
   Pastikan Python sudah terpasang, lalu jalankan perintah berikut di terminal:
   ```bash
   pip install -r requirements.txt
2. **Menjalankan Streamlit:**
   Masuk ke folder proyek dan jalankan:
   ```bash
   streamlit run app.py
3. **Akses Aplikasi:**
   Buka browser dan akses:
   ```bash
   http://localhost:8501
   ```
## 📁 **Struktur Repositori**

```text
📦 Machine-Learning-UAP
 ┣ 📂 dashboardUAP
 ┃ ┣ 📂 data
 ┃ ┃ ┗ 📜 clean_tweets.csv
 ┃ ┣ 📂 bert_models
 ┃ ┃ ┣ 📂 bert
 ┃ ┃ ┗ 📂 distilbert
 ┃ ┗ 📜 app.py
 ┣ 📜 uap_machine_learning_fix.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

## **✅ Kesimpulan**
Berdasarkan hasil evaluasi, dapat disimpulkan bahwa:

**- Model BERT** memberikan performa paling stabil dengan akurasi 84%.

**-** Implementasi **Transfer Learning** terbukti jauh lebih efektif untuk data teks kompleks dibandingkan model baseline.

**-** Seluruh tahapan proyek telah dilaksanakan sesuai dengan ketentuan **Ujian Akhir Praktikum (UAP)**.

## **📚 Referensi**

**Dataset**: [Twitter Airline Sentiment (Kaggle)](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)

**Dokumentasi:** [HuggingFace Transformers](https://huggingface.co/docs/transformers) & [TensorFlow](https://www.tensorflow.org/)
* **Akademik:** Modul UAP Pembelajaran Mesin - Universitas Muhammadiyah Malang

---

<p align="center">
  <b>Qinada Farah</b><br>
  NIM: 202210270311489<br>
  Program Studi Informatika<br>
  Universitas Muhammadiyah Malang
</p>



