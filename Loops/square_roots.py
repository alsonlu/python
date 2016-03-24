def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a/x) / 2
        if abs(x - y) < .0000001:
            return x, abs(x - y)
        x = y

result = mysqrt(3)
sqrt = result[0]
diff = result[1]
