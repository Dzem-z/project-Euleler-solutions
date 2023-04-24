import time
start = time.time()
#--------------------------------
def primes_sieve( limit ):
    a = [ True ] * limit                          
    a[ 0 ] = a[ 1 ] = False

    for ( i, isprime ) in enumerate( a ):
        if isprime:
            yield i
            for n in range( i * i, limit, i ):
                a[ n ] = False

size = 10000

prime_gen = primes_sieve(size)
result = 1
while result < 10**6:
    l = next(prime_gen)
    result*= l

print(result//l)


#--------------------------------
print(time.time()-start," ------seconds------\n")
