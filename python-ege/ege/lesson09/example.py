rows = [[1,2,3,4,9], [2,2,3,4,10], [3,4,5,6,7]]
count = 0
for row in rows:
    a = sorted(row)
    if len(set(a)) == 5 and 2 * (a[0] + a[-1]) > sum(a[1:-1]):
        count += 1
print(count)
