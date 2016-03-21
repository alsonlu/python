count = 'banana'.count('a')
print(count)

fruit = 'banana'
sliced_fruit = fruit[0:5:2]
print(sliced_fruit)

reversed_fruit = fruit[::-1]
print(reversed_fruit)


def is_palindrome(word):
    if word == word[::-1]:
        print('Yes')
    else:
        print('No')

is_palindrome('racecar')
is_palindrome('doggie')


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

print(any_lowercase4('SSSa'))


def rotate_word(word, rotate_amount):
    word = word.lower()
    new_word = ''
    for char in word:
        new_word += chr(ord(char) + rotate_amount)
    print(new_word)

rotate_word('cheer', 7)
rotate_word('hal', 1)
rotate_word('melon', -10)
