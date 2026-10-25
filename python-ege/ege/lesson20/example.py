T = 34
def moves(p):
    a,b=p
    return ((a+2,b),(a,b+2),(2*a,b),(a,2*b))
def w1(p):
    return sum(p)<T and any(sum(q)>=T for q in moves(p))
def l1(p):
    return sum(p)<T and not w1(p) and all(w1(q) for q in moves(p))
def w2(p):
    return sum(p)<T and not w1(p) and any(l1(q) for q in moves(p))
print([s for s in range(1,29) if w2((5,s))])
