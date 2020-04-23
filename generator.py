def calc_cubes(n):
    for x in range(n):
        yield x**3

for x in calc_cubes(10):
    print(x)

def gen_fibon(n):
    a = 1
    b = 1
    for x in range(n):
        yield a
        a, b = b, a+b

for x in gen_fibon(100):
    print(x)

g = gen_fibon(10)

print(next(g))
