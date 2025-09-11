# Program Mencetak Bilangan Ganjil dari N sampai 1

Program ini adalah aplikasi sederhana yang ditulis dalam bahasa Python untuk mencetak bilangan ganjil dari N sampai 1 berdasarkan input pengguna.

## Pengertian

Bilangan ganjil adalah bilangan bulat yang tidak habis dibagi 2. Program ini menerima input bilangan bulat N dari pengguna, kemudian mencetak semua bilangan ganjil dari N turun sampai 1.

**Contoh:**
- Input: 10 → Output: 9 7 5 3 1
- Input: 7 → Output: 7 5 3 1
- Input: 6 → Output: 5 3 1

## Prerequisites

- Python 3.x terinstal pada komputer Anda
- Text editor atau IDE untuk menjalankan kode Python

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**
   - Salin kode program di atas dan simpan dengan nama file `bilangan_ganjil.py`

2. **Jalankan Program**
   - Buka terminal atau command prompt
   - Navigasi ke direktori tempat Anda menyimpan file
   - Jalankan program dengan perintah:
     ```
     python bilangan_ganjil.py
     ```

3. **Masukkan Input**
   - Program akan meminta Anda untuk memasukkan bilangan bulat N
   - Masukkan nilai bilangan bulat positif

4. **Lihat Hasil**
   - Program akan menampilkan deretan bilangan ganjil dari N sampai 1


## Algoritma Program

1. **Input Validation**: Memastikan input adalah bilangan bulat positif
2. **Determine Starting Point**: 
   - Jika N ganjil, mulai dari N
   - Jika N genap, mulai dari N-1
3. **Loop**: 
   - Menggunakan for loop dengan step -2 untuk mencetak bilangan ganjil
   - Atau menggunakan while loop dengan decrement 2

## Penanganan Error

Program telah dilengkapi dengan penanganan error untuk:
- Input yang bukan bilangan bulat (ValueError)
- Input bilangan negatif atau nol

## Variasi Program

Program juga menyediakan versi alternatif dengan while loop untuk menunjukkan cara berbeda dalam menyelesaikan masalah yang sama.