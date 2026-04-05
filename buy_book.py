n , r = map(int, input().split())
a = list(map(int, input().split(' ')))
a = sorted(a)

my_sum = 0
answer = 0
for i in range(n):
    my_sum += a[i]
    if my_sum <= r:
        answer += 1

print(answer)