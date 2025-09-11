def cetak_bilangan_ganjil(n):
    """
    Fungsi untuk mencetak bilangan ganjil dari N sampai 1.

    Parameters:
    n (int): Bilangan bulat masukkan pengguna
    """
    print(f"Bilangan ganjil dari {n} sampai 1:")

    # Jika n genap, mulai dari n-1
    # Jika n ganjil, mulai dari n
    start = n if n % 2 == 1 else n - 1

    # Cetak bilangan ganjil dari start sampai 1 dengan step -2
    for i in range(start, 0, -2):
        print(i, end=" ")

    # Tambahkan newline di akhir
    print()


def main():
    """Fungsi utama program"""
    print("  PROGRAM MENCETAK BILANGAN GANJIL")

    try:
        # Meminta input dari pengguna
        input_n = input("Masukkan bilangan bulat N: ")

        # Konversi input string ke integer
        n = int(input_n)

        # Validasi input harus positif
        if n <= 0:
            print("Error: Masukkan harus bilangan bulat positif!")
            return

        # Memanggil fungsi untuk mencetak bilangan ganjil
        cetak_bilangan_ganjil(n)

    except ValueError:
        # Menangani error jika input bukan bilangan bulat
        print("Error: Masukkan harus berupa bilangan bulat!")


# Menjalankan program utama
if __name__ == "__main__":
    main()