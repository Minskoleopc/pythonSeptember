
# functions
# postional arguments
def addition(x,y):
    return x + y
q1 = addition(12,2) # actual argument
print(q1)

# program 2
def addition2(x,y):
    return x + y
q1 = addition2(y = 18,x= 90) # actual argument
print(q1)

# default values
# program 3
def addition3(x = 1,y = 1):
    return x + y
print(addition3())
print(addition3(12,3))

# program 4
def addition4(*agrs):
    print(agrs)
    total = 0
    for item in agrs:
        total = total + item
    return total

q4 = addition4(23,4,5,6,7,2,2,4,5,6,7,84,6,7,7,3,4,4)
print(q4)

#program 5
def filterElements(x,*args):
    #args = list(args)
    return tuple(filter(lambda a: a > x,args))

q5 = filterElements(25,45,6,77,33,44,66,2,3,4,99,77,44,55,66,77,23,44)
q6 = filterElements(70,45,6,77,33,44,66,2,3,4,99,77,44,55,66,77,23,44)
print(q5)
print(q6)

# program 6
def info(**kwargs):
    print(kwargs)
    kwargs['city'] = "pune"
    return kwargs

q7 = info(firstName = "chinmay",lastName = "deshpande",rollNo = 23)
print(q7)

# int as a parameter and integer as return type

def mul(s,t):
    return s + t
w1 = mul(13,5)
print(w1)
print(type(w1))


# float as a parameter and float as a return type
def mul(x,y):
    return x*y
w2 = mul(12.4,34.5)
print(w2)

# list as a parameter and list as return type
cities = ["pune","mumbai","banglore"]
def addCity(lst,cityName):
    lst.append(cityName)
    return lst
print(addCity(cities,"nagpur"))

# tuple as parameter and tuple as return
def updatetuple(v):
    a = list(v) #[2,3]
    a[0] = 77 #[77,3]
    a = tuple(a) #(77,3)
    return a
print(updatetuple((2,3)))

# string as parameter and string as return
def greet(word):
    return "Good " + word + "!"
print(greet("morning"))

# dict as parameter and dictionary as return

info = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}

def addCity(dict):
    dict['city'] = "pune"
    return dict
print(addCity(info))

# set as parameter and set as return type

setA = {11,22,33,44}
def addEl(setA):
    setA.add(444)
    return setA
print(addEl(setA))

# function as parameter
square = lambda  x : x * x
def calculate(square,value):
    return square(value)

print(calculate(square,2))
print(calculate(square,4))

# function as return type
def cal():
    return lambda x : x * x
q1 = cal()
# q1 = lambda x : x * x
print(q1(5))
















