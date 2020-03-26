from random import shuffle
from random import randint

mylist = [1, 2, 3, 4, 5, 6]
shuffle(mylist)
print(mylist)
print(randint(0, 10000))
inputnum = input('Enter a Number: ')
print(f'You entered {inputnum}')
inputint = int(inputnum)
print(f'You entered {inputint}')
mylist = [x for x in range(0, 11) if x%2==0]
print(mylist)