a = [[2, 1, 4], [3, 8, 1], [1, 2, 5]]
n, m = len(a), len(a[0])
dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        prev = []
        if i > 0: prev.append(dp[i - 1][j])
        if j > 0: prev.append(dp[i][j - 1])
        dp[i][j] = a[i][j] + (max(prev) if prev else 0)
print(dp[-1][-1])
