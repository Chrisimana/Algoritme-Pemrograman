import math  # Import modul math untuk fungsi sqrt


def hitung_persegi():
    """
    Fungsi untuk menghitung luas dan keliling persegi.
    """
    print("\n--- PERSEGI ---")
    try:
        sisi = float(input("Masukkan panjang sisi: "))
        if sisi <= 0:
            print("Error: Panjang sisi harus positif!")
            return

        luas = sisi * sisi
        keliling = 4 * sisi

        print(f"Luas persegi: {luas:.2f}")
        print(f"Keliling persegi: {keliling:.2f}")

    except ValueError:
        print("Error: Masukkan harus berupa angka!")


def hitung_persegi_panjang():
    """
    Fungsi untuk menghitung luas dan keliling persegi panjang.
    """
    print("\n--- PERSEGI PANJANG ---")
    try:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))

        if panjang <= 0 or lebar <= 0:
            print("Error: Panjang dan lebar harus positif!")
            return

        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)

        print(f"Luas persegi panjang: {luas:.2f}")
        print(f"Keliling persegi panjang: {keliling:.2f}")

    except ValueError:
        print("Error: Masukkan harus berupa angka!")


def hitung_segitiga():
    """
    Fungsi untuk menghitung luas dan keliling segitiga.
    """
    print("\n--- SEGITIGA ---")
    print("Pilih jenis segitiga:")
    print("1. Segitiga Sembarang")
    print("2. Segitiga Siku-siku")

    try:
        pilihan = int(input("Masukkan pilihan (1/2): "))

        if pilihan == 1:
            # Segitiga sembarang
            a = float(input("Masukkan panjang sisi a: "))
            b = float(input("Masukkan panjang sisi b: "))
            c = float(input("Masukkan panjang sisi c: "))

            if a <= 0 or b <= 0 or c <= 0:
                print("Error: Panjang sisi harus positif!")
                return

            # Hitung keliling
            keliling = a + b + c

            # Hitung luas menggunakan rumus Heron
            s = keliling / 2  # semi-perimeter
            luas = math.sqrt(s * (s - a) * (s - b) * (s - c))

            print(f"Luas segitiga: {luas:.2f}")
            print(f"Keliling segitiga: {keliling:.2f}")

        elif pilihan == 2:
            # Segitiga siku-siku
            alas = float(input("Masukkan panjang alas: "))
            tinggi = float(input("Masukkan panjang tinggi: "))

            if alas <= 0 or tinggi <= 0:
                print("Error: Alas dan tinggi harus positif!")
                return

            # Hitung sisi miring
            sisi_miring = math.sqrt(alas ** 2 + tinggi ** 2)

            # Hitung luas dan keliling
            luas = 0.5 * alas * tinggi
            keliling = alas + tinggi + sisi_miring

            print(f"Luas segitiga: {luas:.2f}")
            print(f"Keliling segitiga: {keliling:.2f}")
            print(f"Sisi miring: {sisi_miring:.2f}")

        else:
            print("Error: Pilihan tidak valid!")

    except ValueError:
        print("Error: Masukkan harus berupa angka!")


def tampilkan_menu():
    """
    Fungsi untuk menampilkan menu pilihan.
    """
    print("\n" + "=" * 50)
    print("PROGRAM MENGHITUNG LUAS DAN KELILING")
    print("=" * 50)
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Keluar")
    print("=" * 50)


def main():
    """
    Fungsi utama program.
    """
    print("Selamat datang di Program Geometri!")

    # Loop utama program
    while True:
        tampilkan_menu()

        try:
            pilihan = int(input("Masukkan pilihan (1-4): "))

            if pilihan == 1:
                hitung_persegi()
            elif pilihan == 2:
                hitung_persegi_panjang()
            elif pilihan == 3:
                hitung_segitiga()
            elif pilihan == 4:
                print("Terima kasih telah menggunakan program!")
                break
            else:
                print("Error: Pilihan harus antara 1-4!")

        except ValueError:
            print("Error: Masukkan harus berupa angka!")

        # Jeda sebelum menampilkan menu kembali
        input("\nTekan Enter untuk melanjutkan...")


# Menjalankan program utama
if __name__ == "__main__":
    main()
