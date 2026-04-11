n = int(input())

mod = 10 ** 9 + 7

a = [1,1,2,3]

def bricklaying(x):
    while len(a) < x:
        i = len(a)
        a.append((a[i-1]+a[i-2]+a[i-3]-a[i-4]) % mod)
    return a[x-1]

for _ in range(n):
    inp = int(input())
    print(bricklaying(inp))