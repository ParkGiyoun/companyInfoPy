from tkinter import *


def InputText(root, r, c):
    txt = Entry(root)
    txt.grid(row=r, column=c)
    return txt
