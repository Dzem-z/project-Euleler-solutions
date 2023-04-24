import time
from math import sqrt
start = time.time()
#---------------------------------------------------------
a= 6
b = 5
c = 3

M = 100
#B = 2 * a * c ** 2
#D = 2 * b * a * c
"""#sol1
counter = 0
for a in range(1, M + 1):
    for b in range(1, a + 1):
        for c in range(1, b + 1):
            print(a,b,c)
            x1 = a * c / ( b + c )
            x2 = b * c / ( a + b )
            x3 = c * a / ( b + a )

            d1 = sqrt( (a - x1) ** 2 + b ** 2) + sqrt( x1 ** 2 + c ** 2)
            d2 = sqrt( (b - x2) ** 2 + a ** 2) + sqrt( x2 ** 2 + c ** 2)
            d3 = sqrt( (c - x3) ** 2 + b ** 2) + sqrt( x3 ** 2 + a ** 2)

            if d1.is_integer():
                counter += 1
                #print(d1)
            #if b % 30 == 0 and c % 30 == 0:
            #    print(d1, d2, d3)
"""

"""#sol2

counter = 0
M = 1

while counter <= 2000:
    for b in range(1, M + 1):
        for c in range(1, b + 1):
            sh = sqrt(M ** 2 + (b + c) ** 2)

            if sh.is_integer():
                counter += 1
        
    M += 1

print(counter, M - 1)
print(time.time()-start," ------seconds------\n")"""
#sol3
counter = 0
M = 1
while counter <= 10 ** 6:
    for b in range(2, 2 * M + 1):
            sh = sqrt(M ** 2 + b ** 2)

            if sh.is_integer():
                counter += min(M + 1, b) - (b + 1) // 2
            #if b % 2000 == 0:
            #    print(M,sh, counter)
    M += 1

print(counter, M - 1)


#counter1 = 0
#counter = 0
""""for M in range(1,1000):
    counter = counter1 = 0
    for b in range(1, M + 1):
        for c in range(1, b + 1):
            sh = sqrt(M ** 2 + (b + c) ** 2)

            #if sh.is_integer():
            counter1 += 1
    for b in range(2, 2 * M + 1):
            sh = sqrt(M ** 2 + b ** 2)

            #if sh.is_integer():
            counter += min(M + 1, b) - (b + 1) // 2
    print(counter, counter1, M)"""
#---------------------------------------------------------
print(time.time()-start," ------seconds------\n")
