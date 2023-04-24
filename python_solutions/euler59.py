import time
start = time.time()
#--------------------------------
def CharGenerator():
    val = ord('a')
    val1 = ord('z')
    for i in range(val,val1+1):
        yield chr(i)

file = open('p059_cipher.txt','r')
file = file.read()
file = file.split(',')
file = [ int(i) for i in file]
key = ['','','']
output = ''
for i in CharGenerator():
    key[ 0 ] = i
    for j in CharGenerator():
        key[ 1 ] = j
        for k in CharGenerator():
            key[ 2 ] = k
            for r in range(100):
                output = output + chr( file[ r ] ^ ord( key[ r % 3 ] ))
            #print( output , key)
            output = ''


key = [ord('e'),ord('x'),ord('p')]
l=0
for i in range(len(file)):
    l = l + (file[ i ] ^ key[ i % 3 ])
print(l)
#--------------------------------
print(time.time()-start," ------seconds------\n")
