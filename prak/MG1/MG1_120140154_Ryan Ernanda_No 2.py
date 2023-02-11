"""
Nama: Ryan Ernanda
NIM: 120140154
Kelas: RA
Program Soal Ke-2
"""
print("Permainan gunting baru kertas")
print("Pilih 1 untuk batu, 2 untuk kertas, 3 untuk gunting")

n = int(input("Berapa kali permainan:"))#inisialisasi variabel sebuah integer, meminta inputan

nilai_a = int(0)#inisialisasi variabel sebuah integer, untuk menyimpan nilai/score dari a
nilai_b = int(0)#inisialisasi variabel sebuah integer, untuk menyimpan nilai/score dari b


for i in range(0, n):#perulangan dari 0 sampai n
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
        nilai_a += 1 #kondisi benar maka nilai_a sebelumnya ditambah 1
    elif (a==1 and b == 2 or a==2 and b==3 or a==3 and b==1):#kondisi jika nilai b > a
        print("Pemain B menang")
        nilai_b += 1#kondisi benar maka nilai_b sebelumnya ditambah 1

print("\nHasil akhir ", end="- ")

#kondisi perbandingan dan mencetak hasil akhir dari permainan
if nilai_a > nilai_b: 
    print("Pemain A menang")
elif nilai_b > nilai_a:
    print("Pemain B menang")
elif nilai_a == 0 and nilai_b==0:
    print("Permainan tidak valid!")
else:
    print("kedua pemain seri")




    