from tkinter import *
from Component.Input import InputText
from Component.label import label
from Process.get_corp_num import start
from Process.DataApi.corpData import DataMain

# 화면 설정
root = Tk()
root.title("기업 회계정보 Sys")

# DATA variable
_BasicData = [
    ("기업명", []),
    ("회계연도", []),
    ("매출액", []),
    ("영업이익", []),
    ("법인세차감전순이익", []),
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
# 기업명 입력
inputLabel = label(root, "기업명", 0, 0)
inputCorp = InputText(root, 0, 1)


# 결과 창
def return_result(result_Text):
    # 법인등록번호
    label(root, "법인등록번호", 1, 0)
    label(root, result_Text, 1, 1)


# 검색 버튼
def btncmd():
    # corp_num : 공공데이터 API 사용을 위한 법인등록번호
    corp_num = start(inputCorp.get())

    # Data Frame Module Control
    DataMain(corp_num, inputCorp.get(), DFF)

    num_for_print = corp_num[:6]+"-"+corp_num[6:]
    return_result(num_for_print)

    inputCorp.delete(END)


SearchBtn = Button(root, text="검색", command=btncmd)
SearchBtn.grid(row=0, column=2)

# ==================================================
# Main loop
root.mainloop()
