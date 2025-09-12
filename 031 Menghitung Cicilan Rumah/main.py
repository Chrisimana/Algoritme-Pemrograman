def hitung_cicilan(harga_asal, harga_jual, lama_cicilan):
    """
    Fungsi untuk menghitung cicilan rumah per tahun.
    harga_asal   : Harga rumah sebelum dijual ke klien
    harga_jual   : Harga rumah yang dijual ke klien
    lama_cicilan : Lama waktu cicilan (tahun), misal 20, 15, 10, 5
    """
    total_selisih = harga_jual - harga_asal
    cicilan_per_tahun = harga_jual / lama_cicilan
    return cicilan_per_tahun, total_selisih


if __name__ == "__main__":
    print("=== Program Menghitung Cicilan Rumah ===")
    try:
        harga_asal = float(input("Masukkan harga rumah asal: "))
        harga_jual = float(input("Masukkan harga rumah yang dijual ke klien: "))

        print("\nPilih skema cicilan (tahun): 20 | 15 | 10 | 5")
        lama_cicilan = int(input("Masukkan lama cicilan: "))

        if lama_cicilan not in [20, 15, 10, 5]:
            print("Skema cicilan tidak valid! Hanya boleh 20, 15, 10, atau 5 tahun.")
        else:
            cicilan, selisih = hitung_cicilan(harga_asal, harga_jual, lama_cicilan)
            print("\n=== Hasil Perhitungan ===")
            print(f"Harga Asal       : Rp{harga_asal:,.0f}")
            print(f"Harga Jual       : Rp{harga_jual:,.0f}")
            print(f"Selisih Harga    : Rp{selisih:,.0f}")
            print(f"Lama Cicilan     : {lama_cicilan} tahun")
            print(f"Cicilan per tahun: Rp{cicilan:,.0f}")
    except ValueError:
        print("Input tidak valid! Masukkan angka yang benar.")
