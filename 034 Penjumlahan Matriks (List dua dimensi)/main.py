a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8, 9], [10, 11, 12]]
c = []

print('Matriks A')
for x in a:
    print(x)
print('Matriks B')
for x in b:
    print(x)
for i in range(len(a)):
    el = []
    for j in range(len(a[0])):
        jum = a[i][j] + b[i][j]
        el.append(jum)
    c.append(el)
print("Hasil Penjumlahan")
for x in c:
    print(x)