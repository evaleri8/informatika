start, target = 20, 42
dp = [0] * (target + 1)
dp[start] = 1
for x in range(start,target + 1):
    nxt = [x + 1]
    tens, units = x // 10 % 10, x % 10
    if tens < units:
        nxt.append(x // 100 * 100 + units * 10 + tens)
    for y in nxt:
        if y <= target:
            dp[y] += dp[x]
print(dp[target])
