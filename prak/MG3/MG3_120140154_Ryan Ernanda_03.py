"""
Nama: Ryan Ernanda
NIM: 120140154
Kelas: RA

Penjelasan Program : 
Penggunaan access modifier bertujuan dalam melindungi akses data, memodifikasi data, 
dan memberi tahu lokasi data digunakan. Class Restoran sifatnya protected karena pada data tersebut
perlu digunakan pada class lain. atribut class Jabat menggunakan private untuk data bersumber dari luar. 
"""

# Membuat class Restoran.
class Restoran:
    # Konstruktor.
    def __init__(self, nama_Restoran, lokasi):
        # Atribut protect.
        self._nama_Restoran = nama_Restoran
        self._lokasi = lokasi

    # lokasi restoran.
    def getter_lokasi(self):
        return f"Restoran {self._nama_Restoran} dengan lokasi {self._lokasi}."

# Membuat anak class Jabat
class Jabat(Restoran):
    # Konstruktor.
    def __init__(self, Restoran, nama, jabatan):
        # Attribut private untuk modifikasi data dalam class sendiri.
        self.__nama= nama
        self.__jabatan = jabatan
        # Inisialisasi dengan tujuan class parent.
        super().__init__(Restoran._nama_Restoran, Restoran._lokasi)

    # get info Jabat di Restoran.
    def getter_info(self):
        # Akses private pada atribut dan protect untuk class lain
        nama = self.__nama
        jabatan = self.__jabatan 
        nama_Restoran = self._nama_Restoran
        return f"{nama} dengan jabatan {jabatan} di {nama_Restoran}."

"""        
Implementasi class Restoran dan anak class Jabat.
"""

# Inisialisasi objek dari setiap Restoran.
Restoran1 = Restoran("Bakso", "Bandar Lampung")
Restoran2 = Restoran("Nasi Padang", "Padang")
Restoran3 = Restoran("Mie", "Kota China")
# Inisialisasi objek dari setiap Jabat.
Jabat1 = Jabat(Restoran1, "Ryan Ernanda", "Pemilik")
Jabat2 = Jabat(Restoran2, "Elon Musk", "Manajer")
Jabat3 = Jabat(Restoran3, "Agung", "Karyawan")
# Memanggil get_lokasi() bersifat public.
for Resto in Restoran1, Restoran2, Restoran3:
    print(Resto.getter_lokasi()) 
print("")
# Memanggil get_info() bersifat public.
for penjabat in Jabat1, Jabat2, Jabat3:
    print(penjabat.getter_info()) 