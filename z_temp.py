n = int(input())
def func(n):
    if n == 1 or n ==0:
        return 1
    else:
        return func(n-1) * n

print(func(n))