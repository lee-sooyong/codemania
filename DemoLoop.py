# # DemoLoop.py
lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i>5:
        break
    print("item:{0}".format(i))

print("---continue구문---")
for i in lst:
    if i % 2 == 0:
        continue
    print("item:{0}".format(i))

    print("---continue구문---")
for i in lst:
    if i % 2 == 1:
        continue
    print("item:{0}".format(i))


# 수열함수
print(range(10))
print(list(range(10)))
print(set(range(10)))
print(tuple(range(10)))
print(list(range(2000,2022)))
print(list(range(10,0,-1)))
#수동으로 루프를 돌리는 경우
for i in range(5):
    print(i)