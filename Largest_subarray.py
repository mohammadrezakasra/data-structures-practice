n = int(input())
a = list(map(int,input().split(' ')))

answer = a[0] #  تو این بزرگترین زیر بازه را داریم
my_sum = a[0] # تو این بزرگترین دنباله که داریم

for i in range(1,n):
    my_sum = max(my_sum + a[i],a[i])
    answer = max(answer,my_sum)

print(answer)