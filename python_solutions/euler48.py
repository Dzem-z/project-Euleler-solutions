import time, sympy
start = time.time()
#---------------------------
s=0
for i in range(1,1000):
	s+=i**i
	s%=10**10

print(s)
#---------------------------
print(time.time()-start," ------seconds------\n")
