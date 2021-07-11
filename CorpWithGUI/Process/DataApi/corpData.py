''' 
@CopyRight 

2021-07-08
Republic of Korea

Park.Giyoun
Hankuk University of Foreign Studies
Industrial & Management Engineering
'''
import requests as rq
import json
import xmltodict
# 서비스키는 apiKey.py를 통해 관리 (이 파이썬 파일과 같은 경로에 위치 해야한다.)
from Process.DataApi.apiKey import serviceKey

ServiceKey = serviceKey
Year = "2020"


# ==== MODULE ====
# 재무제표 데이터
def GetData(Data):
    Data_content = rq.get(Data).content
    Data_dict = xmltodict.parse(Data_content)

    # string 형태의 json
    Data_jsonString = json.dumps(
        Data_dict['response']['body']['items']['item'], ensure_ascii=False)

    # string -> json
    Data_jsonObj = json.loads(Data_jsonString)

    return Data_jsonObj


# 재무비율 데이터
def rateConverter(L_asset):
    result = []
    # 0 총자산이익률 ROA
    # = 매출액순이익률 * 총자산회전율 (당기순이익 / 총 자산)
    result.append(L_asset[1]/L_asset[4])

    # 1 매출액 순이익률 ROS
    # = 당기순이익 / 매출액
    result.append(L_asset[1]/L_asset[3])

    # 2 매출 총 이익률
    # = 매출 총 이익 / 매출액 [여기서 ROS와 매출 총 이익률은 같다.]
    result.append(L_asset[1]/L_asset[3])

    # 3 매출액 영업이익률
    # = 영업이익 / 매출액
    result.append(L_asset[0]/L_asset[3])

    # 4 매출액 계속사업이익률
    # = 계속사업이익(법인세 차감 전 이익) / 매출액
    result.append(L_asset[2]/L_asset[3])

    # 5 총자산회전률
    # = 매출액 / 총 자산
    result.append(L_asset[3]/L_asset[4])

    # 6 유동자산회전률
    # = 매출액 / 유동자산
    result.append(L_asset[3]/L_asset[5])

    # 7 비유동자산회전률
    # = 매출액 / 비유동자산
    result.append(L_asset[3]/L_asset[10])

    # 8 부채구성비율
    # = 총부채 / 총자산
    result.append(L_asset[9]/L_asset[4])

    # 9 부채비율
    # = 총부채 / 자기자본
    result.append(L_asset[9]/L_asset[7])

    return result


# ==== Data Frame Module ====
def DataFrameModule(DFF, Assets, Rates):
    for i in range(len(Assets)):
        DFF[0][i][1].append(Assets[i])

    for i in range(len(Rates)):
        DFF[1][i][1].append(Rates[i])

    return DFF


# ===== MAIN =====
# 법인등록번호는 스크래핑 해온 데이터 "CorpNum"사용.
def DataMain(CorpNum, Corp, DFF):
    # 손익계산서 URL
    S_I = "http://apis.data.go.kr/1160100/service/GetFinaStatInfoService/getIncoStat?serviceKey=" + \
        ServiceKey+"&numOfRows=10&pageNo=1&numOfRows=xml&crno="+CorpNum+"&bizYear="+Year
    # 재무상태표 URL
    S_FP = "http://apis.data.go.kr/1160100/service/GetFinaStatInfoService/getBs?serviceKey=" + \
        ServiceKey+"&numOfRows=18&pageNo=1&numOfRows=xml&crno="+CorpNum+"&bizYear="+Year

    S_I_Data = GetData(S_I)
    S_FP_Data = GetData(S_FP)

    # 재무제표 DATA LIST (변수 명 : Assets)
    Assets = []
    Assets.append(Corp)
    for i in range(4):
        Assets.append(int(S_I_Data[i]['crtmAcitAmt'])/1000000)
    for i in range(9):
        Assets.append(int(S_FP_Data[i]['crtmAcitAmt'])/1000000)

    print("Assets(재무정보):", Assets)

    # 재무비율 DATA LIST (변수 명 : Rates)
    Rates = [Corp]
    Rates = Rates + rateConverter(Assets[1:])
    print("Rates(재무비율): ", Rates)

    DFF = DataFrameModule(DFF, Assets, Rates)
    return DFF


# 영미식 단위로 끊어주는 함수
def money(mon):
    a = int(mon)
    print(a)
    result = str(a)
    count = 0
    while (a > 0):
        a = a//1000
        if(a != 0):
            count += 1
    for i in range(count):
        info = -3*count
        index = info+i*3
        result = result[:index] + ',' + result[index:]

    return result
# O(n)
