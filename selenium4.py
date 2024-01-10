from selenium import webdriver


# 다양한 패키지 불러오기
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
