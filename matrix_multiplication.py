n = int(input())
a = list(map(int, input().split()))

INF = float('inf')
dp = [[INF] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

for i in range(n):
    for j in range(1, n - i):
        l = i
        r = i + j
        for k in range(l, r):
            dp[l][r] = min(
                dp[l][r],
                dp[l][k] + dp[k+1][r] + a[l] * a[k+1] * a[r+1]
            )

print(dp[0][n-1])
