import time
start = time.time()
#---------------------------

s=100
sum = 0
for n in range(1,s+1):
    r=n-1
    t=n
    while t <= 10**6 and r > n/2:
        t*=r/(n-r+1)
        r-=1
    if t > 10**6:
        sum+=2*r-n+1
print(sum)
#---------------------------
print(time.time()-start," ------seconds------\n")
