import math


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


def right_justify(string):
    length_of_string = len(string)
    print(length_of_string)
    num_spaces_to_add = 70 - length_of_string
    spaces = " " * num_spaces_to_add
    print(spaces + string)

right_justify("monty")


def draw_grid(cell_width, cell_height, num_of_cells):
    cells_per_row = math.sqrt(num_of_cells)
    cell_dashes = '-' * cell_width
    print_row(cell_dashes, cell_width)
    print_row(cell_dashes, cell_width)
    print_row(cell_dashes, cell_width)
    print_row(cell_dashes, cell_width)
    print_entire_line(cell_dashes)


def print_row(cell_dashes, cell_width):
    print_entire_line(cell_dashes)
    print_line_with_spaces(cell_width)
    print_line_with_spaces(cell_width)
    print_line_with_spaces(cell_width)
    print_line_with_spaces(cell_width)


def print_horizontal_grid_lines(cell_dashes):
    print(cell_dashes, end=' ')


def print_entire_line(cell_dashes):
    print_plus_sign()
    print_horizontal_grid_lines(cell_dashes)
    print_plus_sign()
    print_horizontal_grid_lines(cell_dashes)
    print_plus_sign()
    print_horizontal_grid_lines(cell_dashes)
    print_plus_sign()
    print_horizontal_grid_lines(cell_dashes)
    print_plus_sign()
    print()


def print_line_with_spaces(cell_width):
    print_vertical_line()
    print_spaces(cell_width)
    print_vertical_line()
    print_spaces(cell_width)
    print_vertical_line()
    print_spaces(cell_width)
    print_vertical_line()
    print_spaces(cell_width)
    print_vertical_line()
    print()


def print_spaces(cell_width):
    line = ' ' * cell_width
    print(line, end=' ')


def print_vertical_line():
    print('|', end=' ')


def print_plus_sign():
    print('+', end=' ')

draw_grid(4, 4, 16)
