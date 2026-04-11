n = int(input())
a = [1, 1, 2, 3]
def bricklay(x):
    if x== 1:
        return a[0]
    elif x == 2:
        return a[1]
    elif x == 3:
        return a[2]
    elif x == 4:
        return a[3]
    else:
        for i in range(4,x):
            a.append((a[i-1]+a[i-2]+a[i-3]-a[i-4])%(10 **9 + 7))
    return a[x-1]


ans = []

for i in range(n):
    inp = int(input())
    if len(a) < inp:
        ans.append(bricklay(inp))
    else:
        ans.append(bricklay(inp))

for i in range(n):
    print(ans[i])