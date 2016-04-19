import string

file_input = open('../file/PrideAndPrejudice.txt')
to_start = False
word_dict = {}
for line in file_input:
    if line == 'Produced by Anonymous Volunteers\n':
        to_start = True
    if to_start:
        for word in line.split():
            key = word.strip(string.whitespace + string.punctuation).lower()
            if not key == '':
                word_dict[key] = word_dict.setdefault(key, 1) + 1

word_tuples = []
for key in word_dict:
    word_tuples.append((word_dict[key], key))

word_tuples.sort(reverse=True)
print(word_tuples[:20])

print(word_dict)
print(len(word_dict))
