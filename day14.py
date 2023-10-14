

# MRO in python
class A(object):
    def method(self):
        print("A is called") # 3
        super().method()
class B(object):
    def method(self):
        print("B is called") #5
        super().method()

class C(object):
    def method(self):
        print("C method is called") # 6

class X(A,B):
    def method(self):
        print("X is called") #2
        super().method()

class Y(B,C):
    def method(self):
        print("Y method is called") #4
        super().method()
class P(X,Y,C):
    def method(self):
        print("P is called") # 1
        super().method()

p = P()
p.method()

# program 2
# Polmorphism
class Duck:
    def talk(self):
        print("quack quack")

class Human:
    def talk(self):
        print("Hi hello")

def call_talk(obj):
    obj.talk()

a = Duck()
b = Human()
call_talk(a)
call_talk(b)

# program 2
#
# class Duck:
#     def talk(self):
#         print("quack quack")
#
# class Human:
#     def talk(self):
#         print("Hi hello")
#
# class Dog:
#     def bark(self):
#         print("Bow Bow")
#
# def call_talk(obj):
#     obj.talk()
#
# a = Duck()
# b = Human()
# c = Dog()
# call_talk(a)
# call_talk(b)
# call_talk(c)

#Program 3
# class Duck:
#     def talk(self):
#         print("quack quack")
#
# class Human:
#     def talk(self):
#         print("Hi hello")
#
# class Dog:
#     def bark(self):
#         print("Bow Bow")
#
# def call_talk(obj):
#     if(hasattr(obj,'talk')):
#         obj.talk()
#     elif(hasattr(obj,'bark')):
#         obj.bark()
#     else:
#         print("wrong object is called")
#
# a = Duck()
# b = Human()
# c = Dog()
# call_talk(a)
# call_talk(b)
# call_talk(c)

# same class same method name and different signature
# program 4 overloading
class Calculator:
    # def addition(self,x,y):
    #     print(x+y)
    #
    # def addition(self, x, y ,z):
    #     print(x + y + z)
    #
    # def addition(self, x, y ,z ,a):
    #     print(x + y + z + a)

    # hack
    def addition(self,x = None,y= None,z= None,a=None):
        if(x != None and y != None and z != None and a != None):
            print(x+y+z+a)
        elif(x != None and y != None and z != None):
            print(x+y+z)
        elif(x != None and y != None):
            print(x+y)

a = Calculator()
a.addition(12,12)
a.addition(12,12,34)
a.addition(12,33,44,55)


# Overriding
# same method name , same signature but different class

class WorldBank:
    def save(self):
        print("save worldbank is called")

    def loan(self):
        print("loan worldbank is called")


class SBI(WorldBank):
    def loan(self):
        print("SBI loan method is called")
    def save(self):
        print("SBI save method is called")

class PNB(WorldBank):
    pass


a = SBI()
a.loan()
a.save()

b = PNB()
b.save()
b.loan()

# Operator overloading
# '+' operator

print(12 + 23)  # 35
print("hello "+" world") # "hello world"
print([11,22,33]+[44,55,66]) # [11,22,33,44,55,66]

# operator overloading
class Bookx:
    def __init__(self,x):
        self.pages = x
class Booky:
    def __init__(self,y):
        self.pages = y

ramayan = Bookx(1200)
mahabharat = Booky(2400)
#print(ramayan + mahabharat)
print(ramayan.pages+ mahabharat.pages)



# program 2
class Bookx:
    def __init__(self,x):
        self.pages = x

    def __add__(self, other):
        return self.pages + other.pages

class Booky:
    def __init__(self,y):
        self.pages = y

class BookZ:
    def __init__(self,z):
        self.pages = z
    def __add__(self, other):
        return self.pages + other

ramayan = Bookx(12)
mahabharat = Booky(13)
vedas = BookZ(13)
a = ramayan + mahabharat # 25
print(vedas + a)
#print(ramayan+mahabharat+vedas)

# program 2

class Bookx:
    def __init__(self,page):
        self.page = page
    def __gt__(self, other):
        return self.page > other.page
class Booky:
    def __init__(self,page):
        self.page = page

q1 = Bookx(23)
q2 = Booky(34)
print(q1 > q2)
#print(q1.page > q2.page)


# program 3 multiplication

class Teacher:
    def __init__(self,name,salary):
        self.name = name
        self.salaryperday = salary

    def __mul__(self, other):
        return  self.salaryperday * other.days

class Attendance:
    def __init__(self,days):
        self.days = days


amol = Teacher("amol rao",1200)
amolq =  Attendance(23)
print(amol * amolq)
#print(amol.salaryperday *  amolq.days)














































