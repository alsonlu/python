def has_duplicates(word_list):
    duplicate_dict = dict()
    for word in word_list:
        if word in duplicate_dict:
            return True
        else:
            duplicate_dict[word] = 1
    return False


print(has_duplicates([1, 2, 3, 4, 5]))
print(has_duplicates([1, 1, 1, 1]))
