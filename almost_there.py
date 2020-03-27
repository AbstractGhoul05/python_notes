def almost_there(num):
    return (abs(100-num) <= 10) or (abs(200-num) <= 10)

num = int(input("Enter a number: "))
print(almost_there(num))