T = 34
def moves(a,b):
    return ((a+2,b),(a,b+2),(2*a,b),(a,2*b))
def win1(a,b):
    return a+b<T and any(x+y>=T for x,y in moves(a,b))
possible = []
for s in range(1,29):
    if any(x+y<T and win1(x,y) for x,y in moves(5,s)):
        possible.append(s)
print(min(possible))
