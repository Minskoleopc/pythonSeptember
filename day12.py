

#Inhertitance and polymorphism

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

amol = Student()
amol.setFirstName("amol")
amol.setLastName("rao")
amol.setAge(12)

amol.getAge()
amol.getLastName()
amol.getFirstNname()

class Teacher:
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

    def setSalary(self,sl):
        self.salary = sl
    def getSalary(self):
        print(self.salary)

amol = Teacher()
amol.setFirstName("amol")
amol.setLastName("rao")
amol.setAge(12)
amol.setSalary(1000)

amol.getAge()
amol.getLastName()
amol.getFirstNname()
amol.getSalary()





