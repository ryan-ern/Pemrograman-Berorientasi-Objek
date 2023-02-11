# Program Aplikasi Teks Editor
import tkinter as tk
from tkinter import CENTER, font
from tkinter.filedialog import *

#membuat jendela tkinter
root = tk.Tk()
root.title('Text Editor Ryn')
root.minsize(900,800)

#fungsi buka file
def openfile():
    print("Buka File")
    path = askopenfilename (
        filetypes = [('Text Files','.txt'),('All Files','.*')]
    )
    if not path:
        return 
    text.delete('1.0', tk.END)
    with open(path, mode = 'r', encoding = 'utf-8') as file_dibuka:
        teks = file_dibuka.read()
        text.insert(tk.END, teks)
    root.title(path)

#fungsi menyimpan file
def savefile():
    print("Menyimpan File")
    path = asksaveasfilename(
        defaultextension='.txt',
        filetypes = [('Text Files','.txt'),('All Files','.*')],
    )
    if not path:
        return
    with open(path, mode='w', encoding='utf-8') as file_tampil:
        teks = text.get('1.0', tk.END)
        file_tampil.write(teks)
    
    root.title(path)

# frame tombol dan teks
fm_tombol = tk.Frame(
    master = root, 
    bg = '#1bb7c2'
)
fm_tombol.pack(fill = tk.BOTH, side = tk.LEFT)

frme_teks = tk.Frame(
    master = root, 
    width = 800
)
frme_teks.pack(fill = tk.BOTH, side=tk.RIGHT, expand = 1)
text = tk.Text(master=frme_teks)
text.pack(fill =tk.BOTH, expand= 1)

# buat tombol
bttn_open = tk.Button(master=fm_tombol, bg='#15d49b', fg='#fff', text='Open', command=openfile)
bttn_save = tk.Button(master=fm_tombol, bg='#15d49b', fg='#fff', text='Save As', command=savefile)

# grid tombol
bttn_open.grid(row=0, column=0, sticky='ew', padx=25, pady=7)
bttn_save.grid(row=1, column=0, sticky='ew', padx=25, pady=7)

root.mainloop()