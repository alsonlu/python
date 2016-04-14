def make_histogram(input_string):
    hist = dict()
    for character in input_string:
        hist[character] = hist.get(character, 0) + 1
    return hist


def sort_by_desc(input_string):
    hist = make_histogram(input_string)
    tuple_list = []
    for key in hist:
        tuple_list.append((hist[key], key))
    tuple_list.sort(reverse=True)
    print(tuple_list)


print(sort_by_desc('assdddffff'))
