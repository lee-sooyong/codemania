class Person:
    " Super Class "
    def __init__(self, name, phoneNumber):
        self.Name = name 
        self.PhoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.Name, 
                        self.PhoneNumber))
   
class Student(Person):
    " Sub Class "
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 Person 생성자를 호출
        Person.__init__(self, name, phoneNumber)
        self.Subject = subject
        self.StudentID = studentID
    def printInfo(self): #Person의 PrintInfo()메서드를 재정의
        print("Info(Name:{0}, Phone Number:{1})".format(self.Name, self.PhoneNumber))
        print("Info(Subject:{0}, Student ID:{1})".format(self.Subject, self.StudentID))
        
p = Person("전우치", "010-222-3333")
s = Student("이순신", "010-333-4444", "컴공", "990000")
p.printInfo()
s.printInfo()
