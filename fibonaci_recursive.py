def fibonaci(a):
    a = 0
    b = 1
    for i in range(a):
        c = a + b
        a = b
        b = c
    return c
print(fibonaci(6))
