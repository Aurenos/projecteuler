## Kile Deal - 2013
## Project Euler Problem #20
## Status: Solved

sum = 0

n = range(1,(1001*2)+1)
x = 0
increment = 2
ct = 0

while x < len(n):
    if ct == 5: 
        ct = 0
        increment *= 2
    else:
        sum += n[x]
        x += increment
        ct += 1
        
print sum
