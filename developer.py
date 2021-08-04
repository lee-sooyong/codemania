#상속 연습
class Developer:
    def __init__(self,name):
        self.name = name 
    def getSalary(self,day):
        result = day * 50000
        print("개발자 월급:", result)

class WebDeveloper(Developer):
    def __init__(self,name,skill):
        Developer.__init__(self,name)
        self.skill = skill
    def getSalary(self,day):
        result = day * 150000
        print("웹 개발자 월급:", result)
    
class MobileDeveloper(Developer):
    def __init__(self,name,skill):
        Developer.__init__(self,name)
        self.skill = skill 
    def getSalary(self,day):
        result = day * 250000
        print("모바일 개발자 월급:", result)

#인스턴스 생성
dev = Developer("전우치")
webDev = WebDeveloper("이순신", "ASP.NET")
mobileDev = MobileDeveloper("박문수", "iOS")
dev.getSalary(20); webDev.getSalary(20); mobileDev.getSalary(20)

