from tkinter import *
from tkinter import ttk

from pandas.core import frame

from Component.Input import InputText
from Component.label import label
from matplotlib import pyplot as plt
import pandas as pd
from pandastable import Table


def toDF(data):
    result1 = pd.DataFrame(dict(data[:1]+data[1:5]), index=data[0][1])
    result2 = pd.DataFrame(dict(data[:1]+data[5:]), index=data[0][1])
    result = (result1, result2)
    print(result)
    return result

# 검색결과인 모든 기업들의 정보를 나타내는 Frame


def result_panel(root, normData, rateData):

    if len(normData[0][1]) > 1:
        normDF = toDF(normData)

        # Separator                                     ------------
        separator = ttk.Separator(root, orient='vertical')
        separator.grid(row=0, column=1, sticky="NS")

        # main
        resultMain = Frame(root)
        resultMain.grid(row=0, column=2, padx=20, pady=10, sticky="NSWE")

        label(resultMain, "전체결과", r=0, c=0, ft=15, bn="bold")

        # resultFrame 손익계산서
        label(resultMain, "손익계산서", r=1, c=0)
        resultFrame1 = Frame(resultMain)
        resultFrame1.grid(row=2, column=0, padx=20, pady=10, sticky="NSWE")

        pandasTable = Table(resultFrame1)
        pandasTable.model.df = normDF[0]
        pandasTable.show()

        # resultFrame 재무상태표
        label(resultMain, "재무상태표", r=3, c=0)
        resultFrame2 = Frame(resultMain)
        resultFrame2.grid(row=4, column=0, padx=20, pady=10, sticky="NSWE")

        pandasTable = Table(resultFrame2)
        pandasTable.model.df = normDF[1]
        pandasTable.show()
