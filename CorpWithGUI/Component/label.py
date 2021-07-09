from tkinter import *


def label(root, Text, r, c, rs=1, cs=1, py=0, ):
    label1 = Label(root, text=Text)
    label1.grid(row=r, column=c, rowspan=rs, columnspan=cs, pady=py)
    return label1
