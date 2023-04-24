import time
start = time.time()
#--------------------------------

upperLimit = int(1e+6)

upperLimit = 10000

squares = ( x ** 2 for x in range(int(4 * upperLimit * upperLimit ) ) )

nex = next(squares)
for x in range(upperLimit // 3):
    xsq = x * x
    xcu = xsq * x
    xf = xcu * x
    su = 3 * xf + xsq
    area = su - 4 * xcu
    while nex < area:
        nex = next(squares)
    #print(x, nex)
    if nex == area:
        print(x, area, area ** 0.5, 2 * x, 2 * x - 1)


    
#--------------------------------
print(time.time()-start," ------seconds------\n")
