for x in range(12):
    value = 2 * 12**2 + x * 12 + 3
    if value % 7 == 0:
        print(x, value // 7)
