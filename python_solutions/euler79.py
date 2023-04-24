import time
start = time.time()
#--------------------------------

f = open('p079_keylog.txt', 'r').read().split('\n')[:-1]
print(f)
passcode = ['0', '1', '2', '3', '6', '7', '8', '9']
def Sort(a, b, c):
    indexes = sorted([ passcode.index( a ), passcode.index( b ), passcode.index( c ) ])
    passcode[ indexes[ 0 ] ] = a
    passcode[ indexes[ 1 ] ] = b
    passcode[ indexes[ 2 ] ] = c
def inOrder(a, b, c):
    return passcode.index( a ) < passcode.index( b ) < passcode.index(c)

for i in f:
    if not inOrder(i[ 0 ], i[ 1 ], i[ 2 ]):
        Sort(i[ 0 ], i[ 1 ], i[ 2 ])
    print(passcode)    
print(int(''.join(passcode)))
#--------------------------------
print(time.time()-start," ------seconds------\n")


