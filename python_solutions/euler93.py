import time
start = time.time()
#--------------------------------
def compute(operand1, operator, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        #if operand2 == 0:
        #    return -1000
        return operand1 / operand2
#messy bruteforce
"""


def Swap(operands, i1, i2):
    h = operands[ i1 ]
    operands[ i1 ] = operands[ i2 ]
    operands[ i2 ] = h

operators = ['+', '-', '*', '/']
#outputNumbers = 
#print(len(outputNumbers))
globalMax = 0
digits = [1, 2, 3, 4]
for a in range(1, 7):
    for b in range(a + 1,8):
        for c in range(b + 1, 9):
            for d in range(c + 1, 10):
                outputNumbers = [False] * 3026
                outputNumbers[ 0 ] = True
                #print(a,b,c,d)
                for fe in operators:
                    for se in operators:
                        for te in operators:
                            operands = [a, b, c, d]
                            #print(fe,se,te)
                            for f in range(4):
                                Swap(operands, 0, f)
                                for s in range(1, 4):
                                    Swap(operands, 1, s)
                                    for t in range(2, 4):
                                        Swap(operands, 2, t)
                                        #print(str(operands[ 0 ])+fe+str(operands[ 1 ])+se+str(operands[ 2 ])+te+str(operands[ 3 ]))
                                        e = float(compute( compute( compute( operands[ 0 ], fe, operands[ 1 ]), se, operands[ 2 ]), te, operands[ 3 ]))
                                        #print(e,' = ', '(('+str(operands[ 0 ])+fe+str(operands[ 1 ])+')'+se+str(operands[ 2 ])+')'+te+str(operands[ 3 ]))
                                        outputNumbers[ int(e) if e >= 0 and e.is_integer() else 0 ] = True
                                        e = float(compute( compute( operands[ 0 ], fe, operands[ 1 ]), se, compute(  operands[ 2 ], te, operands[ 3 ])))
                                        outputNumbers[ int(e) if e >= 0 and e.is_integer() else 0 ] = True
                                        Swap(operands, 2, t)
                                    Swap(operands, 1, s)
                                Swap(operands, 0, f)
                localMax = 0
                #print(list(enumerate(outputNumbers[0:100])))
                while outputNumbers[ localMax ] == True:
                    localMax += 1
                #print(localMax)
                if localMax >= globalMax:
                    globalMax = localMax
                    digits = [a, b, c, d]
                    print(digits)

print(''.join([str(i) for i in digits]))"""

#sol2(less messy bruteforce)
from itertools import permutations
globalMax = 0
Operations = ('+','-','*','/')
for a in range(1, 7):
    for b in range(a + 1, 8):
        for c in range(b + 1, 9):
            for d in range(c + 1, 10):
                outputNumbers = [False] * 3026
                outputNumbers[ 0 ] = True
                for perm in permutations((a,b,c,d)):
                    for o1 in Operations:
                        for o2 in Operations:
                            for o3 in Operations:
                                e = float(compute( compute( compute( perm[ 0 ], o1, perm[ 1 ]), o2, perm[ 2 ]), o3, perm[ 3 ]))
                                outputNumbers[ int(e) if e >= 0 and e.is_integer() else 0 ] = True
                                e = float(compute( compute( perm[ 0 ], o1, perm[ 1 ]), o2, compute(  perm[ 2 ], o3, perm[ 3 ])))
                                outputNumbers[ int(e) if e >= 0 and e.is_integer() else 0 ] = True
                localMax = 0
                while outputNumbers[ localMax ] == True:
                    localMax += 1
                if localMax >= globalMax:
                    globalMax = localMax
                    digits = [a, b, c, d]
                    #print(digits)


print(''.join([str(i) for i in digits]))




#--------------------------------
print(time.time()-start," ------seconds------\n")



