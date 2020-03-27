def is_even(num):
    return num%2 == 0


mylist = []
for i in range (11):
    if is_even(i):
        mylist.append(i)

print(mylist)
my_list2 = list(map(is_even, range(0, 11)))   
print(my_list2)

my_list3 = list(filter(is_even, range(0, 11)))
print(my_list3)

lambda s: s[0]