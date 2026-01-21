n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    p = i
    item = a[i]
    while p > 0 and item < a[p-1]:
        a[p] = a[p-1]
        p = p-1
    a[p] = item

print(*a)
