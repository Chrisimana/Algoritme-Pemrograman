# Program Verifikasi ISBN-10

Program ini adalah aplikasi Python untuk memverifikasi kode ISBN-10 berdasarkan aturan standar internasional.

## Fitur Program

1. **Input ISBN-10**: Pengguna memasukkan kode ISBN-10 (boleh menggunakan tanda `-`)
2. **Pembersihan Input**: Tanda `-` dihapus agar hanya tersisa digit dan/atau huruf `X`
3. **Validasi**: Program menghitung validitas ISBN-10 dengan rumus
4. **Tampilkan Hasil**: Menampilkan apakah ISBN-10 valid atau tidak

## Prerequisites

- Python 3.x terinstal pada komputer Anda  
- Text editor atau IDE untuk menjalankan kode Python  

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**  
- Simpan kode Python di atas dengan nama file `isbn10.py`

2. **Jalankan Program**  
- Buka terminal atau command prompt  
- Navigasi ke direktori tempat Anda menyimpan file  
- Jalankan program dengan perintah:  
  ```
  python isbn10.py
  ```

3. **Masukkan Input**  
- Masukkan kode ISBN-10, misalnya `3-598-21508-8`

4. **Lihat Hasil**  
- Program akan menampilkan apakah ISBN-10 tersebut valid atau tidak

## Cara Kerja Program

1. **Input**: ISBN-10 dimasukkan sebagai string  
2. **Normalisasi**: Tanda `-` dihapus, panjang kode harus 10 karakter  
3. **Hitung Nilai**: Setiap digit dikalikan dengan bobot (10 hingga 1)  
4. **Khusus X**: Karakter `X` di akhir berarti angka 10  
5. **Output**: Jika total mod 11 = 0, ISBN-10 valid  

## Penanganan Error

Program ini dilengkapi dengan penanganan sederhana untuk:  
- Panjang ISBN tidak 10 digit  
- Karakter yang bukan angka atau `X`  
- `X` tidak berada di posisi terakhir  
