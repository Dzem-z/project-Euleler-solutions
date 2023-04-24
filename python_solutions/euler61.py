import time
start = time.time()
#---------------------------
def Triangle(n):
    return int(n*(n+1)/2)
def Square(n):
    return int(n*n)
def Pentagonal(n):
    return int(n*(3*n-1)/2)
def Hexagonal(n):
    return int(n*(2*n-1))
def Heptagonal(n):
    return int(n*(5*n-3)/2)
def Octagonal(n):
    return int(n*(3*n-2))

def AreCyclic(firstNum, secNum):
    return str(firstNum)[2:] == str(secNum)[0:2]

def CyclicChain(a,lprev,func,iprev,ifirst):#,exists):
    if len(lprev) == 0:
        if func(iprev,ifirst):
            return 0
        else:
            return None
    ji = 0
    d = [None,0]
    while d[0] == None and ji < len(lprev):
        j = lprev[ji]
        for i in a[j]:
            if func(iprev,i):
                l = lprev[:]
                l.remove(j)
                e = False
                #w = int(str(i)[2:])-10
                #for z in l:
                #    e = e or exists[z][w]
                #if len(l) == 0 or e:
                d[0] = CyclicChain(a,l,func,i,ifirst)#,exists)
                d[1] = i
                if d[0] != None:
                    break
        ji+=1
    if d[0] != None:
        return d[0]+d[1]
    else:
        return None
#exist = [False for i in range(10,100)]
#exists = [exist[:] for i in range(6)]
a = [[Triangle(i) for i in range(150) if len(str(Triangle(i))) == 4 and str(Triangle(i))[2] != '0'],
     [Square(i) for i in range(150) if len(str(Square(i))) == 4 and str(Square(i))[2] != '0'],
     [Pentagonal(i) for i in range(150) if len(str(Pentagonal(i))) == 4 and str(Pentagonal(i))[2] != '0'],
     [Hexagonal(i) for i in range(150) if len(str(Hexagonal(i))) == 4 and str(Hexagonal(i))[2] != '0'],
     [Heptagonal(i) for i in range(150) if len(str(Heptagonal(i))) == 4 and str(Heptagonal(i))[2] != '0'],
     [Octagonal(i) for i in range(150) if len(str(Octagonal(i))) == 4 and str(Octagonal(i))[2] != '0']]
#for e,i in enumerate(a):
#    for j in i:
#        exists[e][int(str(j)[0:2])-10] = True

#print(exists[0])
for i in a[0]:
	c = CyclicChain(a,[1,2,3,4,5],AreCyclic,i,i)#,exists)
	if c != None:
		c+=i
		break

print(c)
"""

for i in a[0]:
    l0 = [1,2,3,4,5]
    for j in l0:
        for i1 in a[j]:
            if AreCyclic(i,i1):
                l1 = l0[:]
                l1.remove(j)
                for j1 in l1:
                    for i2 in a[j1]:
                        if AreCyclic(i1,i2):
                            l2 = l1[:]
                            l2.remove(j1)
                            for j2 in l2:
                                for i3 in a[j2]:
                                    if AreCyclic(i2,i3):
                                        l3 = l2[:]
                                        l3.remove(j2)
                                        for j3 in l3:
                                            for i4 in a[j3]:
                                                if AreCyclic(i3,i4):
                                                    l4 = l3[:]
                                                    l4.remove(j3)
                                                    for j4 in l4:
                                                        for i5 in a[j4]:
                                                            if AreCyclic(i4,i5) and AreCyclic(i5,i):
                                                                print("\n\n\ncycle found\n\n\n")
                                                                print(i,i1,i2,i3,i4,i5)
                                                                print("\n\n\n")
                                                                print(i+i1+i2+i3+i4+i5)



"""
#---------------------------
print(time.time()-start," ------seconds------\n")
