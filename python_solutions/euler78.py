import time
start = time.time()
#--------------------------------

size = 100000
#array = [ [0 for i in range(size)] for j in range(size) ]
#array[0][0] = 1
"""#1
for number in range(size):
    for series in range(0,number):
        array[number][series] = array[number-1][series]
    for series in range(number,size):
        for inum in range(1,number + 1):
            array[number][series] += array[inum][series - inum ]
    print(number, array[number][-5:],'\n\n')
"""

array = [ [0 for i in range(size)] for j in range(2) ]
array[0][0] = 1


"""#2
for number in range(0,size):
    for series in range(number - 1,size):
        array[1][series] += array[1][series - number ] % (10**6)
        array[1][series] += array[0][series] % (10**6)
    for i in range(number,size):
        array[0][i] = array[1][i]
        array[1][i] = 0
    #if number % 100 == 0:
    #print(number, array[0][-100:],'\n\n')
"""


#3
nofp = [ 0 for i in range(size) ]
nofp[1] = 1

def g(k):
    return k*(3*k-1)//2

n = 2
while nofp[n - 1] != 0:
    k = 1
    while g(k) < n:
        nofp[n] += nofp[n - g(k)] * ( -1 if k % 2 == 0 else 1)
        nofp[n] %= 10**6
        if k > 0:
            k *= -1
        else:
            k*= -1
            k += 1
    n+= 1
print(n)




#for i in range(size):
#    array[ i ] = p(i)
#    print( array[ i ] )



#for j in range(size):
#    print(array[0][j])
#--------------------------------
print(time.time()-start," ------seconds------\n")
