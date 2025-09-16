def generate_fibonacci(n):
    """
    Fungsi untuk menghasilkan deret Fibonacci sampai suku ke-N.

    Parameters:
    n (int): Jumlah suku Fibonacci yang ingin ditampilkan

    Returns:
    list: Deret bilangan Fibonacci
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    # Inisialisasi dua suku pertama
    fibonacci_sequence = [1, 1]

    # Menghitung suku-suku berikutnya
    for i in range(2, n):
        next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence


def main():
    """Fungsi utama program"""
    print("      PROGRAM DERET FIBONACCI")

    try:
        # Meminta input dari pengguna
        input_n = input("Masukkan bilangan bulat positif N: ")

        # Konversi input string ke integer
        n = int(input_n)

        # Validasi input harus positif
        if n <= 0:
            print("Error: Masukkan harus bilangan bulat positif!")
            return

        # Menghasilkan deret Fibonacci
        fibonacci_sequence = generate_fibonacci(n)

        # Menampilkan hasil deret Fibonacci
        print(f"\nDeret Fibonacci sampai suku ke-{n}:")

        # Format output dengan koma dan tanpa koma di akhir
        if n == 1:
            print("1")
        else:
            # Mengonversi setiap angka menjadi string dan menggabungkan dengan koma
            fibonacci_str = ", ".join(str(term) for term in fibonacci_sequence)
            print(fibonacci_str)

    except ValueError:
        # Menangani error jika input bukan bilangan bulat
        print("Error: Masukkan harus berupa bilangan bulat!")


# Menjalankan program utama
if __name__ == "__main__":
    main()
