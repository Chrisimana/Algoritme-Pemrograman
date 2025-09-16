def kapital_pertama(s: str, i: int):
    # Basis: jika indeks melebihi panjang string, return None
    if i >= len(s):
        return None
    # Jika huruf pada indeks i adalah kapital, kembalikan huruf tersebut
    if s[i].isupper():
        return s[i]
    # Jika tidak, lanjutkan rekursi ke indeks berikutnya
    return kapital_pertama(s, i + 1)


if __name__ == "__main__":
    print("=== Program Mencari Huruf Kapital Pertama (Rekursif) ===")
    teks = input("Masukkan sebuah string: ")
    hasil = kapital_pertama(teks, 0)

    if hasil:
        print(f"Huruf kapital pertama dalam string adalah: {hasil}")
    else:
        print("Tidak ada huruf kapital dalam string.")
