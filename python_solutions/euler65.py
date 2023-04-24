import time
start = time.time()
#--------------------------------
def SqrtConvergents( N):
    nominator = 1
    denominator = int(N / 3 * 2 if N % 3 == 0 else 1)
    const = 1
    N -= 1
    for i in range(N, 1, -1):
        handler = nominator + int( i / 3 * 2 if i % 3 == 0 else 1) * denominator
        nominator = denominator
        denominator = handler

    return 2 * denominator + nominator

a = str(SqrtConvergents(100))
su = 0
for j in a:
    su += int(j)
print(su)
#--------------------------------
print(time.time()-start," ------seconds------\n")
