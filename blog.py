from  bs4 import BeautifulSoup
import requests

# 검색어 입력
query = input("검색어를 입력하세요 : ")

# Google 검색 URL
url = "https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0" + query

# requests 이용해 웹 페이지 가져오기
response = requests.get(url)

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, "html.parser")

# Google 검색결과중에서 타이틀을 포함하는 div 태그를 찾음
divs = soup.select("a.link_tit")

# 타이틀 텍스트만 추출해서 넘버링하고 , 상위 10개만 출력
for i, div in enumerate(divs[0:10]):
    print(f"{i + 1}. {div.text}")
    