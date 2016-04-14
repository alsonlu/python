fin = open('../file/words.txt')

tuple_dict = dict()
for line in fin:
    char_list = list(line.strip('\n'))
    char_list.sort()
    tuple_list = tuple(char_list)
    tuple_dict.setdefault(tuple_list, []).append(line.strip('\n'))

keys_to_remove = []
for key in tuple_dict:
    if len(tuple_dict[key]) == 1:
        keys_to_remove.append(key)

for key_to_remove in keys_to_remove:
    tuple_dict.pop(key_to_remove)

print(tuple_dict)

