# compile time error

# program 1
# def add()
#     print(9+9)
# add()

# program 2
# def sub():
# print(7 - 5)
# sub()

# run time error
# program 3
# print("hello")
# numOne = int(input("Enter the number one"))
# numTwo = int(input("Emter the number two"))
# print(numOne / numTwo)
# print("Bye")

# program 4
#           0       1          2
# cities = ["pune","mumbai","bangalore"]
# print(cities[4])

# logical error
# sal = 10000
# def totalSalary(sal):
#     return sal * 0.10
# print(totalSalary(sal))

# Run time errors can be managed by exceptions
# Exceptions
# print("hello")
# print(2/0)
# print("bye")


# program 7
# try   except
# print("hello")
# try:
#     numOne = int(input("Enter num A"))
#     numTwo = int(input("Enter the number B"))
#     print(numOne / numTwo)
# except Exception as e:
#     print(e)
# print("bye")
#
# # program 8
# print("hello")
# try:
#     a = [11,22,3]
#     print(a[4])
# except Exception:
#     print('No many elements available')
# print("bye")
#
# # program  9
# # try   except  except
# print("hello")
# print("hello")
# try:
#     numOne = int(input("Enter num A"))
#     numTwo = int(input("Enter the number B"))
#     print(numOne / numTwo)
#     a = [11,22,3]
#     print(a[2])
#     print(q3)
#
# except ZeroDivisionError as e:
#     print(e)
#     print("please enter correct input")
# except IndexError as e:
#     print(e)
#     print("Not many elements available")
# except Exception as e:
#     print(e)

# print("bye")
# # program 10
# # try except finally
# print("hello")
# try:
#     numOne = int(input("Enter num A"))
#     numTwo = int(input("Enter the number B"))
#     print(numOne / numTwo)
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     print("i will always run")
# print("bye")

# program 11
# try except except else finally

try:
    numOne = int(input("Enter num A"))
    numTwo = int(input("Enter the number B"))
    print(numOne / numTwo)
    a = [11,22,3]
    print(a[2])
    #print(q3)

except ZeroDivisionError as e:
    print(e)
    print("please enter correct input")
except IndexError as e:
    print(e)
    print("Not many elements available")
except Exception as e:
    print(e)
else:
    print("Coming without exception")
finally:
    print("I am added and will always executed")


# user defined exceptions
# assert keyword
# logging warning










































