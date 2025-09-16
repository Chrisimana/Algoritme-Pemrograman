# Rumus: ax² + bx + c = 0
# D = b² - 4ac

import math  # Import modul math untuk fungsi sqrt


def hitung_akar_persamaan_kuadrat(a, b, c):
    """
    Fungsi untuk menghitung akar-akar persamaan kuadrat.

    Parameters:
    a (float): Koefisien x²
    b (float): Koefisien x
    c (float): Konstanta

    Returns:
    tuple: Jenis akar dan nilai akar-akar
    """
    # Menghitung diskriminan
    D = b ** 2 - 4 * a * c

    # Menentukan jenis akar berdasarkan nilai diskriminan
    if D < 0:
        # Akar imaginer
        return "imaginer", None, None
    elif D == 0:
        # Akar kembar
        x = -b / (2 * a)
        return "kembar", x, x
    else:
        # Dua akar real berbeda
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return "real berbeda", x1, x2


def main():
    """Fungsi utama program"""
    print("  PROGRAM MENGHITUNG AKAR PERSAMAAN KUADRAT")

    print("Format persamaan: ax² + bx + c = 0")

    try:
        # Meminta input dari pengguna
        a = float(input("Masukkan nilai a (koefisien x²): "))
        b = float(input("Masukkan nilai b (koefisien x): "))
        c = float(input("Masukkan nilai c (konstanta): "))

        # Validasi nilai a tidak boleh 0
        if a == 0:
            print("Error: Nilai a tidak boleh 0 (bukan persamaan kuadrat)!")
            return

        # Menghitung akar-akar persamaan kuadrat
        jenis_akar, x1, x2 = hitung_akar_persamaan_kuadrat(a, b, c)

        # Menampilkan hasil perhitungan
        print("\nHasil Perhitungan:")
        print(f"Persamaan: {a}x² + {b}x + {c} = 0")
        print(f"Diskriminan (D) = {b ** 2 - 4 * a * c}")

        if jenis_akar == "imaginer":
            print("Akar-akar persamaan adalah imaginer (tidak real)")
        elif jenis_akar == "kembar":
            print(f"Akar kembar: x₁ = x₂ = {x1:.2f}")
        else:
            print(f"Akar pertama: x₁ = {x1:.2f}")
            print(f"Akar kedua: x₂ = {x2:.2f}")

    except ValueError:
        # Menangani error jika input bukan angka
        print("Error: Masukkan harus berupa angka!")
    except ZeroDivisionError:
        # Menangani error pembagian dengan nol
        print("Error: Terjadi pembagian dengan nol!")


# Menjalankan program utama
if __name__ == "__main__":
    main()
