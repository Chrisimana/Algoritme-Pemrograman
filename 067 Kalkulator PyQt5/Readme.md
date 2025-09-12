# Kalkulator Sederhana dengan PyQt5

Program ini adalah aplikasi GUI sederhana menggunakan PyQt5 untuk melakukan operasi aritmatika dasar.

## Fitur Program

1. **Input Ekspresi**: Pengguna memasukkan ekspresi aritmatika
2. **Operasi Didukung**: 
   - Penjumlahan (+)  
   - Pengurangan (-)  
   - Perkalian (*)  
   - Pembagian (/)  
   - Pangkat (^)  
   - Modulus (%)  
3. **Hitung**: Klik tombol "Hitung" untuk mendapatkan hasil
4. **Clear**: Klik tombol "Clear" untuk menghapus input dan hasil
5. **Tampilkan Hasil**: Menampilkan hasil perhitungan ke layar

## Prerequisites

- Python 3.x  
- Modul **PyQt5** (install dengan `pip install pyqt5`)

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**  
   - Simpan kode Python di atas dengan nama file `kalkulator.py`

2. **Jalankan Program**  
   - Buka terminal atau command prompt  
   - Jalankan dengan perintah:  
     ```
     python kalkulator.py
     ```

3. **Masukkan Ekspresi**  
   - Contoh:  
     - `5+10`  
     - `8-3`  
     - `4*6`  
     - `20/5`  
     - `2^3`  
     - `10%3`  

4. **Lihat Hasil**  
   - Hasil perhitungan ditampilkan di bagian bawah jendela

## Cara Kerja Program

1. **Input**: Ekspresi string dari pengguna  
2. **Parsing**: Simbol `^` diubah menjadi `**` agar sesuai dengan Python  
3. **Evaluasi**: Menggunakan fungsi `eval()` untuk menghitung ekspresi  
4. **Output**: Hasil ditampilkan ke layar  

## Penanganan Error

Program dilengkapi dengan penanganan sederhana untuk:  
- Pembagian dengan nol  
- Ekspresi tidak valid  
