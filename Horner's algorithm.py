MOD = 10**9 + 7
n, x = map(int, input().split())
a = list(map(int, input().split()))

answer = a[0] % MOD
for i in range(1, n + 1):
    answer = (answer * x + a[i]) % MOD

print(answer)