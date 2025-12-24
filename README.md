✈️ Analisis Sentimen Twitter Maskapai Penerbangan

Ujian Akhir Praktikum (UAP) – Pembelajaran Mesin

Gambaran Umum

Proyek ini merupakan implementasi sistem analisis sentimen berbasis pembelajaran mesin yang diterapkan pada tweet terkait maskapai penerbangan. Sistem mengklasifikasikan sentimen teks ke dalam tiga kelas, yaitu Negative, Neutral, dan Positive.

Aplikasi dikembangkan dalam bentuk website sederhana menggunakan Streamlit dan mengintegrasikan tiga model pembelajaran mesin, yaitu satu model Neural Network Non-Pretrained (LSTM) serta dua model Pretrained (DistilBERT dan BERT) dengan pendekatan transfer learning.

Proyek ini dibuat untuk memenuhi seluruh ketentuan Ujian Akhir Praktikum (UAP) Mata Kuliah Pembelajaran Mesin.

Dataset

Nama Dataset: Twitter Airline Sentiment
Jenis Data: Data Teks
Jumlah Data: ±14.000 tweet
Kelas Sentimen: Negative, Neutral, Positive

Sumber dataset berasal dari Kaggle (CrowdFlower):
https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment

Dataset ini bersifat open-access dan umum digunakan untuk penelitian analisis sentimen.

Pra-pemrosesan Data

Tahapan pra-pemrosesan teks yang digunakan pada proyek ini meliputi:

Mengubah teks menjadi huruf kecil

Menghapus URL

Menghapus mention (@username)

Menghapus angka dan karakter non-alfabet

Menghilangkan spasi berlebih

Pra-pemrosesan dapat diaktifkan atau dinonaktifkan langsung melalui antarmuka aplikasi Streamlit.

Model yang Digunakan

LSTM (Non-Pretrained)
Model Neural Network yang dilatih dari awal (from scratch) tanpa menggunakan bobot pretrained. Model ini digunakan sebagai baseline untuk perbandingan performa.
File model disimpan pada:
models/lstm_model.h5
models/tokenizer_lstm.pkl

DistilBERT (Pretrained)
Model pretrained berbasis Transformer dengan pendekatan transfer learning yang lebih ringan dan efisien.
Direktori model:
models/bertmodels/distilbert/

BERT (Pretrained)
Model pretrained berbasis Transformer dengan performa terbaik untuk analisis sentimen.
Direktori model:
models/bertmodels/bert/

Pemetaan Label Sentimen

0 = Negative
1 = Neutral
2 = Positive

Evaluasi Model

Evaluasi dilakukan terhadap ketiga model menggunakan metrik Accuracy, Precision, Recall, F1-Score, Confusion Matrix, serta grafik Loss dan Accuracy.

Seluruh proses pelatihan dan evaluasi model terdokumentasi dalam file notebook:
notebooks/UAP_Machine_Learning_fix.ipynb

Perbandingan Model

Model: LSTM
Akurasi: XX%
Analisis: Model baseline dengan performa stabil

Model: DistilBERT
Akurasi: XX%
Analisis: Efisien dan memiliki akurasi tinggi

Model: BERT
Akurasi: XX%
Analisis: Akurasi terbaik dengan kebutuhan komputasi lebih besar

Implementasi Aplikasi Streamlit

Aplikasi Streamlit menyediakan fitur input teks manual, prediksi batch menggunakan dataset, pemilihan model (LSTM, DistilBERT, BERT), opsi pra-pemrosesan teks, serta menampilkan hasil prediksi sentimen beserta emoji.

Dataset batch yang digunakan berada pada:
data/clean_tweets.csv
(dengan pemisah titik koma ;)

Cara Menjalankan Aplikasi

Langkah 1: Install dependency
pip install -r requirements.txt

Langkah 2: Jalankan aplikasi Streamlit
streamlit run app.py

Langkah 3: Akses melalui browser
http://localhost:8501

Struktur Proyek

twitter-airline-sentiment-uap/
├── app.py
├── requirements.txt
├── data/clean_tweets.csv
├── models/
│ ├── lstm_model.h5
│ ├── tokenizer_lstm.pkl
│ └── bertmodels/
│ ├── distilbert/
│ └── bert/
├── notebooks/UAP_Machine_Learning_fix.ipynb
└── README.md

Informasi Akademik

Mata Kuliah: Pembelajaran Mesin
Jenis Tugas: Ujian Akhir Praktikum (UAP)
Topik: Analisis Sentimen Twitter Maskapai Penerbangan
Tools: TensorFlow, PyTorch, Hugging Face, Streamlit

Catatan

Proyek dibuat secara original, menggunakan dataset open-access, dan siap untuk didemokan secara lokal kepada asisten praktikum.
