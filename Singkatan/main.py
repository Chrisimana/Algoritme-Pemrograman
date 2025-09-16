print(".:: Program Singkatan ::.")

kalimat = input("Masukkan Kalimat : ")

singkatan = ""

daftar_kata = kalimat.strip().split(" ")

for kata in daftar_kata:
    singkatan += kata[0].upper()

print(f"Singkatan : {singkatan}")
