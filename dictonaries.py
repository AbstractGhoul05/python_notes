my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print(my_dict['key2'])
new_dict = {'key1':24840, 'key2':['hi', 'hello'], 'key3':{'insideKey1':'insideval', 'insideKey2':'insideval2'}}
print(new_dict['key3']['insideKey2'])
print(new_dict['key2'][0].upper())
new_dict['key4'] = 12345
print(new_dict)
new_dict['k5'] = 'new_val_5'
print(new_dict)
print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())