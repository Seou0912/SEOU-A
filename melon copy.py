import requests
from bs4 import BeautifulSoup

# song_num_text = "javascript:melon.link.goAlbumDetail('11352904')";
def get_nums(song_num_text):
    song_num = []
    for num in song_num_text:
        if num.isdigit(): #10진수로 변환이 가능하면 10진수로 변환했을때 나오는 숫자 반환, 숫자로 변형이 안되면 0내보내기
            song_num.append(num)
    song_num= "".join(song_num)
    return song_num
#    print(song_num)
#    print(type(song_num))

# get_nums(song_num_text)

header_user =  { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
} 
url = "https://www.melon.com/chart//index.htm"
req = requests.get(url, headers=header_user)

html=req.text
soup = BeautifulSoup(html, "html.parser")

lst50 = soup.select(".lst50")                    # . 클래스
lst100 = soup.select(".lst100")

lst_all = lst50 + lst100

for rank, i in enumerate(lst_all,1):
    title = i.select_one(".ellipsis.rank01 a")   # a 밑에 내용 붙임, 같은 뜻으로   = print(f"순위 : {rank.script()}")
    
    singer = i.select_one(".ellipsis.rank02 a")
    singer_link = get_nums(singer["href"])
    
    album = i.select_one(".ellipsis.rank03 a")
    album_link = get_nums(album["href"])
    
    print(f"순위 : {rank}")
    print(f"제목 : {title.text} => 링크 : https://www.melon.com/album/timeline.htm?albumId={album_link}")
    print(f"가수 : {singer.text} => 링크 : https://www.melon.com/artist/timeline.htm?artistId={singer_link}")
    print(f"앨범 : {album.text}")
    print()
    