n , c = map(int,input().split())
x = list(map(int,input().split()))

x_sort = reversed(sorted(x))

for i in x_sort:
    c = c - (min(c,max(0,i-c)))

print(c)