# Proyek Akhir: Student Dropout Prediction - Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah menghasilkan banyak lulusan berkualitas. Namun demikian, institusi ini menghadapi permasalahan yang cukup serius yaitu tingginya jumlah mahasiswa yang tidak menyelesaikan studinya atau mengalami **dropout**.

Tingkat dropout yang tinggi dapat berdampak pada reputasi institusi, efektivitas proses pendidikan, serta keberlanjutan akademik mahasiswa. Oleh karena itu, pihak institusi ingin mengidentifikasi faktor-faktor yang mempengaruhi kemungkinan mahasiswa mengalami dropout agar dapat melakukan intervensi lebih awal.

Melalui proyek ini dilakukan analisis data untuk memahami faktor-faktor yang berkaitan dengan dropout mahasiswa serta membangun model machine learning untuk memprediksi risiko dropout mahasiswa di masa depan.

---

# Permasalahan Bisnis

Beberapa permasalahan bisnis yang ingin dijawab dalam proyek ini antara lain:

1. Berapa persentase mahasiswa yang mengalami dropout di Jaya Jaya Institut?
2. Apakah kepemilikan beasiswa mempengaruhi kemungkinan mahasiswa untuk dropout?
3. Apakah nilai masuk mahasiswa berpengaruh terhadap keberhasilan akademik mereka?
4. Apakah performa akademik pada semester pertama berkaitan dengan kemungkinan mahasiswa dropout?
5. Apakah usia mahasiswa saat pendaftaran memiliki hubungan dengan status akademik mahasiswa?

Dengan menjawab pertanyaan tersebut, institusi diharapkan dapat mengidentifikasi mahasiswa yang berisiko dropout lebih awal.

---

# Cakupan Proyek

Proyek ini mencakup beberapa tahapan dalam proses data science sebagai berikut:

1. **Business Understanding**  
   Memahami permasalahan bisnis terkait tingginya tingkat dropout mahasiswa.

2. **Data Understanding**  
   Melakukan eksplorasi dataset untuk memahami struktur data dan karakteristik mahasiswa.

3. **Data Preparation**  
   Membersihkan data, menangani missing value, serta melakukan transformasi data yang diperlukan untuk analisis dan modeling.

4. **Exploratory Data Analysis (EDA)**  
   Mengidentifikasi hubungan antara berbagai faktor seperti performa akademik, beasiswa, nilai masuk, dan usia dengan status akademik mahasiswa.

5. **Modeling**  
   Mengembangkan model machine learning menggunakan algoritma **Random Forest** untuk memprediksi kemungkinan mahasiswa mengalami dropout.

6. **Evaluation**  
   Mengevaluasi performa model menggunakan metrik evaluasi seperti accuracy, precision, recall, dan F1-score.

7. **Business Dashboard**  
   Membuat dashboard analitik menggunakan **Metabase** untuk memvisualisasikan faktor-faktor yang berkaitan dengan dropout mahasiswa.

8. **Machine Learning Prototype**  
   Membangun prototype aplikasi prediksi menggunakan **Streamlit** agar pengguna dapat melakukan prediksi risiko dropout mahasiswa secara langsung.

---

# Persiapan

## Sumber Data

Dataset yang digunakan dalam proyek ini merupakan dataset performa akademik mahasiswa yang mencakup berbagai informasi seperti:

- status perkawinan
- jalur masuk
- program studi
- nilai masuk
- kepemilikan beasiswa
- usia saat pendaftaran
- performa akademik semester pertama dan kedua
- status akademik mahasiswa (Dropout, Enrolled, Graduate)

Dataset ini digunakan untuk menganalisis faktor-faktor yang mempengaruhi kemungkinan mahasiswa mengalami dropout.

---

# Setup Environment

## 1. Clone Repository

`git clone https://github.com/muhfauzan-chycn/student-dropout-prediction.git`

Masuk ke folder proyek:

`cd student-dropout-prediction`

---

## 2. Install Dependecies

Install semua library yang diperlukan:

`pip install -r requirement.txt`


---

## 3. Menjalankan Notebook Analisis

Untuk melihat proses analisis data dan modeling:

`jupyter notebook`

Kemudian buka file notebook:

`Proyek_Akhir_Jaya_Institut.ipynb`


