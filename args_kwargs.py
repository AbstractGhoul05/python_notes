def my_args(*args):
    return sum(args)

def my_kwargs(**kwargs):
    if 'fruit' in kwargs:
        print("My favourite fruit is {}".format(kwargs['fruit']))
    else:
        print('Fruit not found :(')

def my_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0], kwargs['food']))

print(my_args(1, 5, 8))
print(my_kwargs(fruit='apple'))
print(my_args_kwargs(10, 20, 30, fruit='apple', food='eggs', animal='lion'))
