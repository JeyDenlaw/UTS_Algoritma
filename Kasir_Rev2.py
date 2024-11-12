barang = {
    "Buku": 20000,
    "Pensil": 3000,
    "Penghapus": 2000,
    "Pulpen": 5000
}

keranjang = []

def tampilkan_daftar_barang():
    print("===================")
    print("   Daftar Barang   ")
    print("===================")
    for nama_barang, harga in barang.items():
        print(f"- {nama_barang} : Rp{harga}")
    print("___________________")

def tambah_barang_ke_keranjang():
    nama_barang = input("Masukkan nama barang yang ingin ditambahkan: ")
    if nama_barang in barang:
        try:
            jumlah = int(input(f"Masukkan jumlah {nama_barang}: "))
            if jumlah > 0:
                keranjang.append((nama_barang, jumlah))
                print(f"{jumlah} {nama_barang} berhasil ditambahkan ke keranjang.")
            else:
                print("Jumlah harus lebih dari 0.")
        except ValueError:
            print("Masukkan jumlah yang valid.")
    else:
        print("Barang tidak ditemukan.")

def cetak_struk():
    print("\nStruk Belanja")
    print("==================")
    total_harga = 0
    for nama_barang, jumlah in keranjang:
        harga_satuan = barang[nama_barang]
        total_item = harga_satuan * jumlah
        print(f"{nama_barang} x {jumlah} = Rp {total_item}")
        total_harga += total_item
    print("================")
    print(f"Total Harga: Rp {total_harga}")
    print("================")

while True:
    print("\nMenu:")
    print("1. Tampilkan Daftar Barang")
    print("2. Tambah Barang ke Keranjang")
    print("3. Cetak Struk")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        tampilkan_daftar_barang()
    elif pilihan == '2':
        tambah_barang_ke_keranjang()
    elif pilihan == '3':
        cetak_struk()
    elif pilihan == '4':
        break
    else:
        print("Pilihan tidak valid.")
