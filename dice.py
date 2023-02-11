from tkinter import *
import random
import tkinter.font as tkFont

root=Tk()
root.geometry("700x450")
root.title("Dean: Roll Dice")

label=Label(root,text="",font=("Courier",200))

def roll():
    a=0
    dadu=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    ab=str(random.choice(dadu))
    ac=str(random.choice(dadu))
    label.configure(text=f'{ab}{ac}')
    label.pack()
    if(ab=='\u2680' and ac=='\u2680' or ab=='\u2681' and ac=='\u2681' or ab=='\u2682' and ac=='\u2682' or ab=='\u2683' and ac=='\u2683' or ab=='\u2684' and ac=='\u2684' or ab=='\u2685' and ac=='\u2685'):
        print("You Win")
    else:
        print("You Lose")
    
button=Button(root,bg="#428aa7",fg="white",text="klik untuk mulai",width=30,height=5,bd=2,command=roll)
button.config(font=("Courier",10))
button.pack(padx=10,pady=10)

root.mainloop()