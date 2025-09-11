# Program Menghitung Akar-Akar Persamaan Kuadrat

Program ini adalah aplikasi sederhana yang ditulis dalam bahasa Python untuk menghitung akar-akar persamaan kuadrat menggunakan rumus diskriminan.

## Pengertian

Persamaan kuadrat adalah persamaan polinomial berderajat dua dengan bentuk umum:

**ax² + bx + c = 0**

Dimana:
- a, b, dan c adalah koefisien dengan a ≠ 0
- x adalah variabel yang nilainya dicari

Untuk menyelesaikan persamaan kuadrat, digunakan rumus diskriminan:

**D = b² - 4ac**

Nilai diskriminan (D) menentukan jenis akar-akar persamaan:
1. **D < 0**: Akar-akar imaginer (tidak real)
2. **D = 0**: Akar kembar (satu akar real)
3. **D > 0**: Dua akar real berbeda

Rumus untuk menghitung akar-akar persamaan kuadrat:
- **x₁ = (-b + √D) / (2a)**
- **x₂ = (-b - √D) / (2a)**

## Prerequisites

- Python 3.x terinstal pada komputer Anda
- Text editor atau IDE untuk menjalankan kode Python

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**
   - Salin kode program di atas dan simpan dengan nama file `akar_kuadrat.py`

2. **Jalankan Program**
   - Buka terminal atau command prompt
   - Navigasi ke direktori tempat Anda menyimpan file
   - Jalankan program dengan perintah:
     ```
     python akar_kuadrat.py
     ```

3. **Masukkan Input**
   - Program akan meminta Anda untuk memasukkan nilai koefisien a, b, dan c
   - Masukkan nilai numerik untuk masing-masing koefisien
   - Pastikan nilai a tidak nol (a ≠ 0)

4. **Lihat Hasil**
   - Program akan menampilkan jenis akar dan nilai akar-akar persamaan
   - Hasil akan ditampilkan dengan dua angka di belakang koma


## Penanganan Error

Program telah dilengkapi dengan penanganan error untuk:
- Input yang bukan angka (ValueError)
- Nilai a = 0 (bukan persamaan kuadrat)
- Pembagian dengan nol (ZeroDivisionError)


