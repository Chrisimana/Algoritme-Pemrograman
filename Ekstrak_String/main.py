def ekstrak_string(teks: str):
    huruf = ""
    angka = ""
    simbol = ""

    for char in teks:
        if char.isalpha():
            huruf += char
        elif char.isdigit():
            angka += char
        else:
            simbol += char

    hasil = [huruf, int(angka) if angka else 0, simbol]
    return hasil


if __name__ == "__main__":
    print("Program Ekstrak String")
    masukan = input("Masukkan sebuah string: ")
    hasil = ekstrak_string(masukan)

    print("Hasil ekstraksi:", hasil)
