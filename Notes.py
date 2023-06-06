import os, sys
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

window = Tk()
window.title("Notes")
window.geometry("800x600")

menu_bar = Menu(window)
file_menu = Menu(menu_bar)

menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)

window.mainloop()



def addNote():
    # some code
    pass

def saveNote():
    # some code
    pass

def readNote():
    # some code
    pass

def changeNote():
    # some code
    pass

def delNote():
    # some code
    pass

