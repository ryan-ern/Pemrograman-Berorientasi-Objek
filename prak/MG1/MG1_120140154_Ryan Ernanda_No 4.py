"""
Nama: Ryan Ernanda
NIM: 120140154
Kelas: RA
Program Soal Ke-4
"""

#fungsi transpose list
def transpose(ls):
    #jumlah lebar kolom
    length_kolom = len(ls[0])
    
    #Inisialisasi list kosong
    ls2 = []
    
    #perulangan list untuk proses transpose
    for i in range(0,length_kolom):
        row = []
        for x in ls:
            row.append(x[i])
        ls2.append(row)
    return ls2

#Fungsi enkripsi kata
def enkripsi(kata,jumlah_bagi):
    #mengganti semua spasi menjadi tidak ada
    kata = kata.replace(" ","")
    
    #Inisialisasi panjang kata
    length = len(kata)
    
    #Inisialisasi list kosong
    ls = []
    
    #Memisahkan kata sesuai jumlah baginya
    for i in range(0,length,jumlah_bagi):
        ls.append(kata[i:i+jumlah_bagi])
    
    #Menambahkan digit 0 di akhir kata jika ada yang kosong
    for i,x in enumerate(ls):
        if len(x)<jumlah_bagi:
            jumlah_digit_kurang = jumlah_bagi-len(x)
            for j in range(0,jumlah_digit_kurang):
                ls[i] = ls[i]+"0"
                
    #Inisialisasi list kosong
    ls2 = []      
    
    #memisah list kata menjadi per karakter agar bisa ditranspose
    for x in ls:
        row = []
        for i in range(0,len(x)):
            row.append(x[i])
        ls2.append(row)
    
    #Menjalankan fungsi transpose
    ls2 = transpose(ls2)
    
    #Menyusun hasil enkripsi ke bentuk kalimat
    hasil = ""
    for x in ls2:
        for y in x:
            hasil = hasil+y
        hasil = hasil+" "
        
    return hasil

#Fungsi untuk dekripsi kata
def dekripsi(kata,jumlah_bagi):   
    #mengganti semua spasi menjadi tidak ada
    kata = kata.replace(" ","")
    
    #Inisialisasi panjang kata
    length = len(kata)
    
    #Inisialisasi list kosong
    ls = []
    
    #Jumlah baris dekripsi
    jumlah_baris = int(length/jumlah_bagi)
    
    #Memisah kata sesuai jumlah baris dekripsinya
    for i in range(0,length,jumlah_baris):
        ls.append(kata[i:i+jumlah_baris])
        
    #Inisialisasi list kosong
    ls2 = []      
    
    #Memisah list kata menjadi per karakter agar bisa ditranspose
    for x in ls:
        row = []
        for i in range(0,len(x)):
            row.append(x[i])
        ls2.append(row)
      
    #Menjalankan fungsi transpose
    ls2 = transpose(ls2)
    
    hasil = ""
    for x in ls2:
        for y in x:
            hasil = hasil+y
    
    #Menyusun hasil dekripsi
    for i in range(0,len(hasil)):
        if hasil[-1:] == "0":
            hasil = hasil[:-1]
        
    return hasil
 
#meminta input dari user 
kata = input("Masukkan kata: ")
metode = int(input("Metode (1 = enkripsi, 2 = dekripsi): "))
jumlah_bagi = int(input("Jumlah pembagian huruf: "))
print("")

#Menjalankan fungsi enkripsi / dekripsi sesuai pilihan user dan mencetak jawabannya
if metode == 1:
    hasil = enkripsi(kata,jumlah_bagi)
    print("Hasil:",hasil)
elif metode == 2:
    hasil = dekripsi(kata,jumlah_bagi)
    print("Hasil:",hasil)
else:
    print("Input Tidak Tersedia")