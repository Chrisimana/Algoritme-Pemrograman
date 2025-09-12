# Program Perkalian Matriks

Program ini adalah aplikasi Python untuk melakukan perkalian dua matriks dengan ukuran yang sesuai.

## Fitur Program

1. **Input Matriks A**: Memasukkan ukuran dan elemen-elemen matriks A
2. **Input Matriks B**: Memasukkan ukuran dan elemen-elemen matriks B
3. **Perkalian Matriks**: Mengalikan matriks A dan B jika jumlah kolom A = jumlah baris B
4. **Tampilkan Hasil**: Menampilkan hasil perkalian dalam format matriks

## Prerequisites

- Python 3.x terinstal pada komputer Anda
- Text editor atau IDE untuk menjalankan kode Python

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**
   - Simpan kode Python di atas dengan nama file `perkalian_matriks.py`

2. **Jalankan Program**
   - Buka terminal atau command prompt
   - Navigasi ke direktori tempat Anda menyimpan file
   - Jalankan program dengan perintah:
     ```
     python perkalian_matriks.py
     ```

3. **Masukkan Input**
   - Tentukan ukuran matriks A (baris dan kolom) serta elemen-elemennya
   - Tentukan ukuran matriks B (baris dan kolom) serta elemen-elemennya

4. **Lihat Hasil**
   - Program akan menampilkan hasil perkalian matriks A x B jika ukurannya sesuai

## Cara Kerja Program

1. **Input**: Pengguna memasukkan dua buah matriks dengan ukuran masing-masing
2. **Validasi Ukuran**: Program memeriksa apakah kolom A = baris B
3. **Perhitungan**: Menggunakan nested loop untuk menghitung perkalian
4. **Output**: Menampilkan hasil dalam bentuk matriks

## Penanganan Error

Program dilengkapi dengan penanganan error untuk:
- Input yang bukan angka
- Jumlah elemen tidak sesuai dengan ukuran baris/kolom
- Ukuran matriks yang tidak sesuai untuk perkalian
