import time
start = time.time()
#---------------------------
#1

def delay(ms):
    start = time.time()
    while(time.time() - start < ms / 1000):
        ...


def isChance(num):
    return num == 7 or num == 22 or num == 36

def isCommunityChest(num):
    return num == 2 or num == 17 or num == 33

def isJail(num):
    return num == 10 or num == 30

def nextR(num):
    return ((num + 5) // 10 * 10 + 5) % 40

def nextU(num):
    return 28 if num > 12 and num < 28 else 12

class prob_list(list):
    def __init__(self, *args,size=4, **kwargs):
        self.size = size
        list.__init__(self,*args,**kwargs)
        for i in range( size * 2 - 1):
            self[ i ] = self[ i + 2 ] / size ** 2
    
    def __getitem__(self, index):
        return list.__getitem__(self, index - 2)


def applyChanceProbs(num, probability,  array):
    final = probability * 1 / 16
    array[ num ] += 6 * final
    for i in [0, 10, 11, 24, 39, 5, nextR(num), nextR(num), nextU(num), num - 3]:
        array[ i ] += final

def applyCommunityChestProbs(num, probability, array):
    final = probability * 1 / 16
    array[ 0 ] += final
    array[ 10 ] += final
    array[ num ] += 14 * final


    

l = [1,2,3,4,3,2,1]#[1,2,3,4,5,6,5,4,3,2,1]
probs = prob_list(l, size=4)
#for i in range( probs.size * 2 - 1):
#    probs[ i ] /= probs.size ** 2
#print(probs)
"""print(probs[2])
probs[0] /= 36
print(probs[2])
print(probs[3])
probs[1] /= 36
print(probs[3])"""



squares = [0] * 40
squares[0] = 100
change = [0] * 40
#applyChanceProbs(7,1,squares)
#print("sq=", sum(squares))
#applyCommunityChestProbs(2,1/16,squares)
#print("sq=", sum(squares), 1/16)
#print(sum(probs))
for turn in range(1000):
    for square in range(40):
        for shift in range(2, probs.size * 2 + 1):
            shifted = (square + shift) % 40
            probability = probs[ shift ] * squares[ square ]
            if isJail(shifted):
                change[ 10 ] += probability
            elif isCommunityChest(shifted):
                applyCommunityChestProbs(shifted, probability, change)
            elif isChance(shifted):
                applyChanceProbs(shifted, probability, change)
            else:
                change[ shifted ] += probability
    squares = change[:]
    change = [0] * 40
    #print(squares[ 10 ], squares[ 24 ], squares[ 0 ])
    #delay(200)
        #print(sum(squares), end=" ")
    #print(sum(squares))
        
#squares = [i * 100 for i in squares]
#print(squares)
doubles = [ (squares[i], i) for i in range(40) ]
#print(doubles)
#print(squares[ 10 ], squares[ 24 ], squares[ 0 ])
#print(sum(squares))

print("".join([str(i[1]) for i in reversed(sorted(doubles)[-3:])]))



#2










#---------------------------
print(time.time()-start," ------seconds------\n")
