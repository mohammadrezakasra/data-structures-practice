n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    p = i # شمارند  حلقه While
    item = a[i] # مقداری را ذخیره کردیم گم نشه
    while p > 0 and item < a[p-1]:
        a[p] = a[p-1]
        p = p-1
        print(a)
    a[p] = item
    print()

print(*a)
