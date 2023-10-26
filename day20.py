# count the number of lines
# count the number of words
# count the number of characters

import os , sys

# f = open('file7.txt','w')
# print('please enter  @ to stop writing')
# userInput = None
# while userInput != '@':
#     userInput = input('Enter the text')
#     if userInput != '@':
#         f.write(userInput + "\n")
# f.close()
#
# fname = input('Enter the filename')
# if os.path.isfile(fname):
#     f = open(fname,'r')
# else:
#     print(fname + 'does not exist')
#     sys.exit()
#
# # intialize variables
# countLine = 0
# countWords = 0
# countCharacters = 0
# for line in f:
#     print(line)
#     countLine = countLine + 1
#     countWords = countWords + len(line.split())
#     countCharacters = countCharacters + len(line)
#
# print(countLine)
# print(countWords)
# print(countCharacters)
# f.close()

# program 2
# Opening the files in binary mode
# f1 = open('download.jpg','rb')
# f2 = open('new.jpg','wb')
# bytes = f1.read()
# f2.write(bytes)
# f1.close()
# f2.close()

# program 3
# with open('file7.txt','r') as f:
#     for line in f:
#         print(line)
#
# with open('file7.txt','a+') as f2:
#     str = input("Enter the text" + "\n")
#     f2.write(str)
import pickle
class Employee:
    def __init__(self,name,id,salary):
        self.name = name
        self.id  = id
        self.salary = salary

    def display(self):
        print(self.name,self.id,self.salary)
# f = open('emp.dat','wb')
# users = int(input("Enter the numbers of Empployee to create")) #2
# for x in range(users):
#     name = input('Enter the name')
#     id = input('Enter the id')
#     salary = input("Enter the salary")
#     e = Employee(name,id,salary)
#     pickle.dump(e,f)
# f.close()

# reading the dat file
# f2 = open('emp.dat','rb')
# print('Employee details')
# while True:
#     try:
#         obj = pickle.load(f2)
#         obj.display()
#     except EOFError as e:
#         print(e)
#         break
# f2.close()
























