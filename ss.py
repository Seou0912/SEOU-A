from selenium import webdriver #webdriver=웹 통제하는 라이브러리
from selenium.webdriver.common.keys import Keys #Keys=웹 통해 값 입력할 때 사용하는 라이브러리(키보드)
from selenium.webdriver.common.by import By
import time #time= 컴퓨터에게 쉬는시간 부여하는 라이브러리


#웹사이트 열기
driver = webdriver.Chrome() #webdriver야, chrome 실행시켜라. 경로는 ()에 있어. 크롤링 작업공간과 크롬 드라이버 같은 공간에 있을 경우 공란 ().
driver.get("https://www.naver.com") #네이버 페이지로 이동
driver.implicitly_wait(10) #로딩 끝날 때까지 10초 기다리기

#쇼핑 메뉴 클릭
#driver.find_element_by_css_selector("a.nav.shop").click()
driver.find_element(by=By.CSS_SELECTOR, value="a.nav.shop").click()
time.sleep(2)

#검색창 클릭
#search=driver.find_element_by_css_selector("input.co_srh_input._input")#검색창 위치(크롬>도구더보기>개발자모드 또는 F12)
search=driver.find_element(by=By.CSS_SELECTOR, value="input.co_srh_input._input")#검색창 위치(크롬>도구더보기>개발자모드 또는 F12)
# search=driver.find_element_by_id("query") 
search.click()

#검색어 입력
search.send_keys("햇반") #Keys로 검색할 창에 검색할 단어 입력
search.send_keys(Keys.ENTER) #Keys로 키보드의 엔터라는 값 입력 또는
#btn=driver.find_element_by_id("search_btn") #btn.click() 검색이라는 버튼 위치+버튼 클릭하라는 명령어 click()

#낮은가격순 클릭
#driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/a[2]").click()
#driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]/a[2]").click()
#driver.find_element_by_css_selector(".subFilter_sort__rQUtM").click() #정보 버튼 클릭
#time.sleep(2)

#driver.back() #뒤로가기

import csv

#무한 스크롤 (반복문)

#스크롤 전의 스크롤바 높이
before_h=driver.execute_script("return window.scrollY")

while True :
    driver.find_element(by=By.CSS_SELECTOR, value="body").send_keys(Keys.END) #맨 아래로 스크롤 내린다
    time.sleep(2) #스크롤 하는 동안의 로딩시간
    
    
    #스크롤 후의 스크롤바 높이
    after_h=driver.execute_script("return window.scrollY")
    
    if after_h==before_h:
        break
    before_h=after_h
    
    
##파일 생성
f = open(r"C:\\Users\\flyto\\네이버햇반크롤링0508.csv","w", encoding="CP949", newline="")
csvWriter = csv.writer(f)

    
#상품 정보 div
#items = driver.find_elements_by_css_selector(
#    ".basicList_info_area__17Xyo") #상품정보 포함하고 있는 영역

#items = driver.find_elements_by_css_selector(
#    ".basicList_item__2XT81") #상품정보 포함하고 있는 큰영역
items = driver.find_elements(by=By.CSS_SELECTOR, value=".basicList_item__2XT81") #상품정보 포함하고 있는 큰영역

for item in items:
    
    ##상품명##
    name = item.find_element(by=By.CSS_SELECTOR, value=".basicList_title__3P9Q7").text
    
    ##가격##
    try :
        price =item.find_element(by=By.CSS_SELECTOR, value=
            ".price_num__2WUXn").text
    except:
        #오류가 발생했다면
        price = "판매중단"
    
    ##링크##  
    link = item.find_element(by=By.CSS_SELECTOR, value=
        ".basicList_title__3P9Q7 > a").get_attribute('href')
    
    ##판매자명##
    #item.find_element_by_css_selector(".common_btn_detail__1Fu0c").click() #정보 버튼 클릭
    #seller = item.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/strong").text #정보창 내 업체명을 텍스트로
    #driver.find_element_by_css_selector(".layer_btn_close__2Reyi").click() #정보창 닫기
    
    ##판매자명리스트##
    try:
        item.find_element(by=By.CSS_SELECTOR, value=".basicList_brand__Sa0wB").click() #새탭 열기
        driver.switch_to.window(driver.window_handles[-1]) #새로 열린 탭으로 전환 후 작업.
        
        before_h=driver.execute_script("return window.scrollY") #스크롤 전의 스크롤바 높이
        while True :
            driver.find_element(by=By.CSS_SELECTOR, value="body").send_keys(Keys.END) #맨 아래로 스크롤 내린다
            time.sleep(10) #스크롤 하는 동안의 로딩시간
            after_h=driver.execute_script("return window.scrollY") #스크롤 후의 스크롤바 높이
            if after_h==before_h:
                break
            before_h=after_h
        
        sellerids = driver.find_elements(by=By.CSS_SELECTOR, value=".productList_inner__3wBIh") #판매자명 있는 리스트
                
        for sellerid in sellerids :
            name = sellerid.find_element(by=By.CSS_SELECTOR, value=".productList_title__uCZ0P").text
            seller = sellerid.find_element(by=By.CSS_SELECTOR, value=".productList_mall_link__1-Q4X").text
            price = sellerid.find_element(by=By.CSS_SELECTOR, value=".productList_value__XRe6h").text
            #link = sellerid.find_element(by=By.CSS_SELECTOR, value=".productList_title__uCZ0P").get_attribute('href')
            print(name, price, seller)#, link)
        #driver.close()
        driver.switch_to.window(driver.window_handles[0])
        
    except:
        item.find_element(by=By.CSS_SELECTOR, value=".common_btn_detail__1Fu0c").click() #정보 버튼 클릭
        time.sleep(2)
        seller = item.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/strong").text #정보창 내 업체명을 텍스트로
        driver.find_element(by=By.CSS_SELECTOR, value=".layer_btn_close__2Reyi").click() #정보창 닫기              
  
    print(name, price, seller)
    csvWriter.writerow([name, price, seller])
    
    
f.close()
