import random
import string


def generate_password(length):
    """
    Fungsi untuk menghasilkan password acak dengan panjang tertentu.

    Parameters:
    length (int): Panjang password yang diinginkan

    Returns:
    str: Password acak yang dihasilkan
    """
    # Karakter yang akan digunakan untuk membuat password
    # Huruf besar, huruf kecil, angka, dan simbol
    characters = string.ascii_letters + string.digits + string.punctuation

    # Menghasilkan password acak
    password = ''.join(random.choice(characters) for i in range(length))

    return password


def generate_strong_password(length):
    """
    Fungsi untuk menghasilkan password kuat yang memastikan
    mengandung huruf besar, huruf kecil, angka, dan simbol.

    Parameters:
    length (int): Panjang password yang diinginkan

    Returns:
    str: Password kuat yang dihasilkan
    """
    # Pastikan panjang minimal 8 karakter untuk password kuat
    if length < 8:
        length = 8

    # Pastikan setiap jenis karakter terwakili
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    # Karakter yang tersisa
    remaining_length = length - 4
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = ''.join(random.choice(all_characters) for i in range(remaining_length))

    # Gabungkan semua karakter dan acak urutannya
    password_chars = list(uppercase + lowercase + digit + symbol + remaining_chars)
    random.shuffle(password_chars)

    return ''.join(password_chars)


def check_password_strength(password):
    """
    Fungsi untuk memeriksa kekuatan password.

    Parameters:
    password (str): Password yang akan diperiksa

    Returns:
    str: Tingkat kekuatan password
    """
    strength = 0

    # Kriteria kekuatan password
    if len(password) >= 8:
        strength += 1

    if any(char in string.ascii_uppercase for char in password):
        strength += 1

    if any(char in string.ascii_lowercase for char in password):
        strength += 1

    if any(char in string.digits for char in password):
        strength += 1

    if any(char in string.punctuation for char in password):
        strength += 1

    # Menentukan tingkat kekuatan
    if strength <= 2:
        return "Lemah"
    elif strength == 3:
        return "Sedang"
    elif strength == 4:
        return "Kuat"
    else:
        return "Sangat Kuat"


def main():
    """Fungsi utama program"""
    print("      PROGRAM PEMBANGKIT PASSWORD")

    print("Pilih jenis password:")
    print("1. Password Acak")
    print("2. Password Kuat (minimal 8 karakter)")
    try:
        # Meminta pilihan jenis password
        choice = int(input("Masukkan pilihan (1/2): "))

        if choice not in [1, 2]:
            print("Error: Pilihan harus 1 atau 2!")
            return

        # Meminta panjang password
        length = int(input("Masukkan panjang password: "))

        # Validasi panjang password
        if length <= 0:
            print("Error: Panjang password harus positif!")
            return

        if choice == 2 and length < 8:
            print("Password kuat memerlukan minimal 8 karakter. Panjang diubah menjadi 8.")
            length = 8

        # Menghasilkan password
        if choice == 1:
            password = generate_password(length)
        else:
            password = generate_strong_password(length)

        # Memeriksa kekuatan password
        strength = check_password_strength(password)

        # Menampilkan hasil
        print("\n" + "=" * 50)
        print("PASSWORD BERHASIL DIBUAT")
        print("=" * 50)
        print(f"Password: {password}")
        print(f"Panjang: {len(password)} karakter")
        print(f"Kekuatan: {strength}")
        print("=" * 50)

        # Tips keamanan
        print("\nTips Keamanan Password:")
        print("- Gunakan minimal 12 karakter")
        print("- Gunakan kombinasi huruf besar, huruf kecil, angka, dan simbol")
        print("- Jangan gunakan informasi pribadi")
        print("- Gunakan password yang berbeda untuk setiap akun")

    except ValueError:
        # Menangani error jika input bukan angka
        print("Error: Masukkan harus berupa angka!")


# Menjalankan program utama
if __name__ == "__main__":
    main()