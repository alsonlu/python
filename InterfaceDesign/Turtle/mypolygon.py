import turtle

bob = turtle.Turtle()

# .mainloop tell the window to wait for the user to do something
# turtle.mainloop()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

# square(bob, 300)


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)

# polygon(bob, 100, 8)

""" This is a multiline....
comment
"""


def circle(t, r):
    for i in range(100):
        t.fd(5)
        t.lt(360 / 100)

