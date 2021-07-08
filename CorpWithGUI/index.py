from tkinter import *
from Component.Input import InputText
from Component.label import label
from Process.get_corp_num import start

# 화면 설정
root = Tk()
root.title("기업 회계정보 Sys")


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

    num_for_print = corp_num[:6]+"-"+corp_num[6:]
    return_result(num_for_print)

    inputCorp.delete(END)


SearchBtn = Button(root, text="검색", command=btncmd)
SearchBtn.grid(row=0, column=2)

# ==================================================
# Main loop
root.mainloop()
