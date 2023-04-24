import time
start = time.time()
#------------------------------------
lync = 0
for i in range(10**4):
    j = 0
    num = str(i)
    num1 = num[::-1]
    while j < 50:

        num = str(int(num) + int(num1))
        num1 = num[::-1]
        if num == num1:
            break
        j+= 1
    else:
        lync += 1
print(lync)
"""
def reverse(number):
    reversed = 0
    while number > 0:
        reversed = number%10 + 10*reversed
        number //= 10
    return reversed
lync = 0
for i in range(10**4):
    j = 0
    num = i
    while j < 50:
        num += reverse(num)
        if num == reverse(num):
            break
        j+= 1
    else:
        lync += 1
print(lync)
"""
#---------------------------
print(time.time() - start," ------seconds------\n")
