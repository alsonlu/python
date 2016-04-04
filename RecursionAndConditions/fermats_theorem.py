import math


def check_fermat(a, b, c, n):
    left_side_evaluation = math.pow(variable_a, variable_n) + math.pow(variable_b, variable_n)
    right_side_evaluation = math.pow(variable_c, variable_n)

    if variable_n > 2 and left_side_evaluation == right_side_evaluation:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")

# a^n + b^n = c^n
variable_a = int(input("What would you like to make 'a'?"))
variable_b = int(input("What would you like to make 'b'?"))
variable_c = int(input("What would you like to make 'c'?"))
variable_n = int(input("What would you like to make 'n'?"))
check_fermat(variable_a, variable_b, variable_c, variable_n)
