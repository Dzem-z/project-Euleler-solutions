import time
start = time.time()
#---------------------------------------------------------

def factorial(n):
    ret = 1
    for i in range(1,n + 1):
        ret *= i
    return ret

def evaluate(n):
    summ = 0
    while n != 0:
        summ += factorials[n % 10]
        n //= 10
    return summ

factorials = [ factorial(i) for i in range(10) ]

size = 10 ** 6

lengths = [ 0 for i in range(3*10**6) ]
loops = [2, 145, 169, 871, 872, 40585]
loopsLength = [1, 1, 3, 2, 2, 1]

c = 0

#for i in range(10 ** 6):
#    evaluate(i)

for i in range(2, size):
    actualNum = i
    j = 0
    while actualNum not in loops and lengths[ actualNum ] == 0:
        actualNum = evaluate(actualNum)
        j += 1
    if lengths[ actualNum ] != 0:
        lengths[ i ] = j + lengths[ actualNum ]
    else:
        lengths[ i ] = j + loopsLength[ loops.index(actualNum) ]
    #if i % 1000 == 0:
    #    print(i, j)
    #if i % 1000 == 0:
    #    print( lengths[ i ] )
    if lengths[ i ] == 60 :
        c += 1

print(c)

#---------------------------------------------------------
print(time.time()-start," ------seconds------\n")
