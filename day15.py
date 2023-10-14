
# abstraction
from abc import  ABC ,abstractmethod
class worldBank(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def loan(self):
        pass

class SBI(worldBank):
    def save(self):
        print("i am from SBI")

    def loan(self):
        print("i am from the loan method")

class PNB(worldBank):
    def displayBranch(self):
        print("PNB branch")
    def save(self):
        print("i am from PNB save")
    def loan(self):
        print("i am from PNB save")

a = PNB()
a.loan()
a.save()
a.displayBranch()


# filehandling
# regular expression
# exception handling
# functions

# django