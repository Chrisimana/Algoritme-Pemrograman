# Program Menghitung Luas dan Keliling Bidang Datar

Program ini adalah aplikasi Python untuk menghitung luas dan keliling berbagai bidang datar dengan menu pilihan interaktif.

## Bidang Datar yang Didukung

1. **Persegi**
   - Luas = sisi × sisi
   - Keliling = 4 × sisi

2. **Persegi Panjang**
   - Luas = panjang × lebar
   - Keliling = 2 × (panjang + lebar)

3. **Segitiga**
   - **Segitiga Sembarang** (menggunakan rumus Heron)
     - Luas = √[s(s-a)(s-b)(s-c)] dimana s = (a+b+c)/2
     - Keliling = a + b + c
   - **Segitiga Siku-siku**
     - Luas = ½ × alas × tinggi
     - Keliling = alas + tinggi + sisi miring
     - Sisi miring = √(alas² + tinggi²)

## Prerequisites

- Python 3.x terinstal pada komputer Anda
- Text editor atau IDE untuk menjalankan kode Python

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**
   - Salin kode program di atas dan simpan dengan nama file `geometri.py`

2. **Jalankan Program**
   - Buka terminal atau command prompt
   - Navigasi ke direktori tempat Anda menyimpan file
   - Jalankan program dengan perintah:
     ```
     python geometri.py
     ```

3. **Pilih Menu**
   - Program akan menampilkan menu pilihan
   - Pilih bidang datar yang ingin dihitung (1-3)
   - Pilih 4 untuk keluar dari program

4. **Masukkan Data**
   - Ikuti instruksi untuk memasukkan data yang diperlukan
   - Untuk segitiga, pilih jenis segitiga terlebih dahulu

5. **Lihat Hasil**
   - Program akan menampilkan hasil perhitungan luas dan keliling
   - Tekan Enter untuk kembali ke menu utama


## Fitur Program

- **Menu Interaktif**: Program berjalan terus hingga pengguna memilih keluar
- **Validasi Input**: Memeriksa input yang tidak valid dan angka negatif
- **Multiple Shapes**: Mendukung tiga jenis bidang datar
- **Multiple Triangle Types**: Mendukung dua jenis segitiga
- **User-Friendly**: Interface yang mudah dipahami dengan instruksi jelas
- **Error Handling**: Penanganan error untuk input yang tidak sesuai

## Penanganan Error

Program telah dilengkapi dengan penanganan error untuk:
- Input yang bukan angka
- Input angka negatif atau nol
- Pilihan menu yang tidak valid