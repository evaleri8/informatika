a = [1, 2, 3, 4, 5, 6]
slow = sum((a[i] + a[j]) % 3 == 0 for i in range(len(a)) for j in range(i + 1, len(a)))
freq = [0] * 3
fast = 0
for x in a:
    fast += freq[(-x) % 3]
    freq[x % 3] += 1
assert fast == slow
print(fast)
