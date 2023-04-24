import time
start = time.time()
#---------------------------------------------------------

s = """131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331"""


s = open('p082_matrix.txt', 'r')
s = s.read()
matrix = [ j.split(',') for j in s.split('\n') ]
matrix.pop()

dimSize = len(matrix)

for i in range(dimSize):
    for j in range(dimSize):
        matrix[ i ][ j ] = int(matrix[ i ][ j ])

minPath = float('inf')

#print(matrix)

distance = [ [float('inf') for i in range(dimSize)] for j in range(dimSize) ]
for i in range(dimSize):
    distance[i][0] = matrix[i][0]

for i in range(dimSize):
    for x in range(i + 1):
        for y in range(i):
            if distance[ x ][ y + 1 ] > distance[ x ][ y ] + matrix[ x ][ y + 1 ]:
                distance[ x ][ y + 1 ] = distance[ x ][ y ] + matrix[ x ][ y + 1 ]
            if x > 0:
                if distance[ x - 1 ][ y ] > distance[ x ][ y ] + matrix[ x - 1 ][ y ]:
                    distance[ x - 1 ][ y ] = distance[ x ][ y ] + matrix[ x - 1 ][ y ]
            if x < dimSize - 1:
                if distance[ x + 1 ][ y ] > distance[ x ][ y ] + matrix[ x + 1 ][ y ]:
                    distance[ x + 1 ][ y ] = distance[ x ][ y ] + matrix[ x + 1 ][ y ]
                    
                
#for i in distance:
#    print(i)

for y in range(dimSize):
    minPath = min( distance[ y ][ dimSize - 1 ], minPath)

print(minPath)
#---------------------------------------------------------
print(time.time()-start," ------seconds------\n")
