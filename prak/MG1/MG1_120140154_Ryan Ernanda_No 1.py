"""
Nama: Ryan Ernanda
NIM: 120140154
Kelas: RA
Program Soal Ke-1
"""
bil = int(input("Masukan bilangan : "))
print("Faktor dari", bil ,"adalah : ")# inisialisasi variabel sebuah integer, meminta inputan dan print

for i in range(1, bil+1): #perulangan bilangan dari 1 sampai nilai bil + 1

    if (bil % i == 0): # kondisi jika bil % i adalah 0 bernilai benar

        print(i, end=" ")# menampilkan nilai i
        bagi =(bil / i)# variable operasi hasil bagi dari faktor
        print("{:.0f}".format(bagi), end=" ")# menampilkan faktor dan presisi desimal

    if (i == bagi): 
        break  #kondisi jika nilai i sama dengan nilai bagi maka perulangan akan dihentikan secara paksa
        