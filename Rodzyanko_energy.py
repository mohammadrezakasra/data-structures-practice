n , k = map(int, input().split())
list_fruit = []
for _ in range(n):
    list_fruit.append(list(map(int, input().split())))


# for _ in range(n):
#     for i in list_fruit:
#         if i[0] > i[1]:
#             list_fruit.remove(i)
#         if i[0] < i[1]:
#             if i[0] <= k:
#                 k += i[1] - i[0]
#                 list_fruit.remove(i)

sorted_list_fruit = sorted(list_fruit)
for i in sorted_list_fruit:
    if i[0] <i [1] and i[0] <=k:
        k += i[1] - i[0]

print(k)
