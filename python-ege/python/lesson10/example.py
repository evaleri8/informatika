a = [4, 2, 4, 7, 2, 2, 9]
freq = {}
for x in a:
    freq[x] = freq.get(x, 0) + 1
print(sorted(freq.items()))
print([x for x in sorted(freq) if freq[x] == 2])
