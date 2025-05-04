# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut, sebagai institusi pendidikan yang telah beroperasi sejak tahun 2000 dan memiliki reputasi baik, menghadapi tantangan serius terkait tingginya tingkat siswa yang dropout (berhenti kuliah sebelum lulus). Meskipun banyak lulusan sukses yang dihasilkan, angka putus studi menjadi indikator negatif yang berdampak pada kualitas, citra, dan keberlanjutan institusi dalam jangka panjang.

### Permasalahan Bisnis

1. **Tingginya Tingkat Dropout Mahasiswa**.
Tingkat mahasiswa yang keluar sebelum menyelesaikan studi menunjukkan angka yang mengkhawatirkan, yang dapat berdampak negatif pada reputasi institusi, menurunkan akreditasi, serta mengurangi pendapatan dari biaya pendidikan.
2. **Kurangnya Pemahaman Terhadap Faktor Penyebab Dropout**.
Pihak institusi belum memiliki analisis komprehensif mengenai faktor-faktor utama yang menyebabkan mahasiswa berhenti kuliah, seperti latar belakang ekonomi, performa akademik, kondisi sosial, atau motivasi pribadi.
3. **Ketidakmampuan dalam Memprediksi Mahasiswa yang Berisiko Dropout**.
Tidak adanya sistem atau alat bantu berbasis data untuk memantau dan mengidentifikasi mahasiswa yang berisiko tinggi dropout membuat intervensi pencegahan sulit dilakukan secara tepat waktu dan tepat sasaran.
4. **Kesulitan Menyusun Strategi Intervensi dan Bimbingan yang Efektif**.
Tanpa pemetaan yang jelas terhadap profil risiko mahasiswa, institusi kesulitan dalam merancang program pendampingan, bimbingan akademik, atau dukungan psikologis yang tepat untuk menekan angka dropout.

### Cakupan Proyek

- Mengolah dan menganalisis dataset mahasiswa dari Jaya Jaya Institut.
- Melakukan eksplorasi data untuk menemukan pola spesifik dalam dropout berdasarkan kategori demografis, status keuangan, dan performa akademik.
- Pembuatan Business Dashboard yang mencakup : 
  - Tingkat dropout keseluruhan dan per program studi
  - Distribusi mahasiswa berdasarkan usia, status pernikahan, dan status beasiswa
  - Trend dropout berdasarkan usia
- Pemberian Rekomendasi Bisnis untuk strategi pencegahan dropout berdasarkan temuan data.

### Persiapan

Sumber data: [Student Performance Data](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

#### Setup environment

```
# 1. Salin Repository dari GitHub
git clone https://github.com/fabasassa-lab/HR_Analysis.git

# 2. Pindah ke Folder Proyek
cd nama-repository
```

```
conda create -n env-attrition python=3.10
conda activate env-attrition
pip install pandas numpy matplotlib seaborn scikit_learn tensorflow joblib streamlit xgboost
conda deactivate
```

## Business Dashboard

Link HR Analysis Tableau Public Dashboard : [HR Analysis Dashboard](https://public.tableau.com/app/profile/fauzihan.bagus/viz/HRAnalysis_17457576868510/HRANALYTICSDASHBOARD)

Dashboard ini menyajikan berbagai visualisasi analitik yang komprehensif terkait Human Resources (HR) Analytics, meliputi data mengenai attrition rate, distribusi karyawan berdasarkan departemen, rentang usia, jenis kelamin, latar belakang pendidikan, serta tingkat kepuasan kerja.
Dashboard ini berfungsi sebagai alat strategis untuk memberikan insight berbasis data kepada manajemen dalam memahami dinamika tenaga kerja di organisasi secara lebih mendalam.

Dengan pemetaan visual yang sistematis, manajemen dapat dengan cepat mengidentifikasi area kritis dengan tingkat turnover tinggi, menganalisis faktor penyebab, serta merancang program intervensi yang lebih efektif dan terfokus untuk meningkatkan retensi, kepuasan, dan keterlibatan karyawan.
Penggunaan dashboard ini memperkuat komitmen perusahaan terhadap pengelolaan sumber daya manusia berbasis data (data-driven HR management), sekaligus mendukung pengambilan keputusan yang lebih cepat, akurat, dan strategis guna menghadapi tantangan tenaga kerja yang semakin dinamis.

![HR Dashboard](good_sawo-dashboard.png)

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```
# Clone the repository
git clone <repository-url>

# Install necessary packages
pip install numpy pandas xgboost sqlalchemy scikit-learn joblib streamlit

# Run the Streamlit app
streamlit run app.py
```

Link Student Performance Prediction (Streamlit) : [Streamlit App](https://studentperformanceanalysis-n5yfnn72v5g4ukudrcsgem.streamlit.app/)

## Conclusion

Berdasarkan analisis data dalam dashboard, ditemukan insight berikut:

1. **Departemen R&D memiliki tingkat attrition tertinggi sebesar 56,12%**.
Hal ini menunjukkan adanya tantangan signifikan dalam mempertahankan karyawan di R&D, kemungkinan disebabkan oleh tekanan target penjualan yang tinggi, persaingan industri yang ketat, atau kurangnya jalur pengembangan karir yang jelas.
2. **Karyawan berusia 25–34 tahun menjadi kelompok dengan tingkat attrition tertinggi sebesar 47%**.
Kelompok usia ini biasanya terdiri dari profesional muda yang aktif mencari peluang pertumbuhan karir, kompensasi lebih baik, atau keseimbangan kehidupan kerja yang lebih ideal.
3. **Gender juga menjadi faktor penting, dengan karyawan laki-laki menyumbang attrition lebih tinggi dibanding perempuan**.
Hal ini bisa mengindikasikan adanya perbedaan kebutuhan, kepuasan kerja, atau peluang karir antara gender yang perlu ditangani secara lebih spesifik.
4. **Kepuasan kerja berpengaruh besar terhadap tingkat attrition**.
Job role seperti Sales Executive dan Laboratory Technician memperlihatkan tingkat kepuasan yang rendah, sedangkan Research Scientist relatif lebih puas. Hal ini mengisyaratkan perlunya perbaikan manajemen beban kerja, reward system, dan peluang pengembangan di role yang lebih rentan terhadap ketidakpuasan.
5. **Bidang pendidikan Life Sciences paling terdampak attrition**.
Ini menandakan adanya ketidakcocokan antara ekspektasi lulusan bidang ini dengan realita pekerjaan yang ditawarkan perusahaan, atau kurangnya jalur pengembangan karir yang sesuai.

### Rekomendasi Action Items

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Buat program pengembangan karir, mentoring, dan keseimbangan kerja-hidup (work-life balance) yang lebih menarik untuk usia **25-34**.
- Desain program onboarding yang lebih ramah bagi generasi muda dan program pensiun bertahap (phased retirement) untuk karyawan senior.
- Buat program peningkatan kepuasan kerja seperti pelatihan tambahan, perbaikan beban kerja, atau reward system yang lebih baik di role **Sales Executive** dan **Laboratory Technician**.
- Evaluasi kembali kebijakan rekrutmen, program onboarding, dan program retention untuk latar belakang pendidikan **Life Sciences** dan **Medical**.
- Teliti lebih lanjut penyebab spesifik mengapa banyak karyawan pria keluar, misal terkait beban kerja, peluang promosi, atau fleksibilitas kerja.
