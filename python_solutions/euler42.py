import time
start = time.time()
#---------------------------
f = open('words.txt','r')
a=f.read()[:-1]
s = [word[1:-1] for word in a.split(',')]
values = {chr(i):i-64 for i in range(65,91)}

def evaluate(s):
    v=0
    for i in s:
        v+=values[i]
    return v
seqval = [0.5*n*(n+1) for n in range(1,100)]

triangles=0
c=0
for i in s:
    if evaluate(i) in seqval:
        triangles+=1
print(triangles)
#---------------------------
print(time.time()-start," ------seconds------\n")
