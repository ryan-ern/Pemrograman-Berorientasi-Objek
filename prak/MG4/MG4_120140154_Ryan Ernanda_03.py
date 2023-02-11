"""
Nama: Ryan Ernanda
NIM: 120140154
Kelas: PBO RA
"""
#membuat class hewan
class Hewan:
    #konstruktor
  def __init__(self, nama, usia):
    self.nama = nama
    self.usia = usia

  def makan(self):
    print(self.nama, " sedang makan...")

#membuat child class balok burung dari parent hewan
class Burung(Hewan):
  def __init__(self, nama, usia, warna):
    #penerapan inheritance
    super().__init__(nama, usia)
    self.warna = warna
  def terbang(self):
    print(self.nama, " sedang terbang")

cuckoo = Burung("Cuckoo", 2, ["Kuning", "Putih"])
print(cuckoo.nama)
print(cuckoo.usia)
print(cuckoo.warna)
cuckoo.makan()
cuckoo.terbang()
