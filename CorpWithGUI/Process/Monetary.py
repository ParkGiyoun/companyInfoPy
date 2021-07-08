# 영미식 단위로 끊어주는 함수

def money(mon):
    a = mon
    result = str(mon)
    finalresult = ""
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

# ----------------
# test
# money(1320000)
# result = 1,320,000
# ----------------
# O(n)
