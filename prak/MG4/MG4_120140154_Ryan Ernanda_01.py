"""
Nama: Ryan Ernanda
NIM: 120140154
Kelas: PBO RA
"""

# Membuat parent class Komputer.
class Komputer:
    # Konstruktor.
    def __init__(self, nama, jenis, merk, harga):
        self.nama = nama
        self.jenis = jenis
        self.merk = merk
        self.harga = harga

# Membuat child class Processor dalam parent class 
class Processor(Komputer):
    # Konstruktor.
    def __init__(self, merk, nama, harga, jumlah_core, kecepatan_processor):
        super().__init__(nama, 'CPU', merk, harga) # Mengambil atribut dari parent class Komputer
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

# Membuat child class RAM dalam parent class 
class RAM(Komputer):
    # Konstruktor.
    def __init__(self, merk, nama, harga, capacity):
        super().__init__(nama, 'RAM', merk, harga) # Mengambil atribut dari parent class Komputer
        self.capacity = capacity

# Membuat child class HDD dalam parent class 
class HDD(Komputer):
    # Konstruktor.
    def __init__(self, merk, nama, harga, capacity, rpm):
        super().__init__(nama, 'HDD', merk, harga) # Mengambil atribut dari parent class Komputer
        self.capacity = capacity
        self.rpm = rpm

# Membuat child class VGA dalam parent class 
class VGA(Komputer):
    # Konstruktor.
    def __init__(self, merk, nama, harga, capacity):
        super().__init__(nama, 'VGA', merk, harga) # Mengambil atribut dari parent class Komputer
        self.capacity = capacity

# Membuat child class PSU dalam parent class 
class PSU(Komputer):
    # Konstruktor.
    def __init__(self, merk, nama, harga, daya):
        super().__init__(nama, 'PSU', merk, harga) # Mengambil atribut dari parent class Komputer
        self.daya = daya

# Inisialisasi class komponen komputer.
p1 = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz')
p2 = Processor('AMD', 'Ryzen 5 3600', 250000, 4, '4.3GHz')
ram1 = RAM('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
ram2 = RAM('G.SKILL', 'DDR4 2400MHz', 328000, '4GB')
hdd1 = HDD('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)
hdd2 = HDD('Seagate', 'HDD 2.5 inch', 295000, '1000GB', 7200)
vga1 = VGA('Asus', 'VGA GTX 1050', 250000, '2GB')
vga2 = VGA('Asus', '1060Ti', 250000, '8GB')
psu1 = PSU('Corsair', 'Corsair V550', 250000, '500W')
psu2 = PSU('Corsair', 'Corsair V550', 250000, '500W')

# Merakit komponen menjadi komputer ke 1.
pc1 = [p1, ram1, hdd1, vga1, psu1]
print("Komputer 1")
for komponen in pc1:    
    print(f"{komponen.jenis} {komponen.nama} produksi {komponen.merk}")

# Merakit komponen menjadi komputer ke 2.
pc2 = [p2, ram2, hdd2, vga2, psu2]
print("\nKomputer 2")
for komponen in pc2:    
    print(f"{komponen.jenis} {komponen.nama} produksi {komponen.merk}")