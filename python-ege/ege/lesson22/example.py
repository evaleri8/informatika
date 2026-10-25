from functools import lru_cache
duration={1:3,2:4,3:2,4:5}
deps={1:[],2:[1],3:[2,4],4:[]}
@lru_cache(maxsize=None)
def finish(v):
    return duration[v]+max((finish(u) for u in deps[v]),default=0)
intervals={v:(finish(v)-duration[v],finish(v)) for v in duration}
t=4
print(sorted(intervals.items()))
print(sum(start <= t-1 < end for start,end in intervals.values()))
