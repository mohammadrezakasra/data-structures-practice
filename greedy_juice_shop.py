n, v = list(map(int, input().split()))
my_list = []
for i in range(n):
    my_list.append(list(map(int, input().split())))
    
for i in my_list:
    i.append(i[0]/i[1])


my_list.sort(key = lambda  x: x[2],reverse = True)
ans = 0

for i in my_list:
    if v - i[1] < 0:
        ans += v/i[1] * i[0]
        break
    else:
        v -= i[1]
        ans += i[0]


print(ans)