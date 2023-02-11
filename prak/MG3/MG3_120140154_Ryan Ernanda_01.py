'''
Nama: Ryan Ernanda
NIM: 120140154
Kelas: RA
'''
# Py moduls.
import random 

## Membuat class.
class Kotak:
    # Konstruktor.
    def __init__(self):
        # bom  kosong
        self.__isi = "!bom"
        # belum terbuka 
        self.__status = "!terbuka" 
        self.jumlah_bom = 0

    def getter_isi(self):
        return self.__isi

    def getter_status(self):
        return self.__status

    def setter_isi(self, isi):
        self.__isi = isi
        
    def tampilkan(self):
        symbol = "?"
        if self.__status == "terbuka":
            if self.__isi == "!bom":
                symbol = "o"
            else:
                symbol = "x"
        print(symbol, end = " ")

    def buka_kotak(self):
        self.__status = "terbuka"

class Minesweeper:
    def __init__(self):
        self.__dimensi_area = 3
        self.__jumlah_bom = 0
        self.__daftar_kotak = []
        self.__kotak_terbuka = 0

    def generate_area(self):
        # Input area.
        self.__dimensi_area = int(input("Masukan dimensi area: "))
        
        # Generate jumlah bom.
        self.__jumlah_bom = random.randrange(1, int((self.__dimensi_area ** 2) / 2))
        print(f"\nTerdapat {self.__jumlah_bom} bom pada susunan kotak. Harap berhati-hati!")

        # Inisialisasi class kotak.
        for i in range(self.__dimensi_area ** 2):
            kotak = Kotak()
            kotak.jumlah_bom = self.__jumlah_bom
            self.__daftar_kotak.append(kotak)
    
    def random_bom(self, bom_terdaftar = 0):
        # Validasi.
        if bom_terdaftar >= self.__jumlah_bom:
            return True

        # Random index.
        kotak = random.choice(self.__daftar_kotak)
        if kotak.getter_isi() == "!bom":
            kotak.setter_isi("bom")
            bom_terdaftar += 1
        
        # Rekursif
        self.random_bom(bom_terdaftar)

    def mulai(self):
        # Header game.
        print("Permainan Minesweeper")

        # load data game.
        self.generate_area()
        self.random_bom()

        # Memulai permainan.
        self.tampilkan_status_kotak()
        self.tebak_kotak()
    
    def tampilkan_status_kotak(self):
        print("")
        for i in range(self.__dimensi_area ** 2):
            self.__daftar_kotak[i].tampilkan()
            if (i + 1) % self.__dimensi_area == 0:
                print("")
    
    def tebak_kotak(self):
        # Form pilihan
        index_kotak = int(input(f"Masukkan nomor kotak yang ingin dibuka (1-{len(self.__daftar_kotak)}): "))
        kotak = self.__daftar_kotak[index_kotak - 1]
        
        # Membuka kotak dan validasi hasil
        if kotak.getter_isi() == "bom":
            kotak.buka_kotak()
            self.tampilkan_status_kotak()
            self.selesai()
            return
        elif kotak.getter_status() == "!terbuka":
            kotak.buka_kotak()
            self.tampilkan_status_kotak()
            print("Selamat! Kotak tersebut tidak berisi bom.")
            self.__kotak_terbuka += 1

        # Validasi kemenangan.
        if self.__kotak_terbuka >= (len(self.__daftar_kotak) - self.__jumlah_bom):
            self.menang()
            return

        # Rekursif.
        self.tebak_kotak()
            
    def selesai(self):
        print("\nGame over! Kotak tersebut berisi bom.")
        exit()

    def menang(self):
        print("\nSelamat! Anda telah memenangkan game.")
        exit()

## Memulai Game.
minesweeper = Minesweeper()
minesweeper.mulai()
print("")
