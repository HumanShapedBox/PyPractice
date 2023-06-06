import os, sys
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = None

def new_note():
    global file_name
    file_name = "New file"
    text.delete('1.0', END)

window = Tk()
window.title("Notes")
window.geometry("800x600")

text = Text(window, width=800, height=600)
text.pack()

menu_bar = Menu(window)
file_menu = Menu(menu_bar)

menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)

window.mainloop()





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

