def asal(kota = "Balikpapan"):
    print(f"Saya berasal dari {kota}")

def cetak_list(list = ["kosong"]):
    for x in list:
        print(x)

def cetak_segi_tiga(n = 5):
    for i in range(n):
        for j in range(i+1):
            print("*", end = "")
        print()

asal("Banjarmasin")
asal("Samarinda")
asal("Palangkaraya")
asal("Pontianak")
asal()

cetak_list([1,2,3,4,5])
cetak_list()

cetak_segi_tiga(3)
cetak_segi_tiga()