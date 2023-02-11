class Handphone:
    #konstruktor
    def __init__(self, merek, model, ram, jumlah_stok, harga):
        self.merek_hp =merek
        self.model_hp =model
        self.ram_hp=ram
        self.jumlah_stok_hp= jumlah_stok
        self.harga_hp=harga

    #Getter
    def lihat_stok(self):
        return f"{self.merek_hp} {self.model_hp} {self.ram_hp} dengan harga Rp {self.harga_hp} tersisa {self.jumlah_stok_hp} dengan harga {self.harga_hp} buah"

    #setter
    def ubah_stok(self, stok_baru):
        return f"stok {self.merek_hp} {self.model_hp} terjual dari {self.jumlah_stok_hp} menjadi {stok_baru}"


Handphone1 = Handphone("Samsung", "Galaxy", "8 GB", 200, 53000)
Handphone2 = Handphone("Xiaomi", "Redmi", "4 GB", 400, 63000)
Handphone3 = Handphone("Apple", "SE", "16 GB", 300, 222000)

#dock typing
for handphone in Handphone1, Handphone2, Handphone3:
    print(handphone.lihat_stok())

print()
print(Handphone1.ubah_stok(180))
print(Handphone2.ubah_stok(200))
print(Handphone3.ubah_stok(250))