a = [5, 6, -3, 8, 11, 12]
count = 0
best = None
for x,y in zip(a,a[1:]):
    if x % 3 == 0 or y % 3 == 0:
        count += 1
        s = x + y
        best = s if best is None else max(best,s)
print(count,best)
