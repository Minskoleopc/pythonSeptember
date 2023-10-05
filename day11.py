
# revision

class Employee:
    # class variable
    city = "pune"
    count = 0

    # constructor to intialise instance variable
    def __init__ (self,fn,ln,rollNo):
        Employee.count = Employee.count + 1
        self.firstName = fn
        self.lastName = ln
        self.id = rollNo

    # instance method
    def displayName(self):
        print(self.firstName + self.lastName)

    # class level method to update city
    @classmethod
    def updateCity(cls,cty):
        Employee.city  = cty

    # static method
    @staticmethod
    def displayNoEmployee():
        print(Employee.count)

chinmay = Employee("chinmay","deshpande",7)
chinmay.displayName()
Employee.updateCity("nagpur")
Employee.displayNoEmployee()


# inner class
# program 1
#
# class Employee2 :
#     def __init__(self,fn,ln,age,sal):
#         self.firstName = fn
#         self.lastName = ln
#         self.age  = age
#         self.sal = sal
#         self.d = self.DOB()
#
#     def displayName(self):
#         print(self.firstName+self.lastName)
#
#     class DOB:
#         def __init__(self):
#             self.dd = 11
#             self.mm = 7
#             self.yy = 1989
#
#         def displayDate(self):
#             print(self.dd,self.mm,self.yy)
#
# amol = Employee2("amol","rao",23,34)
# print(amol.firstName)
# print(amol.lastName)
# print(amol.age)
# print(amol.sal)
# date = amol.d
#
# print(date.dd)
# print(date.mm)
# print(date.yy)
# date.displayDate()


# program 2
class Employee2 :
    def __init__(self,fn,ln,age,sal,mm,dd,yy):
        self.firstName = fn
        self.lastName = ln
        self.age  = age
        self.sal = sal
        self.d = self.DOB(mm,dd,yy)

    def displayName(self):
        print(self.firstName+self.lastName)

    class DOB:
        def __init__(self,mm,dd,yy):
            self.dd = dd
            self.mm = mm
            self.yy = yy

        def displayDate(self):
            print(self.dd,self.mm,self.yy)

amol = Employee2("amol","rao",23,34,7,11,1989)
print(amol.firstName)
print(amol.lastName)
print(amol.age)
print(amol.sal)
date = amol.d
print(date.dd)
print(date.mm)
print(date.yy)
date.displayDate()


class Employee3:

    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayName(self):
        print(self.firstName+self.lastName)

    class DOB():
        def __init__(self,dd,mm,yy):
            self.dd = dd
            self.mm = mm
            self.yy = yy

        def displayDate(self):
            print(self.dd,self.mm ,self.yy)

        class Greet:
            word = "Hello"

chinmay = Employee3("chinmay","deshpande")
chinmay.displayName()
amol = Employee3("chinmay","deshpande").DOB(11,7,1989)
print(amol.dd)
print(amol.mm)
print(amol.yy)
amol.displayDate()

sarika = (Employee3("sarika","pansare")
          .DOB(12,33,90)).Greet()
print(sarika.word)

# polymorphism , inheritance











































