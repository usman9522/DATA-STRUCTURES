#iterative
def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        c = 1
        for i in range(a,0,-1):
            c *= i
        return c
print(factorial(5))

#recursive
def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial (a-1)
print(factorial(5))
