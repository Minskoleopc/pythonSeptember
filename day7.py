

names = ["chinmay","deshpande",77,55]

names2 = {
    # prop : value
    # key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "rollNo":77,
    "age":55
}
print(names2)
print(type(names2))

# with contructor
vehicle = dict(
    {
        "color":"blue",
        "type":"sedane",
        "model":12}
)
print(vehicle)
print(type(vehicle))


# program 3
info = {
    "fn":"chinmay",
    "ln":"deshpande",
    "age":30,
    'skills':["python","javascript"]
}
print(info)

# retrive
q1 = info['fn']
q2 = info['age']
print(q1)
print(q2)
q3 = info.get('skills')
print(q3)
# update the value
info = {
    "fn":"chinmay",
    "ln":"deshpande",
    "age":30,
    'skills':["python","javascript"]
}
info['fn'] = "tanmay"
print(info)
info.update({"city":"pune","age":45})
print(info)

# add another key value to dictionary
info = {
    "fn":"chinmay",
    "ln":"deshpande",
    "age":30,
    'skills':["python","javascript"]
}
info['language'] = ["hindi","marathi"]
print(info)
info.update({"country":"India"})
print(info)

# delete the key value from dictionary

info = {
    "fn":"chinmay",
    "ln":"deshpande",
    "age":30,
    'skills':["python","javascript"]
}
info.pop("fn")
print(info)
#{'ln': 'deshpande', 'age': 30, 'skills': ['python', 'javascript']}
info.popitem()
print(info)

# deleting the complete dictionary
# del info
# print(info)


# program 4
info = {
    "fullName":"chinmay deshpande",
    "age":23,
    "rollNo":66,
    "age":88
}
print(info)
# looping over dictionary
# particular key in dictionary
#print("Age" in info)

# loop over a dictionary
for key in info:
    print(key,info[key])


# methods

animal = {
    "name":"tiger",
    "color":"orange",
    "age":34
}
q1 = animal.get("name")
print(q1)

# clear()
# animal.clear()
# print(animal)

#copy()
animal2 = animal.copy()
animal2['city'] = "tadoba"
print(animal)
print(animal2)

#pop(),popitem()
animal2.pop('age')
animal2.popitem()
print(animal2)

#update()
animal = {
    "name":"tiger",
    "color":"orange",
    "age":34
}
animal.update({"city":"tadoba"})
print(animal)
for  key in animal:
    print(key,animal[key])

for prop in animal.keys():
    print(prop)

for val in animal.values():
    print(val)

for k,v in animal.items():
    print(k,v)

# fromkeys()
q6 = dict.fromkeys(["prop","prop2","prop3"],123)
print(q6)

#setdefault()
animal = {
    "name":"tiger",
    "color":"orange",
    "age":34
}
q8 = animal.setdefault("city","pune")
print(q8)
print(animal)



























