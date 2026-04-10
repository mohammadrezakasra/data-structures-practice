n = int(input())

a = []
def bricklay(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    elif x == 3:
        return 2
    elif x == 4:
        return 3
    else:
        return  (bricklay(x-1)+bricklay(x-2)+bricklay(x-3)-bricklay(x-4)) % (10 ** 9 + 7)

for i in range(n):
    print(bricklay(int(input())))