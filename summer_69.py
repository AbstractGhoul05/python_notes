def summer_69(my_list):
    total = 0
    add = True
    for num in my_list:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total            

print(summer_69([1, 8, 45, 90, 6, 3, 13, 64, 9, 57]))