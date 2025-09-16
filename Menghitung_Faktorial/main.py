def hitung_faktorial(n):
    """
    Fungsi untuk menghitung faktorial dan menghasilkan penjabaran proses.

    Parameters:
    n (int): Bilangan bulat positif

    Returns:
    tuple: (hasil_faktorial, string_penjabaran)
    """
    if n == 0 or n == 1:
        return 1, "1"

    hasil = 1
    penjabaran = []

    # Menghitung faktorial dan menyimpan prosesnya
    for i in range(n, 0, -1):
        hasil *= i
        penjabaran.append(str(i))

    # Membuat string penjabaran dengan format "n × (n-1) × ... × 1"
    penjabaran_str = " × ".join(penjabaran)

    return hasil, penjabaran_str


def main():
    """Fungsi utama program"""
    print("      PROGRAM MENGHITUNG FAKTORIAL")

    try:
        # Meminta input dari pengguna
        input_n = input("Masukkan bilangan bulat non-negatif: ")

        # Konversi input string ke integer
        n = int(input_n)

        # Validasi input tidak boleh negatif
        if n < 0:
            print("Error: Masukkan harus bilangan non-negatif!")
            return

        # Menghitung faktorial
        hasil, penjabaran = hitung_faktorial(n)

        # Menampilkan hasil dengan penjabaran
        print(f"\nHasil Perhitungan:")
        print(f"{n}! = {penjabaran} = {hasil}")

    except ValueError:
        # Menangani error jika input bukan bilangan bulat
        print("Error: Masukkan harus berupa bilangan bulat!")


# Menjalankan program utama
if __name__ == "__main__":
    main()
