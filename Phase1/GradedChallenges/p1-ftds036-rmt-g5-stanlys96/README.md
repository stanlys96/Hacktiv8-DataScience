[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/LafLnK4P)
# Graded Challenge 5
*Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada konsep Classification*

> *Sangat disarankan untuk mengerjakan tugas ini menggunakan Google Colab*

---

## Assignment Objectives

*Graded Challenge 5* ini dibuat dengan tujuan sebagai berikut:

- Mampu memperoleh data menggunakan Google BigQuery.

- Mampu memahami efek dari penambahakan fitur terhadap performa dari model Machine Learning.

- Mampu mempersiapkan data untuk digunakan dalam modeling.

- Mampu mengimplementasikan Pipeline dan algoritma Logistic Regression untuk membuat sebuah prediksi.

---

## Dataset
### Source

1. Buka [Google Cloud Platform](https://console.cloud.google.com/), masuk ke BigQuery, lalu buka tab `data-to-insights` atau link [berikut](https://console.cloud.google.com/bigquery?p=data-to-insights&d=ecommerce&t=web_analytics&page=table) untuk langsung menuju ke dataset.

2. Gunakan dataset `ecommerce` dengan tabel `web_analytics`.

3. Detail informasi mengenai kolom pada tabel tersebut dapat Anda lihat [disini](https://support.google.com/analytics/answer/3437719?hl=en). 

4. Berikut adalah beberapa deskripsi tambahan untuk membantu Anda dalam memahami data yang diberikan terkait dengan Google Analytics dan Digital Marketing:

   | Kolom                  | Deskripsi                                                                                      |
   |------------------------|--------------------------------------------------------------------------------------------------|
   | `will_buy_on_return_visit` | Menunjukkan apakah pengunjung akan melakukan pembelian saat mengunjungi kembali situs web (1 = Ya, 0 = Tidak) |
   | `totals.bounces`       | Jumlah pengunjung yang langsung meninggalkan situs web tanpa melakukan aksi apapun              |
   | `totals.timeOnSite`    | Durasi waktu yang dihabiskan pengunjung di situs web                                             |

   *Saran:  Fokuslah memahami kolom yang dijadikan sebagai fitur. Untuk informasi tentang kolom lainnya, Anda dapat melihat pada deskripsi dataset yang telah diberitahukan pada nomer 3.*

5. Lakukanlah pembuatan dataset seperti petunjuk pada bagian berikut ini.

### Dataset Creation

Pada kasus ini anda akan membuat 2 buah dataset untuk pelatihan pemodelan machine learning, dengan ketentuan :

1. Dataset pertama : `dataset_1.csv`
   * Data ini adalah data yang akan dilatih menggunakan 2 fitur yaitu `totals.bounces` dan `totals.timeOnSite` dengan target `will_buy_on_return_visit`.
   * Simpanlah hasil query dibawah ini ke dalam file dengan nama `dataset_1.csv`.
   * Query yang anda gunakan untuk membuat dataset ini adalah sebegai berikut:
      ```sql
      SELECT * EXCEPT(fullVisitorId)
   
      FROM
        # features
        (SELECT
          fullVisitorId,
          IFNULL(totals.bounces, 0) AS bounces,
          IFNULL(totals.timeOnSite, 0) AS time_on_site
        FROM
          `data-to-insights.ecommerce.web_analytics`
        WHERE
          totals.newVisits = 1 #gunakan hanya untuk pengunjung baru
          AND date BETWEEN '20160801' AND '20170531') # latih hanya pada 10 bulan pertama
        JOIN
        (SELECT
          fullvisitorid,
          # membuat label atau target
          IF(COUNTIF(totals.transactions > 0 AND totals.newVisits IS NULL) > 0, 1, 0) AS will_buy_on_return_visit
        FROM
            `data-to-insights.ecommerce.web_analytics`
        GROUP BY fullvisitorid)
        USING (fullVisitorId)
        ;
      ```
  
2. Dataset kedua : `dataset_2.csv`
   * Pada dataset kedua ini, Anda akan menambahkan beberapa fitur baru dari dataset pertama.
   * Dataset kedua ini akan berisi daftar column sebagai berikut :
     | Column |
     | --- |
     | `will_buy_on_return_visit` |
     | `latest_ecommerce_progress` |
     | `bounces` |
     | `time_on_site` |
     | `pageviews` |
     | `source` |
     | `medium` |
     | `channelGrouping` |
     | `deviceCategory` |
     | `country` |
   * Lengkapi query dibawah ini untuk membuat dataset baru dan simpan outputnya dengan nama `dataset_2.csv`.

     *Output Query ini akan menghasilkan 10 columns seperti yang dijelaskan pada poin sebelumnya. **Note: Anda diwajibkan untuk melengkapi query dibawah ini***
     ```sql
     WITH all_visitor_stats AS (
     SELECT
       fullvisitorid,
       #1. buatlah label atau target  "will_buy_on_return_visit" dan hilangkan komentar pada code tersebut .
       /*
       isi code anda disini
       */
       FROM `data-to-insights.ecommerce.web_analytics`
       GROUP BY fullvisitorid
     )
   
     SELECT * EXCEPT(unique_session_id) FROM (
   
       SELECT
           CONCAT(fullvisitorid, CAST(visitId AS STRING)) AS unique_session_id,
           will_buy_on_return_visit,
           
           # 2. lengkapi code berikut ini dengan ketentuan ubahlah type datanya menjadi integer dan hilangkan komentar pada code tersebut.
           /*
           MAX(__(h.eCommerceAction.action_type AS ___)) AS latest_ecommerce_progress,
           */
   
           # perilaku pengguna di situs web
           IFNULL(totals.bounces, 0) AS bounces,
           IFNULL(totals.timeOnSite, 0) AS time_on_site,
           totals.pageviews,
   
           # informasi dari mana pengunjung itu berasal
           trafficSource.source,
           trafficSource.medium,
           channelGrouping,
   
           # informasi tentang device yang digunakan user
           device.deviceCategory,
   
           # informasi tentang geografi user
           IFNULL(geoNetwork.country, "Unknown") AS country
   
       FROM `data-to-insights.ecommerce.web_analytics`,
         UNNEST(hits) AS h
   
         JOIN all_visitor_stats USING(fullvisitorid)
   
       WHERE
         totals.newVisits = 1
         # 3. Gunakan data dari tanggal '20160801' hingga '20170531'
         /*
         isi code anda disini
         */
   
       GROUP BY
       unique_session_id,
       will_buy_on_return_visit,
       bounces,
       time_on_site,
       totals.pageviews,
       trafficSource.source,
       trafficSource.medium,
       channelGrouping,
       device.deviceCategory,
       country
     )
     ```
---

## Problem

Tim Anda sedang melakukan analisis terhadap data dari Google Analytics yang berisi informasi tentang perilaku pengguna dari sebuah website e-commerce. Anda diminta untuk melakukan analisis dan membuat model Machine Learning untuk memprediksi apakah pengguna baru kemungkinan akan melakukan pembelian dimasa mendatang atau tidak. Hasil prediksi tersebut nantinya dapat membantu tim marketing untuk memberikan promosi dan penawaran produk khususnya bagi user yang berpotensi melakukan pembelian.

### Lakukan pada bagian Exploratory Data Analysis

**Gunakan file `dataset_2.csv`** yang Anda dapatkan dari bagian query yang Anda lakukan sebelumnya dan jawablah beberapa soal dibawah ini : 

1. Apakah fitur `bounces`, `time_on_site`, dan `pageviews` memiliki pengaruh yang cukup tinggi untuk memprediksi target `will_buy_on_return_visit`? *(Gunakan Python untuk menjawab pertanyaan ini)*

2. Apa jenis device yang paling sering digunakan oleh user di wilayah `Canada` yang berpotensi melakukan pembelian saat mengunjungi kembali website tersebut ? *(Gunakan Python untuk menjawab pertanyaan ini)*

### Lakukan pada Model Training dan Model Evaluation

1. Buatlah model Machine Learning menggunakan `dataset_1.csv` dengan ketentuan :
   - Gunakan semua fitur pada dataset ini. Anda tidak perlu melakukan Feature Selection.
   - Untuk Feature Engineering yang lain, silakan Anda lakukan.
   - Algoritma yang akan Anda gunakan adalah Logistic Regression.
   - Pada saat training (melakukan `.fit()`), Anda diwajibkan menggunakan Pipeline.

2. Lakukan evaluasi dengan beberapa metrics dan buatlah sebuah Python Function untuk pengecekan `roc_auc_score` dengan kondisi seperti berikut :
   - **Good**: Jika `roc_auc_score` lebih besar dari 0.9.
   - **Fair**: Jika `roc_auc_score` kurang dari sama dengan 0.9 dan lebih besar dari sama dengan 0.8. 
   - **Decent**: Jika `roc_auc_score` kurang dari 0.8 dan lebih besar sama dengan dari 0.7.
   - **Not Great**: Jika `roc_auc_score` kurang dari 0.7 dan lebih besar dari sama dengan 0.6.
   - **Poor**: Jika `roc_auc_score` kurang dari 0.6.

3. Ternyata hasil dari model Machine Learning yang Anda buat kurang memuaskan sehingga Anda diminta oleh tim Anda untuk membuat model yang baru dengan tambahan fitur yang lain. Anda dapat gunakan `dataset_2.csv` pada hal ini.

4. Lakukan pembuatan model Machine Learning menggunakan `dataset_2.csv` dengan ketentuan :
   - Anda diwajibkan melakukan Feature Selection dalam hal ini.
   - Feature Engineering yang lain tetap harus Anda lakukan.
   - Algoritma yang akan Anda gunakan adalah Logistic Regression.
   - Pada saat training (melakukan `.fit()`), Anda diwajibkan menggunakan Pipeline.

5. Lakukan evaluasi pada model tersebut. **Berikan penjelasan apakah model tersebut lebih bagus setelah penambahan fitur ?**

6. Jelaskan apakah model tersebut overfit, good-fit atau underfit.

7. Apakah `roc_auc_score` merupakan metrik terbaik untuk evaluasi model tersebut atau adakah metrik lain yang cocok ?

8. Lakukanlah Hyperparameter Tuning dengan fitur yang telah Anda seleksi dan evaluasi hasilnya. Apakah model anda lebih baik dari model sebelumnnya ?

9. Buatlah Model Inference dari model yang terbaik dan dengan data berikut:
   ```python
   data={ 
          'latest_ecommerce_progress': [5,4], 
          'bounces': [0,0], 
          'time_on_site': [2489, 436], 
          'pageviews': [30, 50], 
          'source': ['google','google'],
          'medium': ['organic', 'referral'],
          'channelGrouping': ['Organic Search','Organic Search'],
          'deviceCategory': ['desktop', 'desktop'],
          'country': ['Canada',np.nan]
          }
   ```
    Silakan cek kesesuaian data diatas dengan column name datasetnya.
---

## Assignment Instructions

_Graded Challenge 5_ dikerjakan dalam format _notebook_ dengan beberapa **kriteria wajib** di bawah ini:

1. Machine learning framework yang digunakan adalah _Scikit-Learn_.

2. Terdapat penggunaan library visualisasi, seperti _matplotlib_, _seaborn_, atau yang lain.

3. Isi _notebook_ harus mengikuti _outline_ di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas kalian.

   2. Query SQL
      > Tulis query yang telah dibuat untuk membuat dataset dari Google Cloud Platform di bagian ini.

   3. Pendahuluan
      > Pendahuluan harus diisi dengan Latar belakang masalah, objective atau tujuan proyek, serta anda juga dapat menambahkan pertanyaan penelitian yang berisi pertanyaan yang akan ditelusuri atau di jawab pada saat melakukan analisis. 

   4. Import Libraries
      > _Cell_ pertama pada _notebook_ **harus berisi dan hanya berisi** semua _library_ yang digunakan dalam _project_.

   5. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.

   6. Exploratory Data Analysis (EDA)
      > Bagian ini berisi eksplorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya. Jangan lupa jelaskan kesimpulan EDA dan keputusan feature engineering apa yang akan lakukan.

   7. Modeling 1 - Dari dataset `dataset_1.csv`

      i. Feature Engineering
         > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

      ii. Model Definition
         > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

      iii. Model Training
         > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.

      iv. Model Evaluation
         > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   8. Modeling 2 - Dari dataset `dataset_2.csv`

      i. Feature Engineering
         > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

      ii. Model Definition
         > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

      iii. Model Training
         > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.

      iv. Model Evaluation
         > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   9. Model Saving
      > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model. **Dengan melihat hasil Model Evaluation, pilihlah satu model terbaik untuk disimpan. Model terbaik ini akan digunakan kembali dalam melakukan Model Inference.**
   
   10. Model Inference
       > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set ataupun test-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled. **Model Inference harus berada pada notebook yang berbeda dari notebook yang dipakai untuk pembuatan model.**

   11. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan _objective_ yang sudah ditulis di bagian pengenalan.

4. *Notebook* harus diupload dalam akun GitHub masing-masing student untuk selanjutnya dinilai.

---

## Assignment Submission

* Simpan assignment tugas Graded Challenge 5 ini dengan format penamaan file `P1G5_<nama_student>.ipynb`. Contoh : `P1G5_raka_ardhi.ipynb`.

* Push assignment yang telah Anda buat ke akun GitHub Classroom Anda masing-masing.

* Sebelum Anda submit, pastikan untuk melakukan running ulang code yang telah Anda buat. Hal ini bertujuan untuk memastikan tidak ada bagian code yang mengalami error.

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| SQL | Mampu melakukan query data dengan kriteria yang telah diberikan |
| Feature Engineering | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (split data, normalisasi, encoding, dll) |
| Logistic Regression | Mengimplementasikan Logistic Regression |
| Hyperparameter Tuning | Mengimplementasikan Hyperparameter Tuning dengan Scikit-Learn |
| Pipeline | Mampu membuat pipeline untuk menggabungkan beberapa langkah preprocessing|
| Model Inference | Mencoba model yang telah dibuat dengan data baru |
| Runs Perfectly | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
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

| Criteria | Meet Expectations | Points|
| --- | --- | --- |
| Model Analysis | Menganalisa informasi dari model yang telah dibuat |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan |

```
Contoh kriteria analisa yang baik diantaranya adalah: 

1. Terdapat penjelasan macam-macam hasil metric evaluasi dan interpretasinya terhadap kasus yang diselesaikan.
2. Dapat menjelaskan KELEBIHAN dan KELEMAHAN dari model yang dibuat DENGAN KAITANNYA DENGAN DOMAIN BUSINESS YANG DIHADAPI yang dibuktikan dengan eksplorasi sederhana (grafik, plot, teori, dll).
3. Dapat memberikan statement untuk improvement selanjutnya dari model yang dibuat. 
4. Dapat menyebutkan insight yang dapat diambil setelah proses EDA, dll.
```

---

## Notes

- **Deadline : pukul 18:00 WIB.**

- **Keterlambatan pengumpulan tugas mengakibatkan skor Graded Challenge 5 menjadi 0.**
