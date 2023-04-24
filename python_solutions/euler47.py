#!/bin/python3

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
primes = list(primes_sieve(200000))

l =[0]*10**6
for i in primes:
    s=i
    while s < len(l):
        l[s]+=1
        s+=i
    
c=0
i=0
while i < len(l) and c != 4:
    if l[i]==4:
        c+=1
    else:
        c=0
    i+=1
print(i-4)
def decomposition(p,primeS=primes):
    s=0
    d=False
    l = iter(primes)
    i=next(l)
    while i <= p:
        while p%i==0:
            d=True
            p/=i
        if d:
           s+=1
           d=0
        i=next(l)
    return s
"""       
c=0
i = 646
while c != 4:
    if decomposition(i) == 4:
        c+=1
        if c == 4:
           break
    else:
        c= 0
    i+=1
    
print(i)"""
    
#---------------------------
print(time.time()-start," ------seconds------\n")
