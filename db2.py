# db2.py
import sqlite3

#연결객체 생성(파일에 영구적으로 기록)
con = sqlite3.connect("d:\\work\\sample.db")

#구문을 수행할 커서 객체를 생성
cur = con.cursor()
#데이터를 담을 테이블을 생성
cur.execute("create table Phonebook (name text, phoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('derick','010-111');")
#입력 파라메터 처리
name="gildong"
phoneNumber="010-222"
cur.execute("insert into PhoneBook values (?, ?);",(name,phoneNumber))
#다중의 레코드(데이터를 입력하는 경우)
datalist = (("tom","010-123"),("dsp","010-456"))
cur.executemany("insert into PhoneBook values (?, ?);",datalist)

#결과를 검색
cur.execute("select * from PhoneBook;")
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

#정삭적으로 작업 완료
con.commit()