import requests
from bs4 import BeautifulSoup

header_user= {
    "user-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
} 
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36

url ="https://naver.com"

#get 방식: 서버에게 리소스(자원)을 받아오기
req = requests.get(url, headers=header_user)
#html = req.text
print(req.request.headers)

#soup = BeautifulSoup(html, "html.parser")
#query = soup.select_one("#search_input_box")
#print(query)