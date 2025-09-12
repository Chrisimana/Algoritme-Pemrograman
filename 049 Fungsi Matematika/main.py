def fungsi(x: int) -> int:
    return 6 * x**2 + 3 * x + 2


if __name__ == "__main__":
    print("=== Program Fungsi y = 6x^2 + 3x + 2 ===")
    for x in range(-10, 11):
        y = fungsi(x)
        print(f"x = {x}, y = {y}")
