
# method 1
names = ["chinmay","sarika","poorva"]
print(names)
print(type(names))

# method2
names = list(["ram","sham",'sarika'])
print(names)

# stores the value by index
# retrive the value
print(names[0])
# add the element
names.append("sham")
# update the list
names[0] = "sameer"
# delete
names.pop()

# tuple
tupleA = (1,2,3)
print(tupleA)
print(type(tupleA))

tupleB = tuple(["sarika","poorva","chinmay","satish"])
print(tupleB)
print(type(tupleB))

tupleC = 1,
print(tupleC)
print(type(tupleC))

# Differenc between list and tuple
# tuples also stored the value by index

cities = ("pune","banglore","mumbai")
print(cities[0])

# retrive
print(cities[len(cities)-1])

# update not possible
# cities[0] = "wardha"
# add the new element not possible
# deleting the element not possible
# tuple allow duplicate


# program 2
#           0           1          2           3         4
country = ("india","srilanka","bangladesh","austrila","japan")
# retrive
print(country[0])

# using for loop using range
for x in range(len(country)):
    #print(x)
    print(country[x])

# another loop without using range function
for item in country:
    print(item)

# program 2 (slicing)
#           0         1            2           3         4
country = ("india","srilanka","bangladesh","austrila","japan")
#            -5          -4           -3      -2          -1
# slicing
#print(country[startIndex:endIndex(not included)])
print(country[1:])
print(country[:3])
print(country[1:3])
print(country[:-1])
print(country[-3])
print(country[-3:4])
print(country[1:-1])
print(country[-1:-4])


# program 3(update)
flowers = ("lily", "jaminse","rose")
print(type(flowers))
flowers = list(flowers)
print(type(flowers))
flowers[0]= "maryGold"
print(flowers)
flowers = tuple(flowers)
print(flowers)

# program 4 delete  the value from tuple
flowers = ("lily", "jaminse","rose")
flowers = list(flowers)
flowers.pop()
print(flowers)
flowers = tuple(flowers)
print(flowers)

# program 5 add the value to tuple
flowers = ("lily", "jaminse","rose")
flowers = list(flowers)
flowers.append("maryGold")
flowers = tuple(flowers)
print(flowers)

# program 6
print(len(flowers))

# program unpacking for tuple
animals = ("tiger","lion","rabbit","bear")
print(animals)
print(type(animals))

a = animals[0]
print(a)
# a1,a2,a3,a4 = animals
# print(a1)
# print(a2)
# print(a3)
# print(a4)
a1,*a2 = animals
print(a1)
print(a2)

animals = ("tiger","lion","rabbit","bear")
a1,*a2,a3 = animals
print(a1)
print(a2)
print(a3)

# addition and multiplication on tuple
tupleA = (1,2,3)
tupleB = (4,5,6)
print(tupleA+ tupleB)
print(tupleA * 2)

# methods
countries = ("UK","autrilia","UK","pakistan","bharat","srilanka")
q1 = countries.index("pakistan")
print(q1)

q2 = countries.count("UK")
print(q2)


































