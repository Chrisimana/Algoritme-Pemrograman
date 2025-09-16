def hapusProduk(akses, produk):
    if akses != "admin":
        raise AssertionError("Anda harus punya akses admin untuk bisa menghapus barang")

    if produk not in ["tas", "jam", "baju", "celana", "buku"]:
        raise ValueError("Produk tidak ada")

hapusProduk("pegawai", "komputer")
