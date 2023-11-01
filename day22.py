# functions
squ  = lambda x : x * x
y  = squ(5)
print(y)

# program 2
birthYear  = [1989,1990,1991,1992]
ages = []
# [34,33,32,31]
for item in birthYear:
    #(2023 - item)
    ages.append(2023 - item)
print(ages)

# program 3
age = lambda  x : 2023 - x
ages = list(map(age,birthYear))
print(ages)
b = list(map(lambda  x : 2023 - x,birthYear))
print(b)

# program 4
numbers = [11,22,33,44,55]
# [21,32,43,54,65]
c = list(map(lambda x:x + 10,numbers))
print(c)

# filter
# program 5
marks = [44,55,77,22,44,53,52]
above50 = []
# [55,77,53,52]
for item in marks:
    print(item)
    if item > 50:
        above50.append(item)
print(above50)

marks = [44,55,77,22,44,53,52]
d = lambda  x : x > 50
e = list(filter(d,marks))
f = list(filter(lambda  x : x > 50,marks))
print(e)
print(f)

# program 6
names = ["chinmay","ram","sham","satish","ganesh","shraddha"]
# ["sham","satish","shraddha"]
k = lambda x : x.startswith('s')
g = list(filter(k,names))
print(g)

# program 7  reduce()
numbers = [11,22,33]
total = 0

for item in numbers:
    total = total + item
print(total)

from functools  import  *
#reduce(lambda acc, char: acc+char, got_chars,0)/len(got_chars)
numbers = [11,22,33]
print(reduce(lambda  acc,num:acc+num,numbers,5)) # 11 # 33  # 66
# map()
# filter()
# reduce()

# program 8 (default values)
def addition(x = 1,y = 1):
    return x + y
e3 = addition(12,4)
e2 = addition(78,2)
print(e3)
print(e2)

# program 9
def info(birthYear ,currentYear):
    return currentYear - birthYear
e1 = info(currentYear= 2023,birthYear= 1989)
print(e1)

# program 10
def addition(*args):
    print(args)
    total = 0
    for item in args:
        total = total + item
    return total

j = addition(23,4,6,6,77,33,44,55,66,77,78,55,77,88,44,44,33)
print(j)

# program 11
def info2(**kwargs):
    print(kwargs)
    kwargs['city'] = "pune"
    return kwargs
e = info2(firstName = "chinmay",lastName = "deshpande",age = 23)
print(e)

# decorators and generators
# regular expression



























