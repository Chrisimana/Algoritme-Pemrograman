kode_genetik = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
}


def translasi_rna(rna: str):
    protein = []
    # bagi string menjadi 3 huruf per kodon
    for i in range(0, len(rna), 3):
        kodon = rna[i:i+3]
        if len(kodon) < 3:
            break  # kodon tidak lengkap
        asam_amin = kode_genetik.get(kodon, None)
        if asam_amin is None:
            protein.append("Unknown")
        elif asam_amin == "STOP":
            break
        else:
            protein.append(asam_amin)
    return protein


if __name__ == "__main__":
    print("=== Program Translasi RNA ke Protein ===")
    rna = input("Masukkan urutan RNA (misal AUGUUUUCU): ").upper().strip()

    hasil = translasi_rna(rna)

    print("\n=== Hasil Translasi ===")
    print("RNA     :", rna)
    print("Protein :", ", ".join(hasil) if hasil else "Tidak ada hasil")
