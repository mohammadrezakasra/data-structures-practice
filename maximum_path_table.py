import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

# dp و parent
dp = [[0]*m for _ in range(n)]
parent = [['']*m for _ in range(n)]

dp[n-1][0] = a[n-1][0]


for j in range(1, m):
    dp[n-1][j] = dp[n-1][j-1] + a[n-1][j]
    parent[n-1][j] = 'R'

for i in range(n-2, -1, -1):
    dp[i][0] = dp[i+1][0] + a[i][0]
    parent[i][0] = 'U'

for i in range(n-2, -1, -1):
    row_dp = dp[i]
    row_dp_down = dp[i+1]
    row_parent = parent[i]
    
    for j in range(1, m):
        if row_dp_down[j] > row_dp[j-1]:
            row_dp[j] = a[i][j] + row_dp_down[j]
            row_parent[j] = 'U'
        else:
            row_dp[j] = a[i][j] + row_dp[j-1]
            row_parent[j] = 'R'

print(dp[0][m-1])

i, j = 0, m-1
path = []

while not (i == n-1 and j == 0):
    c = parent[i][j]
    path.append(c)
    if c == 'U':
        i += 1
    else:
        j -= 1

path.reverse()
print("".join(path))
