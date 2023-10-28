
x = 10
print(x)

#LIST
#          0          1       2       3       4
names = ["chinmay","shirish","ram","satish","sujoy"]
#list stores the value by index
print(type(names))
q1 = names[0]
q2 = names[1]
q3 = names[2]
q4 = names[3]
q5 = names[4]
print(q1)
print(q2)
print(q3)
print(q4)
print(q5)

# program 2
#           0        1        2         3        4         5
cities = ["pune","mumbai","banglore","kolkata","chennai","indore"]
print(cities)

# total number of elements
q6 = len(cities)
print(q6)
print(cities[2])

# program 3
# printing all element of list
fruits = ["apple","mango","banana", "chikoo"]

# using range
# for x in range(startValue,EndValue(not included),stepSize):
#     # statements

for x in range(10):
    print(x)

for x in range(5,10):
    print(x)

for x in range(1,10,2):
    print(x)

for x in range(2,21,2):
    print(x)

for x in range(1,10,3):  # 1 ,4,7
    print(x)

for x in range(3,31,3):
    print(x)

for x in range(7,71,7):
    print(x)

#               0          1        2          3
vegetables = ["cabbage","potato","tomato","ladyfinger"]
print(vegetables[0])
print(vegetables[1])
q7 = len(vegetables)
print(q7)

for x in range(len(vegetables)):
    #print(x)
    print(vegetables[x])

#        0   1  2  3  4
marks = [22,33,44,55,66]
for x in range(len(marks)):
    #print(x)
    print(marks[x])

# without range
animals = ["tiger","lion","rabbit","snake","bear"]
for x in range(len(animals)):
    print(animals[x])

for x in animals:
    print(x)


# program 4
# updating the element of list

country = ["india","srilanka","pakistan","china","bangladesh"]
print(country[0])
country[0] = "Bharat"
print(country)

# program 5
print("india" in country)
print("bharat" in country)
print("Bharat" in country)










