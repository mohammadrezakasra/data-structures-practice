import sys
sys.setrecursionlimit(10**8)

number = int(input())
dic = dict()
def func(x):
    if x in dic:
        return dic[x]

    if x == 0:
        result  = 5
    elif x % 2 == 0:
        result  = (func(x-1) -21)
    else:
        temp = func(x-1)
        result = temp * temp

    dic[x] = result
    return result


print(func(number))

