count = 0
total = 0
for n in range(1, 21):
    if n % 3 == 0:
        count += 1
        total += n
print(count, total)
