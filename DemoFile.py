# DemoFile.py
from os import lstat


strURl="http://bitcamp.com/?page="+str(1)
print(strURl)

#오른쪽으로 정렬
for i in range(1,6):
    print(i,"*",i,"=",i*i)

print("---정렬방식 변경---")
for i in range(1,6):
    print(i,"*",i,"=",str(i*i).rjust(3))

print("---정렬방식 변경---")
for i in range(1,6):
    print(i,"*",i,"=",str(i*i).zfill(3))


#문자열 서식 포매팅
print("{0:x}".format(10)   )
print("{0:b}".format(10)   )
print("{0:,}".format(15000))
print("{0:e}".format(4/3)  )
print("{0:f}".format(4/3)  )
print("{0:.2f}".format(4/3))

#파일에 읽기,쓰기
f=open("d:\\work\\demo.txt","wt")
f.write("첫번째라인\n두번째라인\nabcd\n")
f.close()

f=open("d:/work/demo.txt","rt")
#하나의 문자열 변수로 리턴
result = f.read()
#f.close()
print(result)
print("---현재 위치---")
print(f.tell())
f.seek(0)
print("---한줄씩 처리---")
print(f.readline(),end="")
print(f.readline(),end="")
#리스트로 받기
f.seek(0)
lst = f.readline()
print(lst)
f.close()

#다중의 데이터에 맵핑하는 함수
def add10(x):
    return x+10

lst = [1,2,3]
for i in map(add10, lst):
    print(i)

#급속냉동과 해동
import pickle

colors= ["red","blue","green"]
f=open("d:\\work\\colors","wb")
pickle.dump(colors,f)
f.close()
del colors

#다시 복구
f=open("c:\\work\\colors","rb")
colors=pickle.load(f)
print(colors)
f.close()