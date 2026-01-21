import math

n = int(input())
a = list(map(int,input().split(' ')))

answer = a[0]
my_sum = a[0]

for i in range(1,n):
    my_sum = max(my_sum+a[i],a[i]) #1007 ,
    answer = max(answer,my_sum) #1007 , 10007
print(answer)
