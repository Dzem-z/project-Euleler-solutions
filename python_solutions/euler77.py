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
size = 100
primes = list( primes_sieve( size ) )

primeSums = [ 0 ] * size


for i in primes:
    primeSums[ i ] += 1
    for j in range( i, size ):
        primeSums[ j ] += primeSums[ j - i ]
for e, i in enumerate( primeSums ):
    if i >= 5000:
        print( e )
        break
#--------------------------------
print(time.time()-start," ------seconds------\n")
