from tkinter import *
from tkinter import ttk
from Component.Input import InputText
from Component.label import label
from Process.get_corp_num import start
from Process.DataApi.corpData import DataMain, money

# 화면 설정
root = Tk()
root.title("기업 회계정보 Sys")

# DATA variable
_BasicData = [
    ("기업명", []),
    ("영업이익", []),
    ("당기순이익", []),
    ("법인세차감전순이익", []),
    ("매출액", []),
    ("당기순이익", []),
    ("자산총계", []),
    ("유동자산", []),
    ("자본총계", []),
    ("자본금", []),
    ("부채총계", []),
    ("비유동부채", []),
    ("비유동자산", []),
    ("이익잉여금", [])
]
_RateData = [
    ("기업명", []),
    ("ROA", []),
    ("ROS", []),
    ("매출총이익률", []),
    ("매출액영업이익률", []),
    ("매출액계속사업이익률", []),
    ("총자산회전율", []),
    ("유동자산회전율", []),
    ("비유동자산회전율", []),
    ("부채구성비율", []),
    ("부채비율", [])
]
DFF = [_BasicData, _RateData]


# ==================================================
# ==== MAIN ====
# 기업명 입력
mainFrame = Frame(root)
mainFrame.grid(row=0, column=0, padx=30, pady=10)
inputLabel = label(mainFrame, "기업명", 0, 0, px=2, py=1)
inputCorp = InputText(mainFrame, 0, 1)


# 결과 창
def return_result(result_Text):
    frame1 = Frame(mainFrame)
    frame1.grid(row=1, column=0, rowspan=1, columnspan=4, padx=10, pady=8)
    # Separator                                     ------------
    separator = ttk.Separator(frame1, orient='horizontal')
    separator.grid(row=0, column=0, sticky="WE")

    f_1_1 = Frame(frame1)
    f_1_1.grid(row=1, column=0)

    # Title Label                                   level 1-0
    label(f_1_1, "검색결과", 0, 0, 1, 2, py=5, bn="bold", ft=11)

    # Separator                                     ------------
    separator = ttk.Separator(frame1, orient='horizontal')
    separator.grid(row=2, column=0, sticky="WE")

    f_1_2 = Frame(frame1)
    f_1_2.grid(row=3, column=0)

    # 법인등록번호                                    level 2-0
    label(f_1_2, "법인등록번호", 1, 0, bn="bold", py=3)
    label(f_1_2, result_Text, 1, 1, py=3)

    # 기업명                                         level 2-1
    label(f_1_2, "기업명", 2, 0, bn="bold", py=3)
    label(f_1_2, DFF[0][0][1][-1], 2, 1, py=3)

    # Separator                                     ------------
    separator = ttk.Separator(frame1, orient='horizontal')
    separator.grid(row=4, column=0, sticky="WE")

    f_1_3 = Frame(frame1)
    f_1_3.grid(row=5, column=0)

    # SubTitle Label                                level 3-0
    label(f_1_3, "기본재무정보 (손익계산서, 재무상태표)", 0, 0, 1, 2, py=5, bn='bold', ft=11)

    # Separator                                     ------------
    separator = ttk.Separator(frame1, orient='horizontal')
    separator.grid(row=6, column=0, sticky="WE")

    f_1_4 = Frame(frame1)
    f_1_4.grid(row=7, column=0)

    # 기본 회계 정보                                  level 4-0 ~
    for i in range(len(DFF[0])-1):
        label(f_1_4, DFF[0][i+1][0], i, 0, bn="bold", py=3)
        label(f_1_4, money(DFF[0][i+1][1][-1]), i, 1, py=3)


# 검색 버튼
def btncmd():
    # corp_num : 공공데이터 API 사용을 위한 법인등록번호
    corp_num = start(inputCorp.get())

    # Data Frame Module Control
    DataMain(corp_num[0], corp_num[1], DFF)

    num_for_print = corp_num[0][:6]+"-"+corp_num[0][6:]
    return_result(num_for_print)

    inputCorp.delete('0', END)


# ==== MAIN ====
SearchBtn = Button(mainFrame, text="검색", command=btncmd)
SearchBtn.grid(row=0, column=2, sticky="WE")

# ==================================================
# Main loop
root.mainloop()
