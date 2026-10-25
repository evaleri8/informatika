capacity = 10
requests = [4, 6, 3, 8, 2]
used = 0
backups = []
for size in requests:
    if used + size > capacity:
        backups.append(used)
        used = 0
    used += size
print(backups)
print(used)
