import time
start = time.time()
#---------------------------

def NWD(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

minimum = 2/5
fraction = [2,5]
j = 0
for den in range(10**6, 8, -1):
    if den % 7 == 0:
        continue
    nom = 3*den//7
    
    if nom/den > minimum:
        fraction = [nom, den]
        minimum = nom/den
            
print(fraction,minimum)

#---------------------------
print(time.time()-start," ------seconds------\n")

#0.42857142857142855
