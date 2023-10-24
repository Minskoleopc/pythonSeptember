
# program 1
# filehandling
#txt file
# opening the file in write mode
# f = open('file3.text','w')
# # input from user
# str = input("Enter the  name :")
# # To write into the file
# f.write(str)
# #Closing of file
# f.close()

# program 2
# r = open('file3.text','r')
# str = r.read()
# print(str)
# r.close()

# program3
# f4 = open('text4.txt','a')
# userInput = None
# print('please enter @ to exist the file')
# while(userInput != '@'):
#     userInput = input("Enter the data") # chinmay # sarika # @
#     if(userInput != '@'):
#         f4.write(userInput + "\n")
# f4.close()

# program 4
# r - read
# w = write
# a - append +
# a + append + write mode
#
# f6 = open('file5.txt','a+')
# print('please enter the @ to exist the file')
# userInput  = None
# while(userInput != '@'):
#     userInput = input('Enter the name :')
#     if userInput != '@':
#         f6.write(userInput + "\n")
#
# # reading from the file
# f6.seek(0,0)
# str = f6.read()
# print(str)
# f6.close()

# f6.seek(moveToNumberOfBytes,position)
# f6.seek(5,0) --> start of file
# f6.seek(5,1) --> current position of file
# f6.seek(5,2) --> end of the file
#I am learning javascript , I am learning python

# program 5
# f7 = open('text4.txt','r')
# lst = f7.readlines()
# print(lst)
# for item in lst:
#     print(item)
# f7.close()

# program 6
import os , sys
fileName = input("Enter the name :")
if os.path.isfile(fileName):
    f7 = open(fileName,'r')
else:
    print(fileName + " does not exist")
    sys.exit()
str2 = f7.read()
print(str2)
f7.close()






















