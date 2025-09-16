jum_bil = int(input("Masukkan banyaknya jumlah bilangan? "))
daftar_bil = []
total = 0
for i in range(jum_bil):
    bil = float(input(f"Bilangan ke-{i+1}: "))
    daftar_bil.append(bil)
    total += bil

print("Bilangan yang telah terdata", daftar_bil)
print("Rata-rata:", total/len(daftar_bil))
print("Maksimum: ", max(daftar_bil))
print("Minimum: ", min(daftar_bil))
