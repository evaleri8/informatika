count = 0
for x in range(0,9):
    for y in range(0,8):
        in_a = 0 <= x <= 6 and 0 <= y <= 4
        in_b = 3 <= x <= 8 and 2 <= y <= 7
        if in_a and in_b:
            count += 1
print(count)
