# Program Konversi Berkas Teks Tanpa Baris Baru

Program ini adalah aplikasi Python untuk mengonversi isi berkas teks sehingga tidak memiliki baris baru (`\n`). Semua baris digabungkan menjadi satu string panjang.

## Fitur Program

1. **Input File**: Pengguna memasukkan nama berkas teks input
2. **Hapus Newline**: Program menghapus semua karakter newline dan menggantinya dengan spasi
3. **Output File**: Program menyimpan hasil konversi ke file baru
4. **Tampilkan Status**: Program memberi tahu apakah proses berhasil atau gagal

## Prerequisites

- Python 3.x terinstal pada komputer Anda  
- Text editor atau IDE untuk menjalankan kode Python  
- Berkas teks (`.txt`) yang akan dikonversi  

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**  
   - Simpan kode Python di atas dengan nama file `hapus_newline.py`

2. **Siapkan Berkas Input**  
   - Pastikan Anda memiliki file teks, misalnya `input.txt`

3. **Jalankan Program**  
   - Buka terminal atau command prompt  
   - Navigasi ke direktori tempat Anda menyimpan file  
   - Jalankan program dengan perintah:  
     ```
     python hapus_newline.py
     ```

4. **Masukkan Nama File**  
   - Masukkan nama file input, misalnya `input.txt`  
   - Masukkan nama file output, misalnya `output.txt`  

5. **Lihat Hasil**  
   - File hasil (`output.txt`) akan berisi teks dari `input.txt` tanpa baris baru  

## Cara Kerja Program

1. **Baca File**: Membaca isi file teks input  
2. **Hapus Newline**: Semua `\n` diganti dengan spasi  
3. **Simpan File Baru**: Menyimpan hasil ke file output  
4. **Output**: Menampilkan pesan sukses  

## Penanganan Error

Program dilengkapi dengan penanganan sederhana untuk:  
- File input tidak ditemukan (`FileNotFoundError`)  
- Error saat membaca atau menulis file  
