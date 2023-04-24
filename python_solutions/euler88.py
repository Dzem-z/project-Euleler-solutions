import time
start = time.time()
from functools import reduce  # Required in Python 3
import operator

#--------------------------------
bound = 12001
def prod(iterable):
    return reduce(operator.mul, iterable, 1)

"""#brute force
ks = [float("inf") for i in range(bound) ]

for i in range(2, len(ks)):
    numbers = [ 1 ] * i
    numbers[ 0 ] = 2
    numbers[ 1 ] = 2
    j = 0
    while True:
        while prod(numbers) < sum(numbers):
            #print(numbers)
            numbers[ 0 ] += 1
        if prod(numbers) == sum(numbers):
            ks[ i ] = min( ks[ i ], sum(numbers) )
            if i % 10 == 0:
                print(numbers)
        while j < len(numbers) and numbers[ j ] == numbers[ 0 ]:
            j += 1
        if j >= len(numbers) or (numbers[ j ] + 1) * j > ks[ i ]:
            break
        #print(numbers)
        numbers[ j ] += 1
        b = numbers[ j ]
        while j >= 0:
            numbers[ j ] = b
            j -= 1
        j = 0
        #print(numbers)
        
            
print(ks) 
"""
#2(brute force modification)

ks = [ float("inf") for i in range(bound) ]
numbers = [2, 2]
l = 0
while len(numbers) <= 14:
        j = 0
        i = len(numbers) + prod(numbers) - sum(numbers)
        while i < bound:
            #print(numbers)
            i = len(numbers) + prod(numbers) - sum(numbers)
            if prod(numbers) >= sum(numbers):
                if i < bound:
                    ks[ i ] = min( ks[ i ], prod(numbers) )
            numbers[ 0 ] += 1
        #if l % 100 == 0:
        #    print(numbers)
        while j < len(numbers) and numbers[ j ] == numbers[ 0 ]:
            j += 1
        if j >= len(numbers):
            numbers += [ 1 ]
        #print(numbers)
        numbers[ j ] += 1
        b = numbers[ j ]
        while j >= 0:
            numbers[ j ] = b
            j -= 1
        l += 1
        #print(numbers)
#print(ks[:30])
#print(numbers)
#f = open('p088_output.txt', 'w')
#print(f.write(str(ks).replace(', ','\n')[1:-1]))
#f.close()

print(sum(set(ks[2:])))

#--------------------------------
print(time.time()-start," ------seconds------\n")
