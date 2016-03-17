def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    # if word is length 2 or 1, returns empty string
    return word[1:-1]


def is_palindrome(word):
    if not isinstance(word, str):
        print('is_palindrome is only for strings')
        return None
    if len(word) == 1 or len(word) == 0:
        return True
    elif len(word) == 2 and first(word) == last(word):
        return True
    elif first(word) == last(word):
        return is_palindrome(middle(word))
    else:
        return False

if is_palindrome('noon'):
    print('noon is a palindrome')

if is_palindrome('redivider'):
    print('redivider is a palindrome')

if not is_palindrome('asdf'):
    print('asdf is NOT a palindrome')

is_palindrome(1)
