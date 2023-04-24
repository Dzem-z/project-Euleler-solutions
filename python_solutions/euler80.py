import time
start = time.time()
#---------------------------------------------------------

def Bakshali(S):
    x = int(S ** 0.5) * 10 ** 99
    S *= 10 ** 198
    for i in range(5):
        a = (S - x * x) // (2 * x)
        b = x + a
        x = b - a * a // (2 * b) 
    return x 

total = 0
#print(Bakshali(100))
for i in range(1,101):
    if not (i ** 0.5).is_integer():
        num = Bakshali(i)
        #print(num)
        while num > 0:
            total += num % 10
            num //= 10

print(total)


#---------------------------------------------------------
print(time.time()-start," ------seconds------\n")
