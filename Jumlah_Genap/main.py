def jumlah_genap(a: int, b: int) -> int:
    # Basis: jika a > b, hasilnya 0
    if a > b:
        return 0
    # Jika a genap, tambahkan lalu lanjutkan rekursi
    if a % 2 == 0:
        return a + jumlah_genap(a + 1, b)
    # Jika a ganjil, lanjutkan ke angka berikutnya
    else:
        return jumlah_genap(a + 1, b)


if __name__ == "__main__":
    print("=== Program Jumlah Bilangan Genap (Rekursif) ===")
    try:
        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))
        hasil = jumlah_genap(a, b)
        print(f"Jumlah bilangan genap dari {a} sampai {b} adalah {hasil}")
    except ValueError:
        print("Input tidak valid! Harus berupa bilangan bulat.")
