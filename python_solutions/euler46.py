import time, sympy
start = time.time()
#---------------------------
def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
primes = list(primes_sieve(6000))
odd = 5
while True:
    i = 0
    while primes[i] <= odd:
        l = ((odd-primes[i])/2)**.5
        if l - int(l) == 0:
            break
        i += 1
    else:
        break
    odd+=2





"""
odd = 3
while True:
    i=1
    while i <= odd:
        l = ((odd-i)/2)**.5
        if l - int(l) == 0 and sympy.isprime(i):
            #print(odd,l,i)
            break
        i+=2
    else:
        break
    odd+=2"""
print(odd)
#---------------------------
print(time.time()-start," ------seconds------\n")
