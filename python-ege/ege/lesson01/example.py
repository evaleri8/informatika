from itertools import permutations
names = "ABCD"
edges = {frozenset(e) for e in ("AB", "AC", "AD", "BC", "BD")}
table = {frozenset(e) for e in ((1,2),(1,3),(1,4),(2,3),(3,4))}
solutions = []
for p in permutations(range(1,5)):
    mapping = dict(zip(names,p))
    mapped = {frozenset(mapping[v] for v in e) for e in edges}
    if mapped == table:
        solutions.append(mapping)
print(len(solutions))
for m in solutions: print(m)
