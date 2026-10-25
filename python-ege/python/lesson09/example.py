a = [5, 7, 2, 4, 9]
count = 0
best = None
for i in range(len(a) - 1):
    s = a[i] + a[i + 1]
    if s % 2 == 0:
        count += 1
        if best is None or s > best:
            best = s
print(count, best)
