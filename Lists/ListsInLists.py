numbers = [1, [2, 3, 4], 5, 6]
for number in numbers:
    if isinstance(number, list):
        for sec_num in number:
            print(sec_num)
    else:
        print(number)

t = [3, 1, 2]
t2 = t[:]
t.sort()
print(t)
print(t2)
