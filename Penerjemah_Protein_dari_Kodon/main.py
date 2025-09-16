def terjemahkan_kodon(kodon):
    """
    Fungsi untuk menerjemahkan kodon RNA menjadi nama protein.

    Parameters:
    kodon (str): Kodon RNA (3 huruf)

    Returns:
    str: Nama protein yang sesuai dengan kodon
    """
    # Dictionary untuk mapping kodon ke protein
    tabel_genetik = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan'
    }

    # Konversi kodon ke uppercase untuk handling case insensitive
    kodon_upper = kodon.upper()

    # Cek apakah kodon valid
    if kodon_upper in tabel_genetik:
        return tabel_genetik[kodon_upper]
    else:
        return "Kodon tidak dikenali"


def main():
    """Fungsi utama program"""
    print("==========================================")
    print("    PROGRAM PENERJEMAH PROTEIN")
    print("==========================================")
    print("Daftar kodon yang dikenali:")
    print("AUG, UUU, UUC, UUA, UUG, UCU, UCC, UCA, UCG")
    print("UAU, UAC, UGU, UGC, UGG")
    print("==========================================")

    # Meminta input dari pengguna
    input_kodon = input("Masukkan kodon RNA (3 huruf): ")

    # Validasi panjang input
    if len(input_kodon) != 3:
        print("Error: Kodon harus terdiri dari 3 huruf!")
        return

    # Menerjemahkan kodon
    nama_protein = terjemahkan_kodon(input_kodon)

    # Menampilkan hasil terjemahan
    print(f"\nHasil Terjemahan:")
    print(f"Kodon: {input_kodon.upper()}")
    print(f"Protein: {nama_protein}")


# Menjalankan program utama
if __name__ == "__main__":
    main()
