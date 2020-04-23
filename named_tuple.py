from collections import namedtuple

Dog = namedtuple('Dog', 'age breed color')

bruno = Dog(age=2, breed='Lab', color='brown')
print(bruno.age)
