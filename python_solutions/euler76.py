import time
start = time.time()
#---------------------------------------------------------
target = 101

sums = [ 0 for i in range(target) ]
sums[ 0 ] = 1
for i in range(1, len(sums)):
    for j in range(i, len(sums)):
        sums[ j ] += sums[ j - i ]
print( sums[ 100 ] - 1 )

"""
nofp = [ 0 for i in range(target + 1) ]
nofp[1] = 1

def g(k):
    return k*(3*k-1)//2

n = 1
while n <= target:
    k = 1
    while g(k) < n:
        nofp[n] += nofp[n - g(k)] * ( -1 if k % 2 == 0 else 1)
        nofp[n] %= 10**6
        k *= -1
        if k >= 0:
            k += 1
    n+= 1
print([x - 1 for x in nofp])
print(nofp[ target ])"""
#---------------------------------------------------------
print(time.time()-start," ------seconds------\n")
