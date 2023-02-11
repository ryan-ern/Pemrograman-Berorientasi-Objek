"""
Nama: Ryan Ernanda
NIM: 120140154
Kelas: RA
Program Soal Ke-3
"""
ls = [] #inisialisasi list kosong
dict = {}#inisialisasi Dictionary kosong

n = int(input("Masukan jumlah mahasiswa: "))#input n
print()

for i in range(n): #perulangan dari i=0 sampai ke < n

    dict["nama"] = str(input("Nama mahasiswa {}: " .format(i + 1))) #inisialisasi key nama, meminta value dengan tipe data string  dan perulangan i+1
    dict["nim"] = int(input("Nim mahasiswa {}: " .format(i + 1))) #inisialisasi key nim, meminta value dengan tipe data integer  dan perulangan i+1
    dict["nilai"] = int(input("Nilai mahasiswa {}: " .format(i + 1)))#inisialisasi key nilai, meminta value dengan tipe data integer  dan perulangan i+1
    print()

    ls.append(dict.copy()) #menambahkan list pada urutan terakhir dan mengembalikan nilai dari salinan dict

urut = str(input("Urutkan berdasarkan (nama/nim/nilai): "))#inisialisasi variabel dan input string
urut2 = str(input("Urutkan dari ter (besar/kecil): ")) #inisialisasi variabel dan input string

if urut == "nama":#kondisi jika urut sama dengan nama
    if urut2 == "besar": #kondisi jika urut2 sama dengan besar
        #nested loop
        for i in range(n):
            for j in range(n):
                if ls[j]["nama"] < ls[i]["nama"]:#kondisi nilai j < i dengan key nama
                    ls[i],ls[j]=ls[j],ls[i]#menukarkan isi dari list i, j menjadi j, i

    elif urut2 == "kecil":
        for i in range(n):
            for j in range(n):
                if ls[j]["nama"] > ls[i]["nama"]:
                    ls[j],ls[i]=ls[i],ls[j]#menukarkan isi dari list j,i menjadi i,j

elif urut == "nim":
    if urut2 == "besar":
        for i in range(n):
            for j in range(n):
                if ls[j]["nim"] < ls[i]["nim"]:
                    ls[i],ls[j]=ls[j],ls[i]#menukarkan isi dari list i, j menjadi j, i

    elif urut2 == "kecil":
        for i in range(n):
            for j in range(n):
                if ls[j]["nim"] > ls[i]["nim"]:
                    ls[j],ls[i]=ls[i],ls[j]#menukarkan isi dari list j,i menjadi i,j

elif urut == "nilai":

    if urut2 == "besar":
        for i in range(n):
            for j in range(n):
                if ls[j]["nilai"] < ls[i]["nilai"]:
                    ls[j],ls[i]=ls[i],ls[j]#menukarkan isi dari list i, j menjadi j, i

    elif urut2 == "kecil":
        for i in range(n):
            for j in range(n):
                if ls[j]["nilai"] > ls[i]["nilai"]:
                    ls[j],ls[i]=ls[i],ls[j]#menukarkan isi dari list j,i menjadi i,j

print()
for i in range(n):
    #mencetak dari list i dengan masing" key
    print(ls[i]["nama"], end=" ")
    print(ls[i]["nim"], end=" ")
    print(ls[i]["nilai"],)
