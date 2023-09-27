


# set
# set will not store duplicate values
# setA = set([11,22,33,44,44])
# print(setA)
# print(type(setA))
#
# setB = set((22,33,44,44))
# print(setB)
#
# SetC = set({22,33,44,55})
# print(SetC)
#
# setD = {11,22,33,44,55}
# print(setD)

# Set does not stores the value by index
# names = {"poorva","sarika","satish","ram","chinmay"}
# print(names)
# print(names[0])

names = {"poorva","sarika","satish","ram","chinmay"}
# looping through set
for item in names:
    print(item)

# remove
names.remove('poorva')
print(names)

# discard
q1 = names.discard('sarika')
print(q1)
print(names)

# pop
names.pop()
print(names)

# add
cities = {"pune","banglore","kolkata","chennai"}
cities.add("nagpur")
cities.add("nagpur")
print(cities)

# update
cities = {"pune","banglore","kolkata","chennai"}
cities.update(["wardha","mumbai","amravati"])
cities.update(("Gaya",))
cities.update({"jaipur","udaipur"})
print(cities)

# clear
cities.clear()
print(cities)

setA = {11,22,33}
# setB = setA
# setB.remove(11)

# print(setA)
# print(setB)

setC = setA.copy()
print(setC)
setC.remove(11)
print(setC)
print(setA)

################################################################

# union
setA = {11,22,33}
setB = {44,55,66}

setC = setA.union(setB)
print(setC)

# intersection
setA = {11,22,33}
setB = {44,55,33}
# setC = setA.intersection(setB)
# print(setC)

setA.intersection_update(setB)
print(setA)


# difference()
setA = {11,22,33}
setB = {44,55,33}

setC = setA.difference(setB)
print(setC)

# difference_upadte()
setA.difference_update(setB)
print(setA)


#symmetric_difference
setA = {11,22,33}
setB = {44,55,33}

setC = setA.symmetric_difference(setB)
print(setC)

#symmetric_difference_update()
setA.symmetric_difference_update(setB)
print(setA)


# isdisjoint
setA = {111,222,333}
setB = {44,22,333}
setD = setA.isdisjoint(setB)
print(setD)


setA = {11,22}
setB = {11,22,33}
print(setA.issubset(setB))
print(setB.issuperset(setA))



setA = {11,22,33}
print(len(setA))
print(max(setA))
print(min(setA))


































