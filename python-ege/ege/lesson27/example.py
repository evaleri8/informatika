from decimal import Decimal, localcontext
R=Decimal("1")
K=2
rows=[]
with open("data.txt",encoding="utf-8") as f:
    for line in f:
        parts=line.replace(",",".").split()
        x,y,vx,vy,m=map(Decimal,parts[:5])
        energy=m*(vx*vx+vy*vy)/2
        rows.append((energy,x,y,parts[5]))
rows.sort()
groups=[]
for row in rows:
    if not groups or row[0]-groups[-1][0][0]>R:
        groups.append([])
    groups[-1].append(row)
assert len(groups)==K
max_energy=max(g[len(g)//2][0] for g in groups)
max_d2=Decimal(0)
for g in groups:
    points=[(r[1],r[2]) for r in g if r[3]=="II"]
    for i,(x,y) in enumerate(points):
        for u,v in points[i+1:]:
            max_d2=max(max_d2,(x-u)**2+(y-v)**2)
with localcontext() as ctx:
    ctx.prec=40
    print(int(max_d2.sqrt()*10000),int(max_energy*10000))
