n = int(input())
range_list = []
for i in range(n):
    range_list.append(list(map(int, input().split())))

range_list.sort(key=lambda x: x[1])
answer = 1

temp = 1
end = range_list[0]
for j in range( 1 ,n):
    if end[1] <= range_list[j][0]:
        end = range_list[j]
        temp +=1

    answer = max(answer,temp)

print(answer)

