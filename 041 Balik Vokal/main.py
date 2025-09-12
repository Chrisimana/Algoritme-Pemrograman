def balik_kalimat(kalimat: str) -> str:
    return kalimat[::-1]


def hitung_vokal(kalimat: str) -> int:
    vokal = "aiueoAIUEO"
    return sum(1 for huruf in kalimat if huruf in vokal)


if __name__ == "__main__":
    print("=== Program Membalik Kalimat dan Menghitung Huruf Vokal ===")
    kalimat = input("Masukkan sebuah kalimat: ")

    dibalik = balik_kalimat(kalimat)
    jumlah_vokal = hitung_vokal(kalimat)

    print("\n=== Hasil ===")
    print("Kalimat asli  :", kalimat)
    print("Kalimat dibalik:", dibalik)
    print("Jumlah huruf vokal:", jumlah_vokal)
