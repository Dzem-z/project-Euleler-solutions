import time
start = time.time()
#---------------------------
v=[]
def ispandigital(n):
    a=str(n)
    b=0
    for i in a:
        if 2**int(i)&b:
            return False
        b|=2**int(i)
    return b == 1023
l= [i for i in range(0,10)]
for d6 in [0,5]:
    for d4 in range(0,8,2):
        if d4 != d6:
            l1=l[:]
            l1.remove(d4)
            l1.remove(d6)
            for d1 in range(1,9):
                if d1 in l1:
                    #print(d6,d4,d1)
                    l2=l1[:]
                    l2.remove(d1)
                    for d5 in l2:
                            #print(d6,d4,d1,d5)
                            l9=l2[:]
                            l9.remove(d5)
                            for d3 in l9:
                                if (d4+d5+d3)%3==0:
                                    #print(d6,d4,d1,d5,d3)
                                    l3=l9[:]
                                    l3.remove(d3)
                                    for d7 in l3:
                                        if int(str(d5)+str(d6)+str(d7))%7==0:
                                            #print(d6,d4,d1,d5,d3,d7)
                                            l4=l3[:]
                                            l4.remove(d7)
                                            for d8 in l4:
                                                if int(str(d6)+str(d7)+str(d8))%11==0:
                                                    #print(d6,d4,d1,d5,d3,d7,d8)
                                                    l5=l4[:]
                                                    l5.remove(d8)
                                                    for d9 in l5:
                                                        if int(str(d7)+str(d8)+str(d9))%13==0:
                                                            #print(d6,d4,d1,d5,d3,d7,d8,d9)
                                                            l6=l5[:]
                                                            l6.remove(d9)
                                                            for d10 in l6:
                                                                if int(str(d8)+str(d9)+str(d10))%17==0:
                                                                    
                                                                    l7=l6[:]
                                                                    l7.remove(d10)
                                                                    for d2 in l7:
                                                                        v+=[int(str(d1)+str(d2)+str(d3)+str(d4)+str(d5)+str(d6)+str(d7)+str(d8)+str(d9)+str(d10))]
                                                                        print(v[-1])
                                            
                                
    

#---------------------------
print(time.time()-start," ------seconds------\n")
