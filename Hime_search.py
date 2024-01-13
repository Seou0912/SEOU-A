from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://naver.com"

driver.get(url)

time.sleep(1)


url=driver.find_element(By.LINK_TEXT, "쇼핑").click() # 링크에 해당하는 단어 선택하면 연결되는 문장

brands = input("검색을 원하는 상품을 입력해주세요 : ") 

count = 0
driver.find_element(By.CSS_SELECTOR, ".gnbSearch_inner_2Zksb").click()
time.sleep(1)


driver.find_element(By.CSS_SELECTOR, ".input_searchInput_search_text_3CUDs").send_keys(brands[0])
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".input_searchInput_search_text_3CUDs").send_keys(Keys.ENTER)
time.sleep(3)

for i in range(20) :
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    driver.save_screenshot # 스크린샷 찍는 기능 / 경로 + / 파일 이름 및 형색 생성
    driver.save_screenshot("/Users/seoujung/Desktop/Seou/crawling/kream_py_img/"+brands[0]+str(i)+".png")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


items = soup.select(".item_inner")

rank = 1


for i in items:
    product_title = i.select_one(".adProduct_title__amInq")
    product_price = i.select_one(".adProduct_price__9gODs")
    product_delivery = i.select_one(".price_delivery__yw_We")
    if product in product_name.text:
        print(f'--{brands[count]} {rank}번--')
        print(f'상품명 : {product_title.text}')
        print(f'가격 : {product_price.text}')
        print(f'배송비 : {product_delivery.text}')
        # print(f'{product_selling.text}회')
        print()
            
        rank += 1
    
count += 1

driver.quit()