# DemoLoop3.py
# 리스트 컴프리헨션(약간은 압축된 문법)
lst=[1,2,3,4,5,6,7,8,9,10]
result =[i**2 for i in lst if i>5]
print(result)

tp=("apple","orange","kiwi")
print([len(i)for i in tp])

d={100:"apple",200:"orange"}
print([v.upper() for v in d.values()])

#필터링 함수
lst = [10,25,30]
iterL = filter(None,lst)
for i in iterL:
    print(i)

#함수 정의
def getBiggerThan20(i):
    return i >20

print("---필터링 함수 사용---")
iterL = filter(getBiggerThan20,lst)
for i in iterL:
    print(i)