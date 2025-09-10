# Rumus: Fahrenheit = (Celcius × 9/5) + 32

def konversi_celcius_ke_fahrenheit(suhu_celcius):
    """
    Fungsi untuk mengkonversi suhu dari Celcius ke Fahrenheit.

    Parameters:
    suhu_celcius (float): Suhu dalam satuan Celcius

    Returns:
    float: Suhu dalam satuan Fahrenheit
    """
    # Rumus konversi Celcius ke Fahrenheit
    suhu_fahrenheit = (suhu_celcius * 9 / 5) + 32
    return suhu_fahrenheit


def main():
    """Fungsi utama program"""
    print("Program Konversi Suhu Celcius ke Fahrenheit")

    try:
        # Meminta input dari pengguna
        input_celcius = input("Masukkan suhu dalam Celcius: ")

        # Konversi input string ke float
        suhu_celcius = float(input_celcius)

        # Melakukan konversi suhu
        suhu_fahrenheit = konversi_celcius_ke_fahrenheit(suhu_celcius)

        # Menampilkan hasil konversi
        print("\nHasil Konversi:")
        print(f"Suhu dalam Celcius: {suhu_celcius}°C")
        print(f"Suhu dalam Fahrenheit: {suhu_fahrenheit}°F")

    except ValueError:
        # Menangani error jika input bukan angka
        print("Error: Masukkan harus berupa angka!")

# Menjalankan program utama
if __name__ == "__main__":
    main()