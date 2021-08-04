# 계산기 클래스 정의 
class Calc:
    def __init__(self):
        self.result = 0 
    def add(self,a,b):
        self.result = a + b
    def remove(self,a,b):
        self.result =  a - b
    def multiple(self,a,b):
        self.result =  a * b
    def divide(self,a,b):
        self.result =  a / b 

#인스턴스 생성
calc = Calc()
calc.add(5,3)
print("결과:", calc.result)
calc.remove(5, 2)
print("결과:", calc.result)
calc.multiple(3, 4)
print("결과:", calc.result)
calc.divide(5, 2)
print("결과:", calc.result)

    
