def print_lyrics():
    # Single quotes
    print('I can show you the world')
    # Double quotes
    print("Shining, shimmering splendid")
    print_more_lyrics()
print("Aladdin and Jasmine")
# Empty line to signify end of function not needed, can just be an untabbed line


def print_more_lyrics():
    print("Tell me Princess")
    print("Now when did you last let your heart decide")

print_lyrics()

print("Starting new function...")


def print_twice(string):
    print(string)
    print(string)

print_twice("Sup" * 4)
