import time
start = time.time()
#--------------------------------

def HCD(a,b):
    while b != 0:
        d = a % b
        a = b
        b = d
    return a

maxCordinate = 5000


vector1 = [0, 0]
vector2 = [0, 0]

summ = 0

summ += maxCordinate * maxCordinate * 3
print(summ)
#summ = 0
for x in range(1, maxCordinate + 1):
    for y in range(1, maxCordinate + 1):
        hcd = HCD(x,y)
        #vector2b = [-y // hcd, x // hcd]
        #print(vector1, vector2, vector2b, 'P1 = ',  '[',vector1[ 0 ] + vector2[ 0 ], ',', vector1[ 1 ] + vector2[ 1 ] , ']', 'Q1 = ', '[', vector1[ 0 ] ,',',vector1[ 1], ']')
        summ +=  min((maxCordinate - x) * hcd //y, y * hcd // x) * 2
        #print(summ, x, y)
print(summ)

#--------------------------------
print(time.time()-start," ------seconds------\n")
