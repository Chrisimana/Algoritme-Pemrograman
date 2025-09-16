def evaluasi_kalimat(kalimat: str):
    kalimat = kalimat.lower().replace("?", "").strip()

    if "ditambah" in kalimat:
        bagian = kalimat.split("ditambah")
        a, b = int(bagian[0].split()[-1]), int(bagian[1].strip())
        return a + b

    elif "dikurangi" in kalimat:
        bagian = kalimat.split("dikurangi")
        a, b = int(bagian[0].split()[-1]), int(bagian[1].replace("dengan", "").strip())
        return a - b

    elif "dikali" in kalimat:
        bagian = kalimat.split("dikali")
        a, b = int(bagian[0].split()[-1]), int(bagian[1].strip())
        return a * b

    elif "dibagi" in kalimat:
        bagian = kalimat.split("dibagi")
        a, b = int(bagian[0].split()[-1]), int(bagian[1].strip())
        if b == 0:
            return "Error: pembagian dengan nol!"
        return a / b

    else:
        return "Operasi tidak dikenali"


if __name__ == "__main__":
    print("=== Program Evaluasi Aritmatika dari Kalimat ===")
    print("Ketik 'selesai' untuk menghentikan program.\n")

    while True:
        kalimat = input("Masukkan kalimat aritmatika: ")
        if kalimat.lower().strip() == "selesai":
            print("-- Program berhenti --")
            break

        hasil = evaluasi_kalimat(kalimat)
        print("->", hasil)
