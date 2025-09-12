# Program Menghitung Cicilan Rumah

Program ini adalah aplikasi sederhana yang ditulis dalam bahasa Python untuk menghitung cicilan rumah per tahun berdasarkan harga asal, harga jual, dan lama waktu cicilan dengan skema 20, 15, 10, dan 5 tahun.

## Pengertian

Cicilan rumah adalah pembagian harga rumah yang dijual ke klien ke dalam jangka waktu tertentu (tahun). Dengan program ini, pengguna dapat menghitung besar cicilan per tahun serta melihat selisih harga rumah asal dengan harga jual.

**Rumus Perhitungan:**
- Selisih Harga = Harga Jual – Harga Asal  
- Cicilan per Tahun = Harga Jual ÷ Lama Cicilan

**Contoh:**
- Harga Asal = Rp300.000.000  
- Harga Jual = Rp400.000.000  
- Lama Cicilan = 20 tahun  

Maka:  
Selisih Harga = Rp100.000.000  
Cicilan per Tahun = Rp20.000.000  

## Prerequisites

- Python 3.x terinstal pada komputer Anda
- Text editor atau IDE untuk menjalankan kode Python

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**
   - Simpan kode Python di atas dengan nama `cicilan.py`

2. **Jalankan Program**
   - Buka terminal atau command prompt
   - Navigasi ke direktori tempat Anda menyimpan file
   - Jalankan program dengan perintah:
     ```
     python cicilan.py
     ```

3. **Masukkan Input**
   - Harga rumah asal
   - Harga rumah yang dijual ke klien
   - Lama cicilan (20, 15, 10, atau 5 tahun)

4. **Lihat Hasil**
   - Program akan menampilkan selisih harga
   - Program akan menampilkan cicilan rumah per tahun

## Algoritma Program

1. **Input Data**: Harga rumah asal, harga jual, lama cicilan  
2. **Validasi Input**: Lama cicilan hanya bisa 20, 15, 10, atau 5  
3. **Hitung Selisih Harga**: Harga Jual – Harga Asal  
4. **Hitung Cicilan**: Harga Jual ÷ Lama Cicilan  
5. **Output**: Menampilkan hasil perhitungan ke layar  

## Penanganan Error

Program dilengkapi dengan penanganan error untuk:  
- Input bukan angka (ValueError)  
- Skema cicilan yang tidak valid (selain 20, 15, 10, 5)  
