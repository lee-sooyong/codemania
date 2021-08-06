# web1.py
#크롤링 연습
from os import replace
from bs4 import BeautifulSoup

#페이지 로딩
page=open("d:\\work\\test01.html","rt",encoding="utf-8").read()
#검색이 용이한 객체를 생성
soup=BeautifulSoup(page,"html.parser")
# print(soup.prettify())

#<p> 전체를 가져오기
# print (soup.find_all("p"))
#첫번째 <p> 검색
# print (soup.find("p"))
#조건이 있는 경우: <p class="outer-text">
# print(soup.find_all("p",class_="outer-text"))

#태그를 검색해서 컨텐츠만 가져오기
for item in soup.find_all("p"):
    title=item.text.strip().replace("\n","")
    title2=title.replace("\t","")
    print(title2)
    


