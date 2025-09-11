print(".:: Program Indeks Massa Tubuh ::.")

beratBadan = int(input("Berat Badan (kg.) : "))

#Tinggi Badan dalam cm
tinggiBadanCM = int(input("Tinggi Badan (cm.) : "))

#Tinggi Badan dalam meter
tinggiBadanM = tinggiBadanCM/100
imt = beratBadan/(tinggiBadanM**2)
kriteria = ""
if imt <= 18.5:
    kriteria = "Kurus"
elif 18.5 < imt and imt <= 25:
    kriteria = "Normal"
elif 25 < imt and imt <= 30:
    kriteria = "Gemuk"
else:
    kriteria = "Kegemukan (Obesitas)"

print("Kriteria tubuh anda berdasarkan IMT adalah", kriteria)