---

## 4. Menjalankan Dashboard Metabase

Jalankan Metabase menggunakan Docker:

`docker run -d -p 3000:3000 --name metabase metabase/metabase`

Akses Metabase melalui browser:

`http://localhost:3000`


---

## 5. Menjalankan Dashboard Metabase dengan Database yang Disediakan

Jika ingin menggunakan dashboard yang sudah dibuat dalam proyek ini:

`docker stop metabase`
`docker rm metabase`

Kemudian jalankan kembali Metabase dengan database yang tersedia:

`docker run -d -p 3000:3000 -v "$(pwd)/metabase.db.mv.db:/metabase.db/metabase.db.mv.db" --name metabase metabase/metabase`

Setelah itu akses kembali:

`http://localhost:3000`


Dashboard akan otomatis muncul.

---

## 6. Menjalankan Prototype Machine Learning

Prototype aplikasi prediksi dropout dapat diakses melalui:

https://student-dropout-prediction-muhfauzan-chycn.streamlit.app/

Atau dijalankan secara lokal dengan perintah:

`streamlit run app.py`


---

# Business Dashboard

Dashboard dibuat menggunakan **Metabase** untuk membantu pihak institusi memahami kondisi akademik mahasiswa secara visual.

Dashboard menampilkan beberapa visualisasi utama, antara lain:

1. **Distribusi Status Akademik Mahasiswa**
2. **Status Mahasiswa Berdasarkan Kepemilikan Beasiswa**
3. **Nilai Masuk Mahasiswa Berdasarkan Status Akademik**
4. **Performa Akademik Semester Pertama Berdasarkan Status Mahasiswa**
5. **Usia Mahasiswa Saat Pendaftaran Berdasarkan Status Akademik**

Selain itu dashboard juga menampilkan beberapa **Key Performance Indicator (KPI)** seperti:

- Total Mahasiswa
- Jumlah Mahasiswa Dropout
- Persentase Mahasiswa Dropout

Dashboard ini membantu institusi dalam memahami kondisi akademik mahasiswa serta memonitor potensi risiko dropout.

---

# Conclusion

Berdasarkan hasil analisis data yang dilakukan terhadap dataset mahasiswa Jaya Jaya Institut, diperoleh beberapa temuan penting.

Sekitar **32% mahasiswa dalam dataset mengalami dropout**, yang menunjukkan bahwa tingkat dropout merupakan permasalahan yang cukup signifikan bagi institusi pendidikan.

Hasil analisis juga menunjukkan bahwa performa akademik pada semester pertama memiliki hubungan yang kuat dengan keberhasilan studi mahasiswa. Mahasiswa yang berhasil menyelesaikan lebih banyak mata kuliah pada semester pertama memiliki kemungkinan lebih tinggi untuk lulus.

Selain itu, faktor seperti nilai masuk mahasiswa dan kepemilikan beasiswa juga menunjukkan hubungan dengan status akademik mahasiswa.

Model machine learning yang dibangun menggunakan algoritma **Random Forest** mampu memprediksi kemungkinan mahasiswa mengalami dropout berdasarkan berbagai faktor akademik dan demografis.

---

# Rekomendasi Action Items

Berdasarkan hasil analisis yang telah dilakukan, beberapa rekomendasi yang dapat dipertimbangkan oleh Jaya Jaya Institut antara lain:

1. Mengidentifikasi mahasiswa dengan performa akademik rendah pada semester pertama untuk diberikan bimbingan akademik lebih awal.

2. Mengembangkan program pendampingan akademik bagi mahasiswa yang berisiko mengalami kesulitan dalam perkuliahan.

3. Mengevaluasi sistem beasiswa dan dukungan finansial untuk membantu mahasiswa mempertahankan keberlangsungan studi.

4. Menggunakan model machine learning sebagai sistem **early warning system** untuk mendeteksi mahasiswa yang berpotensi mengalami dropout.

5. Meningkatkan layanan konseling akademik dan mentoring bagi mahasiswa baru agar dapat beradaptasi dengan lingkungan perkuliahan.

Dengan menerapkan langkah-langkah tersebut, diharapkan institusi dapat menurunkan tingkat dropout serta meningkatkan keberhasilan studi mahasiswa.