def reverse(x):
    if abs(x) > 2**31 -1:
        return 0
    if x >= 0:
        if int(str(x)[::-1]) > 2**31 -1:
            return 0
        return int(str(x)[::-1])
    if x < 0:
        y = abs(x)
        if int(str(y)[::-1]) > 2**31 -1:
            return 0
        return -int(str(y)[::-1])

print(reverse(100000))