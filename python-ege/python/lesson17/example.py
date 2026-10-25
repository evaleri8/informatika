dp = [0] * 11
dp[1] = 1
for x in range(1, 11):
    for y in (x + 1, x * 2):
        if y <= 10:
            dp[y] += dp[x]
print(dp[10])
