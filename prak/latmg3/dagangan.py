class Dagangan:
    jumlah_barang=0
    list_barang=[]
    #inisialisasi atribut / Konstruktor
    def __init__(self, nama, stok, harga): 
        Dagangan.jumlah_barang +=1
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.list_barang.append(self)

    def lihat_barang(self):
        print("Nama : ", self.__nama)
        print("Stok :", self.__stok)
        print("Harga :", self.__harga)
        print()

#instansiasi Objek
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 Kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68888)


#akses atribut objek & fungsi
i=0
print("Total laptop:", Dagangan.jumlah_barang,"\n")
print(Dagangan.lihat_barang)
Dagangan.lihat_barang()

