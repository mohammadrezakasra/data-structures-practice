INF = -10**15

n, S = map(int, input().split())
pac = [list(map(int, input().split())) for _ in range(n)]

# data[i] = (size, min_price, sum_price)
data = [(0, 0, 0)]
for p in pac:
    size = p[0]
    prices = p[1:]
    data.append((size, min(prices), sum(prices)))

# dp[i][s] = max toys using first i packages with budget s
dp = [[INF] * (S + 1) for _ in range(n + 1)]
dp[0][0] = 0

# par_info
par_choice = [[0] * (S + 1) for _ in range(n + 1)]
par_prev_s = [[0] * (S + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    size_i, min_i, sum_i = data[i]
    for s in range(S + 1):

        # case 0: buy nothing
        best = dp[i - 1][s]
        choice = 0
        prev_s = s

        # case 1: buy one
        if s >= min_i and dp[i - 1][s - min_i] != INF:
            val = dp[i - 1][s - min_i] + 1
            if val > best:
                best = val
                choice = 1
                prev_s = s - min_i

        # case 2: buy full package
        if s >= sum_i and dp[i - 1][s - sum_i] != INF:
            val = dp[i - 1][s - sum_i] + size_i
            if val > best:
                best = val
                choice = 2
                prev_s = s - sum_i

        dp[i][s] = best
        par_choice[i][s] = choice
        par_prev_s[i][s] = prev_s

# find best
best_s = max(range(S + 1), key=lambda s: dp[n][s])
best_ans = dp[n][best_s]

# backtrack
res = [0] * (n + 1)
i, s = n, best_s
while i > 0:
    c = par_choice[i][s]
    res[i] = c
    s = par_prev_s[i][s]
    i -= 1

print(best_ans)
print("".join(map(str, res[1:])))
