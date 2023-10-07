
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
#Exceptions

# compile time error
# program 1
# x = 1
# if x == 1
#     print("where us colon")


#program 2 # compile time error
# x = 10
# if x % 2 == 0:
#     print("x is even")
#         print("we divide x by 2")


# program 3 # run time error
# def concat(a,b):
#     print(a+b)
# #concat("1"+ 1)
# concat(23,44)

# program 4 # run time erroe
# animal = ["cat","dog","horse","donkey"]
# print(animal[5])

# program 5 # logical error
salary = 1000
def incrementSalary(salary):
    salary = salary * 0.10
    return salary
print(incrementSalary(salary))

# program 6
# f = open('myfile.text','w')
# a = int(input('Enter the number one'))
# b = int(input('Enter the number two'))
# c  = str(a/b)
# f.write(c)
# print("I am closing the file")
# f.close()

# program 7
# A exeception can be a run time error handled by programmer
try:
    f = open("myfile.txt","w")
    x,y = [int(x) for x in input("Enter the two number: ").split()]
    c = x/y
    f.write(str(c))
    numbers = [11,22,33]
    print(numbers[3])
except ZeroDivisionError:
    print('Division by zero happed')
    print('Please donot enter 0 in input')
except IndexError:
    print("array search go out of range")
except Exception as e:
    print(e)
finally:
    f.close()
    print("File closed")

































































