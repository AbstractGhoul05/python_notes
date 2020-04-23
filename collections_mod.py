from collections import Counter


my_list = [1, 1, 3, 4, 7, 3, 4, 4, 4, 5, 6, 7, 6, 6, 7, 3, 3, 3, 7, 2, 6, 6]
print(Counter(my_list))

my_string = "This is a just a random string, is this just a random string, or is it not a random string?"
string_split = my_string.split()
c = Counter(string_split)
print(c)
print(c.most_common(2))
print(c.most_common()[:-3:-1])