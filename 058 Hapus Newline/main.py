def hapus_newline(nama_file: str, output_file: str):
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            isi = f.read()

        # Hapus semua newline
        isi_tanpa_newline = isi.replace("\n", " ")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(isi_tanpa_newline)

        print(f"Berkas '{nama_file}' berhasil dikonversi ke '{output_file}' tanpa baris baru.")
    except FileNotFoundError:
        print(f"Berkas '{nama_file}' tidak ditemukan!")
    except Exception as e:
        print("Terjadi error:", e)


if __name__ == "__main__":
    print("=== Program Konversi Berkas Teks Tanpa Baris Baru ===")
    nama_input = input("Masukkan nama file input (misalnya input.txt): ")
    nama_output = input("Masukkan nama file output (misalnya output.txt): ")

    hapus_newline(nama_input, nama_output)
