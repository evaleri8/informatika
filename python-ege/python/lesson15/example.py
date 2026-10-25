from math import isqrt
n = 36
divisors = set()
for d in range(1, isqrt(n) + 1):
    if n % d == 0:
        divisors.add(d)
        divisors.add(n // d)
print(sorted(divisors))
