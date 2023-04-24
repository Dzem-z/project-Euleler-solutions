import time
start = time.time()
#--------------------------------
size = 1500000
a =  [ [0] for i in range( size ) ]
upLimit = 1224
def AreCoprime(firstNum, secondNum):
    smaller = min(firstNum, secondNum)
    for i in (2, smaller**0.5):
        if i % firstNum == 0 and i % secondNum == 0:
            return False
    return True


for t in range( 1, upLimit ):
    for s in range( t + 1, upLimit ):
        if AreCoprime( s, t):
            d = 1 if s % 2 + t % 2 == 1 else 2
            wire = 2 * s * ( t + s ) // d
            i = 1
            z = (s * s + t * t) // d
            
            while (n := i * wire) < size:
                if z * i in a[ n - 1][1:]:
                    i+= 1
                    continue
                a[ n - 1].append( z * i)
                a[ n - 1][ 0 ] += 1
                a[ n - 1].append( z * n)
                i += 1
                #print( z * i, n)
            #print((s * s - t * t) / d, 2 * s * t / d, (s * s + t * t) / d, wire, s, t)
summary = 0
for i in a:
    summary += 1 if i[ 0] == 1 else 0
print()
print(summary)
#--------------------------------
print(time.time()-start," ------seconds------\n")
