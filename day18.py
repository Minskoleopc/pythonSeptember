
# AssertionError
#
# try:
#     x = int(input("Enter the number between 5 and 10"))
#     assert  x >= 5 and x <= 10
#     print("The number entered is: ",x)
# except AssertionError:
#     print("The condition is not meet")


# try:
#     x = int(input("Enter the number between 5 and 10"))
#     assert  x >= 5 and x <= 10 , "The entered number was not within range"
#     print("The number entered is: ",x)
# except AssertionError as e:
#     print("The condition is not meet")
#     print(e)

# userDefined Exception
print("Hello")
class MyException(Exception):
    def __init__(self,x):
        self.msg = x

# writing a method to check for the low balance
def check(dict):
    for k,v in dict.items():
        if(v < 2000):
            raise MyException("Balance amount is less than 2 thousand for "+ k)

bank = {
    "chinmay":3000,
    "sarika":500,
    "poorva":8000
}
try:
    check(bank)
except MyException as e:
    print(e)

print("Bye")

# Logging the exception
# file concept

#  File handling in python
# opening a file in python
# f = open('myfile2.txt','w')
# # taking inpur from user
# str = input('Enter the text')
# # writing into the file
# f.write(str)
# #closing the file
# f.close()

# read
# Write a program to read the file
#
# f = open('myfile2.txt','r')
# str = f.read()
# print(str)
# f.close()

#append
#opening a file in python
f = open('myfile2.txt','a+')
# taking inpur from user
str = input('Enter the text')
# writing into the file
f.write(str + "\n")
#closing the file
f.close()










