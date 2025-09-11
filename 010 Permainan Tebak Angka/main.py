import random, sys
print(".:: Permainan Tebak Angka ::.\n")
input = int(input("Masukan angka 1 - 5 ? "))

if(input > 5):
     sys.exit("Angka yang anda masukkan tidak valid! Masukan angka 1 - 5!")

com = random.randint(0, 5)

if(input == com):
     print("Tebakkan anda BENAR!!")

else:
    print("Tebakkan anda SALAH!!")