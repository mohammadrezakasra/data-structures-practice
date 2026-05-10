n = int(input())
a =list(map(int, input().split()))
c = [0] * n
for i in range(1,n):
    q =0
    for j in range(1,i):
        q = max(q,a[j]+c[i-j])
        c[i] = q

print(c)