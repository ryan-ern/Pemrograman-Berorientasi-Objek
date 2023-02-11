class Pemain:
    def __init__(self, nama, health_point = 30):
        self.__nama = nama
        self.__health_point = health_point
    
    #Getter
    @property
    def health_point(self):
        return self.__health_point

    #Setter
    @health_point.setter
    def health_point(self, health_point_baru):
        self.__health_point = health_point_baru

    #Getter
    @property
    def nama(self):
        return self.__nama

PemainA = Pemain(input("Masukan nama Pemain A"))
PemainB = Pemain(input("Masukan nama Pemain B"))

print("Permainan gunting baru kertas")
print("Pilih 1 untuk batu, 2 untuk kertas, 3 untuk gunting")

while PemainA.health_point != 0 and PemainB != 0:#perulangan dari 0 sampai n
    print()
    a = int(input("Tangan Pemain A: ")) #meminta inputan dari nilai a
    if(a <1 or a>3):#kondisi digunakan jika inputan tidak sesuai dengan yang disediakan
        print("Pilihan tidak tersedia")
        break
    b = int(input("Tangan Pemain B: "))
    if(b <1 or b>3):
        print("Pilihan tidak tersedia")
        break

    if (a == 1 and b==1 or a==2 and b == 2 or a==3 and b ==3):#kondisi jika nilai a & b bernilai sama
        print("Hasil seri")
    elif (a==1 and b == 3 or a==2 and b==1 or a==3 and b==2):#kondisi jika nilai a > b
        print("Pemain A Menang")
        PemainB.health_point -= 10 #kondisi benar maka nilai_a sebelumnya ditambah 1
    elif (a==1 and b == 2 or a==2 and b==3 or a==3 and b==1):#kondisi jika nilai b > a
        print("Pemain B menang")
        PemainA.health_point -=10 #kondisi benar maka nilai_b sebelumnya ditambah 1

print("\nHasil akhir ", end="- ")

