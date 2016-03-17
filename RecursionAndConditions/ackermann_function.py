def ackermann_function(m, n):
    if m == 0:
        n += 1
        return n
    elif m > 0 and n == 0:
        return ackermann_function(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann_function(m - 1, ackermann_function(m, n - 1))


result = ackermann_function(3, 4)
print("Expected Answer: 125 vs. Actual Answer: " + str(result))
