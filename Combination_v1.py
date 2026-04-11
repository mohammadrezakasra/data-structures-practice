mod = 10 ** 9 + 7

q = int(input())


def func(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * func(n - 1)


def combination(n, r):
    if r > n:
        return 0
    elif r == 0 or n == r:
        return 1
    return (func(n)/(func(r)*func(n-r))) % mod

ans = []
for i in range(q):
    n , r = map(int, input().split())
    ans.append(combination(n,r))

for i in range(q):
    print(int(ans[i]))