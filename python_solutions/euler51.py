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
primes = primes_sieve(10**7)

c=0
z=['0','1','2']

while c < 7:
    try:
        prime = str(next(primes))
    except StopIteration:
        break
    for it in z:
        if c == 7:
            break
        if it in prime:
            arr=[]
            for en,i in enumerate(prime):
                if i == it:
                    c=0
                    arr.append(en)
            if len(arr) != 3:
                continue
            cp = int(it)+1
            prime_s=prime
            while cp-c < 5 and cp < 10:
                prime_s =prime
                for j in arr:
                    prime_s = prime_s[:j] + str(cp) + prime_s[j+1:]
                if sympy.isprime(int(prime_s)):
                            #print(prime_s)
                    c+=1
                cp+=1
            if c > 6:
                break
                        
                        
print(prime)
#---------------------------
print(time.time()-start," ------seconds------\n")
