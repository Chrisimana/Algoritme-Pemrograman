print(".:: Program Bilangan Genap ::.\n")

batas = int(input("Batas Atas Bilangan Genap : "))

i = 1
while(i <= batas):
    if(i % 2 == 0):
        print(i, end=" ")
    i+=1;
