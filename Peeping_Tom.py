import webbrowser
import random
import string
from tkinter import *
import tkinter as tk

def peep():
    # size of string
    n = 6
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))
    webbrowser.open("http://prnt.sc/{}".format(res), new=2)


# create instance
win = tk.Tk()

# title of window
win.title("Peeping Tom")
# size of window
win.geometry("270x200")
win.resizable(width=False, height=False)
# label on window
label1_1 = tk.Button(win, text="Click to peep", bd=1
                     , relief="solid", bg='#34d5eb', font="Times 32", width=15, height=4, command=peep)
label1_1.pack()

# forever loops GUI
win.mainloop()
