from selenium import webdriver

# 다양한 패키지 불러오기
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 키보드 입력이라던지 어떠한 동작과 관련되 기능을 쓰기위한 패키지

from selenium.webdriver.common.keys import Keys

# 클라스, 아이디,ass_selector를 이용하고자 할때
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


# option설정을 넣기위한 초기

options = Options()
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option("detach", True)

#화면크기

# options.add_argument("--start-maximized")

#options.add_argument("--start-fullscreen")

options.add_argument("--window-size=1000, 4500")
#음소거
options.add_argument("--mute-audio")
#시크릿모드
options.add_argument("incognito")
# 화면없이 크롤링하기
#options.add_argument("--headless")

# 걸슬리는 메시지(터미널)
options.add_experimental_option("excludeSwitches", ["enable-logging"])


# 상단에 거슬리는 메세지 (웹)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# 셀레니움 디버그 모드로 실행하기(구글링하기)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)


url = "https://kream.co.kr/"
driver.get(url)
time.sleep(0.5)


# 돋보기를 선택
driver.find_element(By.CSS_SELECTOR, ".search_btn_box").click() 
time.sleep(0.5)

# 슈프림검색
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림") 
time.sleep(1)


# 자동 enter 
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER) 

time.sleep(1)


for i in range(10):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
driver.save_screenshot("/Users/seoujung/Desktop/Seou/crawling/kream_img/supreme"+str(i)+" .png")

html = driver.page_source # 가져와서 parser 진행

soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner")

# 후드 추출

num=1

for i in items:

    product_name = i.select_one(".translated_name") 

    if "후드" in product_name.text:

        product_name = i.select_one(".product_info_brand.brand")

        product_hood = i.select_one(".translated_name")

        product_price = i.select_one(".amount")

    print(num)
    print("--------------------------------------------------------")
    print(f"브랜드 : {product_name.text}")
    print(f"제품명 : {product_hood.text}")
    print(f"가 격 : {product_price.text}")
    print()



num += 1

# print(i.text)
driver.quit()

# 페이지 들어가서 돋보기 눌러 슈프림을 쳐서 드래그하며 많은 데이터 추출 셀레늄이 알아서 추출해주는
