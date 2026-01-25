number = int(input())

def gray_code(n):
    if n == 0:
        return []

    g1 = gray_code(n - 1)
    g2 = list(reversed(gray_code(n - 1)))


    if not g1:
        g1.append([])
        g2.append([])


    # g1 = [ '0' + x for inner in g1 for x in inner]
    # g2 = [ '1' + x for inner in g2 for x in inner]

    g1 = [ ['0'] + x for x in g1]
    g2 = [ ['1'] + x for x in g2]


    G =g1 + g2
    return G

for i in gray_code(number):
    print(*i, sep='')
