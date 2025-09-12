# Program Tabel Data Barang dengan PyQt5

Program ini adalah aplikasi GUI sederhana menggunakan PyQt5 untuk menambahkan data barang beserta harganya ke dalam sebuah tabel.

## Fitur Program

1. **Input Data**: Masukkan nama barang dan harga barang
2. **Tambah ke Tabel**: Klik tombol "Tambah" untuk menambahkan data ke tabel
3. **Tabel Dinamis**: Tabel akan menampilkan daftar barang beserta harga

## Prerequisites

- Python 3.x  
- Modul **PyQt5** (install dengan `pip install pyqt5`)

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**  
   - Simpan kode Python dengan nama file `tabel_barang.py`

2. **Jalankan Program**  
   - Buka terminal atau command prompt  
   - Jalankan dengan perintah:  
     ```
     python tabel_barang.py
     ```

3. **Masukkan Data**  
   - Masukkan nama barang dan harga pada input field  
   - Klik tombol "Tambah"

4. **Lihat Hasil**  
   - Data akan muncul di tabel dengan kolom "Nama Barang" dan "Harga"

## Cara Kerja Program

1. **GUI dengan PyQt5**: Membuat window utama dengan input field dan tabel  
2. **Tambah Data**: Event klik tombol memicu fungsi untuk menambahkan baris baru ke tabel  
3. **Reset Input**: Setelah data ditambahkan, input otomatis dikosongkan  
4. **Output**: Data ditampilkan dalam tabel interaktif  
