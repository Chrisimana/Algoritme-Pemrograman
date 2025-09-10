# Program Menghitung Luas Permukaan Tabung

Program ini adalah aplikasi sederhana yang ditulis dalam bahasa Python untuk menghitung luas permukaan tabung berdasarkan jari-jari dan tinggi yang dimasukkan oleh pengguna.

## Konsep yang Dipelajari

### 1. Variabel
Variabel digunakan untuk menyimpan data dalam program. Contoh dalam kode:
- `input_jari_jari` = menyimpan input jari-jari sebagai string
- `jari_jari` = menyimpan nilai jari-jari yang sudah dikonversi ke float
- `PI` = menyimpan nilai konstanta π
- `luas_permukaan` = menyimpan hasil perhitungan

### 2. Konsol I/O (Input/Output)
- **Input**: Menggunakan fungsi `input()` untuk menerima masukan dari pengguna
- **Output**: Menggunakan fungsi `print()` untuk menampilkan hasil ke konsol

### 3. Konversi Tipe Data
- Input dari pengguna selalu berupa string
- Menggunakan `float()` untuk mengkonversi string menjadi bilangan desimal
- Menggunakan `round()` untuk membulatkan hasil perhitungan

## Rumus Luas Permukaan Tabung

Luas permukaan tabung dihitung dengan rumus:

**Luas Permukaan Tabung = 2 × π × r × (r + t)**

Dimana:
- π (pi) ≈ 3.14159
- r = jari-jari alas tabung
- t = tinggi tabung

## Langkah-Langkah Menggunakan Program

1. **Jalankan Program**
   - Simpan kode sebagai `luas_tabung.py`
   - Buka terminal/command prompt
   - Jalankan dengan: `python luas_tabung.py`

2. **Masukkan Data**
   - Program akan meminta input jari-jari tabung
   - Program akan meminta input tinggi tabung
   - Masukkan nilai numerik positif

3. **Lihat Hasil**
   - Program akan menampilkan hasil perhitungan
   - Nilai ditampilkan dengan 2 angka di belakang koma


## Penanganan Error

Program telah dilengkapi dengan penanganan error untuk:
- Input yang bukan angka (ValueError)
- Input angka negatif atau nol

## Kontribusi

Program ini cocok untuk pemula yang ingin belajar tentang:
- Variabel dan tipe data dalam Python
- Input/output di konsol
- Konversi tipe data
- Penanganan error dasar