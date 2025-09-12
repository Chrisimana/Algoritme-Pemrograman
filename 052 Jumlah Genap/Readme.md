# Program Jumlah Bilangan Genap dengan Rekursi

Program ini adalah aplikasi Python untuk menghitung jumlah bilangan genap dari rentang a sampai b menggunakan fungsi rekursif.

## Fitur Program

1. **Input Batas Rentang**: Pengguna memasukkan nilai a dan b
2. **Hitung Jumlah Genap**: Program menghitung jumlah bilangan genap dari a sampai b
3. **Menggunakan Rekursi**: Fungsi dipanggil berulang hingga mencapai kondisi basis
4. **Tampilkan Hasil**: Program menampilkan jumlah bilangan genap

## Prerequisites

- Python 3.x terinstal pada komputer Anda  
- Text editor atau IDE untuk menjalankan kode Python  

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**  
   - Simpan kode Python di atas dengan nama file `jumlah_genap.py`

2. **Jalankan Program**  
   - Buka terminal atau command prompt  
   - Navigasi ke direktori tempat Anda menyimpan file  
   - Jalankan program dengan perintah:  
     ```
     python jumlah_genap.py
     ```

3. **Masukkan Input**  
   - Masukkan nilai a dan b (contoh: a = 2, b = 8)

4. **Lihat Hasil**  
   - Program akan menampilkan jumlah bilangan genap dari a sampai b

## Cara Kerja Program

1. **Input**: Nilai a dan b dimasukkan oleh pengguna  
2. **Fungsi Rekursif**: 
   - Basis: jika a > b, fungsi mengembalikan 0  
   - Jika a genap, fungsi mengembalikan a + hasil rekursi berikutnya  
   - Jika a ganjil, fungsi memanggil dirinya lagi dengan a+1  
3. **Output**: Jumlah bilangan genap ditampilkan ke layar  

## Penanganan Error

Program ini dilengkapi dengan penanganan sederhana untuk:  
- Input yang bukan bilangan bulat (ValueError)  
