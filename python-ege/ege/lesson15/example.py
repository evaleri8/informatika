candidates = []
for A in range(1,31):
    if all((not (x % 6 == 0)) or x % A == 0 for x in range(10,31)):
        candidates.append(A)
print(max(candidates))
