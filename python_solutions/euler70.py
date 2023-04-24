import time
start = time.time()
#---------------------------

def primes_sieve( limit ):
    a = [ True ] * limit                          
    a[ 0 ] = a[ 1 ] = False

    for ( i, isprime ) in enumerate( a ):
        if isprime:
            yield i
            for n in range( i * i, limit, i ):
                a[ n ] = False


def arePermutations(num1,num2):
    a1 = max(num1,num2)
    a2 = min(num1,num2)
    for i in a2:
        a = a1.find(i)
        a1 = a1[:a]+a1[a+1:]
    return not bool(a1)

def phi(*primes):
    result = 1
    for i in primes:
        result *= i - 1
    return result

print(phi(7))

size = 10**4

minimum = size
value = 0


prime_s = list(primes_sieve(size))
prime_s.reverse()
for b,i in enumerate( prime_s ):
    a = b
    while a < len(prime_s) and prime_s[a]*i > 10**7:
        a+= 1
    while a < len(prime_s):
        j = prime_s[a]
        if arePermutations(str(phi(i,j)),str(i*j)):
            if minimum > i*j / phi(i,j):
                print(i*j)
                minimum = i*j / phi(i,j)
                value = [i,j]
        a+= 1

print(minimum)
print(value[0]*value[1])

#---------------------------
print(time.time()-start," ------seconds------\n")
