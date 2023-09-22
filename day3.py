


# ternary
a = 10
b = 50
if a > b :
    print("a is greater")
else:
    print("b is greater")


print("a is greater") if a > b else print("b is greater")

# program 2
age = 17
q1 = "candrive" if age >= 18 else "cannot drive"
print(q1)

# list


# program 1
# defining a list


names = ["chinmay","shirish","ram"]
print(names)
print(type(names))

marks = [11,22,33,44,55]
print(marks)
print(type(marks))

info = ["chinmay",34,True]
print(info)
print(type(info))


# program 2
#            0         1       2        3           4
flowers = ["lily", "jasmine","rose","marrygold","lotus"]
#           -5       -4       -3         -2          -1

print(flowers[0])
print(flowers[-5])
#slicing the list
#listName[startIndex:endIndex(not included):Steps]

print(flowers[1:3]) # ["jasmine","rose"]
print(flowers[0:4]) # [["lily", "jasmine","rose","marrygold]
print(flowers[-5:-1])
print(flowers[-5:3])
print(flowers[1:-1])
print(flowers[-1:-4])

#      0   1  2  3 4  5  6  7  8  9
marks = [11,22,33,44,55,66,77,88,99,20]
print(marks[0:9:3])

# program 3 looping through list

#            0       1          2       3          4        5
cities2 = ["pune","nagpur","banglore","kolkata","chennai","mysore"]
# total number of elements in list
q1 = len(cities2)
print(q1)

# 2 ways to loop through a list
# list str tuple, dictionary , set
# loop   for loop and while

#           0        1         2        3          4        5
cities2 = ["pune","nagpur","banglore","kolkata","chennai","mysore"]
print(cities2[0])
print(cities2[1])
#one using  range function

#range(startIndex, endIndex (not included),Steps)
#range(endIndex)
for x in range(10):
    print(x)
for x in range(1,10):
    print(x)
for x in range(2,21,2):
    print(x)

#                0          1          2            3
vegetables = ["cabbage","brinjal","cauliflower","ladyfinger"]
print(vegetables[0])
print(len(vegetables))

for item in range(len(vegetables)):
    #print(item)
    print(vegetables[item])

#without using the range function
for item in vegetables:
    print(item)

#           0  1  2    3   4
numbers = [11,22,333,4444,5555]

for  x in numbers:
    print(x)

for x in range(len(numbers)):
    #print(number)
    print(numbers[x])

# program 4
# Check whether a particular element exist in list

countries  = ["india","pakistan","srilanka","bangladesh"]
# using in operator
# print("India" in countries)
x = input("Enter the country name")
if x in countries:
    print("country is available")
else:
    print("country not available")









































