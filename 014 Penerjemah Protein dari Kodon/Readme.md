# Program Penerjemah Protein dari Kodon

Program ini adalah aplikasi sederhana yang ditulis dalam bahasa Python untuk menerjemahkan kodon RNA menjadi nama protein yang sesuai.

## Pengertian

Dalam biologi molekuler, kodon adalah urutan tiga nukleotida pada RNA yang mengkode untuk asam amino tertentu atau sinyal stop selama sintesis protein. Program ini menerjemahkan kodon RNA menjadi nama protein yang sesuai berdasarkan kode genetik standar.

## Tabel Translasi Kodon-Protein

| Kodon       | Protein         |
|-------------|-----------------|
| AUG         | Methionine      |
| UUU, UUC    | Phenylalanine   |
| UUA, UUG    | Leucine         |
| UCU, UCC, UCA, UCG | Serine |
| UAU, UAC    | Tyrosine        |
| UGU, UGC    | Cysteine        |
| UGG         | Tryptophan      |

## Prerequisites

- Python 3.x terinstal pada komputer Anda
- Text editor atau IDE untuk menjalankan kode Python

## Langkah-Langkah Menggunakan Program

1. **Simpan Kode Program**
   - Salin kode program di atas dan simpan dengan nama file `penerjemah_protein.py`

2. **Jalankan Program**
   - Buka terminal atau command prompt
   - Navigasi ke direktori tempat Anda menyimpan file
   - Jalankan program dengan perintah:
     ```
     python penerjemah_protein.py
     ```

3. **Masukkan Input**
   - Program akan menampilkan daftar kodon yang dikenali
   - Program akan meminta Anda untuk memasukkan kodon RNA (3 huruf)
   - Masukkan kodon yang ingin diterjemahkan

4. **Lihat Hasil**
   - Program akan menampilkan hasil terjemahan berupa nama protein
   - Jika kodon tidak dikenali, program akan memberikan pesan error


## Fitur Program

- **Case Insensitive**: Program dapat menerima input dalam huruf besar atau kecil
- **Validasi Input**: Memeriksa apakah input terdiri dari 3 huruf
- **Error Handling**: Memberikan pesan yang jelas untuk kodon yang tidak dikenali
- **User Friendly**: Menampilkan daftar kodon yang dikenali sebelum meminta input

## Penanganan Error

Program telah dilengkapi dengan penanganan error untuk:
- Input yang panjangnya bukan 3 karakter
- Kodon yang tidak terdapat dalam tabel translasi


