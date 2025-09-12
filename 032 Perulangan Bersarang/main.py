def pola_a(n):
    for i in range(n, 0, -1):
        print("x" * i)


def pola_b(n):
    for i in range(n, 0, -2):
        print("x" * i)
        if i - 2 > 0:
            print("-" * (i - 2))


def pola_c(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


def pola_d(n):
    for i in range(1, n + 1):
        print("x" * i)
    for i in range(n - 1, 0, -1):
        print("x" * i)


def pola_e(n):
    for i in range(n, 0, -1):
        if i == n:
            print(". " * (i - 1) + str(i))
        elif i == 1:
            print(". " * (i - 1) + str(i))
        else:
            print(". " * (i - 1) + str(i))

if __name__ == "__main__":
    n = int(input("Masukkan angka (misal 5): "))

    print("\na. Pola A")
    pola_a(n)

    print("\n\nb. Pola B")
    pola_b(n)

    print("\n\nc. Pola C")
    pola_c(n)

    print("\n\nd. Pola D")
    pola_d(n)

    print("\n\ne. Pola E")
    pola_e(n)
