import time
start = time.time()
#---------------------------
H,n3 = 40755,143
while True:
    H += 4*n3+1
    n3 += 1
    np = (.5 + (.25+6*H)**.5)
    if np % 3 == 0:
        break
print(H)
        
#---------------------------
print(time.time()-start," ------seconds------\n")
