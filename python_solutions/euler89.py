import time
start = time.time()
#--------------------------------



def ConvertToRoman(num):
    output = ''
    output = 'M' * ( num // 10 ** 3 )
    num %= 10 ** 3
    if num >= 900:
        output += 'CM'
        num -= 900
    elif num >= 500:
        output += 'D'
        num -= 500
    elif num >= 400:
        output += 'CD'
        num -= 400
    output += 'C' * ( num // 100 )
    num %= 100
    if num >= 90:
        output += 'XC'
        num -= 90
    elif num >= 50:
        output += 'L'
        num -= 50
    elif num >= 40:
        output += 'XL'
        num -= 40
    output += 'X' * ( num // 10 )
    num %= 10
    if num == 9:
        output += 'VX'
        num -= 9
    elif num >= 5:
        output += 'V'
        num -= 5
    elif num == 4:
        output += 'IV'
        num -= 4
    output += 'I' * num
    return output

def ConvertToLatin(romanian):
    romanian += '  '
    i = 0
    number = 0
    while romanian[ i ] == 'M':
        number += 10 ** 3
        i += 1
    if romanian[ i ] == 'C' and romanian[ i + 1 ] == 'M':
        number += 900
        i += 2
    if romanian[ i ] == 'C' and romanian[ i + 1 ] == 'D':
        number += 400
        i += 2
    if romanian[ i ] == 'D':
        number += 500
        i += 1
    while romanian[ i ] == 'C':
        number += 100
        i += 1
    if romanian[ i ] == 'X' and romanian[ i + 1 ] == 'C':
        number += 90
        i += 2
    if romanian[ i ] == 'X' and romanian[ i + 1 ] == 'L':
        number += 40
        i += 2
    if romanian[ i ] == 'L':
        number += 50
        i += 1
    while romanian[ i ] == 'X':
        number += 10
        i += 1
    if romanian[ i ] == 'I' and romanian[ i + 1 ] == 'X':
        number += 9
        i += 2
    if romanian[ i ] == 'I' and romanian[ i + 1 ] == 'V':
        number += 4
        i += 2
    if romanian[ i ] == 'V':
        number += 5
        i += 1
    while romanian[ i ] == 'I':
        number += 1
        i += 1
    return number

romans = open('p089_roman.txt', 'r').read().split('\n')
unoptLen = 0
optLen = 0
for romNum in romans:
    unoptLen += len(romNum)
    number = ConvertToLatin(romNum)
    properRom = ConvertToRoman(number)
    optLen += len(properRom)
    #print(romNum,number,properRom)
    
print(unoptLen, optLen, unoptLen - optLen)

#--------------------------------
print(time.time()-start," ------seconds------\n")
