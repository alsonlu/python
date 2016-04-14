def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


test_dict = {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
inverted_dict = invert_dict(test_dict)
print(inverted_dict)
