a = [[2,1,4],[3,8,1],[1,2,5]]
n,m = len(a),len(a[0])
blocked = {((1,1),(1,2)), ((1,1),(2,1))}
lo = {(0,0):a[0][0]}
hi = dict(lo)
ends = []
for i in range(n):
    for j in range(m):
        v = (i,j)
        if v not in lo: continue
        nxt = [u for u in ((i+1,j),(i,j+1)) if u[0]<n and u[1]<m and (v,u) not in blocked]
        if not nxt: ends.append(v)
        for u in nxt:
            value = a[u[0]][u[1]]
            lo[u] = min(lo.get(u,float("inf")),lo[v]+value)
            hi[u] = max(hi.get(u,float("-inf")),hi[v]+value)
print(max(hi[v] for v in ends), min(lo[v] for v in ends))
