# Program Mencari Huruf Kapital Pertama dengan Rekursi

Program ini adalah aplikasi Python untuk mencari huruf kapital pertama pada sebuah string menggunakan fungsi rekursif.

## Fitur Program

1. **Input String**: Pengguna memasukkan sebuah string
2. **Deteksi Huruf Kapital**: Program memeriksa huruf kapital dari kiri ke kanan
3. **Menggunakan Rekursi**: Fungsi dipanggil berulang hingga menemukan huruf kapital pertama
4. **Tampilkan Hasil**: Program menampilkan huruf kapital pertama yang ditemukan, atau pesan jika tidak ada

## Prerequisites

- Python 3.x terinstal pada komputer Anda  
- Text editor atau IDE untuk menjalankan kode Python  

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**  
   - Simpan kode Python di atas dengan nama file `kapital_pertama.py`

2. **Jalankan Program**  
   - Buka terminal atau command prompt  
   - Navigasi ke direktori tempat Anda menyimpan file  
   - Jalankan program dengan perintah:  
     ```
     python kapital_pertama.py
     ```

3. **Masukkan Input**  
   - Masukkan sebuah string, misalnya `instiTut`

4. **Lihat Hasil**  
   - Program akan menampilkan huruf kapital pertama yang ditemukan, misalnya `T`

## Cara Kerja Program

1. **Input**: String dimasukkan oleh pengguna  
2. **Fungsi Rekursif**: 
   - Basis: jika indeks `i` melebihi panjang string, kembalikan `None`  
   - Jika karakter pada indeks `i` adalah kapital, kembalikan karakter tersebut  
   - Jika tidak, lanjutkan memanggil fungsi dengan `i+1`  
3. **Output**: Huruf kapital pertama atau pesan jika tidak ada huruf kapital  

## Penanganan Error

Program ini sederhana dan tidak memerlukan validasi khusus, namun sebaiknya input berupa string.  
