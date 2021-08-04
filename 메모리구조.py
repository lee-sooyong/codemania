# 메모리구조.py
class SuperClass:
    def __init__(self):
        self.x = 10 
    def printX(self):
        print(self.x)

class SubClass(SuperClass):
    #상속받은 생성자 메서드 재정의
    def __init__(self):
        #부모의 생성자 메서드 호출(필수)
        SuperClass.__init__(self)
        self.y = 20
    def printY(self):
        print(self.y)

s = SubClass()
s.a = 30 
# print("SuperClass:", SuperClass.__dict__)
# print("SubClass:", SubClass.__dict__)
# print("s:", s.__dict__)

s.printX()
s.printY()