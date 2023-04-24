import time
start = time.time()
#---------------------------

def DigitSum(number):
    sum = 0
    while number > 0:
        sum += number%10
        number //= 10
    return sum

maxSum = 0
for i in range(100,0,-1):
    for j in range(100,0,-1):
        digitSum = DigitSum(i**j)
        if digitSum > maxSum:
            maxSum = digitSum
print(maxSum)
#---------------------------
print(time.time()-start," ------seconds------\n")
