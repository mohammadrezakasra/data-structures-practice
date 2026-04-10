n = int(input())
list_of_numbers = list(map(int, input().split()))

max_of_sequence_of_numbers = 0
sum_of_sequence = 0
max_of_list = max(list_of_numbers)
if max_of_list <= 0:
    print(max_of_list)
else:
    for i in range(n):

        sum_of_sequence = max(0, sum_of_sequence + list_of_numbers[i])

        max_of_sequence_of_numbers = max(max_of_sequence_of_numbers, sum_of_sequence)



    ans = max(max_of_list, max_of_sequence_of_numbers)
    print(ans)