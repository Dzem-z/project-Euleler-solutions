import time
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
def ispandigital(n):
    a=str(n)
    b=1
    for i in a:
        if 2**int(i)&b:
            return False
        b|=2**int(i)
    return b == 255
i=7654321
while True:
    if ispandigital(i) and is_prime(i):
        print(i)
        break
    i-=1
        
#---------------------------
print(time.time()-start," ------seconds------\n")
