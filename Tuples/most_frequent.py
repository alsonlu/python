import random


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


hist = make_histogram('aab')
i = 0
prob_dict = dict()
word_list = []
for key in hist.keys():
    if hist[key] not in word_list:
        word_list.extend(hist[key] * key)

while i < 100:
    choice = random.choice(word_list)
    prob_dict[choice] = prob_dict.setdefault(choice, 1) + 1
    i += 1

print(prob_dict)

print(sort_by_desc('assdddffff'))
