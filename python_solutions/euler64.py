import time
from math import sqrt

start = time.time()
#---------------------------
point = [0,0,0]
counter = 0
for root in range(1,10**4+1):
    sq = sqrt(root)
    period = 0
    if sq == int(sq):
        continue
    sq = int(sq)
    down = -sq
    up = 1
    t = down*-1
    c = 0
    root = root
    d = 0
    for l in range(2):
        t = down*-1
        down = (root - down*down)/up
        up = t
        a = 0
        for i in range(sq,0,-1):
            if((i+t)%down == 0):
                a = i
                break
        t = (a+t)/down
        up = -a
        c+= 1
        d = t
        t = up
        up = down
        down = t
        if l == 0:
            point = [d,up,down]
    while d != point[0] or up != point[1] or down != point[2]:
        t = down*-1
        down = (root - down*down)/up
        up = t
        a = 0
        for i in range(sq,0,-1):
            if((i+t)%down == 0):
                a = i
                break
        t = (a+t)/down
        up = -a
        c+= 1
        d = t
        t = up
        up = down
        down = t
    if (c-1) % 2 == 1:
        counter += 1
    #print(root,c-1)

print(counter)

#---------------------------
print(time.time()-start," ------seconds------\n")
