from Ordered_n_tuple import my_filter

n = int(input())

my_filter = [0] * n
my_list = [[1]*n] * (n**n)

for i in range(n*n):
    my_list[i][0] = my_list[i][0] + my_filter[0]
    if my_filter[0] < 2:
        my_filter[0]+=1

print(my_list)
print(filter)