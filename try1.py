# try1.py


#함수 정의

def divede(a,b):
    return a/b

#예외처리(에러처리)
try:
    #함수 호출
    result = divede(5,0) 
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("숫자여야 합니다.")
else:
    print("결과:{0}".format(result))
finally:
    print("무조건 실행")
    
print("전체 코드 실행 종료")