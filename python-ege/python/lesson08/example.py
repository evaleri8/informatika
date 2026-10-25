s = "ABABBAAB"
count = 0
for i in range(len(s) - 1):
    if s[i:i + 2] == "AB":
        count += 1
print(count)
print(s[::-1])
