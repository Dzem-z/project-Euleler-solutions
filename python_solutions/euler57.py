import time
start = time.time()
#---------------------------
a = [1,2]
c= 0
for i in range(1000):
    a = [a[1],2*a[1]+a[0]]
    if len(str(a[0]+a[1])) > len(str(a[1])):
        c+=1
print(c)
#---------------------------
print(time.time()-start," ------seconds------\n")
