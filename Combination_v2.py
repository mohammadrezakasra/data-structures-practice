import time
mod = 10 ** 9 + 7

q = int(input())



def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} time: {end - start:.6f} sec")
        return result
    return wrapper



func_list = [1,1]
def func(n):
    size = len(func_list)
    while n >= size:
        func_list.append(size * func_list[-1])
        size +=1
    return func_list[n]


@timer
def combination(n, r):
    if r > n:
        return 0
    elif r == 0 or n == r:
        return 1
    return (func(n)//(func(r)*func(n-r))) % mod

ans = []
for i in range(q):
    n , r = map(int, input().split())
    ans.append(combination(n,r))

for i in range(q):
    print(ans[i])