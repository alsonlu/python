import math


def eval_loop():
    while True:
        line = input('> ')
        if line == 'done':
            print(line)
            break
        print(eval(line))

eval_loop()
