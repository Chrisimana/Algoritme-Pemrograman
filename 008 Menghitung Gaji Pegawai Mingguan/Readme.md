# Program Menghitung Gaji Pegawai Mingguan

Program ini adalah aplikasi sederhana yang ditulis dalam bahasa Python untuk menghitung gaji pegawai dalam satu minggu berdasarkan upah per jam.

## Pengertian

Program ini menghitung total gaji yang diterima pegawai dalam satu minggu dengan asumsi:
- Satu hari kerja adalah 8 jam
- Lima hari kerja dalam seminggu (Senin sampai Jumat)
- Total jam kerja per minggu adalah 40 jam

Rumus untuk menghitung gaji mingguan adalah:

**Gaji Mingguan = Upah per Jam × 8 jam/hari × 5 hari/minggu**

## Prerequisites

- Python 3.x terinstal pada komputer Anda
- Text editor atau IDE untuk menjalankan kode Python

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**
   - Salin kode program di atas dan simpan dengan nama file `hitung_gaji.py`

2. **Jalankan Program**
   - Buka terminal atau command prompt
   - Navigasi ke direktori tempat Anda menyimpan file
   - Jalankan program dengan perintah:
     ```
     python hitung_gaji.py
     ```

3. **Masukkan Input**
   - Program akan meminta Anda untuk memasukkan upah pegawai per jam
   - Masukkan nilai upah per jam dalam bentuk angka

4. **Lihat Hasil**
   - Program akan menampilkan rincian perhitungan dan total gaji mingguan
   - Hasil akan ditampilkan dalam format mata uang Rupiah


## Asumsi Program

- Jam kerja per hari: 8 jam
- Hari kerja per minggu: 5 hari (Senin-Jumat)
- Tidak termasuk lembur atau potongan lainnya
- Perhitungan hanya berdasarkan upah pokok per jam

## Penanganan Error

Program telah dilengkapi dengan penanganan error untuk:
- Input yang bukan angka (akan menampilkan pesan error)
- Input angka negatif atau nol (akan menampilkan pesan error)

## Kontribusi

Jika Anda ingin berkontribusi atau melaporkan bug, silakan buka issue di repository GitHub atau hubungi developer.
