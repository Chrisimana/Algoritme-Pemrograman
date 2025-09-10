# Asumsi: 1 hari kerja = 8 jam, 5 hari kerja per minggu

def hitung_gaji_mingguan(upah_per_jam, hari_kerja=5):
    """
    Fungsi untuk menghitung gaji pegawai dalam satu minggu.

    Parameters:
    upah_per_jam (float): Upah pegawai per jam
    hari_kerja (int): Jumlah hari kerja dalam seminggu (default: 5)

    Returns:
    float: Total gaji dalam satu minggu
    """
    # Menghitung total jam kerja dalam seminggu
    jam_per_hari = 8
    total_jam_kerja = hari_kerja * jam_per_hari

    # Menghitung total gaji mingguan
    total_gaji = upah_per_jam * total_jam_kerja
    return total_gaji

def main():
    """Fungsi utama program"""
    print("PROGRAM MENGHITUNG GAJI PEGAWAI MINGGUAN")

    try:
        # Meminta input dari pengguna
        input_upah = input("Masukkan upah pegawai per jam: ")

        # Konversi input string ke float
        upah_per_jam = float(input_upah)

        # Validasi input tidak boleh negatif
        if upah_per_jam <= 0:
            print("Error: Upah per jam harus bernilai positif!")
            return

        # Menghitung gaji mingguan
        gaji_mingguan = hitung_gaji_mingguan(upah_per_jam)

        # Menampilkan hasil perhitungan
        print("\nRincian Perhitungan:")
        print(f"Upah per jam: Rp {upah_per_jam:,.2f}")
        print(f"Jam kerja per hari: 8 jam")
        print(f"Hari kerja per minggu: 5 hari")
        print(f"Total jam kerja per minggu: 40 jam")
        print("------------------------------------------")
        print(f"Total gaji mingguan: Rp {gaji_mingguan:,.2f}")

    except ValueError:
        # Menangani error jika input bukan angka
        print("Error: Masukkan harus berupa angka!")

# Menjalankan program utama
if __name__ == "__main__":
    main()