import random  # Import modul random untuk respons yang bervariasi


def buat_respons(pesan_pengguna):
    """
    Fungsi untuk membuat respons chatbot berdasarkan pesan pengguna.

    Parameters:
    pesan_pengguna (str): Pesan yang dikirim oleh pengguna

    Returns:
    str: Respons dari chatbot
    """
    # Konversi pesan ke lowercase untuk memudahkan pemrosesan
    pesan = pesan_pengguna.lower()

    # Daftar respons berdasarkan kata kunci dalam pesan
    if any(kata in pesan for kata in ['halo', 'hai', 'hi', 'hello', 'hey']):
        return random.choice([
            "Halo! Ada yang bisa saya bantu?",
            "Hai! Senang berbicara dengan Anda!",
            "Hello! Bagaimana kabar Anda hari ini?"
        ])

    elif any(kata in pesan for kata in ['nama', 'siapa namamu', 'kamu siapa']):
        return "Saya adalah Chatbot Python. Senang berkenalan dengan Anda!"

    elif any(kata in pesan for kata in ['kabar', 'apa kabar', 'how are you']):
        return random.choice([
            "Saya baik-baik saja, terima kasih! Bagaimana dengan Anda?",
            "Sangat baik! Ada yang bisa saya bantu?",
            "Luar biasa! Senang bisa berbicara dengan Anda."
        ])

    elif any(kata in pesan for kata in ['terima kasih', 'thanks', 'thank you']):
        return random.choice([
            "Sama-sama! Senang bisa membantu.",
            "Dengan senang hati!",
            "Terima kasih kembali!"
        ])

    elif any(kata in pesan for kata in ['bye', 'selamat tinggal', 'sampai jumpa', 'dadah']):
        return random.choice([
            "Selamat tinggal! Senang berbicara dengan Anda.",
            "Sampai jumpa lagi!",
            "Dadah! Jangan lupa kembali lagi ya!"
        ])

    elif any(kata in pesan for kata in ['help', 'bantuan', 'tolong']):
        return "Saya bisa membantu Anda berbicara tentang: salam, nama, kabar, dan topik sehari-hari lainnya."

    elif any(kata in pesan for kata in ['buat apa', 'fungsi', 'kegunaan']):
        return "Saya dibuat untuk melakukan percakapan sederhana dan membantu menjawab pertanyaan dasar."

    elif any(kata in pesan for kata in ['python', 'program', 'kode']):
        return "Python adalah bahasa pemrograman yang hebat! Saya dibuat menggunakan Python."

    elif any(kata in pesan for kata in ['humor', 'lucu', 'joke', 'cerita lucu']):
        return random.choice([
            "Mengapa programmer tidak bisa tidur? Karena mereka selalu debugging mimpi mereka!",
            "Apa bahasa pemrograman favorit hantu? Boo-lang!",
            "Kenapa komputer tidak dingin? Karena Windows selalu terbuka!"
        ])

    elif any(kata in pesan for kata in ['cuaca', 'weather', 'hujan', 'panas']):
        return "Maaf, saya tidak bisa mengakses informasi cuaca saat ini. Tapi semoga hari Anda menyenangkan!"

    else:
        return random.choice([
            "Menarik! Bisa Anda ceritakan lebih banyak?",
            "Saya belum sepenuhnya memahami itu. Bisa diulangi dengan cara lain?",
            "Maaf, saya hanya chatbot sederhana. Bisa bertanya sesuatu yang lain?",
            "Wah, itu topik yang menarik! Ada hal lain yang ingin Anda bicarakan?",
            "Saya masih belajar memahami manusia. Bisa Anda jelaskan dengan lebih sederhana?"
        ])


def main():
    """Fungsi utama program"""
    print("CHATBOT SEDERHANA")

    # Variabel untuk menyimpan status percakapan
    percakapan_aktif = True

    while percakapan_aktif:
        # Meminta input dari pengguna
        pesan_pengguna = input("Anda: ")

        # Cek jika pengguna ingin mengakhiri percakapan
        if pesan_pengguna.lower() in ['bye', 'selamat tinggal', 'sampai jumpa', 'quit', 'exit', 'dadah']:
            print("Chatbot: " + random.choice([
                "Selamat tinggal! Senang berbicara dengan Anda.",
                "Sampai jumpa lagi!",
                "Terima kasih sudah mengobrol. Sampai bertemu lagi!"
            ]))
            percakapan_aktif = False
        else:
            # Membuat dan menampilkan respons chatbot
            respons = buat_respons(pesan_pengguna)
            print("Chatbot:", respons)

            # Tambahkan garis pemisah untuk readability
            print("-" * 50)


# Menjalankan program utama
if __name__ == "__main__":
    main()
