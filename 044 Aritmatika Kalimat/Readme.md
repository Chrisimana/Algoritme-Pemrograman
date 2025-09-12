# Program Evaluasi Aritmatika dari Kalimat

Program ini adalah aplikasi Python untuk mengevaluasi operasi aritmatika sederhana berdasarkan kalimat yang dimasukkan pengguna. Program akan terus berjalan sampai pengguna mengetikkan "selesai".

## Fitur Program

1. **Input Kalimat**: Pengguna memasukkan kalimat aritmatika seperti "Berapa 5 ditambah 10 ?"
2. **Parsing Kalimat**: Program mengenali operasi (tambah, kurang, kali, bagi) dari kata kunci
3. **Evaluasi Operasi**: Program menghitung hasil sesuai angka dan operator
4. **Hentikan Program**: Jika pengguna mengetik "selesai", program berhenti

## Prerequisites

- Python 3.x terinstal pada komputer Anda  
- Text editor atau IDE untuk menjalankan kode Python  

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**  
   - Simpan kode Python di atas dengan nama file `aritmatika_kalimat.py`

2. **Jalankan Program**  
   - Buka terminal atau command prompt  
   - Navigasi ke direktori tempat Anda menyimpan file  
   - Jalankan program dengan perintah:  
     ```
     python aritmatika_kalimat.py
     ```

3. **Masukkan Input**  
   - Contoh:  
     - `Berapa 5 ditambah 10 ?`  
     - `Berapa 10 dibagi 2 ?`  
     - `Berapa 5 dikurangi dengan -5 ?`  
     - `Berapa 2 dikali 10 ?`  

4. **Lihat Hasil**  
   - Program akan menampilkan hasil perhitungan  
   - Jika mengetik `selesai`, program akan berhenti  

## Cara Kerja Program

1. **Input**: Kalimat dari pengguna  
2. **Deteksi Operasi**: Cari kata kunci (`ditambah`, `dikurangi`, `dikali`, `dibagi`)  
3. **Ambil Angka**: Ekstrak angka dari kalimat  
4. **Hitung**: Evaluasi operasi aritmatika  
5. **Output**: Tampilkan hasil ke layar  

## Penanganan Error

Program ini dilengkapi dengan penanganan sederhana untuk:  
- Pembagian dengan nol  
- Kalimat dengan format yang tidak dikenali  
