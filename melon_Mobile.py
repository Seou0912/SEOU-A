from selenium import webdriver
# 다양한 패키지 불러오기
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# 키보드 입력이라던지 어떠한 동작과 관련되 기능을 쓰기위한 패키지
from selenium.webdriver.common.keys import Keys
# 클라스, 아이디,ass_selector를 이용하고자 할때
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver import ActionChains

# option설정을 넣기위한 초기
options = Options()

user_agent ="Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"


options.add_argument(f"user-agent={user_agent}") # 모바일이라속임
options.add_experimental_option("detach", True)

#화면크기
# options.add_argument("--start-maximized")
#options.add_argument("--start-fullscreen")
# options.add_argument("--window-size=1000, 4500")
# 걸슬리는 메시지(터미널)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# 상단에 거슬리는 메세지 (웹)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# 셀레니움 디버그 모드로 실행하기(구글링하기)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "http://m2.melon.com/index.htm"
driver.get(url)

time.sleep(1)
if driver.current_url != url:
    driver.get(url)
# a태그를 활용하여 웹페이지의 하이퍼 링크를 식별한다. 
driver.find_element(By.LINK_TEXT,"멜론차트").click()
time.sleep(1)

driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()
time.sleep(1)

melon_chat = driver.find_element(By.CSS_SELECTOR,"#_chartList")
list_100 = melon_chat.find_elements(By.CSS_SELECTOR, ".list_item")
time.sleep(1)

action = ActionChains(driver)

rank = 1
for i in list_100:
    title = i.find_element(By.CSS_SELECTOR,".title.ellipsis")
    singer = i.find_element(By.CSS_SELECTOR,".name.ellipsis")
    
    action.move_to_element(i).perform()
    i.find_element(By.CSS_SELECTOR, ".inner > span").click()
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    driver.back()
    print("---------------------------------------------------------------------------------------")
    print(f"순위 : {rank}")
    print(f"제목 : {title.text}")
    print(f"가수 : {singer.text}")
    print()
    
    rank += 1
    # print(i.text)
    # print()
    
    
# driver.quit()