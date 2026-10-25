from collections import deque
g = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
dist = {"A": 0}
q = deque(["A"])
while q:
    v = q.popleft()
    for u in g[v]:
        if u not in dist:
            dist[u] = dist[v] + 1
            q.append(u)
print(sorted(dist.items()))
