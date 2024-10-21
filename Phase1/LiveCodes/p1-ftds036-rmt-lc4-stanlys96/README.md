[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Vkp7vLK-)
# Live Code 4 Set 1

---

## Assignment Objectives

*Live Code 4* ini dibuat guna mengevaluasi konsep Time Series Analysis pada pembelajaran Phase 1 sebagai berikut:

- Mampu memahami konsep Time Series Analysis untuk kebutuhan forecasting.

- Mampu mempersiapkan data untuk digunakan dalam pemodelan forecasting.

- Mampu melakukan time series decomposition untuk mengetahui pola seasonal data.

- Mampu menerapkan pengujian stasioneritas dan penerapan teknik differencing pada data.

- Mampu menentukan parameter untuk model forecasting ARIMA dan SARIMA dengan analisis ACF dan PACF.

- Mampu melakukan forecasting data dengan model ARIMA dan SARIMA.

- Mampu menentukan model yang terbaik berdasarkan metrik evaluasi.

---

## Dataset Description

Dataset : `multiTimeline.csv`

| Column | Description |
| --- | --- |
| `Week` | Tanggal pertama pada setiap minggu (berformat `YYYY-MM-DD`) |
| `Pulau Pari: (Indonesia)` |  Informasi persentase popularitas terhadap nilai maksimum dari kata kunci yang dicari. <br><br> - `0 : tidak ada data`, <br> - `50 : popularitas hanya setengah`, <br> - `100 : sangat populer` |

> [!TIP]
> Bukalah terlebih dahulu datasetnya dan perhatikan dengan seksama isi dataset sebelum Anda melakukan Data Loading dengan library Pandas.

---

## Problems

Anda bekerja di sebuah perusahaan travel agent dan diminta untuk menganalisa permintaan paket wisata ke Pulau Pari. Anda memiliki data yang berasal dari Google Trends yang mengandung informasi seberapa populer kata kunci `Pulau Pari` di pencarian Google. Anda diminta untuk memprediksi seberapa populer wisata ke Pulau Pari selama setahun ke depan dari tanggal terakhir dari dataset yang diberikan.

---

## Assignment Instructions

*Live Code 4* dikerjakan dalam format *notebook* dengan beberapa *kriteria wajib* di bawah ini:

1. Time series analysis dan forecasting dilakukan dengan menggunakan library *Statsmodels*.

2. Pengolahan data dilakukan dengan library *Pandas*.

3. Data visualisasi dapat menggunakan library *Matplotlib* atau *Pandas*.

4. Isi *notebook* harus mengikuti *outline* di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, gambaran besar dataset yang digunakan, dan *objective* yang ingin dicapai.
   
   2. Import Libraries
      > *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.
   
   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek tipe data setiap kolom, dll.
 
   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi visualisasi data time series, time series decomposition, ekstraksi periode seasonal, uji stasioner, analisis plot ACF dan PACF.
 
   5. Model Definition and Training
      > Bagian ini berisi proses definisi model hingga pelatihan model menggunakan algoritma ARIMA dan SARIMA.

   6. Model Evaluation
      > Bagian ini berisi evaluasi model menggunakan metrics MAE dan MAPE yang menunjukkan performansi model untuk forecasting data. 

   7. Model Inference
      > Model yang sudah dilatih dan terpilih sebagai model terbaik akan dicoba untuk memprediksi data dimasa depan.

5. Ketentuan Exploratory Data Analysis:
   1. Wajib menampilkan visualisasi data untuk mendapatkan gambaran bentuk time seriesnya. Bagaimana karakteristik dari data time series tersebut ?

   2. Diperlukan untuk melakukan Time Series Decomposition dengan model `additive` atau `multiplicative` sesuai dengan pilihan dan justifikasi yang tepat. Proses ini diperlukan untuk mendapatkan pola seasonal data dan periode seasonal untuk parameter `S` di model SARIMA. Perlu diperhatikan bahwa interval waktu 1 minggu bukan 1 hari.

   3. Uji stasioner data dilakukan di dalam bagian ini dan hanya pada data train saja. Lakukan pengujian apakah data stasioner atau tidak, dan tentukan pula nilai parameter `d`.

   4. Untuk menentukan parameter `p` dan `q`, Anda perlu mengidentifikasinya dari analisis plot ACF dan PACF. Anda juga diizinkan untuk menambahkan metode lain seperti menggunakan acuan metrics BIC dan AIC sebagai bahan perbandingan.

6. Perlu diingat ketika melakukan modeling, gunakan hanya dengan data train dan parameter yang sudah Anda peroleh dari bagian EDA.

7. Pada bagian Model Inference :
   - Lakukanlah prediksi selama setahun ke depan dari tanggal terakhir dari dataset yang diberikan.
   - Gunakan model terbaik berdasarkan hasil analisa yang Anda lakukan pada bagian Model Evaluation.
   - Tampilkan juga hasil prediksi ini dalam bentuk Line Chart.
   - Model Inference dapat Anda kerjakan dalam notebook yang sama dengan proses lainnya.

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `P1LC4_Set_1_<nama-student>.ipynb`, misal `P1LC4_Set_1_raka_ardhi.ipynb`.

- Push Assigment yang telah Anda buat ke akun Github Classroom Anda masing-masing.

- Contoh bentuk isi repository.
    ```
    ├── P1LC4_Set_1_raka_ardhi.ipynb
    ├── multiTimeline.csv
    └── README.md
    ```

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points|
| --- | --- | --- |
| Time Series Decomposition | Mampu melakukan time series decomposition dan menentukan periode seasonal data | 10 pts |
| Stationarity | Mampu menerapkan uji stasioneritas pada data dan melakukan tindaklanjut dari hasil pengujian, menentukan parameter `d` | 10 pts |
| ACF & PACF | Mampu membuat plot ACF & PACF dan mengidentifikasi nilai parameter `p` dan `q` | 20 pts |
| Data Preprocessing | Melakukan pemisahan data ke data train dan test | 5 pts |
| ARIMA | Mampu melakukan forecasting dengan model ARIMA dengan parameter yang tepat | 10 pts |
| SARIMA | Mampu melakukan forecasting dengan model ARIMA dengan parameter yang tepat | 10 pts |
| Model Inference | Mampu memprediksi data hingga setahun ke depan | 10 pts |
| Runs Perfectly | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar | 10 pts |


### Readability

| Criteria | Meet Expectations | Points|
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan menggunakan Markdown untuk penjelasan kode. | 15 pts |

```
Kriteria tertata dengan baik diantaranya adalah : 

1. Terdapat section Perkenalan yang jelas
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
| Model Analysis | Menganalisa informasi dari model yang telah dibuat | 20 pts |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan | 10 pts |

```
Contoh kriteria analisa yang baik diantaranya adalah: 

1. Terdapat penjelasan hasil evaluasi model dengan menggunakan metrics MAE dan MAPE serta interpretasi/kaitannya terhadap kasus yang diselesaikan.
2. Dapat menjelaskan kelemahan/kekurangan dan kelebihan dari model yang dibuat.
3. Dapat menyebutkan insight yang dilakukan pada proses EDA, dll.
```

---

```
Total Points : 130
```

---
## Notes

* **Deadline : pukul 12:15 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor LC 4 menjadi 0.**
