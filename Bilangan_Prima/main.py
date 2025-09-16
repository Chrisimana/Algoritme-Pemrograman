def is_prima(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("=== Program Deteksi Bilangan Prima ===")
    try:
        angka = int(input("Masukkan sebuah bilangan bulat: "))
        if is_prima(angka):
            print(f"{angka} adalah bilangan prima ✅")
        else:
            print(f"{angka} bukan bilangan prima ❌")
    except ValueError:
        print("Input tidak valid! Harus berupa bilangan bulat.")
