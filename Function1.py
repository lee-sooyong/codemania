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

#디버깅 연습
def intersect(prelist, postlist):
    #지역변수
    result= []
    #H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersect("HAM","SPAM"))        