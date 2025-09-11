import math
print(".:: Program Luas Bidang ::.\n")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Lingkaran")
pil = int(input("Pilihan anda ? "))

if(pil == 1):
    sisi = float(input("Berapa sisi persegi ? "))
    luasPersegi = sisi*sisi
    print("Luas Persegi = ", luasPersegi)

elif(pil == 2):
    panjang = float(input("Berapa panjang persegi panjang ? "))
    lebar = float(input("Berapa lebar persegi panjang ? "))
    luasPersegiPanjang = panjang*lebar
    print("Luas Persegi Panjang = ", luasPersegiPanjang)

elif(pil == 3):
    jari2 = float(input("Berapa jari-jari lingkaran ? "))
    luasLingkaran = math.pi * jari2 * jari2
    print("Luas Lingkaran = ", luasLingkaran)
    
else:
    print("Masukan pilihan yang benar !")