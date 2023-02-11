# Nama: Ryan Ernanda
# NIM: 120140154
# Kelas: PBO RA

# Membuat kelas TokoBuku.
class TokoBuku():
    # Konstruktor.
    def __init__(self):
        self.__list_buku = [] # array/ list {nama, genre, penulis, tahun}

        # Menjalankan dan Menambahkan list data buku.
        self.__jumlah()

    # Menampilkan menu.
    def menu(self):
        # Info menu.
        print("\nToko Buku Gramedia")
        print("1) Tambah buku baru")
        print("2) Liat list buku")
        print("3) Modifikasi buku lama")
        print("4) Hapus buku lama")
        print("5) Keluar program")

        # Menu.
        Pilihan = int(input("Masukan nomor input: "))
        if Pilihan == 1:
            self.__create()
        elif Pilihan == 2:
            self.__read()
        elif Pilihan == 3:
            self.__update()
        elif Pilihan == 4:
            self.__delete()
        elif Pilihan == 5:
            exit()
        else:
            print('\nPilihan tidak tersedia!')
        
        # Rekur
        self.menu()

    # Menambahkan jumlah daftar buku. 
    def __jumlah(self):
        jum_buku = int(input("Masukan jumlah buku mula-mula: "))
        for i in range(jum_buku):
            self.__create()

    # Menambahkan daftar buku.
    def __create(self):
        create=self.__list_buku
        buku = {}
        buku["nama"] = input("\nMasukan nama buku: ")
        buku["genre"] = input("Masukan genre buku: ")
        buku["penulis"] = input("Masukan penulis buku: ")
        buku["tahun"] = input("Masukan tahun terbit buku: ")
        if(buku["nama"] != "" and buku["genre"] != "" and buku["penulis"] != "" and buku["tahun"] != ""):
            print("Buku berhasil ditambahkan!")
            create.append(buku)
        else:
            print("Data Tidak Lengkap\nHarap isi Data dengan Lengkap")
            self.__create()

    # Menampilkan daftar buku yang ada.
    def __read(self):
        print('')
        buku_save = self.__list_buku
        for i in range(len(buku_save)):
            buku = buku_save[i]
            print("{}. {} {} {} {}".format(i + 1, buku["nama"], buku["genre"], buku["penulis"], buku["tahun"]))
        if not len(buku_save):
            print('Daftar buku masih kosong!')

    # Update data buku.
    def __update(self):
        nama = input("\nMasukan judul yang ingin diedit: ")
        buku_up = self.__list_buku
        for i in range(len(buku_up)):
            buku = buku_up[i]
            if nama == buku["nama"]:
                data = {}
                data["nama"] = input("Edit nama buku ({}): ".format(buku["nama"]))
                data["genre"] = input("Edit genre buku ({}): ".format(buku["genre"]))
                data["penulis"] = input("Edit penulis buku ({}): ".format(buku["penulis"]))
                data["tahun"] = input("Edit tahun buku ({}): ".format(buku["tahun"]))
                if(data["nama"] != data["nama"] or data["genre"] != data["genre"] or data["penulis"] != data["penulis"] or data["tahun"] != data["tahun"]):
                    print("Data Berhasil Diubah!")
                    self.__list_buku[i] = data
                else:
                    print("Data Tidak Berubah!")
                    self.__update()

    # Mmenghapus data buku.
    def __delete(self):
        nama = input("\nMasukan judul yang ingin dihapus: ")
        buku_del = self.__list_buku
        for i in range(len(buku_del)):
            buku = buku_del[i]
            if nama == buku["nama"]:
                print("Buku Berhasil Dihapus!")
                del buku_del[i]

# Inisialisasi kelas dan menjalankan objek.
toko_buku = TokoBuku() # Inisialisasi.
toko_buku.menu() # Menampilkan daftar menu.