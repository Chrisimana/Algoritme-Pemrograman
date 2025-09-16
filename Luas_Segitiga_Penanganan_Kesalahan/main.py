print(".:: Program Luas Segitiga ::.")

pil = True
while (pil == True):
    try:
        alas = input("Alas: ")
        alas = float(alas)
        if alas < 0:
            raise AssertionError()
    except ValueError:
        print("Nilai yang anda masukkan bukan berupa angka, nilai 1 akan dimasukkan sebagai nilai alas")
        alas = 1
    except AssertionError:
        print("Nilai alas tidak boleh negatif!, nilai akan dimutlakkan!")
        alas = abs(alas)
    else:
        print("Alas yang anda masukkan sudah benar dan akan diproses")

    try:
        tinggi = input("Tinggi: ")
        tinggi = float(tinggi)
        if tinggi < 0:
            raise AssertionError()
    except ValueError:
        print("Nilai yang anda masukkan bukan berupa angka, nilai 1 akan dimasukkan sebagai nilai tinggi")
        tinggi = 1
    except AssertionError:
        print("Nilai tinggi tidak boleh negatif!, nilai akan dimutlakkan!")
        tinggi = abs(alas)
    else:
        print("Tinggi yang anda masukkan sudah benar dan akan diproses")
    luas = alas*tinggi*0.5
    print(f"Alas ({alas}), Tinggi ({tinggi}), Luas = {luas}")

    pilihan = '?'
    while(pilihan != 'y' and pilihan != "t"):
        try:
            pilihan = input("Lanjut (y) atau berhenti (t)? ").lower()
            if(pilihan != 'y' and pilihan != 't'):
                raise ValueError()
        except ValueError:
            print("Masukkan hanya karakter y atau t")
        else:
            if(pilihan == 'y'):
                pil = True
            else:
                pil = False
                print("bye..bye..")
