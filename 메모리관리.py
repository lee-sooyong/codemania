# 메모리관리.py 
class MyClass:
    #생성자
    def __init__(self, value):
        self.value = value 
        print("Instance is created! value=", value)
    #소멸자
    def __del__(self):
        print("Instance is deleted!")

d = MyClass(5)
# del d 
print("전체 코드 실행 종료")

