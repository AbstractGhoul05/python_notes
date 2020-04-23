try:
    f = open('testfile.txt', mode='r')
    f.write("Hello World!")
except TypeError:
    print("Hey, you have a type error")
except OSError:
    print("Hey, you have an OS error")
finally:
    print("I always run")


print("Will this get executed")

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops! that is not a number")
        else:
            print("Yes! Thank You!")
            break
        finally:
            print('End of try/exception/finally')

ask_for_int()
