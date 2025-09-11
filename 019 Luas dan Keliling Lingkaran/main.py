import math

print(".:: Program Luas dan Keliling Lingkaran ::.\n")

pil = -1
while (pil != 3):
    print("MENU")
    print("1. Luas Lingkaran")
    print("2. Keliling Lingkaran")
    print("3. Keluar")
    pil = int(input("Pilihan Anda ? "))

    if (pil == 1):
        jari2 = float(input("Masukkan Jari-Jari : "))
        luas = math.pi * jari2 ** 2
        print("\033[1mLuas Lingkaran = ", luas, "\033[0m")
    elif (pil == 2):
        jari2 = float(input("Masukkan Jari-Jari : "))
        keliling = 2 * math.pi * jari2
        print("\033[1mKeliling Lingkaran = ", keliling, "\033[0m")
    elif (pil == 3):
        print("Bye bye... program dimatikan")
    else:
        print("\033[31mMasukkan pilihan yang benar!\033[0m")