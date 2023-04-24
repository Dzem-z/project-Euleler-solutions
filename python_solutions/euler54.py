import time
start = time.time()
#---------------------------
def Values(array):
    return [i[1] for i in array]
def Straight(array1):
    if array1[0]+1 == array1[1] and array1[1] + 1 == array1[2] and array1[2] +1 == array1[3] and array1[3] + 1 == array1[4]:
        return True
    return False

def RStraight(array):
    array.sort()
    isStraight = Straight(array)
    if isStraight and max(array) == 14:
        return True,True
    return (False,isStraight)

def Flush(array):
    if array[0][0] == array[1][0] and array[2][0] == array[1][0] and array[2][0] == array[3][0] and array[3][0] == array[4][0]:
        return True
    return False

def Royal(arrayv,arrays):
    flush = Flush(arrays)
    straight = RStraight(arrayv)
    if straight[0] and flush:
        return [True]*3
    return False,straight[1],flush

def cardsWithSameValues(array):
    values = {}
    Foak,Toak,FH,TP = [False]*4
    OP = [False,0]
    for i in array:
        values[i] = 0
    for i in array:
        values[i] += 1
    keys = list(values.keys())
    if len(values) == 2:
        
        if values[keys[0]] == 4 or values[keys[1]] == 4:
            print('k0 ',keys[0],'k1 ',keys[1])
            Foak = True
        else:
            FH = True
    elif len(values) == 3:
        if values[keys[0]] == 3 or values[keys[1]] == 3 or values[keys[2]] == 3:
            Toak = True
        else:
            TP = True
    elif len(values) == 4:
        i = 0
        while values[keys[i]] < max(values.values()):
            i+=1
        OP = True,keys[i]
    return (Foak,FH,Toak,TP,OP)


poker_hands = open('/home/adam/Documents/programming/python3/p054_poker.txt','r').read().split('\n')
cards = [i.split(' ') for i in poker_hands[:-1]]
for i in range(len(cards)):
    for j in range(len(cards[i])):
        a = cards[i][j][0]
        cards[i][j] = [cards[i][j][1]]
        
        if a <= '9':
            cards[i][j].append(int(a))
        elif a == 'T':
            cards[i][j].append(10)
        elif a == 'J':
            cards[i][j].append(11)
        elif a == 'Q':
            cards[i][j].append(12)
        elif a == 'K':
            cards[i][j].append(13)
        else:
            cards[i][j].append(14)
    cards[i] = [cards[i][0:5],cards[i][5:]]

wins = 0
print(cards[0])
for e,hands in enumerate(cards):
    winner = 0
    hands_values = Values(hands[0]),Values(hands[1])
    straight = [False, False]
    flush = [False, False]
    royal = [False, False]
    hv = [False,False]
    Foak = [False, False]
    Toak  = [False, False]
    FH  = [False, False]
    TP  = [False, False]
    OP = [[False,0],[False,0]]
    for j in range(1):
        royal[0],straight[0],flush[0] = Royal(hands_values[0],hands[0])
        royal[1],straight[1],flush[1] = Royal(hands_values[1],hands[1])
        if royal[0] + royal[1]:
            #print("royal ",end=' ')
            hv[0] = royal[0]
            hv[1] = royal[1]
            break
        if (straight[0] and flush[0]) or (straight[1] and flush[1]):
            #print("straight flush ",straight,flush,end=' ')
            hv[0] = straight[0]
            hv[1] = straight[1]
            break
        a = cardsWithSameValues(hands_values[0])
        b = cardsWithSameValues(hands_values[1])
        
        #Foak[0],FH[0],Toak[0],TP[0],OP[0] = cardsWithSameValues(hands_values[0])#[::-1]
        #Foak[1],FH[1],Toak[1],TP[1],OP[1] = cardsWithSameValues(hands_values[1])
        Foak[0] = a[0]
        FH[0] = a[1]
        Toak[0] = a[2]
        TP[0] = a[3]
        OP[0] = a[4]
        Foak[1] = b[0]
        FH[1] = b[1]
        Toak[1] = b[2]
        TP[1] = b[3]
        OP[1] = b[4]
        #print(OP)
        if Foak[0] + Foak[1]:
            #print("Foak ",Foak,end=' ')
            hv[0] = Foak[0]
            hv[1] = Foak[1]
            break
        if FH[0] + FH[1]:
            #print("Full House ",end=' ')
            hv[0] = FH[0]
            hv[1] = FH[1]
            break
        if flush[0] + flush[1]:
            #print("Flush ",end=' ')
            hv[0] = flush[0]
            hv[1] = flush[1]
            break
        if straight[0] + straight[1]:
            #print("straight ",straight,end=' ')
            hv[0] = straight[0]
            hv[1] = straight[1]
            break
        if Toak[0] + Toak[1]:
            #print("toak ",end=' ')
            hv[0] = Toak[0]
            hv[1] = Toak[1]
            break
        if TP[0] + TP[1]:
            #print("tp ",end=' ')
            hv[0] = TP[0]
            hv[1] = TP[1]
            break
        if OP[0][0] + OP[1][0]:
            #print("op ",end=' ')
            if OP[0][0] and OP[1][0]:
                hv[0] = OP[0][1] > OP[1][1]
                hv[1] = not hv[0]
            else:
                hv[0] = OP[0][0]
                hv[1] = OP[1][0]
            break
    if hv[0] == hv[1]:
        m = [max(hands_values[0]), max(hands_values[1])]
        while m[0] == m[1]:
            hands_values[0].remove(m[0])
            hands_values[1].remove(m[1])
            m = [max(hands_values[0]), max(hands_values[1])]
        winner = 1 if m[0] > m[1] else 2
    else:
        winner = 1 if hv[0] > hv[1] else 2
    wins += winner%2
    #print(wins, e)
print(wins)
#---------------------------
print(time.time()-start," ------seconds------\n")
