s = "ABBACABBA"
cur = best = 0
prev = None
for ch in s:
    cur = 1 if ch == prev else cur + 1
    best = max(best, cur)
    prev = ch
print(best)
