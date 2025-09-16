# Modul: Variabel, Konsol I/O, dan Konversi Tipe Data

# Import modul math untuk mendapatkan nilai π (pi)
import math

def main():
    """Fungsi utama program"""
    # Tampilkan header program
    print("PROGRAM LUAS PERMUKAAN TABUNG")

    # Input dari pengguna
    # Variabel untuk menyimpan input jari-jari
    input_jari_jari = input("Masukkan jari-jari tabung: ")

    # Variabel untuk menyimpan input tinggi
    input_tinggi = input("Masukkan tinggi tabung: ")

    try:
        # Konversi tipe data dari string ke float
        jari_jari = float(input_jari_jari)
        tinggi = float(input_tinggi)

        # Validasi input tidak boleh negatif atau nol
        if jari_jari <= 0 or tinggi <= 0:
            print("Error: Jari-jari dan tinggi harus bernilai positif!")
            return

        # Hitung luas permukaan tabung
        # Rumus: 2 * π * r * (r + t)
        PI = math.pi  # Konstanta π
        luas_permukaan = 2 * PI * jari_jari * (jari_jari + tinggi)

        # Format hasil menjadi 2 angka desimal
        luas_permukaan_formatted = round(luas_permukaan, 2)

        # Tampilkan hasil
        print("\nHasil Perhitungan:")
        print(f"Jari-jari tabung: {jari_jari}")
        print(f"Tinggi tabung: {tinggi}")
        print(f"Luas permukaan tabung: {luas_permukaan_formatted}")

    except ValueError:
        # Handle error jika konversi gagal
        print("Error: Masukkan harus berupa angka!")

# Menjalankan program utama
if __name__ == "__main__":
    main()
