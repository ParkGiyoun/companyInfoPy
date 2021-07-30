from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msgbox
from Component.Input import InputText
from Component.label import label
from Process.get_corp_num import start
from Process.DataApi.corpData import DataMain, money
from total_result_panel import result_panel

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


def main():
    # 화면 설정
    root = Tk()
    root.geometry("1600x768")
    root.title("기업 회계정보 조회 System")

    # DATA variable
    _BasicData = [
        ("기업명", []),
        ("영업이익", []),
        ("당기순이익", []),
        ("법인세차감전순이익", []),
        ("매출액", []),
        ("자산총계", []),
        ("유동자산", []),
        ("유동부채", []),
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
    mainFrame.grid(row=0, column=0, padx=30, pady=10, sticky="NSWE")
    inputLabel = label(mainFrame, "기업명", 0, 0, px=2, py=1)
    inputCorp = InputText(mainFrame, 0, 1)

    # 결과 창

    def return_result(result_Text):
        # FRAME 1에 해당하는 부분
        # ========================
        frame1 = Frame(mainFrame)
        frame1.grid(row=1, column=0, rowspan=1, columnspan=4,
                    padx=10, pady=8, sticky="NS")
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
        label(f_1_2, "법인등록번호", 0, 0, bn="bold", py=3)
        label(f_1_2, result_Text, 0, 1, py=3)

        # 기업명                                         level 2-1
        label(f_1_2, "기업명", 1, 0, bn="bold", py=3)
        label(f_1_2, DFF[0][0][1][-1], 1, 1, py=3)

        # Separator                                     ------------
        separator = ttk.Separator(frame1, orient='horizontal')
        separator.grid(row=4, column=0, sticky="WE")

        f_1_3 = Frame(frame1)
        f_1_3.grid(row=5, column=0)

        # SubTitle Label                                level 3-0
        label(f_1_3, "기본재무정보 (손익계산서, 재무상태표)", 0,
              0, 1, 2, py=5, bn='bold', ft=11)

        # Separator                                     ------------
        separator = ttk.Separator(frame1, orient='horizontal')
        separator.grid(row=6, column=0, sticky="WE")

        f_1_4 = Frame(frame1)
        f_1_4.grid(row=7, column=0)

        # 기본 회계 정보                                  level 4-0 ~
        for i in range(len(DFF[0])-1):
            label(f_1_4, DFF[0][i+1][0], i, 0, bn="bold", py=3)
            label(f_1_4, money(DFF[0][i+1][1][-1]), i, 1, py=3)

        # ========================
        # Separator                                     ------------
        separator = ttk.Separator(mainFrame, orient='vertical')
        separator.grid(row=1, column=4, sticky="NS")

        # FRAME 2
        frame2 = Frame(mainFrame)
        frame2.grid(row=1, column=5, padx=30, pady=10, sticky="NS")

        # Separator                                     ------------
        separator = ttk.Separator(frame2, orient='horizontal')
        separator.grid(row=1, column=0, sticky="WE")

        f_2_1 = Frame(frame2)
        f_2_1.grid(row=2, column=0)

        # 비율 회계 TITLE
        label(f_2_1, "비율재무제표", 0, 0, 1, 2, py=5, bn="bold", ft=11)

        # Separator                                     ------------
        separator = ttk.Separator(frame2, orient='horizontal')
        separator.grid(row=3, column=0, sticky="WE")

        f_2_2 = Frame(frame2)
        f_2_2.grid(row=4, column=0)

        # 비율 회계 정보
        for i in range(len(DFF[1])-1):
            label(f_2_2, DFF[1][i+1][0], i, 0, bn="bold", py=3)
            label(f_2_2, DFF[1][i+1][1][-1], i, 1, py=3)

        # 종합결과 출력
        result_panel(root, DFF[0], DFF[1])

    # 검색 버튼

    def btncmd():
        # corp_num : 공공데이터 API 사용을 위한 법인등록번호
        corp_num = start(inputCorp.get())

        # Data Frame Module Control
        DataMain(corp_num[0], corp_num[1], DFF)

        num_for_print = corp_num[0][:6]+"-"+corp_num[0][6:]
        return_result(num_for_print)

        inputCorp.delete('0', END)

    # 한번에 검색 팝업

    def searchOnce():
        pop1 = Tk()
        pop1.geometry("630x210")
        pop1.title("한번에 검색")

        # ===내용===

        # =========
        pop1.mainloop()

    # 데이터 초기화 버튼

    def DeleteAll():
        response = msgbox.askokcancel(
            "데이터 초기화", "모든 데이터가 삭제됩니다.\n그래도 계속하겠습니까?")
        if response == 1:
            root.destroy()
            main()

    # 원형도표
    '''
    원형도표의 조건 -> 시작 DATA = END DATA 이어야 한다.
    ex) A = 1 B = 2 C = 3
        - > [1, 2, 3, 1]
    '''

    def cirG():
        if len(DFF[0][0][1]) > 1:
            DFFFF = [DFF[1][1], DFF[1][2], DFF[1][10], DFF[1][6]]
            corpLabel = []
            for i in DFFFF:
                corpLabel.append(i[0])
            corpLabel.append("유동비율")

            compLabel = []
            for i in DFF[0][0][1]:
                compLabel.append(i)

                c_r = []
                for i in range(len(DFF[0][0][1])):
                    value = []
                    for j in DFFFF:
                        print(i)
                        print(j[1][i])
                        rate = int(j[1][i]*100)/100
                        value.append(rate)
                    biul = int((DFF[0][6][1][i]/DFF[0][7][1][i])*100)/100
                    value.append(biul)
                    c_r.append(value)

            # 원형 도표 조건을 위함.
            for i in range(len(c_r)):
                c_r[i].append(c_r[i][0])

            # Initialing the spiderplot by
            # setting figure size and polar
            # projection
            plt.figure(figsize=(10, 6))
            plt.subplot(polar=True)

            theta = np.linspace(0, 2 * np.pi, len(c_r[0]))

            # Arranging the grid into number
            # of sales into equal parts in
            # degrees
            lines, labels = plt.thetagrids(
                range(0, 360, int(360/len(corpLabel))), (corpLabel))
            for i in c_r:
                plt.plot(theta, i)

            # Add legend and title for the plot
            plt.legend(labels=compLabel, loc=1)
            plt.title("기업 원형 도표")
            # Dsiplay the plot on the screen

            plt.show()

    # ==== MAIN ====
    SearchBtn = Button(mainFrame, text="검색", command=btncmd)
    SearchBtn.grid(row=0, column=2, sticky="WE")

    # ==== MENU ====
    menu = Menu(root)

    # 파일 메뉴
    menu_file = Menu(menu, tearoff=0)
    menu_file.add_command(label="한번에 검색", command=searchOnce)
    menu_file.add_separator()
    menu_file.add_command(label="데이터 초기화", command=DeleteAll)
    menu_file.add_separator()
    menu_file.add_command(label="엑셀로 저장")
    menu_file.add_command(label="표 저장")  # 그래프는 그래프 화면에서 저장 가능하다고 알리기.
    menu.add_cascade(label="파일", menu=menu_file)

    # 분석 메뉴
    menu_analysis = Menu(menu, tearoff=0)
    menu_analysis.add_command(label="원형도표", command=cirG)
    menu_analysis.add_command(label="듀퐁도표")
    menu_analysis.add_command(label="재무제표 흐름곡선")
    menu.add_cascade(label="분석", menu=menu_analysis)

    # ==== Main loop ====
    root.config(menu=menu)
    root.mainloop()


main()
