def transform(n):
    s = bin(n)[2:]
    for _ in range(2):
        s += str(s.count("1") % 2)
    return int(s,2)
n = 1
while transform(n) <= 100:
    n += 1
print(n, transform(n))
