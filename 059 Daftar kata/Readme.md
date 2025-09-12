# Program Daftar Kata dan Posisi dari Berkas

Program ini adalah aplikasi Python untuk menghasilkan daftar semua kata dari sebuah berkas teks, disertai dengan posisi urut kata tersebut dalam teks.

## Fitur Program

1. **Input File**: Pengguna memasukkan nama berkas teks input
2. **Ekstrak Kata**: Program memisahkan semua kata dari teks
3. **Nomor Urut**: Setiap kata diberi nomor urut sesuai posisinya dalam teks
4. **Output File**: Program menyimpan daftar kata dan posisi ke file baru

## Prerequisites

- Python 3.x terinstal pada komputer Anda  
- Text editor atau IDE untuk menjalankan kode Python  
- Berkas teks (`.txt`) yang akan diproses  

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**  
   - Simpan kode Python di atas dengan nama file `daftar_kata.py`

2. **Siapkan Berkas Input**  
   - Pastikan Anda memiliki file teks, misalnya `input.txt`

3. **Jalankan Program**  
   - Buka terminal atau command prompt  
   - Navigasi ke direktori tempat Anda menyimpan file  
   - Jalankan program dengan perintah:  
     ```
     python daftar_kata.py
     ```

4. **Masukkan Nama File**  
   - Masukkan nama file input, misalnya `input.txt`  
   - Masukkan nama file output, misalnya `output.txt`  

5. **Lihat Hasil**  
   - File hasil (`output.txt`) akan berisi daftar kata beserta nomor urutnya  

## Cara Kerja Program

1. **Baca File**: Membaca isi file teks input  
2. **Pisah Kata**: Memisahkan string menjadi list kata dengan `split()`  
3. **Nomori Kata**: Memberikan nomor urut mulai dari 1  
4. **Simpan File Baru**: Menyimpan daftar kata dan posisinya ke file output  
5. **Output**: Menampilkan pesan sukses  

## Penanganan Error

Program dilengkapi dengan penanganan sederhana untuk:  
- File input tidak ditemukan (`FileNotFoundError`)  
- Error saat membaca atau menulis file  
