number = int(input())

def gray_code(n):
    if n == 1:
        return "01"
    else:
        strings = ''
        for i in "01":
            strings += (2 ** n) * i
        gray_code(n-1) + gray_code(n-1)
        return strings

gray_code(number)

