def input_matriks(nama):
    baris = int(input(f"Masukkan jumlah baris matriks {nama}: "))
    kolom = int(input(f"Masukkan jumlah kolom matriks {nama}: "))
    matriks = []
    print(f"Masukkan elemen matriks {nama} (baris per baris):")
    for i in range(baris):
        row = list(map(int, input().split()))
        if len(row) != kolom:
            print("Jumlah elemen tidak sesuai dengan jumlah kolom!")
            return None
        matriks.append(row)
    return matriks, baris, kolom


def kali_matriks(A, B):
    hasil = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil


def tampilkan_matriks(M):
    for row in M:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    print("=== Program Perkalian Matriks ===")
    try:
        A, barisA, kolomA = input_matriks("A")
        B, barisB, kolomB = input_matriks("B")

        if kolomA != barisB:
            print("Ukuran matriks tidak sesuai untuk perkalian! (kolom A harus = baris B)")
        else:
            print("\nHasil perkalian matriks A x B adalah:")
            hasil = kali_matriks(A, B)
            tampilkan_matriks(hasil)
    except Exception as e:
        print("Terjadi error:", e)
