

# abstraction  Vs interface

#interface means complete abstraction

# program 1
from abc import ABC , abstractmethod
class Student(ABC):
    @abstractmethod
    def fullName(self):
        pass
    @abstractmethod
    def address(self):
        pass
    def displayCountry(self):
        print("India")

class Teacher(Student):
    def fullName(self):
        print("chinmay deshpande")
    def address(self):
        print("pune")
class Professor(Student):
    def fullName(self):
        print("amol rao")
    def address(self):
        print("nagpur")
chinmay = Teacher()
shirish = Professor()

chinmay.displayCountry()
shirish.displayCountry()

# program 2

class Car(ABC):
    def __init__(self,regno):
        self.regNo = regno

    def openTank(self):
        print("Fill the fuel in the tank")
        print(self.regNo)
    @abstractmethod
    def steering(self):
        pass
    @abstractmethod
    def braking(self):
        pass

class Maruti(Car):
    def steering(self):
        print("Manual steering")
    def braking(self):
        print("Hydraulic brakes")

class Audi(Car):
    def steering(self):
        print("Automatic steering")

    def braking(self):
        print("Gas brakes")

xz = Maruti("123")
xz.braking()
xz.steering()
xz.openTank()


q6 = Audi("456")
q6.braking()
q6.steering()
q6.openTank()

# interface
class myclass(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
#
# class Oracle(myclass):
#     def connect(self):
#         print("I am connect to oracle DB")
#     def disconnect(self):
#         print("I am disconnected from oracle DB")
#
# class MySQl(myclass):
#     def connect(self):
#         print("I am connect to MySQl db ")
#     def disconnect(self):
#         print("I am disconnected from MySQl db")
#
# class Database:
#     str = input("Enter the databaseName: ")
#     # convert the string into the class
#     className = globals()[str]
#     x = className()
#     x.connect()
#     x.disconnect()

#Exceptions
#compile time error
# syntax error
# def abc
#     print("hello")
# abc()

# runtime errors (run time errors) # Exceptions
# a = int(input("Enter the firstNumber"))
# b = int(input("Enter the secondNumber"))
# print("hello")
# print(a/b)
# print("Bye")

# logical errors
salary = 15000

def hikekSalary(sl):
    return sl * 0.10 + salary
print(hikekSalary(salary))






















