n , k = map(int, input().split())

first_shaip = []

for i in range(n):
    first_shaip.append((input()))

star_shape = []
for i in range(n):
    star_shape.append("*" * n)

print(star_shape)
def func(shape):
    if shape[0] == '.':
        return first_shaip
    elif shape[0] == '*':
        return star_shape
    else :
        return shape[0]

print(first_shaip)
print(func(first_shaip))