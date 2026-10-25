events=[("08:00:00",1,4),("09:00:00",2,6),("10:00:00",1,7),("11:00:00",2,5),("13:00:00",3,8)]
capacity=10
used=0
totals={}
backups=[]
for time,client,size in events:
    totals[client]=totals.get(client,0)+size
    if used+size>capacity:
        if time<="11:59:59": backups.append(used)
        used=0
    used+=size
best_client=min(totals,key=lambda c:(-totals[c],c))
print(best_client,sum(sorted(backups,reverse=True)[:2]))
