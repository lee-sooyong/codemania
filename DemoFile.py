# DemoFile.py
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
