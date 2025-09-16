def hitung_deret_harmonik(n):
    """
    Fungsi untuk menghitung deret harmonik dan membuat string penjabaran.

    Parameters:
    n (int): Bilangan bulat positif

    Returns:
    tuple: (hasil_deret, string_penjabaran)
    """
    if n <= 0:
        return 0, ""

    hasil = 0.0
    penjabaran = []

    # Menghitung deret harmonik dan menyimpan prosesnya
    for i in range(1, n + 1):
        hasil += 1 / i
        if i == 1:
            penjabaran.append("1")
        else:
            penjabaran.append(f"(1/{i})")

    # Membuat string penjabaran dengan format "1 + (1/2) + (1/3) + ... + (1/N)"
    penjabaran_str = " + ".join(penjabaran)

    return hasil, penjabaran_str


def main():
    """Fungsi utama program"""
    print("      PROGRAM DERET HARMONIK")

    try:
        # Meminta input dari pengguna
        input_n = input("Masukkan bilangan bulat positif N: ")

        # Konversi input string ke integer
        n = int(input_n)

        # Validasi input harus positif
        if n <= 0:
            print("Error: Masukkan harus bilangan bulat positif!")
            return

        # Menghitung deret harmonik
        hasil, penjabaran = hitung_deret_harmonik(n)

        # Menampilkan hasil dengan penjabaran
        print(f"\nHasil Perhitungan:")
        print(f"{penjabaran} = {hasil:.9f}")

    except ValueError:
        # Menangani error jika input bukan bilangan bulat
        print("Error: Masukkan harus berupa bilangan bulat!")
    except ZeroDivisionError:
        # Menangani error pembagian dengan nol
        print("Error: Terjadi pembagian dengan nol!")


# Menjalankan program utama
if __name__ == "__main__":
    main()
