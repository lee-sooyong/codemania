# web2.py
#웹서버와 통신
import urllib.request
#웹크롤링
from bs4 import BeautifulSoup

data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")

#검색을 할 객체를 생성
soup = BeautifulSoup(data, "html.parser")
# <td class="title">
# 	<a href="/webtoon/detail?titleId=20853&no=50&weekday=fri">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
cartoons=soup.find_all("td",class_="title")
print("갯수:{0}".format(len(cartoons)))
title=cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)
#전체 리스트
for item in cartoons:
    title=item.find("a").text
    print(title.strip())