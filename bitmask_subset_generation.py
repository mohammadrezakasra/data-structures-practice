import math

n = int(input())
my_set = list(map(int, input().split()))

answer = math.inf

all_subsets = []
for mask in range(2**n): # تمام زیر مجموع های ممکن
    sub = []
    for i in range(n):
        if mask & (1 << i):
            sub.append(my_set[i])
    all_subsets.append(sub)


for  i in range(len(all_subsets)//2):
    temp = abs(sum(all_subsets[i]) - sum(all_subsets[len(all_subsets) - i - 1]))
    if answer > temp:
        answer = temp

print(answer)
