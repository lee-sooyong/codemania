# db1.py
import sqlite3

#연결객체 생성(일단은 메모리에 임시로 저장)
con = sqlite3.connect(":memory:")
#구문을 수행할 커서 객체를 생성
cur = con.cursor()
#데이터를 담을 테이블을 생성
cur.execute("create table Phonebook (name text, phoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('derick','010-111');")

#결과를 검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)