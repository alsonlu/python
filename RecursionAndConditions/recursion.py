import turtle


def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)
        # print statement below goes in opposite order as it resolves from the lowest n to the highest (since highest is where it starts)
        print(n)


recurse(3, 0)


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)


draw(turtle.Turtle(), 4, 5)
