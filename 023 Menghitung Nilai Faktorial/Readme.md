# Program Menghitung Nilai Faktorial

Program ini adalah aplikasi sederhana yang ditulis dalam bahasa Python untuk menghitung nilai faktorial dari sebuah bilangan bulat non-negatif dengan menampilkan penjabaran proses perhitungannya.

## Pengertian

Faktorial dari bilangan bulat non-negatif n adalah hasil perkalian semua bilangan bulat positif dari n down to 1. Faktorial ditulis dengan tanda seru (!).

**Rumus Faktorial:**
n! = n × (n-1) × (n-2) × ... × 1

**Khusus:**
0! = 1 (menurut konvensi matematika)

**Contoh:**
4! = 4 × 3 × 2 × 1 = 24
5! = 5 × 4 × 3 × 2 × 1 = 120

## Prerequisites

- Python 3.x terinstal pada komputer Anda
- Text editor atau IDE untuk menjalankan kode Python

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**
   - Salin kode program di atas dan simpan dengan nama file `faktorial.py`

2. **Jalankan Program**
   - Buka terminal atau command prompt
   - Navigasi ke direktori tempat Anda menyimpan file
   - Jalankan program dengan perintah:
     ```
     python faktorial.py
     ```

3. **Masukkan Input**
   - Program akan meminta Anda untuk memasukkan bilangan bulat non-negatif
   - Masukkan nilai bilangan yang ingin dihitung faktorialnya

4. **Lihat Hasil**
   - Program akan menampilkan penjabaran proses perhitungan
   - Program akan menampilkan hasil akhir faktorial


## Algoritma Program

1. **Input Validation**: Memastikan input adalah bilangan bulat non-negatif
2. **Special Case Handling**: Menangani kasus khusus 0! dan 1! yang hasilnya 1
3. **Factorial Calculation**: 
   - Menggunakan loop untuk menghitung hasil faktorial
   - Menyimpan proses perkalian untuk ditampilkan
4. **Output Formatting**: 
   - Membuat string penjabaran proses dengan format "n × (n-1) × ... × 1"
   - Menampilkan hasil akhir

## Penanganan Error

Program telah dilengkapi dengan penanganan error untuk:
- Input yang bukan bilangan bulat (ValueError)
- Input bilangan negatif

## Variasi Program

Program juga menyediakan versi alternatif dengan rekursi untuk menunjukkan cara berbeda dalam menyelesaikan masalah yang sama.

## Aplikasi Faktorial dalam Matematika

Faktorial digunakan dalam berbagai bidang matematika, terutama dalam:
- Kombinatorika dan teori probabilitas
- Ekspansi deret Taylor
- Fungsi gamma dalam matematika lanjut