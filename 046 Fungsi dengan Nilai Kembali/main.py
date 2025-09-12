def tambah(a,b):
    return a + b

def kali(a,b,c):
 return a*b*c

def jumlah(list):
    jumlah = 0
    for x in list:
        jumlah+=x
    return jumlah

def maksimum(a,b,c):
    if(a > b and a > c):
        return a
    elif(b > c):
        return b
    else:
        return c

hasil1 = tambah(5,10)
print(f"hasil1 = {hasil1}")
hasil2 = kali(2,3,4)
print(f"hasil2 = {hasil2}")
hasil3 = jumlah([1,2,3,4,5])
print(f"hasil3 = {hasil3}")
hasil4 = maksimum(5,10,7)
print(f"hasil4 = {hasil4}")