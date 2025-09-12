# Program Membalik Kalimat dan Menghitung Huruf Vokal

Program ini adalah aplikasi Python untuk membalik sebuah kalimat yang dimasukkan pengguna sekaligus menghitung jumlah huruf vokalnya.

## Fitur Program

1. **Input Kalimat**: Pengguna memasukkan sebuah kalimat
2. **Membalik Kalimat**: Program akan menampilkan kalimat dalam urutan terbalik
3. **Hitung Huruf Vokal**: Program menghitung jumlah huruf vokal (a, i, u, e, o)
4. **Tampilkan Hasil**: Program menampilkan kalimat asli, kalimat terbalik, dan jumlah vokal

## Prerequisites

- Python 3.x terinstal pada komputer Anda  
- Text editor atau IDE untuk menjalankan kode Python  

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**  
   - Simpan kode Python di atas dengan nama file `balik_vokal.py`

2. **Jalankan Program**  
   - Buka terminal atau command prompt  
   - Navigasi ke direktori tempat Anda menyimpan file  
   - Jalankan program dengan perintah:  
     ```
     python balik_vokal.py
     ```

3. **Masukkan Input**  
   - Masukkan kalimat yang ingin dibalik dan dihitung jumlah vokalnya  

4. **Lihat Hasil**  
   - Program akan menampilkan kalimat asli, kalimat terbalik, serta jumlah huruf vokal  

## Cara Kerja Program

1. **Input**: Kalimat dimasukkan oleh pengguna  
2. **Balik Kalimat**: Menggunakan slicing `[::-1]` untuk membalik string  
3. **Hitung Vokal**: Menghitung jumlah huruf vokal dengan iterasi per karakter  
4. **Output**: Menampilkan hasil ke layar  

## Penanganan Error

Program ini sederhana, namun sebaiknya:  
- Input harus berupa string (teks)  
- Jika input kosong, hasil tetap ditampilkan tetapi jumlah vokal = 0  
