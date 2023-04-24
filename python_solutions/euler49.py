import time, sympy
start = time.time()
#---------------------------
def primes_sieve(limit):
    a = [True] * limit                          
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     
                a[n] = False
primes = list(primes_sieve(10**5))[167:1230]
for i in range(len(primes)-1):
    s=set(str(primes[i]))
    j=i+1
    while 2*primes[j]-primes[i] <= primes[-1]:
                if s == set(str(primes[j])) and set(str(2*primes[j]-primes[i]))==s and len(s) == len(set(str(primes[j]))) and len(s) == len(set(str(2*primes[j]-primes[i]))) and sympy.isprime(2*primes[j]-primes[i]):
                   print(str(primes[i])+str(primes[j])+str((2*primes[j]-primes[i])))
                j+=1
#---------------------------
print(time.time()-start," ------seconds------\n")
