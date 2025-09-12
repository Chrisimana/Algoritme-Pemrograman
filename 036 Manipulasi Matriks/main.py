def buat_matriks(baris, kolom):

    return [[0 for _ in range(kolom)] for _ in range(baris)]


def tampilkan_matriks(matriks, nama="Matriks"):

    print(f"\n{nama}:")
    if not matriks:
        print("Matriks kosong")
        return

    for i, baris in enumerate(matriks):
        # Format setiap baris dengan spasi yang konsisten
        baris_str = " | ".join(f"{elem:>6}" for elem in baris)
        print(f"Baris {i + 1}: [ {baris_str} ]")


def ubah_nilai_matriks(matriks):

    if not matriks:
        print("Matriks belum dibuat!")
        return

    try:
        # Meminta input posisi dan nilai baru
        baris = int(input("Masukkan nomor baris: ")) - 1
        kolom = int(input("Masukkan nomor kolom: ")) - 1
        nilai_baru = int(input("Masukkan nilai baru: "))

        # Validasi indeks
        if 0 <= baris < len(matriks) and 0 <= kolom < len(matriks[0]):
            nilai_lama = matriks[baris][kolom]
            matriks[baris][kolom] = nilai_baru
            print(f"Nilai berhasil diubah dari {nilai_lama} menjadi {nilai_baru}")
        else:
            print("Error: Posisi baris/kolom tidak valid!")

    except ValueError:
        print("Error: Masukkan harus berupa bilangan bulat!")


def tambah_matriks(matriks_a, matriks_b):

    if not matriks_a or not matriks_b:
        print("Kedua matriks harus sudah dibuat!")
        return None

    if len(matriks_a) != len(matriks_b) or len(matriks_a[0]) != len(matriks_b[0]):
        print("Error: Ukuran matriks tidak sama!")
        return None

    hasil = buat_matriks(len(matriks_a), len(matriks_a[0]))
    for i in range(len(matriks_a)):
        for j in range(len(matriks_a[0])):
            hasil[i][j] = matriks_a[i][j] + matriks_b[i][j]

    return hasil


def tampilkan_menu():

    print("\n" + "=" * 50)
    print("PROGRAM MANIPULASI MATRIKS")
    print("=" * 50)
    print("1. Buat Matriks Baru")
    print("2. Tampilkan Matriks")
    print("3. Ubah Nilai Matriks")
    print("4. Tambah Dua Matriks")
    print("5. Keluar")
    print("=" * 50)


def main():

    # Inisialisasi variabel matriks
    matriks_a = []
    matriks_b = []
    matriks_hasil = []

    print("Selamat datang di Program Manipulasi Matriks!")

    # Loop utama program
    while True:
        tampilkan_menu()

        try:
            pilihan = int(input("Masukkan pilihan (1-5): "))

            if pilihan == 1:
                # Membuat matriks baru
                try:
                    baris = int(input("Masukkan jumlah baris: "))
                    kolom = int(input("Masukkan jumlah kolom: "))

                    if baris <= 0 or kolom <= 0:
                        print("Error: Jumlah baris dan kolom harus positif!")
                        continue

                    # Pilih matriks yang akan dibuat
                    print("Pilih matriks:")
                    print("1. Matriks A")
                    print("2. Matriks B")
                    pilih_matriks = int(input("Masukkan pilihan (1/2): "))

                    if pilih_matriks == 1:
                        matriks_a = buat_matriks(baris, kolom)
                        print("Matriks A berhasil dibuat!")
                    elif pilih_matriks == 2:
                        matriks_b = buat_matriks(baris, kolom)
                        print("Matriks B berhasil dibuat!")
                    else:
                        print("Error: Pilihan tidak valid!")

                except ValueError:
                    print("Error: Masukkan harus berupa bilangan bulat!")

            elif pilihan == 2:
                # Menampilkan matriks
                print("\nMatriks yang tersedia:")
                print("1. Matriks A")
                print("2. Matriks B")
                print("3. Matriks Hasil")

                try:
                    pilih_tampil = int(input("Pilih matriks yang akan ditampilkan (1-3): "))

                    if pilih_tampil == 1:
                        tampilkan_matriks(matriks_a, "Matriks A")
                    elif pilih_tampil == 2:
                        tampilkan_matriks(matriks_b, "Matriks B")
                    elif pilih_tampil == 3:
                        tampilkan_matriks(matriks_hasil, "Matriks Hasil")
                    else:
                        print("Error: Pilihan tidak valid!")

                except ValueError:
                    print("Error: Masukkan harus berupa bilangan bulat!")

            elif pilihan == 3:
                # Mengubah nilai matriks
                print("\nPilih matriks yang akan diubah:")
                print("1. Matriks A")
                print("2. Matriks B")

                try:
                    pilih_ubah = int(input("Masukkan pilihan (1/2): "))

                    if pilih_ubah == 1:
                        tampilkan_matriks(matriks_a, "Matriks A (Sebelum)")
                        ubah_nilai_matriks(matriks_a)
                        tampilkan_matriks(matriks_a, "Matriks A (Sesudah)")
                    elif pilih_ubah == 2:
                        tampilkan_matriks(matriks_b, "Matriks B (Sebelum)")
                        ubah_nilai_matriks(matriks_b)
                        tampilkan_matriks(matriks_b, "Matriks B (Sesudah)")
                    else:
                        print("Error: Pilihan tidak valid!")

                except ValueError:
                    print("Error: Masukkan harus berupa bilangan bulat!")

            elif pilihan == 4:
                # Menambah dua matriks
                tampilkan_matriks(matriks_a, "Matriks A")
                tampilkan_matriks(matriks_b, "Matriks B")

                matriks_hasil = tambah_matriks(matriks_a, matriks_b)
                if matriks_hasil:
                    tampilkan_matriks(matriks_hasil, "Hasil Penjumlahan (A + B)")

            elif pilihan == 5:
                # Keluar dari program
                print("Terima kasih telah menggunakan program!")
                break

            else:
                print("Error: Pilihan harus antara 1-5!")

        except ValueError:
            print("Error: Masukkan harus berupa angka!")

        # Jeda sebelum menampilkan menu kembali
        input("\nTekan Enter untuk melanjutkan...")


# Menjalankan program utama
if __name__ == "__main__":
    main()