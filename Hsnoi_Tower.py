#A variable for count the step of transmission of rings
step = 1
def hanoi(n, a, b, c):
    global step
    if n == 1:
        print(step, a, b)
        step += 1
    else:

        hanoi(n - 1, a, c, b) #Move n - 1 rings from A to B
        print(step, a, b)#Move the remain ring from A to C
        step += 1
        hanoi(n - 1, c, b, a)        #Move n - 1 rings from B to C

n = int(input())
hanoi(n, 'A', 'B', 'C')

