count = 0
total = 0
with open("data.txt", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            total += int(line)
            count += 1
print(count, total)
