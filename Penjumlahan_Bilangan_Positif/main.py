print(".:: Program Penjumlahan 5 Bilangan Positif ::.\n")

sum = 0
for i in range(5):
    n = float(input(f"Bilangan ke-{i+1} : "))
    if(n <= 0):
        continue
    sum += n

print("Hasil Penjumlahan : ", sum)
