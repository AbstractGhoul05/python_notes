import math

def count_primes(limit):
    primes = [2]
    x = 3
    if limit < 7:
        return 0
    while x <= limit:
        for y in primes:
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))