

# type

#introvert      # extrovert
# calm          loud
# less social   more social
# less outing   more outing

# Human
# Properties - age , color , gender , height , weight
# Method - walk() , talk()

# Vehicle
# Properties - color , regNo , model , type
# Method - start() , stop

# Bank
# Properties - bankAccNo , accName , bal , type , branchName , IFSC code
# Method - deposit() , withdrawl()

x = 10
print(x)
print(type(x))
# 9 , -9 , 0

y = 17.7
print(y)
print(type(y))
# 7.7 , -8.8 ,0.7

z = True
print(z)
print(type(z))
#True False

n = "chinmay"
print(n)
print(type(n))
# " " , "A", "1", "-1", "Adbc", "Aasfaf123$$$"

# comparison operator
# entity < entiry ====> boolean ====> True or False
# < , > , <= , >= , != , ==
print(4 == 4)
print(4 != 5)
print(4 == 5)
print(4 >= 5)
print(4 <= 5)
print(4 >= 4)
print(4 <= 4)
print(4 > 5)
print(4 < 5)

# logical operator
# and

# True     and     True    =====> True
# False    and     True    =====> False
# True     and     False   =====> False
# False    and     False   =====> False

print(7 == 7 and 8 == 8)
print(7 != 7 and 8 == 8)
print(7 == 7 and 8 != 8)
print(7 != 7 and 8 != 8)

# or
# True     or     True    =====> True
# False    or     True    =====> True
# True     or    False    =====> True
# False    or    False    =====> False

print(2 == 2 or 3 == 3)
print(7 != 7 or 8 == 8)
print(7 == 7 or 8 != 8)
print(7 != 7 or 8 != 8)

# not !
# True   not --- False
# False  not --- True
print(not (8 == 8))
print(not (8 != 8))

# conditional statements

# one input and multiple outcomes
# numT > 0 and numT <= 5  ======> 10 % discount
# numT > 5 and numT <= 10 ======> 20 % discount
# numT > 10               ======> 30 % discount

#if condition:
    # statements

numT = 17
if numT > 0 and numT <= 5:
    print("10 % discount")
if numT > 5 and numT <= 10:
    print("20 % discount")
if numT > 10:
    print("30 % discount")

# if elif  else

numT2 = -17

if numT2 > 0  and  numT2 <= 5:
    print("10 % discount")
elif numT2 > 5 and numT2 <= 10:
    print("20 % discount")
elif numT2 > 10:
    print("30 % discount")
else:
    print("incorrect input")

marks = 50
# if marks > 90:
#     print("Grade A")
# if marks > 75:
#     print("Grade B")
# if marks > 65:
#     print("Grade C")

if marks > 90:
    print("Grade A")
elif marks > 75:
    print("Grade B")
elif marks > 65:
    print("Grade C")
else :
    print("please try again !")



s = 10
t = 50

if s > t:
    print("s is greater")
else:
    print("t is greater")


x = 10
y = 50
z = 300

if x > y and x > z:
    print("x is greater")
elif y > x and y > z:
    print("y is greater")
else:
    print("z is greater")

































# tenaray operator