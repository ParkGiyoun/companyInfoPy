from tkinter import *
from Component.Input import InputText
from Component.label import label
from get_corp_num import get_corp_num

# 화면 설정
root = Tk()
root.title("기업 회계정보 Sys")


# ==================================================
# 기업명 입력
inputLabel = label(root, "기업명", 0, 0)
inputCorp = InputText(root, 0, 1)


# 결과 창
def return_result(result_Text):
    label(root, result_Text, 1, 2)


# 검색 버튼
def btncmd():
    print(inputCorp.get())

    return_result(inputCorp.get())
    corp_num = get_corp_num(inputCorp.get())
    corp_num.start()

    inputCorp.delete("1.0", END)


SearchBtn = Button(root, text="검색", command=btncmd)
SearchBtn.grid(row=0, column=2)

# ==================================================
# Main loop
root.mainloop()
