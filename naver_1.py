import requests
from bs4 import BeautifulSoup

url ="https://naver.com"

#get 방식: 서버에게 리소스(자원)을 받아오기
req = requests.get(url)
html = req.text
#print(html)

soup = BeautifulSoup(html, "html.parser")
query = soup.select_one("#search_input_box")
print(query)