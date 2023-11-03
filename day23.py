#program 1
def addTwo(fun):
    def inner():
        v = fun()
        return v + 2
    return inner

@addTwo
def num():
    return 10
print(num())


# program 2
def double(fun):
    def inner():
        v = fun()
        return v * 2
    return inner

@double
def num():
    return 10
print(num())

# program 3
def decor(fun):
    def inner():
        v = fun()
        return v + 2
    return inner

def decor1(fun):
    def inner():
        v = fun()
        return v * 2
    return inner

@decor
@decor1
def num():
    return 10
print(num())

# program 4
for x in range(1 ,11):
    print(x)

#(1,2,3,4,5,6,7,8,9,10)

def gen(x,y):
    while(x<= y):
        yield  x
        x = x + 1
f = gen(1,10)
# (1 2 3 4 5 6 7 8 9 10)

for ele in f:
    print(ele)

# program 5
def genb():
    yield "A"
    yield "B"
    yield "C"
s = genb()

print(next(s))
print(next(s))
print(next(s))

for ele in s:
    print(ele)












