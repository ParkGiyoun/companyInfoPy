from tkinter import *


def label(root, Text, r, c, rs=1, cs=1, bn='', px=0, py=0, ft=10):
    label1 = Label(root, text=Text, font=('굴림', ft, bn))
    label1.grid(row=r, column=c, rowspan=rs,
                columnspan=cs,  sticky="WE", padx=px, pady=py)
    return label1
