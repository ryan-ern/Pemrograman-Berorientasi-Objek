"""
Nama: Ryan Ernanda
NIM: 120140154
Kelas: PBO RA
"""

# Membuat parent class yaitu Robot
class Robot:  
    jumlah_turn = 0 
    # Konstruktor
    def __init__(self, nama, health, menyerang):
        self.nama = nama
        self.health = health
        self.menyerang = menyerang

    # untuk melakukan aksi menyerang ke musuh
    def lakukan_aksi(self, musuh):
        musuh.health -= self.menyerang

# Membuat child class yaitu Antares dari parent class
class Antares(Robot): 
    # Memiliki base health 50000 HP dengan base attack 5000 DMG
    def __init__(self):
        super().__init__("Antares", 50000, 5000)

    # didalam fungsi ini terdapat proses yang dapat melakukan proses seperti dibawh ini
    def lakukan_aksi(self, musuh):
        if Robot.jumlah_turn % 3 == 0:
            # if jika kondisi ini benar maka akan melakukan proses ini, jika kondisi ini bernoilai salah maka akan menjalankan program yang lain.
            menyerang_tambahan = int(self.menyerang * 0.5)
            self.menyerang += menyerang_tambahan
            super().lakukan_aksi(musuh)
            print("Robot ({}) menyerang sebanyak {} DMG".format(
                self.nama, self.menyerang))
            self.menyerang -= menyerang_tambahan
        else:  # program selain if atau program kondisi setelahnya
            super().lakukan_aksi(musuh)
            print("Robot ({}) menyerang sebanyak {} DMG".format(
                self.nama, self.menyerang))

# Membuat child class yaitu Lecalicus dari parent class
class Lecalicus(Robot):  
    # Memiliki base health 45000 HP dengan base attack 5500 DMG
    def __init__(self):
        super().__init__("Lecalicus", 45000, 5500)

    # Dalam melakukan aksi, health pada Lecalicus akan bertambah sebanyak 7000 HP dan damage nya akan menjadi 2x lipat secara sementara (1 turn)
    def lakukan_aksi(self, musuh):
        if Robot.jumlah_turn % 4 == 0:
            self.health += 7000
            print("Robot ({}) menambah darah sebanyak 4000 HP".format(self.nama))
            menyerang_tambahan = self.menyerang
            self.menyerang += menyerang_tambahan
            super().lakukan_aksi(musuh)
            print("Robot ({}) menyerang sebanyak {} DMG".format(self.nama, self.menyerang))
            self.menyerang -= menyerang_tambahan
        else:
            super().lakukan_aksi(musuh)
            print("Robot ({}) menyerang sebanyak {} DMG".format(
                self.nama, self.menyerang))

# Membuat child class yaitu Alphasetia dari parent class
class Alphasetia(Robot):  
    # Memiliki base health 40000 HP dengan base attack 6000 DMG
    def __init__(self):
        super().__init__("Alphasetia", 40000, 6000)

    # health Alphasetia akan bertambah sebanyak 4000 HP dan damage nya akan menjadi 2x lipat secara sementara (1 turn)
    def lakukan_aksi(self, musuh):
        if Robot.jumlah_turn % 2 == 0:
            self.health += 4000
            print("Robot ({}) menambah darah sebanyak 4000 HP".format(self.nama))
        super().lakukan_aksi(musuh)
        print("Robot ({}) menyerang sebanyak {} DMG".format(self.nama, self.menyerang))

# Menampilkan teks selamat datang
print("Selamat datang di pertandingan Robot Yamako")
# Menampilkan pilihan robot yang ingin diinputkan
pilih_robot = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
pilih_lawan = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
# program mmenampilkan beberapa pilihan jika 1 untuk batu 2 untuk kertas dan 3 untuk gunting sebagai berikut.
print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")

# Menampilkan navigasi pilihan robot yang ingin diinputkan
if pilih_robot == 1:
    # percabangan if daan menampilkan fungsi dibawah ini
    myrobot = Antares()
elif pilih_robot == 2:
    # percabangan if daan menampilkan fungsi dibawah ini
    myrobot = Alphasetia()
else:
    # percabangan if daan menampilkan fungsi dibawah ini
    myrobot = Lecalicus()

# Menampilkan navigasi pilihan robot lawan yang ingin diinputkan
if pilih_robot == 1:
    enemyrobot = Antares()
elif pilih_robot == 2:
    enemyrobot = Alphasetia()
else:
    enemyrobot = Lecalicus()

""" Porses program untuk menyelesaikan soal kali ini """
# perulangan while jika tangan_myrobot.health > 0 and tangan_enemyrobot.health > 0, kemudian dilakukan proses seperti dibawah ini.
while myrobot.health > 0 and enemyrobot.health > 0:
    print()
    Robot.jumlah_turn += 1
    print("Turn saat ini: {}".format(Robot.jumlah_turn))
    print("Robotmu ({} - {} HP), robot lawan ({} - {} HP)".format(myrobot.nama,
          myrobot.health, enemyrobot.nama, enemyrobot.health))

    tangan_myrobot = int(input("Pilih tangan robotmu ({}): ".format(myrobot.nama)))
    tangan_enemyrobot = int(input("Pilih tangan robot lawan ({}): ".format(enemyrobot.nama)))

    if tangan_myrobot == tangan_enemyrobot:
        print("Pertandingan Seri")
    elif tangan_myrobot - tangan_enemyrobot== 1 or tangan_myrobot - tangan_enemyrobot== -1:
        if tangan_myrobot > tangan_enemyrobot:
            myrobot.lakukan_aksi(enemyrobot)
        else:
            enemyrobot.lakukan_aksi(myrobot)
    else:
        if tangan_myrobot < tangan_enemyrobot:
            myrobot.lakukan_aksi(enemyrobot)
        else:
            enemyrobot.lakukan_aksi(myrobot)

# jika tangan_enemyrobot.health <= 0 dan ellse maka menampilkan kondisi dibawah ini.
if enemyrobot.health <= 0:
    print("Robotmu ({}) memenangkan pertandingan".format(myrobot.nama))
else:
    print("Robot lawan ({}) memenangkan pertandingan".format(enemyrobot.nama))