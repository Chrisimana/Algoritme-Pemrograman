def daftar_kata(nama_file: str, output_file: str):
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            isi = f.read()

        # Pisahkan teks menjadi kata-kata (berdasarkan spasi)
        kata_list = isi.split()

        with open(output_file, "w", encoding="utf-8") as f:
            for i, kata in enumerate(kata_list, start=1):
                f.write(f"{i}. {kata}\n")

        print(f"Berkas '{output_file}' berhasil dibuat dengan daftar kata dan posisinya.")
    except FileNotFoundError:
        print(f"Berkas '{nama_file}' tidak ditemukan!")
    except Exception as e:
        print("Terjadi error:", e)


if __name__ == "__main__":
    print("=== Program Daftar Kata dan Posisi dari Berkas ===")
    nama_input = input("Masukkan nama file input (misalnya input.txt): ")
    nama_output = input("Masukkan nama file output (misalnya output.txt): ")

    daftar_kata(nama_input, nama_output)
