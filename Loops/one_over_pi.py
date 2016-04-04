import math


def estimate_pi():
    totalsum = 0
    k = 0
    while True:
        num = math.factorial(4 * k) * (1103 + 26390 * k)
        denom = math.pow(math.factorial(k), 4) * math.pow(396, 4 * k)
        last_term = num / denom
        totalsum += last_term
        if last_term < 1e-15:
            break
        k += 1
    return ((2 * math.sqrt(2)) / 9801) * totalsum

print('estimate_pi result: ' + str(estimate_pi()))
print('one over pi: ' + str(1 / math.pi))
