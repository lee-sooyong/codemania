# Function2.py

#지역변수와 전역변수
x=2
def func1(a):
    return x+a

#호출
print(func1(1))

def func2(a):
    x=5
    return x+a

#호출
print(func2(1))