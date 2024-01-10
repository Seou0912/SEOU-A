from selenium import webdriver
from bs4 import BeautifulSoup
import requests

import time

url = "https://section.cafe.naver.com/ca-fe/home"

# req = requests.get(url)
# html = req.text
# print(html)

driver = webdriver.Chrome() # 크롬을 불러 초기화
driver.get(url)
html = driver.page_source
print(html)