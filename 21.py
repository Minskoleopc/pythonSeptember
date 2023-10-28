
# Basic function
def addA(x,y):
    return x + y
q1 = addA(12,3)
print(q1)

# int as parameter and int as return
def subB(x,y):
    return x - y
q2 = subB(12,6)
print(q2)

# float as a parameter and float as return
def calculateRadius(val):
    return 2.0 * val * val
q3 = calculateRadius(14.4)
print(q3)

# program 3
# boolean as parameter and boolean as return type
def canDrive(vehicleAvail, age):
    if vehicleAvail and age >= 18:
        return True
    else:
        return False

q4 = canDrive(True,20)
print(q4)

# program 4
# str as parameter and string as return type
def greet(word):
    return "Good" + " "+ word
q5 = greet("Morining")
print(q5)

#program 5
# list as parameter and list as return type
listA = [11,22,33,44]
def addElement(list):
    list.append(55)
    return list
q6 = addElement(listA)
print(q6)

# program 6
# dictionary as parameter and dictionary as return type
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":12,
    "rollNo":34
}

def addCity(information):
    information.update({'city':"pune"})
    return information
q7 = addCity(info)
print(q7)

# program 7
# tuple as parameter and tuple as return type
marks = (12,13,14)
def updateMarks(tupA):
    tupA = list(tupA)
    tupA[2] = 15
    tupA = tuple(tupA)
    return tupA

a,b,c = updateMarks(marks)
print(a)
print(b)
print(c)

# program 8
# set as parameter and set as return type
setA = {11,22,33,44,55,66}
def addVal(setX):
    setX.add(77)
    return setX
q2 = addVal(setA)
print(q2)

# program 9
# lamba function
mul = lambda x : x * x
print(mul(3))

# function as parameter
addTwo = lambda x: x + 2
def addingValues(fn,x):
    # fn = lambda x: x + 2
    return fn(6)
q4 =addingValues(addTwo,6)
print(q4)

# program 10
#function as a return type
def calculateAge():
    return lambda birthYear:2023 - birthYear
q1 = calculateAge()
print(q1(1989))

# map filter reduce




















