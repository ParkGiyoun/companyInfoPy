# 키 값 입력을 위함
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
# 페이지 불러올 때 까지 기다기기 위함
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def start(corp):
    browser = webdriver.Chrome("CorpWithGUI\Process\chromedriver.exe")

    # 주소 get
    browser.get("http://dart.fss.or.kr/")

    # 검색창 element
    searchElem = browser.find_element_by_id("textCrpNm")

    # 검색창 click
    # searchElem.click()

    # 검색
    searchElem.send_keys(corp)  # 여기선 위의 import 필요 없음.
    searchElem.send_keys(Keys.ENTER)

    # 2021-07-11 ----
    # 기업 링크 Xpath
    linkXpath = "/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/table/tbody/tr[1]/td[2]/span/a"
    # ---------------

    # 기업 리스트 조회까지 대기
    try:
        # 기업 링크 클릭
        corpLink = WebDriverWait(browser, 2).until(
            EC.presence_of_element_located((By.XPATH, linkXpath)))
        resultCorp = corpLink.text
        corpLink.click()
    finally:
        print("공시 System....")

    # 법인등록번호 Xpath
    xpath = "/html/body/div[8]/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[7]/td"
    CorpNum = ""

    # 기업 정보 팝업이 될 때 까지 대기
    try:
        CorpNumber = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        CorpNum = CorpNumber.text
    finally:
        print("정보 조회...")
        browser.quit()

    # 사용할 법인 등록 번호
    CorpNum = CorpNum[:6]+CorpNum[7:]
    return CorpNum, resultCorp
