from itertools import product
for x,y,z in product((0,1), repeat=3):
    f = ((not x) or y) and (y == z)
    if f:
        print(x,y,z)
