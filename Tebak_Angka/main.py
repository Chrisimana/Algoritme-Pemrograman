import random
print(".:: Permainan Tebak Angka ::.\n")

komp = random.randint(1,10)

print("Komputer telah memikirkan suatu angka dari 1 - 10. Tebak angka tersebut!")

kesempatan = 3

while(kesempatan > 0):
    angka = int(input("Tebakkan saya : "))
    if(angka < 1 or angka > 10):
        print("Masukkan angka yang benar! Angka yang dipikirkan komputer antara 1 - 10")
    elif(angka == komp):
        print("Tebakkan anda benar!, komputer memikirkan angka ", angka)
        kesempatan = 0
    else:
        kesempatan-=1
    if(kesempatan == 0):
        print("Salah!!, angka yang dipilih komputer adalah", komp)
    else:
        print("Tebakkan anda salah! Coba lagi.")
        print("Sisa kesempatan = ", kesempatan)
