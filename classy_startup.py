chocolate=  list(map(int, input().split()))

ans = [0] * 4
i = 0
while True:
    chocolate[0] -= 1
    ans[i] += 1
    if chocolate[0] == 0:
        break
    i= (i + 1) % 4
    chocolate[2] -= 1
    ans[i] += 1
    if chocolate[2] == 0:
        break
    i= (i + 1) % 4

print(*ans)