import matplotlib.pyplot as plt
import matplotlib
import numpy as np

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


# DATA variable
_BasicData = [
    ("기업명", ["삼성전자", "LG전자"]),
    ("영업이익", [3000, 2500]),
    ("당기순이익", [2600, 2300]),
    ("법인세차감전순이익", [2700, 2350]),
    ("매출액", [3200, 2570]),
    ("자산총계", [35000, 23000]),
    ("유동자산", [20000, 20000]),
    ("유동부채", [23000, 17000]),
    ("자본총계", [10000, 3000]),
    ("자본금", [7000, 2000]),
    ("부채총계", [25000, 20000]),
    ("비유동부채", [2000, 3000]),
    ("비유동자산", [15000, 3000]),
    ("이익잉여금", [13000, 7000])
]
_RateData = [
    ("기업명", ["삼성전자", "LG전자"]),
    ("ROA", [1.3, 1.1]),
    ("ROS", [1.5, 1.4]),
    ("매출총이익률", [3.5, 2.2]),
    ("매출액영업이익률", [1.7, 2.8]),
    ("매출액계속사업이익률", [3.3, 2.7]),
    ("총자산회전율", [2.1, 3.6]),
    ("유동자산회전율", [1.4, 2.4]),
    ("비유동자산회전율", [1.5, 2.6]),
    ("부채구성비율", [2.1, 1.6]),
    ("부채비율", [1.5, 2.1])
]
DFF = [_BasicData, _RateData]


# 원형도표
# 기존에 그래프 팝업할 조건을 만족시킬 경우, 이 함수를 실행한다.
def circleGraph(DFF):
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
    print("?", len(c_r[0]))

    # Initialing the spiderplot by
    # setting figure size and polar
    # projection
    plt.figure(figsize=(10, 6))
    plt.subplot(polar=True)
    theta = np.linspace(0, 2 * np.pi, len(c_r[0]))

    # Arranging the grid into number
    # of sales into equal parts in
    # degrees
    print(corpLabel)
    lines, labels = plt.thetagrids(
        range(0, 360, int(360/len(corpLabel))), (corpLabel))

    for i in c_r:
        plt.plot(theta, i)

    # Add legend and title for the plot
    plt.legend(labels=compLabel,
               loc=1)
    plt.title("기업 원형 도표")

    # Dsiplay the plot on the screen
    plt.show()


circleGraph(DFF)
