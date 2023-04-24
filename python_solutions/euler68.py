import time
start = time.time()
#--------------------------------
strings = []
for num in range(14,21):
    table = [ [] for i in range(11)]
    arr = []
    for i in range(10,0,-1):
        for b in range(num-i-1,0,-1):
            if b != i and num-b != 2*i and b != num-b-i and num-b-i < 11 and b < 11:
                table[num-b-i].append([i,b,num-b-i])
                arr.append([i,b,num-b-i])
                #print(i,b,num-i-b)
    
    digits = []
    for a in arr:
        if a[0] !=6:
            continue
        digits = a
        
        for b in table[ a[ 1 ] ]:
            
            if not ( b[ 1 ] in digits or b[ 0 ] in digits ):
                digits1 = digits + b[:2]
                for c in table[ b[ 1 ] ]:
                    if not ( c[ 1 ] in digits1 or c[ 0 ] in digits1 ):
                        digits2 = digits1 +  c[:2]
                        for d in table[ c[ 1 ] ]:
                            l = num - a[2] -d[1]
                            if not ( d[ 1 ] in digits2 or d[ 0 ] in digits2 or l in digits2 or l in d) and l > 0 and l < 11 :
                                mi = min( a[0] ,b[0], c[0], d[0], l)
                                
                                index = (a[0] ,b[0], c[0], d[0], l).index(mi)
                                w =  [a] + [b] + [c] + [d] + [[ l ,a[2],d[1]]]
                                q = [ w[i % 5] for i in range( index, index - 5, -1) ] 
                                s = ''
                                for i1 in q:
                                    for i2 in i1:
                                        s += str(i2)
                                if len(s) == 16:
                                    strings += [s]
print(max(strings))
#--------------------------------
print(time.time()-start," ------seconds------\n")
