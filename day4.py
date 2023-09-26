


# Human ----- amol
# Property - color , gender , height weigh
# Method - walk() , talk()


#Vehicle ---- audi
#Property - color , type , model , companyName
#Method - start() , stop()


# Bank acc
# Property - accName , accNo , bal
# Method - deposit() , withdrawl()


names = ["sarika","poorva","shraddha","roshni","sumit"]
q1  = len(names)
print(q1)

# append()
fruits = ["apple","mango","banana","orange","apple"]
fruits.append("chikoo")
print(fruits)

# count
q1 = fruits.count("apple")
print(q1)

#index()
#                0             1          2           3           4
vegetables = ["cauliflower", "brinjal","cabbage", "ladyfinger","brinjal"]
q2 = vegetables.index("brinjal")
q3 = vegetables.index("brinjal",2)
print(q2)
print(q3)

#reverse()
vegetables.reverse()
print(vegetables)


#pop()
#          0         1         2         3
cities = ["pune","banglore","kolkata","chennai"]
cities.pop()
cities.pop(2)
print(cities)

#remove()
cities.remove("banglore")
print(cities)


#extend()
country = ["india","pakistan","srilanka","china","cuba"]
country.extend(["USA","UK","Germany"])
print(country)

numA = [11,22,33]
numB = [44,55,66]
#numA.extend(numB)
numB.extend(numA)
print(numA)
print(numB)

#insert()
animals = ["tiger","lion","rabbit","snake"]
animals.insert(3,"deer")
print(animals)

# clear()
animals.clear()
print(animals)

#sort()
cities2 = ["chennai","banglore","kolkata","gaya","wardha","nagpur"]
cities2.sort()
print(cities2)

#copy()

flowers = ["lily","rose","jasmine","marrygold"]

# flowersB = flowers
# flowersB[2] = "lotus"
# print(flowersB)
# print(flowers)

flowerC = flowers.copy()
flowerC[2] = "lotus"
print(flowerC)
print(flowers)


# tuple
# add
# update
# remove
# finxed size , values stored by index  ------- tuple()

listA = [11,22,33,44]
print(listA)
print(type(listA))

listB = list([55,66,77,88])
print(listB)
print(type(listB))
listB[2] = 666
print(listB)


# tuple
tupleA = tuple(["apple","mango","banana"])
print(tupleA)
listA = list(tupleA)
print(listA)
listA.append("chikoo")
tupleA = tuple(listA)
print(tupleA)
#tupleA[2] = "chikoo"

names = tuple(["poorva","sarika","vikas"])
print(names)
cities = ("pune","chennai","kolkata","banglore","mysore")
print(cities)
country = "india",
print(country)

# tuple stores the value by index
q1 = cities[0]
print(q1)
# loop using range()

for x in range(5):
    #print(x)
    print(cities[x])

# without range()
for city in cities:
    print(city)





















































































