fin = open('../file/words.txt')
word_dict = dict()
for line in fin:
    word_dict[line.rstrip('\n')] = 1

print('abrasives' in word_dict)
print('asdf' in word_dict)
