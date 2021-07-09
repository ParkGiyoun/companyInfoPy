from tkinter import *


def label(root, Text, r, c, rs=1, cs=1, py=0, ):
    separator = root.Separator(root, orient='horizontal')
    separator.pack(fill='x')
    root.Label(root, text="Second Label").pack()
