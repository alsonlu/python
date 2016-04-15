fin = open('../file/words.txt')

tuple_dict = dict()
for line in fin:
    char_list = list(line.strip('\n'))
    char_list.sort()
    tuple_list = tuple(char_list)
    tuple_dict.setdefault(tuple_list, []).append(line.strip('\n'))

tuple_list = []
for value in tuple_dict.values():
    if len(value) == 1:
        tuple_list.append((len(value), value))

possible_bingos = []
for key in tuple_dict:
    if len(key) == 8:
        possible_bingos.append((len(tuple_dict[key]), tuple_dict[key]))

tuple_list.sort(reverse=True)
possible_bingos.sort(reverse=True)
print(possible_bingos)
print(tuple_list)
