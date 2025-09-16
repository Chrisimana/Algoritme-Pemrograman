def harga_diskon(harga_asal, diskon):
    assert diskon <= 100, "Diskon harus kurang dari 100%"
    assert diskon > 0, "Diskon harus bernilai positif"
    harga_diskon = harga_asal - (harga_asal*diskon/100)
    return harga_diskon

harga = input("Masukkan harga: ")
assert harga.isdigit(), "Harga yang dimasukkan harus berupa angka"
harga = int(harga)
diskon = input("Masukkan diskon (tanpa persen/%): ")
assert diskon.isdigit(), "Masukkan diskon hanya berupa angka"
diskon = float(diskon)

print("Harga diskon menjadi: ",
harga_diskon(harga, diskon), "rupiah")
