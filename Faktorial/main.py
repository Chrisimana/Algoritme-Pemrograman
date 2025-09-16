def faktorial(n: int) -> int:
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif")
    hasil = 1
    for i in range(n, 0, -1):
        hasil *= i
    return hasil


def format_faktorial(n: int) -> str:
    if n < 0:
        return "Tidak bisa menghitung faktorial bilangan negatif"
    urutan = " x ".join(str(i) for i in range(n, 0, -1))
    hasil = faktorial(n)
    return f"{urutan} = {hasil}"


if __name__ == "__main__":
    print("=== Program Faktorial ===")
    try:
        angka = int(input("Masukkan sebuah bilangan bulat: "))
        print(format_faktorial(angka))
    except ValueError as e:
        print("Error:", e)
