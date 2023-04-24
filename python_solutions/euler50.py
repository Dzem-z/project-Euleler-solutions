import time, sympy
start = time.time()
#---------------------------
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

def primes_sieve(limit):
    a = [True] * limit                          
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     
                a[n] = False

primes = iter(primes_sieve(10**3*5))
primes_array = [next(primes)]
maxi = [0,0]

for i in primes:
    primes_array.append(primes_array[-1]+i)
m=10**6
#print(primes_array)
for i in range(1,len(primes_array),2):
    if is_prime(primes_array[i]) and primes_array[i] < m:
        #print("ci",i,primes_array[i])
        maxi=[i,primes_array[i]]

i = 0
while i < len(primes_array) and len(primes_array) - i > maxi[0]:
    if primes_array[i]%2:
        j=len(primes_array)-1
    else:
        j=len(primes_array)-2
    while j-i > maxi[0]:
            #print(primes_array[j]-primes_array[i])
            if is_prime(primes_array[j]-primes_array[i]) and primes_array[j]-primes_array[i] < m:
                #print("cj",j-i,j,i,primes_array[j]-primes_array[i])
                maxi = [j-i,primes_array[j]-primes_array[i]]
            j-=2
    i+=1

print(maxi)
#---------------------------
print(time.time()-start," ------seconds------\n")
