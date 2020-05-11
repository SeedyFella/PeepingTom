import webbrowser
import random
import string
from tkinter import *
import tkinter as tk


def peep_old():
    # older sreenshots
    n = 6
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))
    web = webbrowser
    web.open("https://prnt.sc/{}".format(res), new=2)


def peep_new():
    # newer screenshots
    n = 3
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))
    web = webbrowser
    web.open("https://prnt.sc/sem{}".format(res), new=2)


# create instance
win = tk.Tk()

# title of window
win.title("Peeping Tom")
# size of window
win.geometry("300x200")
win.resizable(width=False, height=False)
win.configure(bg='#03a5fc')

# ALL SCREENSHOTS
button1_1 = tk.Button(win, text="All Screenshots", bd=1
                      , relief="solid", font="Times 21", width=15, height=1, command=peep_old)
button1_1.pack()
button1_1.place(bordermode=OUTSIDE, height=75, width=250, x=25, y=100)

# RECENT SCREENSHOTS
button1_2 = tk.Button(win, text="Recent Screenshots", bd=1
                      , relief="solid", font="Times 21", width=15, height=1, command=peep_new)
button1_2.pack()
button1_2.place(bordermode=OUTSIDE, height=75, width=250, x=25, y=15)

# forever loops GUI
win.mainloop()
