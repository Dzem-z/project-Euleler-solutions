import time
start = time.time()
#---------------------------
"""pentagonal = [n*(3*n-1)/2 for n in range(1,1000)]

for e,n1 in enumerate(pentagonal):
    for n2 in pentagonal[e:]:
        if n1+n2 in pentagonal[e:] and (n1+2*n2 in pentagonal or 2*n1+n2 in pentagonal):
            print(n1,n2,n1+n2,n1+2*n2,'>>>>>')"""
f=1
for n1 in range(1,3000):
    for n2 in range(n1,3000):
        a=(1-12*(2*n1*(3*n1-1)-n2*(3*n2-1)))
        b=(1-12*(n1*(3*n1-1)-n2*(3*n2-1)))
        if a>=0 and (a**0.5+1)%6==0 and b>0 and (b**0.5+1)%6 == 0:
            print((b**0.5+1)/6,n1,n2,(a**0.5+1)/6,':',(b**0.5+1)/6*(3*(b**0.5+1)/6-1),':',n1*(3*n1-1),':',n2*(3*n2-1),':',(a**0.5+1)/6*(3*(a**0.5+1)/6-1))
            f=0
            break
        if not f:
            break
#---------------------------
print(time.time()-start," ------seconds------\n")
