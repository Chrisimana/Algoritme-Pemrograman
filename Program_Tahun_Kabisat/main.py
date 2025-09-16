print(".:: Program Tahun Kabisat ::.\n")

tahun = int(input("Tahun : "))

if tahun % 4 == 0:
    if tahun % 100 == 0:
        if tahun % 400 == 0:
            print("Tahun ", tahun, " adalah tahun kabisat")
        else:
            print("Tahun ", tahun, " bukan tahun kabisat")
    else:
        print("Tahun ", tahun, " bukan tahun kabisat")
else:
 print("Tahun ", tahun, " bukan tahun kabisat")
