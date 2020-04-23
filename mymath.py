def check_triangle(x, y, z):
    if x+y > z:
        if y+z > x:
            if z+x > y:
                return True
    
    return False

def findz(x, y):
    for x in range(1, 10):
        for y in range(1, 10):
            try:
                z = ((x+y)/((x*y)-1))
            except:
                print("Zero division")
            else:
                if z.is_integer():
                    if check_triangle(x, y, z):
                        print(f"{x}, {y}, {int(z)}")


sidelist = ((6, 4, 2), (9, 8, 1), (10, 3, 2), (14, 6, 1), (24, 5, 1))

for a, b, c in sidelist:
    x = (a+b-c)/2
    y = (a-b+c)/2
    z_2 = (-a+b+c)/2
    findz(x, y)
