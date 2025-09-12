# Program Translasi RNA ke Protein

Program ini adalah aplikasi Python untuk menerjemahkan urutan RNA menjadi protein (rantai polipeptida) berdasarkan aturan kodon.

## Fitur Program

1. **Input RNA**: Pengguna memasukkan urutan RNA berupa string huruf A, U, G, dan C
2. **Pisah Kodon**: RNA dibagi menjadi kodon (3 nukleotida per unit)
3. **Translasi**: Kodon diubah menjadi asam amino sesuai tabel kode genetik
4. **STOP Kodon**: Jika ditemukan UAA, UAG, atau UGA maka translasi dihentikan
5. **Tampilkan Hasil**: Menampilkan urutan protein hasil translasi

## Prerequisites

- Python 3.x terinstal pada komputer Anda
- Text editor atau IDE untuk menjalankan kode Python

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**
   - Simpan kode Python di atas dengan nama file `translasi_protein.py`

2. **Jalankan Program**
   - Buka terminal atau command prompt
   - Navigasi ke direktori tempat Anda menyimpan file
   - Jalankan program dengan perintah:
     ```
     python translasi_protein.py
     ```

3. **Masukkan Input**
   - Masukkan urutan RNA, misalnya `AUGUUUUCU`

4. **Lihat Hasil**
   - Program akan menampilkan hasil translasi berupa urutan protein

## Cara Kerja Program

1. **Input**: RNA string dari pengguna
2. **Looping Kodon**: Dibagi setiap 3 nukleotida
3. **Pemetaan Kodon**: Dicocokkan dengan tabel kode genetik
4. **STOP**: Translasi berhenti jika ditemukan kodon STOP
5. **Output**: Urutan protein ditampilkan ke layar

## Penanganan Error

Program dilengkapi dengan penanganan sederhana untuk:
- RNA dengan panjang tidak kelipatan 3 (kodon terakhir diabaikan)
- Kodon tidak dikenal (ditandai sebagai "Unknown")
