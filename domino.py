n = int(input())

ans_list = [1,2]

for i in range(2,n):
    ans_list.append((ans_list[i-1]+ans_list[i-2])%(10 ** 9 + 7))

print(ans_list[-1])
