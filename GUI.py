import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Teks Editor")
        #setting window size
        width=900
        height=800
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_911=tk.Entry(root)
        GLineEdit_911["borderwidth"] = "1px"
        GLineEdit_911["disabledforeground"] = "#982626"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_911["font"] = ft
        GLineEdit_911["fg"] = "#000000"
        GLineEdit_911["justify"] = "left"
        GLineEdit_911["text"] = "Entry"
        GLineEdit_911.place(x=100,y=0,width=800,height=800)

        GButton_328=tk.Button(root)
        GButton_328["activebackground"] = "#ee3232"
        GButton_328["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_328["font"] = ft
        GButton_328["fg"] = "#000000"
        GButton_328["justify"] = "center"
        GButton_328["text"] = "Buka"
        GButton_328.place(x=10,y=30,width=80,height=30)
        GButton_328["command"] = self.GButton_328_command

        GButton_102=tk.Button(root)
        GButton_102["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_102["font"] = ft
        GButton_102["fg"] = "#000000"
        GButton_102["justify"] = "center"
        GButton_102["text"] = "Save"
        GButton_102.place(x=10,y=80,width=80,height=30)
        GButton_102["command"] = self.GButton_102_command

    def GButton_328_command(self):
        print("command")


    def GButton_102_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
