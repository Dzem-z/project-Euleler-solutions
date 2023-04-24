import time, sympy
start = time.time()
#---------------------------
def arePairs(num1, num2):
    return sympy.isprime(int(str(num1) + str(num2))) and sympy.isprime(int(str(num2) + str(num1)))
def primes_sieve(limit):
    a = [True] * limit                          
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False
primes = list(primes_sieve(10**4))
for i in primes:
    for j in primes[primes.index(i):]:
        if arePairs(i,j):
            pairs[i,j] = 

print(pairs[0:100])





#---------------------------------
"""
def primes_sieve(limit):
    a = [True] * limit                          
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False
a = list(primes_sieve(10**4))
f = False
for i in a:
    if f:
        break
    for j in a:
        if f:
            break
        if sympy.isprime(int(str(i) + str(j))) and sympy.isprime(int(str(j) + str(i))):
            print('\n',i,j,end=' ')
            for k in a:
                if f:
                    break
                if sympy.isprime(int(str(i) + str(k))) and sympy.isprime(int(str(k) + str(i))) and sympy.isprime(int(str(j) + str(k))) and sympy.isprime(int(str(k) + str(j))):
                    print('\n',i,j,k,end=' ')
                    for z in a:
                        if f:
                            break
                        if sympy.isprime(int(str(i) + str(z))) and sympy.isprime(int(str(z) + str(i))) and sympy.isprime(int(str(z) + str(j))) and sympy.isprime(int(str(j) + str(z))) and sympy.isprime(int(str(k) + str(z))) and sympy.isprime(int(str(z) + str(k))):
                            print('\n',i,j,k,z)
                            
                            for c in a:
                                if sympy.isprime(int(str(i) + str(c))) and sympy.isprime(int(str(c) + str(i))) and sympy.isprime(int(str(c) + str(j))) and sympy.isprime(int(str(j) + str(c))) and sympy.isprime(int(str(k) + str(c))) and sympy.isprime(int(str(c) + str(k))) and sympy.isprime(int(str(z) + str(c))) and sympy.isprime(int(str(c) + str(z))):
                                    print('\n',i,j,k,z,c)
                                    print("---------------found------------------")
                                    print(i+j+k+z+c)
                                    f = True
                                if f:
                                    break
"""
#---------------------------
print(time.time()-start," ------seconds------\n")
