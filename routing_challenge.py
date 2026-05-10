n , m = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

dp[0][0] = a[0][0]

for i in range(1,m):
    dp[0][i] = dp[0][i-1] + a[0][i]

for i in range(1,n):

    for j in range(0,m):
        dp[i][j] = dp[i-1][j] + a[i][j]

    for j in range(1,m):
        dp[i][j] = min(dp[i][j], dp[i][j-1] + a[i][j])

    for j in range(m-2,-1,-1):
        dp[i][j] = min(dp[i][j], dp[i][j+1] + a[i][j])


print(dp[n-1][m-1])