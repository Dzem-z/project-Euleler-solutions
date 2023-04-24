import time
import math
start = time.time()
#---------------------------

limit = 12001
#1
def NWD(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

summ = 0


for i in range(2, limit): 
    for j in range(i // 3 + 1, i // 2 + i % 2):
        
        if NWD(i, j) == 1:
            summ += 1
            #if j % 3000 == 0:
            #    print(j,"/", i)
print(summ)
"""
sums = [ i for i in range(limit) ]
sums[ 1 ] = 0

for i in range(2, limit):
    if sums[ i ] == i:
        #j = 2 * i
        j = i
        while j < limit:
            sums[ j ] = sums[ j ] // i * ( i - 1 )
            j += i
"""
    



print(summ)

#---------------
print(time.time()-start," ------seconds------\n")
