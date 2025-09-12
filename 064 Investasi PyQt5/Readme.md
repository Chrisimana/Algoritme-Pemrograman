# Program Penghitung Investasi dengan Bunga Tahunan (PyQt5)

Program ini adalah aplikasi GUI sederhana menggunakan PyQt5 untuk menghitung nilai akhir investasi dengan bunga tahunan.

## Fitur Program

1. **Input Modal Awal**: Pengguna memasukkan modal awal
2. **Input Bunga Tahunan**: Bunga dalam persen per tahun
3. **Input Lama Investasi**: Jumlah tahun investasi
4. **Hitung Nilai Akhir**: Program menghitung nilai akhir dengan rumus bunga majemuk
5. **Tampilkan Hasil**: Hasil akhir ditampilkan dalam format rupiah

## Prerequisites

- Python 3.x  
- Modul **PyQt5** (install dengan `pip install pyqt5`)

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**  
   - Simpan kode Python dengan nama file `investasi.py`

2. **Jalankan Program**  
   - Buka terminal atau command prompt  
   - Jalankan dengan perintah:  
     ```
     python investasi.py
     ```

3. **Masukkan Data**  
   - Modal awal (contoh: `1000000`)  
   - Bunga per tahun dalam persen (contoh: `5`)  
   - Lama investasi dalam tahun (contoh: `10`)  

4. **Lihat Hasil**  
   - Program akan menampilkan nilai akhir investasi setelah periode tertentu  

## Cara Kerja Program

1. **Input**: Modal, bunga tahunan, dan lama investasi  
2. **Perhitungan**: Menggunakan rumus bunga majemuk. 
3. **Output**: Menampilkan jumlah akhir investasi  

## Penanganan Error

Program dilengkapi dengan penanganan sederhana untuk:  
- Input yang bukan angka  
- Input kosong  
