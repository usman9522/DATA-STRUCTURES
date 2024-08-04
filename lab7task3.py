import random
def getrandomnumber(start, end):
    return random.randint(start, end)
def hashf(a,s):
    return a%s

def exp(s):
    lis = []
    for i in range(50):
        table = [None]*s
        count = 0
        while True:
            n = getrandomnumber(1, 100)
            i = hashf(n, s)
            if table[i] is None:
                table[i] = n
                count += 1
            else:
                break

        lis.append(count)
    return lis
for i in range(10,101,10):
    a = exp(i)
    summ = sum(a)
    avg = summ/50
    print('Size',i,'has average : ',avg)

