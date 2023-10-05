


# constructor  #  instance variable , # class variable
# instance method , class method
# creating objects

class Bank:

    # class level variable
    city  = "pune"
    #Setting the instance variable
    def __init__(self,accName,accNo,bal):
        self.accName = accName
        self.accNo = accNo
        self.bal= bal
        self.transactions = []

    def deposit(self,amt):
        self.bal = self.bal+ amt
        self.transactions.append(amt)
        return self.bal

    def withDrawl(self,amt):
        if(self.bal > amt):
            self.bal = self.bal - amt
            self.transactions.append(-amt)
            return self.bal
        else:
            print("insufficient bal")

    def lastFiveTransaction(self):
        # slicing
        return self.transactions[-5:]

    # updating the class level variable
    @classmethod
    def updateCity(cls,cty):
        Bank.city = cty


chinmay = Bank("chinmay deshpande",123,1000)
print(chinmay.city)
Bank.updateCity("nagpur")
print(chinmay.city)

chinmay.withDrawl(1500)
print(chinmay.withDrawl(500))

chinmay.deposit(100)
chinmay.deposit(200)
chinmay.deposit(50)
chinmay.deposit(25)
chinmay.deposit(30)
chinmay.deposit(300)
chinmay.withDrawl(300)

print(chinmay.transactions)
print(chinmay.lastFiveTransaction())

# program static method
# static method are only for info process
# static methods we donot update any class level variable or we donot update any instance variable

# total of objects created from the class
# static methods
# static methods can be called on className

class Employee:
    country = "india"
    counter = 0

    def __init__(self,firstName,lastName,adharNo):
        Employee.counter =  Employee.counter + 1
        self.firstName = firstName
        self.lastName = lastName
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName + self.lastName)

    @staticmethod
    def displayCountOfObject():
        return Employee.counter

amol = Employee("amit","bhure",123)
chinmay = Employee("chinmay","despande",456)
komal = Employee("komal","lende",456)
print(Employee.displayCountOfObject())


# program 3
# Creating two classes , passing one class object to another class

class EmployeeB :
    def __init__(self,firstName,lastName ,age ,salary):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.salary = salary

    def displayinfo(self):
        print(self.firstName)
        print(self.lastName)
        print(self.age)
        print(self.salary)

class InfoClass:
    @staticmethod
    def displayInfoBasic(e):
        print(e.firstName)
        print(e.lastName)

abhisha = EmployeeB("abhisha","burande",24,1000)
InfoClass.displayInfoBasic(abhisha)

# inner class
# inheritance and polymorphism















































