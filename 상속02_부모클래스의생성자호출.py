class Person:
    def __init__(self, name, phoneNumber):
        self.Name = name
        self.PhoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber) 
        self.Subject = subject
        self.StudentId = studentID



