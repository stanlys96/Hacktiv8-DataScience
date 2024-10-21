[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/lE_RIU9Q)
# Graded Challenge 4

_Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada konsep Regression._

---

## Assignment Objectives

*Graded Challenge 4* ini dibuat dengan tujuan sebagai berikut :

- Mampu memahami konsep regression dengan Linear Regression.

- Mampu mempersiapkan data untuk digunakan dalam model Linear Regression.

- Mampu mengimplementasikan Linear Regression untuk membuat sebuah prediksi.

---

## Dataset Description

Dataset : `house-price-v2.csv`

Description : Dataset ini berisi informasi mengenai harga sebuah rumah yang dijual pada sebuah website penjualan properti sehingga terdapat kemungkinan seorang agen properti rumah mengiklankan rumah yang sama dengan tujuan mempercepat terjualnya rumah tersebut.

| Column | Description |
| --- | --- |
| `area` | Area spesifik sebuah rumah |
| `city` | Kota dimana rumah berada |
| `lattitude` | Garis lintang sebuah rumah |
| `longitude` | Garis bujur sebuah rumah |
| `property_type` | Jenis properti |
| `bedrooms` | Jumlah kamar tidur |
| `bathrooms` | Jumlah kamar mandi |
| `land_area` | Luas tanah (m<sup>2</sup>) |
| `building_area` | Luas bangunan (m<sup>2</sup>) |
| `floors` | Jumlah lantai/tingkatan rumah |
| `maid_bedrooms` | Jumlah kamar tidur pembantu |
| `maid_bathrooms` | Jumlah kamar mandi pembantu |
| `certificate` | Jenis sertifikat bangunan |
| `voltage` | Daya listrik sebuah rumah |
| `building_age` | Usia bangunan |
| `year` | Tahun rumah tersebut dibangun |
| `condition` | Kondisi terkini sebuah rumah |
| `garage` | Apakah rumah tersebut memiliki garasi mobil atau tidak (`1` : Iya, `0` : Tidak) |
| `carport` | Apakah rumah tersebut memiliki carport atau tidak (`1` : Iya, `0` : Tidak) |
| `price` | Harga rumah |

---

## Problem

Saat ini, Anda merupakan seorang Data Scientist yang bekerja pada perusahaan PT. Rumah Baru Keluarga. Perusahaan tempat Anda bekerja menyediakan layanan pembelian rumah yang dijual oleh beberapa agent rumah. Kelebihan perusahaan Anda terletak pada layanan tanya-jawab harga rumah dengan customer yang tidak terbatas dan free charge, layanan pengurusan dokumen kepemilikan rumah super cepat, dan layanan estimasi biaya pembelian rumah yang presisi. Karena ketiga hal ini, tidak heran banyak orang yang mempercayakan rumah barunya ke perusahaan Anda.

Buatlah sebuah model Machine Learning dengan menggunakan algoritma Linear Regression untuk memprediksi harga sebuah rumah. Dataset terlampir pada repository dan jawablah pertanyaan dibawah ini.

***Note : Anda diwajibkan untuk menjawab pertanyaan-pertanyaan dibawah ini. Namun, Anda juga dipersilakan untuk melakukan Exploratory Data Analysis (EDA) dan analisa model lainnya pada bagian Model Evaluation diluar pertanyaan yang diminta.***

### Lakukan pada bagian Exploratory Data Analysis (EDA)

Jawablah beberapa soal dibawah ini : 

1. Berdasarkan daya listriknya (`voltage`), rumah dapat dibedakan menjadi beberapa kategori dibawah ini : 
   * Golongan `R-1` : 450 VA - 2200 VA
   * Golongan `R-2` : 3300 VA - 5500 VA
   * Golongan `R-3` : 6600 VA - ke atas

   Buatlah Pie Chart yang menggambarkan persentase masing-masing golongan diatas !

2. Menurut sebuah sumber, salah satu definisi rumah mewah adalah rumah dengan `building_area` minimal 300 m<sup>2</sup>. Carilah top 5 `area` yang memiliki rumah mewah terbanyak berdasarkan dataset yang ada kemudian tampilkan juga rata-rata harga dari masing-masing area tersebut.

3. Keluarga Bapak Slamet hendak mencari rumah untuk mereka tempati. Karena keuangan mereka yang terbatas, mereka mengasumsikan bahwa rumah yang dibuat sebelum tahun 2000 akan jauh lebih murah harganya mengingat usia rumah yang sudah tua. 
   
   Dari dataset yang ada, terdapat beberapa rumah yang dibuat sebelum tahun 2000. Apakah Anda selaku Data Analyst akan merekomendasikan rumah-rumah ini ? Buktikan rekomendasi Anda dengan menggunakan data, tidak hanya asumsi personal saja !

### Lakukan pada bagian Model Evaluation

Algoritma yang akan Anda pakai adalah Linear Regression. Setelah model terbentuk, lakukanlah analisa terhadap performansi model seperti : 

1. Nyatakan apakah model termasuk ke dalam kategori good-fit, overfit, atau underfit beserta alasannya yang dapat dibuktikan dengan suatu eksplorasi.

