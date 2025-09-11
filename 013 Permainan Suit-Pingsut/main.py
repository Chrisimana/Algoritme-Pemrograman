import random
import sys
import os
from time import sleep


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    print("╔══════════════════════════════════════════════════╗")
    print("║               PERMAINAN SUIT/PINGSUT             ║")
    print("║                  Gajah-Manusia-Semut             ║")
    print("╚══════════════════════════════════════════════════╝")
    print()


def print_choices():
    print("Pilihan Anda:")
    print("┌─────────────┬─────────────┬─────────────┐")
    print("│   1. Jempol │  2. Telunjuk│ 3. Kelingking│")
    print("│    (Gajah)  │   (Manusia) │    (Semut)   │")
    print("└─────────────┴─────────────┴─────────────┘")
    print()


def print_result(user_choice, comp_choice, result):
    choices = {
        1: "Gajah 🐘",
        2: "Manusia 👨",
        3: "Semut 🐜"
    }

    symbols = {
        1: "✊",
        2: "✌️",
        3: "🤏"
    }

    print("\n" + "═" * 50)
    print("HASIL PERMAINAN")
    print("═" * 50)
    print(f"Pilihan Anda: {choices[user_choice]} {symbols[user_choice]}")
    print(f"Pilihan Komputer: {choices[comp_choice]} {symbols[comp_choice]}")
    print("─" * 50)

    if "menang" in result:
        print(f"🎉 {result.upper()} 🎉")
    elif "kalah" in result:
        print(f"💀 {result.upper()} 💀")
    else:
        print(f"🤝 {result.upper()} 🤝")

    print("═" * 50)


def main():
    clear_screen()
    print_header()
    print_choices()

    try:
        pil = int(input("Masukkan pilihan Anda (1-3): "))
        if pil < 1 or pil > 3:
            print("\n❌ Pilihan tidak valid! Harap masukkan angka 1, 2, atau 3.")
            sys.exit()
    except ValueError:
        print("\n❌ Input tidak valid! Harap masukkan angka.")
        sys.exit()

    # Animasi loading
    print("\nKomputer sedang memilih", end="")
    for _ in range(3):
        sleep(0.5)
        print(".", end="", flush=True)
    sleep(0.5)

    # Pilihan komputer
    kom = random.randint(1, 3)

    # Menentukan hasil
    if kom == 1:  # Komputer memilih Gajah
        if pil == 1:
            result = "Sama-sama Gajah! Sesama gajah saling membantu..."
        elif pil == 2:
            result = "Diinjek gajah.. kamu kalah!"
        else:
            result = "Kamu gigit gajah, kamu menang!"
    elif kom == 2:  # Komputer memilih Manusia
        if pil == 1:
            result = "Kamu abis nginjek manusia, kamu menang!"
        elif pil == 2:
            result = "Sama-sama Manusia! Jangan berantem lah..."
        else:
            result = "Kamu dibunuh manusia, kamu kalah!"
    else:  # Komputer memilih Semut
        if pil == 1:
            result = "Kamu abis dikerjain sama semut, kamu kalah!"
        elif pil == 2:
            result = "Kamu gak sengaja injek semut, kamu menang!"
        else:
            result = "Sesama semut saling membahu..!"

    clear_screen()
    print_header()
    print_result(pil, kom, result)

    # Tawarkan untuk bermain lagi
    print("\n")
    play_again = input("Apakah Anda ingin bermain lagi? (y/n): ").lower()
    if play_again == 'y' or play_again == 'ya':
        main()
    else:
        print("\nTerima kasih telah bermain! 👋")
        sys.exit()


if __name__ == "__main__":
    main()