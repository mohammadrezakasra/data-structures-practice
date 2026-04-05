n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

answer = 0
time = 0
for i in a:
    if i > time:
        time += 1
        answer +=1
    else:
        continue

print(answer)