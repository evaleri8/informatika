a = [2, 1, 4, 2, 0, 3]
limit = 7
left = total = best = 0
for right, x in enumerate(a):
    total += x
    while total > limit:
        total -= a[left]
        left += 1
    best = max(best, right - left + 1)
print(best)
