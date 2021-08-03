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

#불변형식을 함수 내부에서 읽기+쓰기
g=1
def testScope(a):
    global g
    g=2
    return g+a

#호출
print(testScope(1))
print("전역변수 g:",g)

#기본값을 셋팅
def times(a=10,b=20):
    return a*b

#호출
print(times())
print(times(a=5))
print(times(3,4))

#키워드 인자(파라메터명을 명시)
def connectURI(server, port):
    strURL= "http://"+server+ ":"+port
    return strURL

#호출
print(connectURI("bitCamp","80"))
print(connectURI(port="80",server="bitCamp"))

#가변인자(다양한 갯수를 소화)
def union(*ar):
    #지역변수(리스트)
    result=[]
    #HAM(0) | EGG(1)
    for item in ar:
        #H(0) | A(1) | M(2)
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))