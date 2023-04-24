import time
start = time.time()

"""###first approach
max_sol = 0
v = 2
sq = v*v

for D in range(2,30,1):
    if D == sq:
        v+= 1
        sq = v*v
        continue
    x = 1.1
    y = 1
    while x - int(x) != 0:
        x = (1+D*y*y)**0.5
        y+=1
    print(y-1,x,D)
"""
#second approach
Dmax = 0
max_sol = 0
v = 2
sq = v*v
vp = v-1

for D in range(2,1001,1):
    if D == sq:
        vp = v
        v+= 1
        sq = v*v
        continue
    n2 = v
    d2 = 1
    a = 0
    nominator = vp
    denominator = 1
    n0 = n1 = n2 = 0
    d0 = d1 = d2 = 0
    x = y = 0
    a = vp
    n0 = a
    d0 = 1
    if n0*n0 -D*d0*d0 == 1:
        if n0 > max_sol:
            max_sol = n0
            Dmax = D
        continue
    denominator = (D - nominator * nominator ) / denominator
    a = ( nominator + vp ) // denominator
    nominator = -nominator + a * denominator
    n1 = a*n0 + 1
    d1 = a
    x = n1
    y = d1
    while x*x -D*y*y != 1:
        denominator = int((D - nominator * nominator ) // denominator)
        a = int(( nominator + vp ) // denominator)
        nominator = -nominator + a * denominator
        n2 = int(a*n1 + n0)
        d2 = int(a*d1 + d0)
        n0 = n1
        d0 = d1
        n1 = n2
        d1 = d2
        
        x = n2
        y = d2
    if x > max_sol:
        max_sol = x
        Dmax = D
    #print("x=",x,"y=",y, "D=" ,D)
print(max_sol,Dmax)
print(time.time()-start," ------seconds------\n")
