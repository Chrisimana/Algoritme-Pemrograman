print(".:: Program Bilangan Ganjil dan Jumlahnya ::.\n")

batas = int(input("Batas Atas Bilangan Ganjil : "))

print("Bilangan Ganjil : ", end = "")
sum = 0
for i in range(batas+1):
    if(i % 2 == 1):
        print(i, end=" ")
        sum+=i

print("\nJumlah : ", sum)
