

# till we have studied .
# int , str , float , boolean
# set , tuple , dictionary , list
# inbuilt data type
# user defined data type
# what are user defined data type ???

class Person:
    # constructor to set the instance variable
    def __init__(self):
        self.firstName = "chinmay"
        self.lastName = "deshpande"
        self.age = 30
        self.rollNo  = 44

    #instance method
    def displayName(self):
        print(self.firstName + self.lastName)

chinmay = Person()
print(type(chinmay))
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.age)
print(chinmay.rollNo)
chinmay.displayName()


amol = Person()
print(amol.firstName)
print(amol.lastName)
print(amol.age)
print(amol.rollNo)
amol.displayName()

amol.firstName = "amol"
amol.lastName = "rao"
amol.age = 77
amol.rollNo = 22
amol.displayName()

# program 2
class PersonB:
    def __init__(self,firstName,lastName,age,rollNo):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.rollNo = rollNo

    def displayName(self):
        print(self.firstName + self.lastName)

sarika = PersonB("sarika","pansare",23,45)
amol = PersonB("amol","rao",34,45)

print(type(sarika))
print(type(amol))

print(amol.firstName)
print(amol.lastName)
print(amol.age)
print(amol.rollNo)

print(sarika.firstName)
print(sarika.lastName)
print(sarika.age)
print(sarika.rollNo)

amol.displayName()
sarika.displayName()

# Program 3
# Differnce between instance variable and class variable

class PersonC:
    # class variable
    country = "India"
    def __init__(self,fn,ln,ag,adharNo):
        self.firstName = fn
        self.lastName = ln
        self.age = ag
        self.adharNo = adharNo
    @classmethod
    def updateCountry(cls,cntry):
        PersonC.country = cntry

    def displayName(self):
        print(self.firstName + self.lastName)


PersonC.updateCountry("USA")
ram = PersonC("ram","dani",23,34)
sham = PersonC("sham","radhi",21,44)
ganesh = PersonC("ganesh","deshpande",22,43)

print(ram.country)
print(sham.country)
print(ganesh.country)

# ram.country = "bharat"
# print(ram.country)



















