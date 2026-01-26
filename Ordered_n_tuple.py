n = int(input())

lst = [0] * n
for i in range(n):
     lst[i] = [i+1]
def n_tuple(n):
     temp = []
     if n == 1:
          return lst

     for xxx in n_tuple(n-1):
          for y in lst:
              temp.append([*xxx, *y])

     return temp

for i in  n_tuple(n):
     print(*i)





# lst_1 = [1,2,3]
# lst_2 = [1,2,3]
# lst_3 = []
# for x in lst_1:
#     for y in lst_2:
#         lst_3.append([x,y])
#
# print(lst_3)
# temp = []
# # [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
# for x in lst_3:
#     for y in lst_1:
#         temp.append([*x,y])
#
# print(temp)