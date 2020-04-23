def new_decorator(some_func):
    def wrap_func():
        print("This is a new line before the func")
        some_func()
        print("This is a new line after the func")

    return wrap_func

@new_decorator
def cool():
    print("I am very very cool!")

cool()
