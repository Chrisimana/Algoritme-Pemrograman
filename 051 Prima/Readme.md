# Program Deteksi Bilangan Prima

Program ini adalah aplikasi Python untuk mengecek apakah sebuah bilangan bulat merupakan bilangan prima atau bukan.

## Fitur Program

1. **Input Angka**: Pengguna memasukkan sebuah bilangan bulat
2. **Deteksi Prima**: Program memeriksa apakah angka tersebut bilangan prima
3. **Tampilkan Hasil**: Menampilkan status prima atau bukan

## Prerequisites

- Python 3.x terinstal pada komputer Anda  
- Text editor atau IDE untuk menjalankan kode Python  

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**  
   - Simpan kode Python di atas dengan nama file `prima.py`

2. **Jalankan Program**  
   - Buka terminal atau command prompt  
   - Navigasi ke direktori tempat Anda menyimpan file  
   - Jalankan program dengan perintah:  
     ```
     python prima.py
     ```

3. **Masukkan Input**  
   - Masukkan sebuah bilangan bulat  

4. **Lihat Hasil**  
   - Program akan menampilkan apakah angka tersebut bilangan prima atau bukan  

## Cara Kerja Program

1. **Input**: Angka dimasukkan oleh pengguna  
2. **Validasi**: Jika angka ≤ 1 maka bukan prima  
3. **Pemeriksaan**:  
   - Jika angka = 2 maka prima  
   - Jika genap > 2 maka bukan prima  
   - Jika ganjil, diperiksa pembagi dari 3 sampai √n  
4. **Output**: Hasil ditampilkan ke layar  

## Penanganan Error

Program ini dilengkapi dengan penanganan sederhana untuk:  
- Input yang bukan bilangan bulat (ValueError)  
