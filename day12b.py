# class Student:
#     def setFirstName(self,fn):
#         self.firstName = fn
#     def getFirstNname(self):
#         print(self.firstName)
#
#     def setLastName(self,ln):
#         self.lastName = ln
#     def getLastName(self):
#         print(self.lastName)
#
#     def setAge(self,ag):
#         self.age = ag
#     def getAge(self):
#         print(self.age)
#
# class Teacher(Student):
#     pass
#
# amolT = Teacher()
# amolT.setAge(12)
# amolT.setFirstName("amol")
# amolT.setLastName("rao")
#
# amolT.getAge()
# amolT.getLastName()
# amolT.getFirstNname()

# program 2
class Student:
    def setFirstName(self,fn):
        self.firstName = fn
    def getFirstNname(self):
        print(self.firstName)

    def setLastName(self,ln):
        self.lastName = ln
    def getLastName(self):
        print(self.lastName)

    def setAge(self,ag):
        self.age = ag
    def getAge(self):
        print(self.age)

class Teacher(Student):
    def setSalary(self,sl):
        self.salary = sl

    def getSalary(self):
        print(self.salary)


amolT = Teacher()
amolT.setAge(12)
amolT.setFirstName("amol")
amolT.setLastName("rao")
amolT.setSalary(1000)

amolT.getAge()
amolT.getLastName()
amolT.getFirstNname()
amolT.getSalary()

# program 3
# class Person:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#
#     def displayFullName(self):
#         print(self.firstName + self.lastName)
#
# class Professor(Person):
#     pass
#
# amolP = Professor("amolp","raop")
# amolP.displayFullName()
# print(amolP.firstName)
# print(amolP.lastName)


class Person:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayFullName(self):
        print(self.firstName + self.lastName)

class Professor(Person):
    salary = 1000
    def displaySalary(self):
        print(self.salary)

amolP = Professor("amolp","raop")
amolP.displayFullName()
amolP.displaySalary()
print(amolP.firstName)
print(amolP.lastName)
print(amolP.salary)

# program 4

class PersonC:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName+ self.lastName)

class ProfessorC(PersonC):
    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl

    def displaySalary(self):
        print(self.salary)

amolP =  ProfessorC("amolC","raoC",1000)
print(amolP.firstName)
print(amolP.lastName)
print(amolP.salary)

amolP.displayName()
amolP.displaySalary()











