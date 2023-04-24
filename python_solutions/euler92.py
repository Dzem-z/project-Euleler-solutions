import time
start = time.time()
#--------------------------------

upperBound = 10 ** 3
counter = 0
result = 0
summ = 0
"""#1
lookupTable = [ None ] * 1000

for i in range(1, upperBound):
    if i % 100000 == 0:
        print('\n', i)
    result = i
    while result != 1 and result != 89:
        summ = 0
        while result != 0:
            summ += (result % 10) ** 2
            result //= 10
        result = summ
        if lookupTable[ result ] != None:
            break
        print(result, i, end=' ')
    if lookupTable[ result ] == True:
        result = 89
    if i < 1000:
        lookupTable[ i ] = True if result == 89 else False
    if result == 89:
        counter += 1
print('\n', counter)

"""#2

count = 0

def factorial(n):
    result = 1
    for i in range(1,n + 1):
        result *= i
    return result

upperBound = 7

factorials = list(map(factorial, [ i for i in range(upperBound + 1) ] ))
#print(factorials)

digits = [ 0 ] * upperBound
digits[ upperBound - 1 ] = 1
pos = upperBound - 1
prev = 0
while pos >= 0:
    #print(digits)
    while pos < upperBound - 1:
        pos += 1
        digits[ pos ] = prev
        
    
    while digits[ pos ] < 10:
        number = 0
        for i in range(upperBound):
            number += digits[ i ] * 10 ** (upperBound - i - 1)
        #print(number)
        while number != 1 and number != 89:
            summ = 0
            while number != 0:
                summ += (number % 10) ** 2
                number //= 10
            number = summ
        
        if number == 89:
            c = 1
            denominator = 1
            for i in range(1, upperBound):
                if digits[ i ] == digits[ i - 1 ]:
                    c += 1
                else:
                    denominator *= factorials[ c ]
                    c = 1
            denominator *= factorials[ c ]
            #print(digits, denominator, factorials[ upperBound ] / denominator)
            count += factorials[ upperBound ] // denominator
        digits[ pos ] += 1
    while pos >= 0 and digits[ pos ] == 10:
        pos -= 1
    digits[ pos ] += 1
    prev = digits[ pos ]

print(count)

#--------------------------------
print(time.time()-start," ------seconds------\n")
