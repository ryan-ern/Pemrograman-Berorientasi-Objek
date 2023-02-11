'''
Nama    : Ryan Ernanda
NIM     : 120140154
Kelas   : PBO-RA
'''

import random
import tkinter as tk
import tkinter.font as tkFont

#membuat jendela tkinter
root = tk.Tk()
root.geometry("300x450")
root.minsize(300,450)
root.title("Ryan Batu Gunting Kertas")

#label
judul=tk.Label(root)
ft = tkFont.Font(family='Times',size=16)
judul["font"] = ft
judul["fg"] = "#333333"
judul["justify"] = "center"
judul["text"] = "Pengguna VS Bot"
judul.place(x=50,width=200,height=25)

#inisiasi variabel global
Skor_pengguna = 0
Skor_komputer = 0
pilihan_pengguna = ""
pilihan_komputer = "" 

#fungsi dua metode
def pilih_nomor(pilihan):
    choose = {'batu':0,'kertas':1,'gunting':2}
    return choose[pilihan]
def nomor_dipilih(nomor):
    choose= {0:'batu',1:'kertas',2:'gunting'}
    return choose[nomor]

#fungsi komputer memilih random
def komputer_pilih_random():
    return random.choice(['batu','kertas','gunting']) 

#area text
def hasil(pilihan_pengguna,pilihan_komputer):
    global Skor_pengguna
    global Skor_komputer
    user=pilih_nomor(pilihan_pengguna)
    pc=pilih_nomor(pilihan_komputer)
    if(user==pc):
        print("Seri")
    elif(user==0 and pc == 2 or user == 1 and pc == 0 or user ==2 and pc==1):
        print("Kamu Menang")
        Skor_pengguna+=1
    else:
        print("Komputer Menang")
        Skor_komputer+=1
    answer = "Pilihan User: {pu} \nPilihan Komputer : {pc} \n Skor Kamu : {u} \n Skor Komputer : {c} ".format(pu=pilihan_pengguna,pc=pilihan_komputer,u=Skor_pengguna,c=Skor_komputer)    
    text_area.delete(1.0,tk.END)
    text_area.insert(tk.END,answer)

#fungsi 3 metode pilihan
def batu():
    global pilihan_pengguna
    global pilihan_komputer
    pilihan_pengguna='batu'
    pilihan_komputer=komputer_pilih_random()
    hasil(pilihan_pengguna,pilihan_komputer)

def kertas():
    global pilihan_pengguna
    global pilihan_komputer
    pilihan_pengguna='kertas'
    pilihan_komputer=komputer_pilih_random()
    hasil(pilihan_pengguna,pilihan_komputer)

def gunting():
    global pilihan_pengguna
    global pilihan_komputer
    pilihan_pengguna='gunting'
    pilihan_komputer=komputer_pilih_random() 
    hasil(pilihan_pengguna,pilihan_komputer)

#area text
text_area = tk.Text(master=root,height=12,width=30,bg="#FFFF99")
text_area.grid(column=0,row=1,padx=30, pady=50, sticky='ew')
answer = "Pilihan User: {pu} \nPilihan Komputer : {pc} \n Skor Kamu : {u} \n Skor Komputer : {c} ".format(pu='-',pc='-',u='-',c='-')    
text_area.insert(tk.END,answer)

#tiga tombol
button1 = tk.Button(text="Batu",bg="skyblue",command=batu)
button1.grid(column=0,row=2, sticky='ew', padx=25, pady=7)
button2 = tk.Button(text="Gunting",bg="pink",command=gunting)
button2.grid(column=0,row=3, sticky='ew', padx=25, pady=7)
button3 = tk.Button(text="Kertas",bg="lightgreen",command=kertas)
button3.grid(column=0,row=4, sticky='ew', padx=25, pady=7)

#run semua ke window
root.mainloop()