import time, sympy
start = time.time()
"""#ver1
#---------------------------
i = 1
digits,digits2=[1],[2]
while digits != digits2 or digits2 != digits3 or digits3 != digits4 or digits4 != digits5 or digits5 != digits6:
    i+=1
    digits = sorted(list(str(i)))
    digits2 = sorted(list(str(2*i)))
    digits3 = sorted(list(str(3*i)))
    digits4 = sorted(list(str(4*i)))
    digits5 = sorted(list(str(5*i)))
    digits6 = sorted(list(str(6*i)))
print(i,i*2,i*3,i*4,i*5,i*6)
#---------------------------
print(time.time()-start," ------seconds------\n")
"""

#ver2
#---------------------------
e=0
i =1
digits, digits2 = [],[1]
w=0
while w != 7:
    val = 16*10**e
    i=10**(e+1)
    while i < val and w != 7:
        j=0
        set1= set(list(str(i)))
        set2 = set(list(str(2*i)))
        w = 3
        while set1 == set2 and w < 7:
            set1 = set2
            set2 = set(list(str(w*i)))
            w+=1
        i+=1
    
    e+=1
i-=1
print(i,i*2,i*3,i*4,i*5,i*6)
#---------------------------
print(time.time()-start," ------seconds------\n")
