import ptvsd

def area(a, b, c):
    s = semiperimeter(a, b, c)
    return ((s*(s-a)*(s-b)*(s-c))**0.5)

def semiperimeter(a, b, c):
    return (a+b+c)/2

sidelist = ((6, 4, 2), (9, 8, 1), (10, 3, 2), (14, 6, 1), (24, 5, 1))

for a, b, c in sidelist:
    print(f"Semi perimeter: {semiperimeter(a, b, c)}")
    print(f"Area: {area(a, b, c)}")
