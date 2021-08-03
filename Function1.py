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

#불변형식과 가변형식
a=1.2
print(id(a))
a=2.3
print(id(a))

print("---가변형식---")
lst = [1,2,3,]
print (id(lst))
lst.append(4)
print(id(lst))

# 객체는 참조를 통해 입출력이 된다.
#Pass By Reference
wordlist = ["j","A","M"]
#함수 정의
def change(x):
    #지역변수에 복사해서 수정
    x1=x[:]
    x1[0] = "H"
    print("함수내부:",x1)

#함수 호출
change(wordlist)
print("함수 호출후: ",wordlist)