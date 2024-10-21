[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jGFD2OSj)
# Graded Challenge 6 - Set 1

*Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada konsep Clustering*

---

## Assignment Objectives

*Graded Challenge 6* ini dibuat dengan tujuan sebagai berikut:

- Mampu memperoleh data menggunakan Google BigQuery.

- Mampu mempersiapkan data untuk digunakan dalam Clustering.

- Mampu memahami konsep Clustering dengan menggunakan Scikit-Learn.

- Mampu mengimplementasikan Clustering pada data yang telah ditentukan.

---

## Dataset

```{attention}
Perhatikan petunjuk penggunaan dataset!
```

1. Pada tugas kali ini, dataset yang digunakan **tidak akan menggunakan `bigquery-public-data`**. 

2. Masuk ke dalam Google BigQuery. Gunakan informasi dibawah ini sebagai tempat untuk mengambil data (gunakan sebagai informasi untuk klausa `FROM`).
   * Project ID : `ftds-hacktiv8-project`
   
   * Dataset Name : 
     
     + Batch Offline : `phase1_ftds_<nomor-batch>_hck` contoh `phase1_ftds_001_hck`

     + Batch Online : `phase1_ftds_<nomor-batch>_rmt` contoh `phase1_ftds_001_rmt`

     + Batch BSD : `phase1_ftds_<nomor-batch>_bsd` contoh `phase1_ftds_001_bsd`
   
   * Table Name : `credit-card-information`

3. Ambil data dengan kriteria berikut ini : 
   * Batch ganjil (FTDS-001, FTDS-003, dst) : semua data dengan column `CUST_ID` bernilai ganjil.
   
   * Batch genap (FTDS-002, FTDS-004, dst) : semua data dengan column `CUST_ID` bernilai genap.

4. Berikut ini adalah informasi dari setiap column. 
   <img src='https://i.ibb.co/2sbf0Js/P1-G4-Dataset-Information.png'>

5. Simpan dataset dalam bentuk `.csv` dengan nama `P1G6_Set_1_<nama-students>.csv` misal `P1G6_Set_1_raka_ardhi.csv`.

6. Salin query yang telah dibuat di Google Cloud Platform. Tulislah pada bagian atas notebook!

7. Tampilkan `10 data pertama` dan `10 data terakhir` dari dataset pada notebook !

---

## Problem

Anda adalah seorang Data Scientist disebuah perusahaan Bank ABC. Tim marketing meminta anda untuk melakukan Customer Segmentation dari data kartu kredit yang sudah Anda dapatkan peroleh sebelumnya. Data ini merupakan data informasi penggunaan kartu kredit selama 6 bulan terakhir. 

Atas permintaan tersebut, Anda akan membuat proses Clustering dan memberikan rekomendasi bisnis dari setiap Customer Cluster yang terbentuk. Selain itu, tim marketing juga meminta insight bisnis lain dari data yang Anda gunakan yang akan Anda jawab pada bagian Exploratory Data Analysis (EDA). 

***Note : Anda diwajibkan untuk menjawab pertanyaan-pertanyaan dibawah ini. Untuk menjawab soal dibawah ini, mohon tulis ulang masing-masing soal didalam markdown notebook. Anda juga dipersilakan untuk melakukan Exploratory Data Analysis (EDA) lain dan analisa model lainnya pada bagian Model Evaluation diluar pertanyaan yang diminta.***

### Lakukan pada bagian Exploratory Data Analysis (EDA)

1. Apakah terdapat pola antara pengaruh `TENURE` dengan variabel `PURCHASES`, `BALANCE`, dan `PAYMENTS` ? *Buatlah visualisasi yang menunjukkan hubungan ini berikan rekomendasi bisnis untuk tim marketing mengenai hal ini.*

2. Apakah nasabah dengan `CREDIT_LIMIT` yang tinggi cenderung lebih sering melakukan pembelian ? Lakukanlah analisis untuk mengetahui bagaimana `CREDIT_LIMIT` mempengaruhi frekuensi pembelian (`PURCHASES_FREQUENCY`). Buatlah visualisasi yang menunjukkan hubungan ini berikan rekomendasi bisnis untuk tim marketing mengenai hal ini.

---

## Assignment Instructions

*Graded Challenge 6* dikerjakan dalam format ***notebook*** dengen beberapa **kriteria wajib** di bawah ini:

* Machine learning framework yang digunakan adalah *Scikit-Learn*.

* Ada penggunaan library visualisasi, seperti *matplotlib*, *seaborn*, atau yang lain.

* Isi *notebook* harus mengikuti *outline* di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, gambaran besar dataset yang digunakan, dan *objective* yang ingin dicapai.
   
   2. Query SQL
      > Tulis query yang telah dibuat untuk mengambil data dari Google Cloud Platform di bagian ini.

   3. Import Libraries
      > *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.
   
   4. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.
   
   5. Exploratory Data Analysis (EDA)
      > Bagian ini berisi explorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.
   
   6. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.
   
   7. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   8. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.
   
   9. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   10. Model Saving
       > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model.

   11. Model Inference
       > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled.
   
   12. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.
    
---

## Assignment Submission

* Simpan assignment pada sesi ini dengan nama `P1G6_Set_1_<nama-students>.ipynb` misal `P1G6_Set_1_raka_ardhi.ipynb`.

* Push assignment yang telah Anda buat ke akun GitHub Classroom Anda masing-masing.

* Sebelum Anda submit, pastikan untuk melakukan running ulang code yang telah Anda buat. Hal ini bertujuan untuk memastikan tidak ada bagian code yang mengalami error.

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations |
| --- | --- |
| SQL | Mampu melakukan query data dengan kriteria yang telah diberikan |
| Feature Engineering | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (normalisasi, encoding, dll) |
| PCA | Mampu melakukan reduksi dimensi dengan menggunakan PCA |
| K-Means | Mengimplementasikan K-Means dan mengevaluasi hasil cluster yang terbentuk (**minimal 2 teknik berbeda**) |
| Model Inference | Mencoba model yang telah dibuat dengan data baru |
| Runs Perfectly | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar|

### Readability

| Criteria | Meet Expectations |
| --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode |

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

| Criteria | Meet Expectations |
| --- | --- |
| Model Analysis | Menganalisa informasi dari model yang telah dibuat |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan |

```
Contoh kriteria analisa yang baik diantaranya adalah: 

1. Terdapat penjelasan macam-macam hasil metric evaluasi dan interpretasinya terhadap kasus yang diselesaikan.
2. Dapat menjelaskan KELEBIHAN dan KELEMAHAN dari model yang dibuat DENGAN KAITANNYA DENGAN DOMAIN BUSINESS YANG DIHADAPI yang dibuktikan dengan eksplorasi sederhana (grafik, plot, teori, dll).
3. Dapat memberikan statement untuk improvement selanjutnya dari model yang dibuat.
4. Dapat melakukan analisa mengenai karakteristik masing-masing cluster yang terbentuk.
5. Dapat menyebutkan insight yang dapat diambil setelah proses EDA, dll.
```

---

## Notes

* **Deadline : pukul 18:00 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor GC 6 menjadi 0.**
