from tkinter import *


def label(root, Text, r, c):
    label1 = Label(root, text=Text)
    label1.grid(row=r, column=c)
    return label1
