#
mod = 10 ** 9 + 7
q = int(input())

func_list = [1,1]
def func(n):
    size = len(func_list)
    while n >= size:
        func_list.append((size * func_list[-1])% mod)
        size +=1
    return func_list[n]



def combination(n_func, r_func):
    if r_func > n_func:
        return 0
    elif r_func == 0 or n_func == r_func:
        return 1
    x = (func(r_func) * func(n_func - r_func)) % mod
    return (func(n_func) * pow(x, mod - 2, mod)) % mod



ans = []
for _ in range(q):
    n , r = map(int, input().split())
    ans.append(combination(n,r))

for i in ans:
    print(i)