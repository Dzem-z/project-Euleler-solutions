import time
start = time.time()
#---------------------------
p = [0 for i in range(1001)]
def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def isrighttriangle(a,b,p):
    c=(i**2+j**2)**0.5
    if c - int(c) == 0:
            p1=int(c)+i+j
            if p1 <=1000:
                p[p1]+=1
            

primes=list(primes_sieve(500))
pr=0
for i in range(2,300):
    for j in range(i+1,500):
            isrighttriangle(i,j,p)
    
            
print(p)
print(p.index(max(p)))
#---------------------------
print(time.time()-start," ------seconds------\n")
