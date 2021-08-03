# Function1.py
# 리턴을 하지 않는 함수
def setValue(newValue):
    #지역변수
    x=newValue
    print("지역변수:",x)

#호출
result = setValue(5)
print(result)

def swap(x,y):
    return y,x

#호출
result = swap(3,4)
print(result)