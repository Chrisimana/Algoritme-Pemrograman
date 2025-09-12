def validasi_isbn10(isbn: str) -> bool:
    # Hapus tanda "-" jika ada
    isbn = isbn.replace("-", "").strip()

    # ISBN-10 harus tepat 10 karakter
    if len(isbn) != 10:
        return False

    total = 0
    for i in range(10):
        char = isbn[i]
        if char == "X" and i == 9:  # X hanya boleh di posisi terakhir
            nilai = 10
        elif char.isdigit():
            nilai = int(char)
        else:
            return False  # karakter tidak valid

        total += nilai * (10 - i)

    return total % 11 == 0


if __name__ == "__main__":
    print("=== Program Verifikasi ISBN-10 ===")
    kode = input("Masukkan kode ISBN-10 (misal 3-598-21508-8): ")

    if validasi_isbn10(kode):
        print("ISBN-10 valid ✅")
    else:
        print("ISBN-10 tidak valid ❌")
