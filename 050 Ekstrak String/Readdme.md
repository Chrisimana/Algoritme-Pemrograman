# Program Ekstrak String menjadi Huruf, Angka, dan Simbol

Program ini adalah aplikasi Python untuk mengekstrak string menjadi tiga bagian yaitu huruf, angka, dan simbol.

## Fitur Program

1. **Input String**: Pengguna memasukkan string campuran
2. **Pisah Elemen**: Program memisahkan huruf, angka, dan simbol
3. **Konversi Angka**: Angka yang terpisah digabungkan lalu dikonversi ke integer
4. **Tampilkan Hasil**: Program menampilkan hasil ekstraksi dalam bentuk list `[huruf, angka, simbol]`

## Prerequisites

- Python 3.x terinstal pada komputer Anda  
- Text editor atau IDE untuk menjalankan kode Python  

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**  
   - Simpan kode Python di atas dengan nama file `ekstrak_string.py`

2. **Jalankan Program**  
   - Buka terminal atau command prompt  
   - Navigasi ke direktori tempat Anda menyimpan file  
   - Jalankan program dengan perintah:  
     ```
     python ekstrak_string.py
     ```

3. **Masukkan Input**  
   - Masukkan string campuran, misalnya `ab13@**5df#`

4. **Lihat Hasil**  
   - Program akan menampilkan list hasil ekstraksi, misalnya `["abdf", 135, "@**#"]`

## Cara Kerja Program

1. **Iterasi String**: Program memeriksa setiap karakter dalam string
2. **Klasifikasi**: 
   - Jika huruf → masuk ke variabel huruf
   - Jika angka → masuk ke variabel angka
   - Jika simbol → masuk ke variabel simbol
3. **Gabungkan Angka**: Semua digit digabung jadi integer
4. **Output**: Tampilkan list `[huruf, angka, simbol]`

## Penanganan Error

Program ini sederhana, namun sebaiknya:  
- Jika tidak ada angka, nilai default angka adalah `0`  
- Input bisa berupa kombinasi huruf, angka, dan simbol apa pun  
