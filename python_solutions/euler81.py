import time
start = time.time()
#---------------------------------------------------------

s = """131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331"""

s = open('p081_matrix.txt', 'r')
s = s.read()
matrix = [ j.split(',') for j in s.split('\n') ]
matrix.pop()

dimSize = len(matrix)

for i in range(dimSize):
    for j in range(dimSize):
        matrix[ i ][ j ] = int(matrix[ i ][ j ])



distance = [ [float('inf') for i in range(dimSize)] for j in range(dimSize) ]

distance[0][0] = matrix[0][0]

for i in range(1):
    for x in range(dimSize - 1):
        for y in range(dimSize - 1):
            if distance[ x ][ y + 1 ] > distance[ x ][ y ] + matrix[ x ][ y + 1 ]:
                distance[ x ][ y + 1 ] = distance[ x ][ y ] + matrix[ x ][ y + 1 ]
            if distance[ x + 1 ][ y ] > distance[ x ][ y ] + matrix[ x + 1 ][ y ]:
                distance[ x + 1 ][ y ] = distance[ x ][ y ] + matrix[ x + 1 ][ y ]
    
distance[ dimSize - 1 ][ dimSize - 1] = min(distance[ dimSize - 1 ][ dimSize - 2 ], distance[ dimSize - 2 ][ dimSize - 1 ]) + matrix[ dimSize - 1 ][ dimSize - 1 ]
"""for i in distance:
    print(i)
print()
for i in matrix:
    print(i)
"""
print(distance[ dimSize - 1 ][ dimSize - 1 ])
#---------------------------------------------------------
print(time.time()-start," ------seconds------\n")
