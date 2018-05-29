def string_length_greater_than_20(fin):
    for line in fin:
        if len(line) - line.count(' ') > 19:
            print(line)


def no_e(fin):
    total_count = 0
    no_e_count = 0
    for line in fin:
        total_count += 1
        if str.find(line, 'e') < 0:
            no_e_count += 1
    print(no_e_count / total_count * 100)


def avoid(fin, forbidden_letters):
    count = 0
    for line in fin:
        found = False
        for char in forbidden_letters:
            if str.find(line, char) >= 0:
                found = True
        if not found:
            count += 1
    print(count)


def uses_all(word, letters):
    for char in letters:
        if str.count(word, char) == 0:
            print('False')
            return
    print(word)


def is_abecedarian(word):
    for i in range(len(word)):
        if i == len(word) - 1:
            print(True)
            return
        elif word[i] > word[i + 1]:
            print(False)
            return


uses_all('asdf', 'aeiou')
is_abecedarian('abcde')

fin = open('../file/words.txt')
# string_length_greater_than_20(fin)
# no_e(fin)
# avoid(fin, 'zxyvw')
