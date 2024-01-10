from selenium import webdriver
from bs4 import BeautifulSoup
import time

#사람인척 하기위해 속이는 코드
header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
key_word = input("검색어를 입력해주세요 : ")

#탐색을 원하는 url
url = base_url + key_word

#탐색을 원하는 사이트의 데이터 달라고 요청
# req = requests.get(url, headers=header_user)  BeuifulSoup
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

#스크롤 실행 코드 가져오기
#driver.execute_script("window.scroollTo(0,5000")
for i in range(10):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)

html = driver.page_source     #ㅍ 가져와서 집어넣은

soup = BeautifulSoup(html, "html.parser")

total_area = soup.select(".view_wrap")

if total_area:
    areas = total_area
else :
    print(total_area)
    print("클래스 변경 필요")



rank_num = 1
for i in areas:
    ad = i.select_one(".link_ad")
    if ad:
        continue
    print(f"[{rank_num}]")
    title = i.select_one(".title_link._cross_trigger")
    name = i.select_one(".name")
    print("--------------------------------------------------------------------------")
    print(title.text)
    print(name.text)
    print(title["href"])
    print()

    rank_num += 1