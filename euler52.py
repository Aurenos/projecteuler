## Kile Deal - 2013
## Project Euler Problem #52
## Status: Solved

def same_digits(x):
    multiples = [x*i for i in xrange(2,7)]
    strx = str(x)
    for num in multiples:
        if len(strx) != len(str(num)): return False
        
        for digit in strx:
            if digit not in str(num): return False
    
    return True

answer = 0
n = 2

while answer == 0:
    
    if same_digits(n):
        answer = n
    else:
        n += 1
        
print answer
    