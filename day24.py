

# list comprehension
listA = [1,2,3,4,5,6,7,8,9,10]
#[2,4,6,8,10,12,14,16,18,20]
listB = []
for item in listA:
    listB.append(item * 2)
print(listB)

q2 = [item * 2 for item in listA]
print(q2)
#[expression  for item in iterable condition]

# program 1
listC = [1,2,3,4,5,6,7,8,9,10]
q3 = [item * item for  item in listC]
print(q3)

# program 2
listD = [11,22,33,44,55,66,77,88,99,100]
q4 = [item + 2 for item in listD ]
print(q4)

# program 3
listD = [11,22,33,44,55,66,77,88,99,100,-24,55,-36,-6,11]
listE = [item + 2 for item in listD if item > 0]
print(listE)
listF = [item if item < 0 else item + 2  for item in listD  ]
print(listF)

# program 4
names = ["chinmay","shirish","sam","sameer","satish","sachin"]
listG =  [item.upper() for item in names]
print(listG)
listH = [item.upper() for item in names if item.startswith('s')]
print(listH)

# program 5
# table of 5
listK = [item * 5  for item in range(1,11)]
print(listK)

# Regression ====>
# Javascript ----> Django

# program 6
str =  "I am learning javascript"
#["I","a","l","j"]

listG = [item[0] for item in  str.split(" ")]
["I","am","learning","javascript"]
print(listG)






































