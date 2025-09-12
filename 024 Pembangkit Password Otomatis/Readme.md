# Program Pembangkit Password Otomatis

Program ini adalah aplikasi Python untuk menghasilkan password acak yang aman dengan panjang yang dapat ditentukan oleh pengguna.

## Fitur Program

1. **Password Acak**: Menghasilkan password acak dengan karakter campuran
2. **Password Kuat**: Menghasilkan password yang dijamin mengandung huruf besar, huruf kecil, angka, dan simbol
3. **Penilaian Kekuatan**: Menganalisis dan menampilkan tingkat kekuatan password
4. **Tips Keamanan**: Menyediakan tips untuk membuat password yang aman

## Jenis Karakter yang Digunakan

- **Huruf Besar**: A-Z
- **Huruf Kecil**: a-z
- **Angka**: 0-9
- **Simbol**: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

## Prerequisites

- Python 3.x terinstal pada komputer Anda
- Modul `random` dan `string` (sudah termasuk dalam Python standard library)

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**
   - Salin kode program di atas dan simpan dengan nama file `password_generator.py`

2. **Jalankan Program**
   - Buka terminal atau command prompt
   - Navigasi ke direktori tempat Anda menyimpan file
   - Jalankan program dengan perintah:
     ```
     python password_generator.py
     ```

3. **Pilih Jenis Password**
   - Pilih 1 untuk Password Acak
   - Pilih 2 untuk Password Kuat (minimal 8 karakter)

4. **Masukkan Panjang Password**
   - Masukkan panjang password yang diinginkan
   - Untuk password kuat, minimal 8 karakter

5. **Lihat Hasil**
   - Program akan menampilkan password yang dihasilkan
   - Program akan menampilkan panjang dan kekuatan password
   - Program akan memberikan tips keamanan


## Kriteria Kekuatan Password

Program menilai kekuatan password berdasarkan:
- **Panjang**: Minimal 8 karakter
- **Huruf Besar**: Mengandung minimal 1 huruf besar
- **Huruf Kecil**: Mengandung minimal 1 huruf kecil
- **Angka**: Mengandung minimal 1 angka
- **Simbol**: Mengandung minimal 1 simbol

Tingkat kekuatan:
- **Lemah**: Memenuhi 0-2 kriteria
- **Sedang**: Memenuhi 3 kriteria
- **Kuat**: Memenuhi 4 kriteria
- **Sangat Kuat**: Memenuhi semua kriteria dengan panjang ≥ 12 karakter

## Keamanan Password

Program menggunakan modul `random` yang aman untuk kriptografi (cryptographically secure) untuk menghasilkan password yang benar-benar acak dan sulit ditebak.

## Penanganan Error

Program telah dilengkapi dengan penanganan error untuk:
- Input yang bukan angka
- Panjang password yang tidak valid
- Pilihan menu yang tidak valid

## Tips Password yang Aman

1. **Panjang**: Minimal 12 karakter
2. **Kompleksitas**: Kombinasi huruf besar, huruf kecil, angka, dan simbol
3. **Unik**: Jangan gunakan password yang sama untuk multiple akun
4. **Tidak Personal**: Hindari informasi pribadi seperti nama, tanggal lahir, dll.
5. **Password Manager**: Pertimbangkan menggunakan password manager untuk menyimpan password secara aman