2. Apa **KELEBIHAN** dari model yang Anda buat. Buktikan dengan eksplorasi yang memadai (sebisa mungkin buatlah beberapa baris code untuk mendukung justifikasi yang Anda simpulkan).

3. Apa **KELEMAHAN** dari model yang Anda buat. Buktikan dengan eksplorasi yang memadai (sebisa mungkin buatlah beberapa baris code untuk mendukung justifikasi yang Anda simpulkan).

### Lakukan pada bagian Model Inference

Setelah berkonsultasi dengan Anda, Keluarga Bapak Slamet memustukan untuk membeli rumah dengan kriteria dibawah ini 

| Column | Kriteria |
| --- | --- |
| `area` | BSD City |
| `city` | Tangerang |
| `lattitude` | -6.3007333 |
| `longitude` | 106.586126 |
| `property_type` | rumah |
| `bedrooms` | 3 |
| `bathrooms` | 2 |
| `land_area` | 181 |
| `building_area` | 182 |
| `floors` | 2 |
| `maid_bedrooms` | 1 |
| `maid_bathrooms` | 1 |
| `certificate` | shm - sertifikat hak milik |
| `voltage` | 5500 |
| `building_age` | 1 |
| `year` | 2021 |
| `condition` | baru |
| `garage` | 1 |
| `carport` | 1 |

Berikan harga rekomendasi dari model Machine Learning yang Anda buat sebelumnya berdasarkan kriteria dari rumah idaman Bapak Slamet. 

---

## Assignment Instructions

*Graded Challenge 4* dikerjakan dalam format ***notebook*** dengen beberapa **kriteria wajib** di bawah ini:

* Machine learning framework yang digunakan adalah *Scikit-Learn*.

* Terdapat penggunaan library visualisasi, seperti *matplotlib*, *seaborn*, atau yang lain.

* Isi *notebook* harus mengikuti *outline* di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, gambaran besar dataset yang digunakan, dan *objective* yang ingin dicapai.
   
   2. Import Libraries
      > *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.
   
   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.
   
   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi eksplorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya. **Jawab pertanyaan mengenai EDA yang telah ditentukan pada bagian ini. Anda juga dipersilakan melakukan eksplorasi lain mengenai EDA diluar dari pertanyaan yang diberikan diatas.**
   
   5. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-set dan test-set, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

   6. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   7. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.
   
   8. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   9. Model Saving
      > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model.

   10. Model Inference
       > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set ataupun test-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled. **Model Inference harus berada pada notebook yang berbeda dari notebook yang dipakai untuk pembuatan model.**
   
   11. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.
    
---

## Assignment Submission

* Simpan assignment tugas Graded Challenge 4 ini dengan format penamaan file `P1G4_<nama_student>.ipynb`. Contoh : `P1G4_raka_ardhi.ipynb`.

* Push assignment yang telah Anda buat ke akun GitHub Classroom Anda masing-masing.

* Sebelum Anda submit, pastikan untuk melakukan running ulang code yang telah Anda buat. Hal ini bertujuan untuk memastikan tidak ada bagian code yang mengalami error.

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Feature Engineering | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (split data, normalisasi, encoding, dll) | 35 pts |
| Linear Regression | Mengimplementasikan Linear Regression dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Model Inference | Mencoba model yang telah dibuat dengan data baru | 10 pts |
| Runs Perfectly | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar | 10 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 15 pts |

```
Kriteria tertata dengan baik diantaranya adalah: 

1. Terdapat section Perkenalan yang jelas dan lengkap terkait masalah dan latar belakang masalah yang akan diselesaikan.
2. Tidak menyalin markdown dari tugas lain.
3. Import library rapih (terdapat dalam 1 cell dan tidak ada unused libs).
4. Pemakaian fungsi markdown yang optimal (Heading, text formating, dll).
5. Terdapat komentar pada setiap baris kode.
6. Adanya pemisah yang jelas antar section, dll.
7. Tidak adanya typo.
```

### Analysis

| Criteria | Meet Expectations | Points|
| --- | --- | --- |
| Model Analysis | Menganalisa informasi dari model yang telah dibuat | 35 pts |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan | 20 pts |

```
Contoh kriteria analisa yang baik diantaranya adalah: 

1. Terdapat penjelasan macam-macam hasil metric evaluasi dan interpretasinya terhadap kasus yang diselesaikan.
2. Dapat menjelaskan KELEBIHAN dan KELEMAHAN dari model yang dibuat DENGAN KAITANNYA DENGAN DOMAIN BUSINESS YANG DIHADAPI yang dibuktikan dengan eksplorasi sederhana (grafik, plot, teori, dll).
3. Dapat menjelaskan maksud dari slope & intercept yang didapat dari hasil proses training.
4. Dapat memberikan langkah apa yang sebaiknya dilakukan untuk meningkatkat performansi model.
5. Dapat menyebutkan insight yang dapat diambil setelah proses EDA.
6. Dapat mengkaitkan performansi model yang didapat dengan kasus yang dihadapi, seperti apakah model acceptable untuk diimplementasikan, keterhubungan antara tingkat error yang didapat dengan uang yang harus disiapkan oleh calon pembeli, dll.
```

---

```
Total Points : 135
```

---

## Notes

* **Deadline : pukul 18:00 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor GC 4 menjadi 0.**
