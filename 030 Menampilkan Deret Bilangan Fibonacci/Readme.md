# Program Menampilkan Deret Bilangan Fibonacci

Program ini adalah aplikasi sederhana yang ditulis dalam bahasa Python untuk menampilkan deret bilangan Fibonacci sampai suku ke-N berdasarkan inputan pengguna.

## Pengertian

Deret Fibonacci adalah deret bilangan dimana setiap suku adalah jumlah dari dua suku sebelumnya.

**Rumus Deret Fibonacci:**
F₁ = 1
F₂ = 1
Fₙ = Fₙ₋₁ + Fₙ₋₂ untuk n > 2

**Contoh:**
- N = 1: 1
- N = 2: 1, 1
- N = 3: 1, 1, 2
- N = 4: 1, 1, 2, 3
- N = 5: 1, 1, 2, 3, 5
- N = 6: 1, 1, 2, 3, 5, 8
- N = 7: 1, 1, 2, 3, 5, 8, 13

## Prerequisites

- Python 3.x terinstal pada komputer Anda
- Text editor atau IDE untuk menjalankan kode Python

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**
   - Salin kode program di atas dan simpan dengan nama file `fibonacci.py`

2. **Jalankan Program**
   - Buka terminal atau command prompt
   - Navigasi ke direktori tempat Anda menyimpan file
   - Jalankan program dengan perintah:
     ```
     python fibonacci.py
     ```

3. **Masukkan Input**
   - Program akan meminta Anda untuk memasukkan bilangan bulat positif N
   - Masukkan nilai N (jumlah suku Fibonacci yang ingin ditampilkan)

4. **Lihat Hasil**
   - Program akan menampilkan deret Fibonacci sampai suku ke-N
   - Output akan diformat dengan koma sebagai pemisah dan tanpa koma di akhir

## Algoritma Program

1. **Input Validation**: Memastikan input adalah bilangan bulat positif
2. **Special Case Handling**: Menangani kasus khusus N = 0, N = 1, dan N = 2
3. **Fibonacci Calculation**: 
   - Menggunakan loop untuk menghitung suku-suku Fibonacci
   - Menyimpan setiap suku dalam list
4. **Output Formatting**: 
   - Mengonversi list bilangan menjadi string dengan koma sebagai pemisah
   - Memastikan tidak ada koma di akhir deret

## Penanganan Error

Program telah dilengkapi dengan penanganan error untuk:
- Input yang bukan bilangan bulat (ValueError)
- Input bilangan negatif atau nol