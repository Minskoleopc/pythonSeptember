


# Define a string in python
first_name = "chinmay"
lastName = "deshpande"
print(first_name)
print(lastName)

# accessing the charcter of strinfg
# String stores the value by index

#  0   1   2   3
#  p   u   n   e
city = 'pune'
print(city[0])
print(city[1])
print(city[2])
print(city[3])

# looping through string for loop
# 0   1   2   3  4  5  6  7  8  9
# c   h   a   n  d  r  a  p  u  r
city2 = "chandrapur"

#using range()
for char in range(len(city2)):
    #print(char)
    print(city2[char])

# withoutrange()
for char in city2:
    print(char)

# program 2

city3 = "chandrapur"
#   0    1    2    3    4     5    6    7    8    9
#   c    h    a    n    d     r    a    p    u    r
#  -10  -9   -8    -7  -6    -5  -4   -3   -2    -1
#city3[startIndex:endIndex(not included):step]
print(city3[2])
print(city3[1:6])
print(city3[:8])
print(city3[2:])
print(city3[-1])
print(city3[-9:])
print(city3[-9:8])
print(city3[1:-1])
print(city3[0:-1:2])

# program 3
firstName = "chinmay"
lastName =  "deshpande"
print("My firstName is "+firstName+" my lastName is "+lastName)

# program 4

#upper()
first_name = "sarika"
q1 = first_name.upper()
print(q1)

#lower()
last_name = "Deshpande"
q2 = last_name.lower()
print(q2)

# strip()
city2 = " goa "
print(len(city2))
city2 = city2.strip()
print(len(city2))

# lstrip()
city2 = " goa "
city2 = city2.lstrip()
print(len(city2))
# rstrip()
city2 = " goa "
city2 = city2.rstrip()
print(len(city2))
# reading excel

# split()
info = "chinmay shirish deshpande"
# ["chinmay,"shirish","deshpande"]
# ["chinm","y shirish deshp","nde"]
q4 = info.split(" ")
q5 = info.split("a")
print(q4)
print(q5)

# join()
info = ["chinmay","shirish","deshpande"]
q6 = "-".join(info)
q7 = "@".join(info)
print(q7)

# replace()
info2 = "I am learning javascript"
q8 = info2.replace("javascript", "python")
print(q8)

# startsWith()
city10 = "kanpur"
q9 = city10.startswith("kan")
print(q9)
# endsWith()
q10 = city10.endswith("r")
q11 = city10.endswith("pur")
print(q10)
print(q11)

# find()
#   0   1   2  3  4  5 6
#   n   a   g  p  u  r a

city11 = "nagpura"
q11 = city11.find("a",2)
q12 = city11.find("a",2,5)
print(q11)
print(q12)

# index()
# city11 = "nagpur"
# q13 = city11.index("i")
# print(q13)
# raises the error

# count()
city12 = "chandrapur"
# c  h  a  n  d  r  a  p  u  r
q14 = city12.count("a")
print(q14)

# isdigit()
info1 = "1233a2425435365464564"
q15 = info1.isdigit()
print(q15)

#isalpha()
info2 = "aasfdafds"
q16 = info2.isalpha()
print(q16)

# isalnum()
info3 = "asdsa"
info3a = "123123"
info4 = "123asdasd"
info5 = "asd123@@"

print(info3.isalnum())
print(info3a.isalnum())
print(info4.isalnum())
print(info5.isalnum())






















