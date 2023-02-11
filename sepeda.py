class Sepeda:
    jumlah_sepeda=0

    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna
        self.max_speed=40
        Sepeda.jumlah_sepeda +=1

sepeda = Sepeda('Sepeda', 'Hitam')
sepeda = Sepeda('Sepeda', 'Hitam')
sepeda = Sepeda('Sepeda', 'Hitam')

print(sepeda.jumlah_sepeda)