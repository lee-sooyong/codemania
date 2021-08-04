# -*- 생성자와 소멸자 그리고 참조 카운트 관리  -*-
class MyClass:
    def __init__(self, value):
        self.value = value
        print("Instance is created! Value = ", value)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성 
d = MyClass(10)
d_copy = d
del d_copy 
del d




