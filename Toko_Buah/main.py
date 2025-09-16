stock = {
 'pisang': 10,
 'jambu': 5,
 'apel': 0,
 'durian': 7,
 'manggis': 1
}

harga = {
 'pisang': 10000,
 'jambu': 15000,
 'apel': 20000,
 'durian': 15000,
 'manggis': 5000
}

print('----------TOKO BUAH-------------')
print('Daftar Buah')
for key in stock:
    print(key, end=", ")
print()

buah = input('Buah apa yang ingin anda beli? ')
jumlah = int(input('Berapa jumlah buah yang anda beli? '))
if(stock[buah]>= jumlah):
    stock[buah] = stock[buah] - jumlah
    print("Total harga pembelian", harga[buah]*jumlah)
    print(f"Sisa stock buah {buah} : {stock[buah]}")
else:
    print('Maaf, stock kami tidak mencukupi')
