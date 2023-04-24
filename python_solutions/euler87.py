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
target = 50 * 10 ** 6

squares = [ i ** 2 for i in list(primes_sieve(int(target ** 0.5) + 100)) ]
cubes = [ i ** 3 for i in list(primes_sieve(int(target ** (1/3)) + 100)) ]
fourths = [ i ** 4 for i in list(primes_sieve(int(target ** 0.25) + 100)) ]
isDone = [False] * (target + 1)
#"""
counter = 0
#1
f = 0
while fourths[ f ] + cubes[ 0 ] + squares[ 0 ] < target:
    c = 0
    while fourths[ f ] + cubes[ c ] + squares[ 0 ] < target:
        s = 0
        while fourths[ f ] + cubes[ c ] + squares[ s ] < target:
            #if s % 2000 == 0 and c % 100 == 0:
            #    print(squares[ s ], cubes[ c ], fourths[ f ])
            if not isDone[ fourths[ f ] + cubes[ c ] + squares[ s ] ]:
                counter += 1
                isDone[ fourths[ f ] + cubes[ c ] + squares[ s ] ] = True
            s += 1
            
        c+= 1
    f += 1

print(counter)
"""
#2
counter = 0
f = 0
c = 0
d = 0
#block1
while fourths[ f ] + cubes[ c ] + squares[ d ] < target:
    d += 1
#print( fourths[ f ], cubes[ c ], squares[ d ], f, c, d)
c += 1
counter += d
#endofblock1
while fourths[ f ] + cubes[ 0 ] + squares[ 0 ] < target:
    while fourths[ f ] + cubes[ c ] + squares[ 0 ] < target:
        #block2
        while fourths[ f ] + cubes[ c ] + squares[ d ] > target:
            d -= 1
        #endofblock2
        #block1
        while fourths[ f ] + cubes[ c ] + squares[ d ] < target:
            d += 1
        if d % 10 == 0:
            print( fourths[ f ], cubes[ c ], squares[ d ], f, c, d,)#fourths[ f ] + cubes[ c ] + squares[ 0 ])
        c += 1
        
        counter += d
        #endofblock1
    c = 0
    f+= 1

print(counter)
#"""
#--------------------------------
print(time.time()-start," ------seconds------\n")
