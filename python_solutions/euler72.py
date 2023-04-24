import time
start = time.time()
#---------------------------

def NWD(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def primes_sieve( limit ):
    a = [ True ] * limit                          
    a[ 0 ] = a[ 1 ] = False

    for ( i, isprime ) in enumerate( a ):
        if isprime:
            yield i
            for n in range( i * i, limit, i ):
                a[ n ] = False


def decompose(x):
    l = []
    while x != 1:
        p = primes_sieve(x)
            

maX = 10**6 + 1 #10**6
counter = 0

#brute force
"""
for d in range(maX):
    for n in range(1,d):
        if NWD(n,d) == 1:
            counter += 1
    if d % 100 == 0:
        print(d)

print( counter )
""""""#2
sums = [ 0 ]*10**6

for d in primes_sieve(maX):
    sums[ d ] = d - 1

def primes(sums, l = [], mult = 1, diff = 0, m = 10**6):
    for p in primes_sieve(maX):
        if p > m:
            break
        mult *= p
        if mult < 10**6:
            l.append(p)
            diff += sums[ p ]
            sums[ mult ] = mult - 1 - diff
            print("num: ", mult, l)
            primes(sums, l, mult, diff, p)
        else:
            break
        mult //= p
        l.pop()
        diff -= sums[ p ]

primes(sums)
counter = sum(sums)       
"""
counter = 0
#maX -= 1


sums = [ i for i in range(maX) ]
sums[ 1 ] = 0

for i in range(2, maX):
    if sums[ i ] == i:
        #j = 2 * i
        j = i
        while j < maX:
            sums[ j ] = sums[ j ] // i * ( i - 1 )
            j += i
    #if i % 10000 == 0:
        #print( i, sums[ i ] )

#for d in range(maX):
    
counter = sum( sums )  
        


"""
result = 1
factors = [1, 2]
indexes = [0, 1]



1000000
500000 - 1
333333 - 1

200000 - 1

1 2 3 4 5 6 7 8 9 10 11 12
  - - -   -   - - -     -

1 2 3 4 5 6 7 8 9 10

"""
print(counter)


#---------------------------
print(time.time()-start," ------seconds------\n")
