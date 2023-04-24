import time
from sympy import isprime
start = time.time()
#---------------------------
shift = 2
primesc = 3
num = 9
while (shift*2+1)/primesc < 10:
    shift += 2
    for i in range(3):
        num += shift
        if isprime(num):
            primesc+= 1
    num+=shift
print(shift+1)
#---------------------------

print(time.time()-start," ------seconds------\n")
