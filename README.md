# UTS_Algoritma 
Penjelasan Sourcecode Program

Line 1 - 6 merupakan dictionary yang menyimpan nama barang sebagai kunci dan harga barang sebagai nilai. Contohnya, harga "Buku" adalah Rp20.000.

Line 8 berfungsi sebagai keranjang belanja yang akan menyimpan barang-barang yang dipilih oleh pengguna. Setiap item di dalamnya adalah tuple yang berisi nama barang dan jumlah yang dibeli.

Fungsi 'tampilkan_daftar_barang()' pada line 10 - 16 :
- Fungsi ini digunakan untuk menampilkan daftar barang yang tersedia beserta harganya. Menggunakan loop untuk iterasi melalui item dalam dictionary barang dan mencetak nama serta harga setiap barang.

Fungsi 'tambah_barang_ke_keranjang()' pada Line 18 - 31 :
- Fungsi ini meminta pengguna untuk memasukkan nama barang yang ingin ditambahkan ke keranjang.
- Jika barang ada dalam dictionary 'barang', program akan meminta jumlah barang yang ingin ditambahkan.
- Menggunakan 'try-except' untuk menangani kesalahan konversi input ke integer dan memastikan bahwa jumlah yang dimasukkan lebih dari 0. Jika barang tidak ditemukan, akan ada pesan kesalahan.

Fungsi 'Cetak_Struk()' pada Line 33 - 44 :
- Fungsi ini mencetak struk belanja yang berisi rincian barang yang dibeli dan total harga.
- Menggunakan loop untuk iterasi melalui 'keranjang', menghitung total harga untuk setiap item dan menambahkan ke 'total_harga'.
- Setelah semua item dicetak, total harga keseluruhan juga dicetak.

Program Utama pada Line 46 - 64 :
- Program ini berjalan dalam loop tak terbatas (while True) yang menampilkan menu utama kepada pengguna.
- Pengguna dapat memilih opsi dengan memasukkan angka yang sesuai.
- Berdasarkan pilihan pengguna, program akan memanggil fungsi yang sesuai (menampilkan daftar barang, menambahkan barang, mencetak struk, atau keluar dari program).
- Jika pengguna memasukkan pilihan yang tidak valid, program akan memberikan pesan kesalahan.

Terimakasih
