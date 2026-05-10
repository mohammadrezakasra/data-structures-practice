from pprint import pprint

n , m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]


dp[n-1][0] = a[n-1][0]

for i in range(1, m):
    dp[n-1][i] = dp[n-1][i-1] +a[n-1][i]

for i in range(n-2,-1,-1):
    dp[i][0] = dp[i+1][0] + a[i][0]


for i in range(1,n):
    for j in range(1,m):
        if dp[n-i][j] + a[n-i-1][j] > dp[n-i-1][j-1] + a[n-i-1][j]:
            dp[n-i-1][j] = dp[n-i][j] + a[n-i-1][j]

        else:
            dp[n-i-1][j] = dp[n-i-1][j-1] + a[n-i-1][j]



j = m-1
i = 0
parent = ""

while i < n - 1 or j > 0:
    if i == n - 1:
        parent = "R" + parent
        j -= 1
    elif j == 0:
        parent = "U" + parent
        i += 1
    else:
        if dp[i+1][j] > dp[i][j-1]:
            parent = "U" + parent
            i += 1
        else:
            parent = "R" + parent
            j -= 1

print(dp[0][m-1])
print(parent)
