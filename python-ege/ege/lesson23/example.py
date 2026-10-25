from heapq import heappush, heappop
g={1:[(7,5.5),(6,2.0)],6:[(7,1.0)],7:[(100,4.2)],100:[]}
dist={1:0.0}
heap=[(0.0,1)]
while heap:
    d,v=heappop(heap)
    if d != dist[v]: continue
    for u,w in g.get(v,[]):
        nd=d+w
        if nd < dist.get(u,float("inf")):
            dist[u]=nd
            heappush(heap,(nd,u))
print(dist[100])
print(int(dist[100]))
