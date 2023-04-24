import time
start = time.time()
#--------------------------------
class myFrozen(frozenset):
    def __repr__(self):
        return set(self).__repr__()

    def __str__(self):
        return set(self).__str__()
"""
firstCubeS = set()
firstCubeN = set()
secondCubeS = set()
secondCubeN = set()
squares = [[0, 1], [0, 4], [0, 9], [1, 6], [2, 5], [3, 6], [4, 9], [6, 4], [8, 1]]
allSets = set()
for i in range(2 ** 10):
    firstCubeS = set()
    firstCubeN = set()
    secondCubeS = set()
    secondCubeN = set()
    for j in range(9):
        if squares[ j ][ (i >> j) % 2 ] == 6 or squares[ j ][ (i >> j) % 2 ] == 9:
            firstCubeS.add(6)
            firstCubeN.add(9)
        else:
            firstCubeS.add(squares[ j ][ (i >> j) % 2 ])
            firstCubeN.add(squares[ j ][ (i >> j) % 2 ])
        if squares[ j ][ not ((i >> j) % 2) ] == 6 or squares[ j ][ not ((i >> j) % 2) ] == 9:
            secondCubeS.add(6)
            secondCubeN.add(9)
        else:
            secondCubeS.add(squares[ j ][ not ((i >> j) % 2) ])
            secondCubeN.add(squares[ j ][ not ((i >> j) % 2) ])
        #secondCube.add(squares[ j ][ not ((i >> j) % 2) ])
    firsts = [myFrozen(firstCubeS), myFrozen(firstCubeN)]
    seconds = [myFrozen(secondCubeS), myFrozen(secondCubeN)]
    e = 0
    while e < len(firsts):
        if len(firsts[ e ]) > 6:
            firsts.pop( e )
        else:
            e += 1
    e = 0
    while e < len(seconds):
        if len(seconds[ e ]) > 6:
            seconds.pop( e )
        else:
            e += 1
    sets = [firsts, seconds]
    for a in range(len(sets)):
        for b in range(len(sets[ a ])):
            if len( sets[ a ][ b ] ) == 4:
                s = set(sets[ a ][ b ])
                for c in range(10):
                    s.add(c)
                    if len(s) == 5:
                        s1 = set(s)
                        for d in range(10):
                            s1.add(d)
                            if len(s1) == 6:
                                sets[ a ].append( myFrozen(s1) )
                                s1 = set(s)
            if len( sets[ a ][ b ] ) == 5:
                s = set( sets[ a ][ b ] )
                for c in range(10):
                    s.add(c)
                    if len(s) == 6:
                        sets[ a ].append( myFrozen(s) )
                        s = set( sets[ a ][ b ])
        while len(sets[ a ]) > 0 and len(sets[ a ][ 0 ]) != 6:
            sets[ a ].pop( 0 )
    firsts = myFrozen(firsts)
    seconds = myFrozen(seconds)
    #print(firsts, seconds)
    for f in firsts:
        for s in seconds:
            allSets.add(myFrozen((myFrozen(f), myFrozen(s))))
#print(allSets)
for i in allSets:
    for j in i:
        print( j )
print(len(allSets))
"""
"""
firstCube = set()
secondCube = set()
squares = [[0, 1], [0, 4], [0, 9], [1, 6], [2, 5], [3, 6], [4, 9], [6, 4], [8, 1]]
allSets = set()
for i in range(2 ** 9):
    firstCube = set()
    secondCube = set()
    for j in range(9):
        firstCube.add(squares[ j ][ (i >> j) % 2 ])
        secondCube.add(squares[ j ][ not ((i >> j) % 2) ])
        #secondCube.add(squares[ j ][ not ((i >> j) % 2) ])
    firsts = [myFrozen(firstCube)]
    seconds = [myFrozen(secondCube)]
    if 6 in firstCube:
        firsts.append(myFrozen(firstCube.difference({6}).union({9})))
    if 9 in firstCube:
        firsts.append(myFrozen(firstCube.difference({9}).union({6})))
    if 6 in secondCube:
        seconds.append(myFrozen(secondCube.difference({6}).union({9})))
    if 9 in secondCube:
        seconds.append(myFrozen(secondCube.difference({9}).union({6})))
    e = 0
    while e < len(firsts):
        if len(firsts[ e ]) > 6:
            firsts.pop( e )
        else:
            e += 1
    e = 0
    while e < len(seconds):
        if len(seconds[ e ]) > 6:
            seconds.pop( e )
        else:
            e += 1
    sets = [firsts, seconds]
    for a in range(len(sets)):
        for b in range(len(sets[ a ])):
            if len( sets[ a ][ b ] ) == 4:
                s = set(sets[ a ][ b ])
                for c in range(10):
                    s.add(c)
                    if len(s) == 5:
                        s1 = set(s)
                        for d in range(10):
                            s1.add(d)
                            if len(s1) == 6:
                                sets[ a ].append( myFrozen(s1) )
                                s1 = set(s)
            if len( sets[ a ][ b ] ) == 5:
                s = set( sets[ a ][ b ] )
                for c in range(10):
                    s.add(c)
                    if len(s) == 6:
                        sets[ a ].append( myFrozen(s) )
                        s = set( sets[ a ][ b ])
        e = 0
        for b in range(3):
            if e < len( sets[ a ] ) and len(sets[ a ][ e ]) != 6:
                sets[ a ].pop(e)
            else:
                e += 1
    firsts = myFrozen(sets[ 0 ])
    seconds = myFrozen(sets[ 1 ])
    #print(firsts, seconds)
    for f in firsts:
        for s in seconds:
            allSets.add(myFrozen((myFrozen(f), myFrozen(s))))
#for i in allSets:
#    for j in i:
#        print( j )
print(allSets)
print(len(allSets))

"""
#brute force (faster than previous solutions :P )



def setMembership(num, Set):
    if num == 6 or num == 9:
        return 6 in Set or 9 in Set
    else:
        return num in Set
counter = 0
squares = [[0, 1], [0, 4], [0, 9], [1, 6], [2, 5], [3, 6], [4, 9], [6, 4], [8, 1]]
sets = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]
while sets[ 0 ][ 0 ] < 5:
    valid = True
    for num in squares:
        if (not setMembership(num[ 0 ], sets[ 0 ]) or not setMembership(num[ 1 ], sets[ 1 ])) and (not setMembership(num[ 0 ], sets[ 1 ]) or not setMembership(num[ 1 ] ,sets[ 0 ])):
            valid = False
            break
    if valid:
        counter += 1
    if sets[ 1 ][ 5 ] <= 9:
        sets[ 1 ][ 5 ] += 1
    if sets[ 1 ][ 5 ] == 10:
        p = 5
        while p >= 0 and sets[ 1 ][ p ] >= 4 + p:
            p -= 1
        if p < 0:
            p = 0
            j = 5
            while j >= 0 and sets[ 0 ][ j ] >= 4 + j:
                j -= 1
            if j < 0:
                break
            sets[ 0 ][ j ] += 1
            j += 1
            while j < 6:
                sets[ 0 ][ j ] = sets[ 0 ][ j - 1 ] + 1
                j += 1
            sets[ 1 ][ 0 ] = -1
        sets[ 1 ][ p ] += 1
        p += 1
        while p < 6:
            sets[ 1 ][ p ] = sets[ 1 ][ p - 1 ] + 1
            p += 1
            
print(counter // 2)
#--------------------------------
print(time.time()-start," ------seconds------\n")
