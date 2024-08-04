def basketball(a):
    lis = []
    for i in range(len(a)):
        if a[i] == 'D':
            lis.append(lis[-1]*2)
        elif a[i] == '+':
            lis.append(lis[-1]+lis[-2])
        elif a[i] == 'C':
            lis.pop()
        else:
            lis.append(int(a[i]))
    return sum(lis)
print(basketball(["5","2","C","D","+"]))


