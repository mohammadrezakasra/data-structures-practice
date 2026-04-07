n , k = map(int, input().split())
c_i = list(map(int, input().split()))

if k == 1:
    print(max(c_i))
elif k == 2:
    print(min(c_i[0], c_i[-1]))
else:
    print(min(c_i))