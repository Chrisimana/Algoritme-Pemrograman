print(".:: Program Segitiga Siku-Siku ::.\n")

n = int(input("Masukkan sisi : "))

for i in range(n):
    for j in range(i+1):
        print("x", end="")
    print()
