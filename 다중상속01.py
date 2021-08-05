
class Tiger:
    def jump(self):
        print("호랑이 점프")    
    def cry(self):
        print("호랑이 어흥")

class Lion:
    def bite(self):
        print("사자 물어뜯기")
    def cry(self):
        print("사자 응애")

class Liger(Lion,Tiger):
    def play(self):
        print("라이거와 놀기")


l = Liger()
l.cry()
print("메서드 해석 순서:",Liger.__mro__)

        
