T = 15
def moves(s):
    return (s + 1, s * 2)
def w1(s):
    return s < T and any(t >= T for t in moves(s))
def l1(s):
    return s < T and not w1(s) and all(w1(t) for t in moves(s))
print([s for s in range(1, T) if w1(s)])
print([s for s in range(1, T) if l1(s)])
