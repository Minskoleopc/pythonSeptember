

# single inheritance

class Student:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)


class Teacher(Student):
    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl

    def displaySalary(self):
        print(self.salary)

amol = Teacher("amol","rao",1000)
print(amol.firstName)
print(amol.lastName)
print(amol.salary)
amol.displayName()
amol.displaySalary()


# example 2

# Multi-lvel

class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayGName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        self.firstName = fn
        self.lastName = ln
        self.fname = ffn
    def displayFname(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self ,fn,ln,ffn,ssn):
        super().__init__(fn,ln,ffn)
        self.sname = ssn

    def displaySname(self):
        print(self.sname + self.lastName)

chinmay = Son("manohar","deshpande","shirish","chinmay")
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.fname)
print(chinmay.sname)
chinmay.displayGName()
chinmay.displayFname()
chinmay.displaySname()

# program 3
# Hierarchical inheritance

class MotherA:

    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayMName(self):
        print(self.firstName + self.lastName)


class SonA(MotherA):
    def __init__(self,fn,ln,sn):
        super().__init__(fn,ln)
        self.sname = sn

    def displaySname(self):
        print(self.sname + self.lastName)


class DaughterA(MotherA):
    def __init__(self,fn,ln,dn):
        super().__init__(fn, ln)
        self.dname = dn

    def displayDname(self):
        print(self.dname)

chinmay = SonA("kanchan",'deshpande',"chinmay")
gauri = DaughterA("kamchan","dani","gauri")

chinmay.firstName
chinmay.lastName
chinmay.sname
chinmay.displayMName()
chinmay.displaySname()

gauri.firstName
gauri.lastName
gauri.dname
gauri.displayMName()
gauri.displayDname()

# Mulitple inheritance

class FatherA:
    def __init__(self,fn,ln):
        self.firstName  = fn
        self.lastName = ln
    def displayName(self):
        print("Father displayName is called")
        print(self.firstName + self.lastName)

class MotherA:
    def __init__(self,fn,ln):
        self.firstName  = fn
        self.lastName = ln
    def displayName(self):
        print("Mother displayName is called")
        print(self.firstName + self.lastName)

class SonM(MotherA,FatherA):
    def __init__(self,fn,ln,sname):
        super().__init__(fn,ln)
        self.sname = sname

    def displaySname(self):
        print(self.firstName + self.lastName)

chinmay = SonM("ninad","deshpande","chinmay")
chinmay.displaySname()
chinmay.displayName()










































