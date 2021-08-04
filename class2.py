# class2.py
#클래스를 정의
class Person():
    #공유 데이터로 사용(C#의 static멤버변수)
    num_person=0
    def __init__(self):
        self.name="default name"
        #카운트를 하는 코드
        Person.num_person+=1
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1=Person()
p2=Person()
p3=Person()
print("인스턴스 갯수:{0}".format(Person.num_person))

#동적으로 확장이 된다.
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)
#인스턴스에 추가
p1.age=30
print(p1.age)
# print(p2.age)
print("bbb")