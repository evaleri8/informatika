import re
s="--067*8-90**7-6*0-9--"
number=r"(?:0|[6789][06789]*)"
pattern=number+r"(?:[-*]"+number+r")*"
best=max((len(m.group()) for m in re.finditer(pattern,s)),default=0)
print(best)
