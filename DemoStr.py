# DemoStr.py
#str형식의 메서드
print(dir(str))

names=["전우치","홍길동","이순신"]
for name in names:
    print("안녕하세요 {0}님 더운 여름입니다.".format(name))
    print("="*40)


#메서드 연습
strA="python is powerful"
print(len(strA))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p",7))
print("demo.ppt".endswith("ppt"))
strB="<<< spam and ham >>>"
print(strB)
#앞뒤에 있는 캐릭터 제거
result=strB.strip("<> ")
print(result)
result2 = result.replace("spam","spam egg")
print(result2)
#문자열을 리스트로 변환(공백문자 기준)
lst= result2.split()
print(lst)
#하나의 문자열로 합치기
print(" ".join(lst))

#정규 표현식
import re

#패턴을 통한 검색
print(re.match("[0-9]*th","35th"))
print(re.search("[0-9]*th","35th"))
result=re.search("[0-9]*th","35th")
print(result.group())
#약간의 함정
print(bool(re.match("[0-9]*th", "  35th")))
print(bool(re.search("[0-9]*th" , "  35th")))
print(bool(re.search("apple","this is apple")))
print("---우편번호---")
print(bool(re.search("\d{5}","우리 동네는 52300")))
print(bool(re.search("\d{4}","올해는 2021년입니다.")))
