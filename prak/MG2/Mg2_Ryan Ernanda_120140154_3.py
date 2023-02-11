# Nama: Ryan Ernanda
# NIM: 120140154
# Kelas: PBO RA
"""
Saya memngambil studi kasus tentang manajemen barang laptop, yang saya implementasikan ke PBO. pada kasus ini saya menggunakan class laptop sebagai templat untuk tempat barangnya dan berfungsi untuk mendeklarasikan sebuah objek. kelas ini memiliki atribut merek, tipe, ram, str(storage), harga.
yang bisa dilakukan oleh kelas ini hanya melihat barang dan mengubah harga barang.
"""
class Laptop:
    jumlah_laptop=0
    #inisialisasi atribut / Konstruktor
    def __init__(self, merek, tipe, ram, str, harga): 
        Laptop.jumlah_laptop +=1
        self.merek = merek
        self.tipe = tipe
        self.ram = ram
        self.str = str
        self.harga = harga

    def lihat(self):
        print("Merek : ", self.merek)
        print("Tipe :", self.tipe)
        print("RAM :", self.ram, "GB")
        print("Storage :", self.str)
        print("Harga :", self.harga)
        print()

    def ubah_harga(self, harga_baru):
        return f"Laptop Merek {self.merek}, Dengan Tipe {self.tipe}, RAM {self.ram}GB dan Storage {self.str} \nBerubah Dari Harga {self.harga}, Menjadi Rp.{harga_baru}\n"

#instansiasi Objek
laptop1 = Laptop("Acer", "Z476-31TB", 8, "1TB HDD", "Rp.16.000.000")
laptop2 = Laptop("Asus", "ROG", 16, "512GB HDD&128GB SSD", "Rp.28.000.000")
laptop3 = Laptop("lenovo", "legion", 32, "1TB HDD/512GB SSD", "Rp.23.000.000")

#akses atribut objek & fungsi
i=0
print("Total laptop:", Laptop.jumlah_laptop,"\n")
for laptop in laptop1, laptop2, laptop3:
    laptop.lihat()
pil=input("Apakah Anda Ingin Update Harga?(yes)\n:")
if pil=="yes":
    for harga_laptop in laptop1, laptop2, laptop3:
        i+=1
        print(harga_laptop.ubah_harga(input(f"Ubah Harga Laptop ke-{i}:\nRp.")))  