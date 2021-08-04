class Tiger:
    def cry(self):
        print("호랑이 어흥~~")
class Lion:
    def cry(self):
        print("사자 으르릉~~")
class Liger(Tiger, Lion):  
    def play(self):
        print("라이거와 놀기")

l = Liger()
l.cry()
print("Liger클래스의 MRO:", Liger.__mro__)
