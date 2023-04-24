import time
start = time.time()
#---------------------------
9*1+90*2+900*3+9000*4
l=1
for i in range(2,7):
    d=10**i
    s=0
    for j in range(0,i):
        if s+9*10**j*(j+1) > d:
            break
        s+=9*10**j*(j+1)
    num=int((d-s)/i)
    w = (d-s)-num*i
    l*=int(str(num+10**j)[w-1])
print(l)
#---------------------------
print(time.time()-start," ------seconds------\n")


