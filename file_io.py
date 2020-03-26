myfile = open('myfile.txt')
with open('myfile.txt', mode='w') as my_file:
    my_file.write('this is the first line\n')
    my_file.write('this is the second line\n')
    my_file.write('this is the third line')
print(myfile.read())
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
contents = myfile.read()
print(contents)
myfile.seek(0)
print(myfile.readlines())
newFile = open("C:\\Users\\aayus\\Documents\\Python\\myfile.txt")
print(newFile.read())
newFile.close()
with open('myfile.txt') as some_file:
    contents = some_file.read()
with open('myfile.txt', mode='a') as another_file:
    another_file.write('this is the fourth line')
print(myfile.read())
with open('random_new_file.txt', mode='w+') as a_new_file:
    a_new_file.write('I CREATED THIS!')
with open('random_new_file.txt', mode='r') as same_new_file:
    print(same_new_file.read())