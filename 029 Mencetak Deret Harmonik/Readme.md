# Program Mencetak Deret Harmonik

Program ini adalah aplikasi sederhana yang ditulis dalam bahasa Python untuk mencetak dan menghitung deret harmonik berdasarkan inputan pengguna.

## Pengertian

Deret harmonik adalah deret tak hingga yang didefinisikan sebagai jumlah dari reciprocals (kebalikan) dari bilangan bulat positif.

**Rumus Deret Harmonik:**
Hₙ = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

**Contoh:**
- N = 1: 1 = 1.0
- N = 2: 1 + 1/2 = 1.5
- N = 3: 1 + 1/2 + 1/3 ≈ 1.833333333
- N = 4: 1 + 1/2 + 1/3 + 1/4 ≈ 2.083333333
- N = 5: 1 + 1/2 + 1/3 + 1/4 + 1/5 ≈ 2.283333333

## Prerequisites

- Python 3.x terinstal pada komputer Anda
- Text editor atau IDE untuk menjalankan kode Python

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**
   - Salin kode program di atas dan simpan dengan nama file `deret_harmonik.py`

2. **Jalankan Program**
   - Buka terminal atau command prompt
   - Navigasi ke direktori tempat Anda menyimpan file
   - Jalankan program dengan perintah:
     ```
     python deret_harmonik.py
     ```

3. **Masukkan Input**
   - Program akan meminta Anda untuk memasukkan bilangan bulat positif N
   - Masukkan nilai N yang ingin dihitung deret harmoniknya

4. **Lihat Hasil**
   - Program akan menampilkan penjabaran proses perhitungan
   - Program akan menampilkan hasil akhir deret harmonik dengan 9 angka desimal

## Algoritma Program

1. **Input Validation**: Memastikan input adalah bilangan bulat positif
2. **Harmonic Series Calculation**: 
   - Menggunakan loop untuk menghitung jumlah deret harmonik
   - Menyimpan proses penjumlahan untuk ditampilkan
3. **Output Formatting**: 
   - Membuat string penjabaran proses dengan format "1 + (1/2) + (1/3) + ... + (1/N)"
   - Menampilkan hasil akhir dengan presisi 9 angka desimal

## Penanganan Error

Program telah dilengkapi dengan penanganan error untuk:
- Input yang bukan bilangan bulat (ValueError)
- Input bilangan negatif atau nol
- Pembagian dengan nol (ZeroDivisionError)