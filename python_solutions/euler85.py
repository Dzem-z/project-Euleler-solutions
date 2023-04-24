import time
start = time.time()
#---------------------------------------------------------

size = 2005
target = 2 * 10 ** 6
rectangleArray = [ 0 for i in range(size) ]
rectangleArray[ 1 ] = 1
for i in range(2, size):
    rectangleArray[ i ] = rectangleArray[ i - 1 ] + i


j = 1
lastVal = rectangleArray[ 1 ]
while lastVal < target:
    j += 1
    lastVal = lastVal + j
    
    #print(lastVal)
print("///////", j)
closestValue = lastVal
area = lastVal
jCopy = j
for i in range(2, jCopy // 2 + 1):
    lastVal = lastVal + rectangleArray[ j ] * i
    if abs(target - closestValue) > abs(target - lastVal):
        closestValue = lastVal
        area = i * j
    #if j % 10 == 0:
    #print(lastVal)
    while lastVal > target:
        lastVal = lastVal - rectangleArray[ i ] * j
        j -= 1
        if abs(target - closestValue) > abs(target - lastVal):
            closestValue = lastVal
            area = i * j
        
        #if j % 10 == 0:
        #print(lastVal)

print("c:", closestValue, "\narea:", area)

#for i in range(2, size):
    #lastVal = rectangleArray[ i ]
    #print( lastVal )
    
    #j -= 
    #while lastVal < 10:
     #   lastVal = lastVal + rectangleArray[ i ] * j
     #   j += 1
     #   print(lastVal)

#print( rectangleArray )

#---------------------------------------------------------
print(time.time()-start," ------seconds------\n")
